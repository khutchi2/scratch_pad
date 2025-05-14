#!/usr/bin/env python3
"""
Abbottabad Dataset Explorer – **Web Edition**
===========================================
A FastAPI application exposing a read‑only web portal onto an EFS‑mounted copy
of the Abbottabad compound dataset (or any folder).

Changes in this patch
---------------------
* **FIX:** FastAPI errored on startup (`RuntimeError: Directory '<file>.static' does not exist'`).
  The static directory is now **created before** it is mounted, eliminating the
  startup failure on first run.

Key features remain the same: file tree, filename search, previews for images,
video, audio, PDFs, HTML, and DOCX→HTML via *pypandoc 1.15*.
"""

from __future__ import annotations

import argparse
import mimetypes
import os
import sys
from functools import lru_cache
from pathlib import Path
from typing import List

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

try:
    import pypandoc  # type: ignore
except ImportError:
    pypandoc = None

# ---------------------------------------------------------------------------
# CLI / Config
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Abbottabad Dataset Explorer – Web")
    parser.add_argument("--root", default="/mnt/efs/abbottabad", help="Dataset root")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=5000)
    return parser.parse_args()


ARGS = parse_args()
DATA_ROOT = Path(ARGS.root).expanduser().resolve()
if not DATA_ROOT.exists():
    print(f"Error: dataset root {DATA_ROOT} not found", file=sys.stderr)
    sys.exit(1)

# ---------------------------------------------------------------------------
# Prepare static directory *before* mounting
# ---------------------------------------------------------------------------

STATIC_DIR = Path(__file__).with_suffix(".static")
STATIC_DIR.mkdir(exist_ok=True)  # <-- ensures dir exists early

# ---------------------------------------------------------------------------
# FastAPI app
# ---------------------------------------------------------------------------

app = FastAPI(title="Abbottabad Dataset Explorer", docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

@lru_cache(maxsize=4096)
def is_dir(path: Path) -> bool:  # noqa: D401 (simple predicate)
    return path.is_dir()


def safe_join(rel_path: str) -> Path:
    """Join user path safely under DATA_ROOT (no traversal)."""
    target = (DATA_ROOT / rel_path).resolve()
    if not str(target).startswith(str(DATA_ROOT)):
        raise HTTPException(status_code=400, detail="Invalid path")
    return target


def list_dir(rel_path: str = "") -> List[dict]:
    """Return non‑recursive listing of *rel_path*."""
    dir_path = safe_join(rel_path)
    if not dir_path.is_dir():
        raise HTTPException(404, "Not a directory")
    return [
        {
            "name": p.name,
            "path": str(Path(rel_path) / p.name),
            "is_dir": p.is_dir(),
        }
        for p in sorted(dir_path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
    ]

# ---------------------------------------------------------------------------
# API Endpoints
# ---------------------------------------------------------------------------

@app.get("/api/list", response_class=JSONResponse)
async def api_list(path: str = ""):
    return list_dir(path)


@app.get("/api/search", response_class=JSONResponse)
async def api_search(q: str = Query(..., min_length=1)):
    q_lower = q.lower()
    results = []
    for root, _, files in os.walk(DATA_ROOT):
        for name in files:
            if q_lower in name.lower():
                rel = os.path.relpath(os.path.join(root, name), DATA_ROOT)
                results.append(rel)
                if len(results) >= 2000:
                    return results
    return results


@app.get("/preview")
async def preview(path: str):
    abs_path = safe_join(path)
    if not abs_path.exists():
        raise HTTPException(404, "File not found")

    # DOCX → HTML via Pandoc
    if abs_path.suffix.lower() == ".docx" and pypandoc is not None:
        try:
            html = pypandoc.convert_file(str(abs_path), to="html", format="docx")
            return HTMLResponse(html)
        except Exception:
            pass  # fallback to FileResponse below

    mime, _ = mimetypes.guess_type(abs_path.name)
    return FileResponse(abs_path, media_type=mime or "application/octet-stream")

# ---------------------------------------------------------------------------
# Minimal front‑end (vanilla JS)
# ---------------------------------------------------------------------------

INDEX_HTML = STATIC_DIR / "index.html"
INDEX_TEMPLATE = """<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\"><title>Abbottabad Dataset Explorer</title>
<link rel=\"stylesheet\" href=\"https://cdn.jsdelivr.net/npm/modern-normalize/modern-normalize.min.css\">
<style>
body{display:flex;height:100vh;margin:0;font-family:sans-serif}
#tree{width:320px;overflow:auto;border-right:1px solid #ccc;padding:4px}
#preview{flex:1;display:flex;justify-content:center;align-items:start;overflow:auto}
#preview>*{max-width:100%;max-height:100vh}
ul{list-style:none;padding-left:1em}
li{cursor:pointer;margin:2px 0}
li.dir{font-weight:bold}
li:hover{text-decoration:underline}
</style>
</head>
<body>
<div id=\"tree\"></div>
<div id=\"preview\"><p>Select a file…</p></div>
<script>
async function list(path=""){
  const res=await fetch(`/api/list?path=${encodeURIComponent(path)}`);return res.json();
}
function createNode(item){
  const li=document.createElement('li');
  li.textContent=item.name;
  li.dataset.path=item.path;
  li.className=item.is_dir?'dir':'file';
  if(item.is_dir)li.addEventListener('click',toggleDir);
  else li.addEventListener('click',viewFile);
  return li;
}
async function toggleDir(e){
  e.stopPropagation();
  const li=e.target;
  if(li.dataset.loaded){li.querySelector('ul').classList.toggle('hidden');return;}
  const ul=document.createElement('ul');
  const children=await list(li.dataset.path);
  children.forEach(ch=>ul.appendChild(createNode(ch)));
  li.appendChild(ul);
  li.dataset.loaded=true;
}
async function viewFile(e){
  const path=e.target.dataset.path;
  const prev=document.getElementById('preview');
  prev.innerHTML='Loading…';
  const ext=path.split('.').pop().toLowerCase();
  if(['png','jpg','jpeg','gif','webp'].includes(ext)){
    prev.innerHTML=`<img src="/preview?path=${encodeURIComponent(path)}"/>`;
  }else if(['mp4','mkv','mov','avi'].includes(ext)){
    prev.innerHTML=`<video controls src="/preview?path=${encodeURIComponent(path)}" style="max-width:100%"></video>`;
  }else if(['mp3','wav','flac','ogg'].includes(ext)){
    prev.innerHTML=`<audio controls src="/preview?path=${encodeURIComponent(path)}"></audio>`;
  }else if(ext==='pdf'){
    prev.innerHTML=`<iframe style="width:100%;height:100vh" src="/preview?path=${encodeURIComponent(path)}"></iframe>`;
  }else{
    const r=await fetch(`/preview?path=${encodeURIComponent(path)}`);
    const ct=r.headers.get('content-type');
    if(ct && ct.startsWith('text/html')){
      prev.innerHTML=await r.text();
    }else{ // unknown binary ⇒ trigger download
      window.open(`/preview?path=${encodeURIComponent(path)}`,'_blank');
      prev.innerHTML='<p>Download triggered.</p>';
    }
  }
}
(async()=>{
  const root=await list("");
  const ul=document.createElement('ul');
  root.forEach(item=>ul.appendChild(createNode(item)));
  document.getElementById('tree').appendChild(ul);
})();
</script>
</body></html>"""

if not INDEX_HTML.exists():
    INDEX_HTML.write_text(INDEX_TEMPLATE, encoding="utf-8")


@app.get("/", response_class=HTMLResponse)
async def root():
    return HTMLResponse(INDEX_HTML.read_text("utf-8"))

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "flask_viewer_new:app",
        host=ARGS.host,
        port=ARGS.port,
        log_level="info",
    )
