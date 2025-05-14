#!/usr/bin/env python3
"""
Abbottabad Dataset Explorer (Pandoc Edition)
-------------------------------------------
A PyQt 6 desktop application that browses an EFS-mounted directory (or any local
path) and previews documents, images, HTML, audio and video.  It now uses
**pypandoc 1.15** (with a system Pandoc install) to convert *DOCX → HTML* for
inline viewing instead of *docx2html*.

Requirements
------------
    # GUI & multimedia
    pip install "PyQt6>=6.6" "PyQt6-Qt6" "PyQt6-WebEngine"

    # DOCX→HTML conversion
    pip install "pypandoc==1.15"
    # and make sure Pandoc ⩾ 2.0 is installed on the OS PATH

On Linux you may also need GStreamer for media playback, e.g.:
    sudo apt install gstreamer1.0-libav gstreamer1.0-plugins-{base,good,bad,ugly}

Usage
-----
    python abbottabad_explorer.py            # assumes /mnt/efs/abbottabad
    python abbottabad_explorer.py --root /path/to/dataset

Mounting EFS (example)
----------------------
    sudo yum install -y amazon-efs-utils      # (Amazon Linux)
    sudo mkdir -p /mnt/efs/abbottabad
    sudo mount -t efs fs-12345678:/ /mnt/efs/abbottabad
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from PyQt6.QtCore import Qt, QSortFilterProxyModel, QUrl
from PyQt6.QtGui import QDesktopServices, QPixmap, QFileSystemModel
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QSplitter,
    QStackedWidget,
    QTreeView,
    QVBoxLayout,
    QWidget,
    QSizePolicy,
)
from PyQt6.QtWebEngineWidgets import QWebEngineView

# -----------------------------------------------------------------------------
# Optional dependency: pypandoc
# -----------------------------------------------------------------------------
try:
    import pypandoc  # type: ignore
except ImportError:  # graceful fallback if not available
    pypandoc = None


class Viewer(QWidget):
    """Stacked widget that shows the appropriate preview for a file."""

    def __init__(self) -> None:
        super().__init__()
        self.stack = QStackedWidget()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.stack)

        # ── Image preview ──────────────────────────────────────────────────
        self.image_label = QLabel(alignment=Qt.AlignmentFlag.AlignCenter)
        self.image_label.setScaledContents(True)
        self.image_label.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )

        # ── Web view (HTML, PDF, converted DOCX) ───────────────────────────
        self.web_view = QWebEngineView()

        # ── Media player (audio / video) ───────────────────────────────────
        self.video_widget = QVideoWidget()
        self.media_player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.media_player.setVideoOutput(self.video_widget)
        self.media_player.setAudioOutput(self.audio_output)

        # Add widgets to the stack in fixed order
        self.stack.addWidget(self.image_label)  # index 0
        self.stack.addWidget(self.web_view)     # index 1
        self.stack.addWidget(self.video_widget) # index 2

    # ---------------------------------------------------------------------
    # Public API
    # ---------------------------------------------------------------------
    def display(self, path: Path) -> None:
        """Display *path* in the appropriate preview widget."""

        if not path.is_file():
            return

        suffix = path.suffix.lower()

        # ── Images ─────────────────────────────────────────────────────────
        if suffix in {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp"}:
            pix = QPixmap(str(path))
            self.image_label.setPixmap(pix)
            self.stack.setCurrentWidget(self.image_label)
            return

        # ── HTML or PDF ───────────────────────────────────────────────────
        if suffix in {".html", ".htm", ".pdf"}:
            self.web_view.load(QUrl.fromLocalFile(str(path)))
            self.stack.setCurrentWidget(self.web_view)
            return

        # ── DOCX via Pandoc ────────────────────────────────────────────────
        if suffix == ".docx":
            if pypandoc is None:
                # pypandoc not installed → open externally
                QDesktopServices.openUrl(QUrl.fromLocalFile(str(path)))
                return
            try:
                html = pypandoc.convert_file(str(path), to="html", format="docx")
            except (RuntimeError, OSError):  # Pandoc missing or error
                QDesktopServices.openUrl(QUrl.fromLocalFile(str(path)))
                return
            self.web_view.setHtml(html, baseUrl=QUrl.fromLocalFile(str(path.parent)))
            self.stack.setCurrentWidget(self.web_view)
            return

        # ── Video or Audio ────────────────────────────────────────────────
        if suffix in {
            ".mp4",
            ".mkv",
            ".mov",
            ".avi",
            ".mp3",
            ".wav",
            ".flac",
            ".ogg",
        }:
            self.media_player.setSource(QUrl.fromLocalFile(str(path)))
            self.media_player.play()
            # Hide video widget for pure-audio formats
            self.video_widget.setVisible(suffix not in {".mp3", ".wav", ".flac", ".ogg"})
            self.stack.setCurrentWidget(self.video_widget)
            return

        # ── Fallback: open with system default app ────────────────────────
        QDesktopServices.openUrl(QUrl.fromLocalFile(str(path)))


class Explorer(QMainWindow):
    """Main application window with a file tree and preview pane."""

    def __init__(self, root_path: Path) -> None:
        super().__init__()
        self.setWindowTitle("Abbottabad Dataset Explorer")

        # ── Search bar ────────────────────────────────────────────────────
        self.search_bar = QLineEdit(placeholderText="Search file name… (wildcards OK)")

        # ── File model ────────────────────────────────────────────────────
        self.model = QFileSystemModel()
        self.model.setRootPath(str(root_path))
        self.model.setNameFilterDisables(False)

        # ── Proxy for filename filter ─────────────────────────────────────
        self.proxy = QSortFilterProxyModel()
        self.proxy.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.proxy.setSourceModel(self.model)

        # ── Tree view ─────────────────────────────────────────────────────
        self.tree = QTreeView()
        self.tree.setModel(self.proxy)
        self.tree.setRootIndex(self.proxy.mapFromSource(self.model.index(str(root_path))))
        self.tree.doubleClicked.connect(self.open_file)
        self.tree.setSortingEnabled(True)
        self.tree.sortByColumn(0, Qt.SortOrder.AscendingOrder)
        self.tree.setHeaderHidden(False)

        # ── Preview widget ────────────────────────────────────────────────
        self.viewer = Viewer()

        # ── Layout ────────────────────────────────────────────────────────
        splitter = QSplitter()
        splitter.addWidget(self.tree)
        splitter.addWidget(self.viewer)
        splitter.setStretchFactor(1, 1)

        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.search_bar)
        layout.addWidget(splitter)
        self.setCentralWidget(container)
        self.resize(1280, 800)

        # Connect search
        self.search_bar.textChanged.connect(self._on_search_text_changed)

    # ------------------------------------------------------------------
    # Slots
    # ------------------------------------------------------------------
    def _on_search_text_changed(self, text: str):
        pattern = f"*{text}*" if text else "*"
        self.proxy.setFilterWildcard(pattern)

    def open_file(self, proxy_index):
        """Open or preview the selected file."""
        source_idx = self.proxy.mapToSource(proxy_index)
        path = Path(self.model.filePath(source_idx))
        if path.is_file():
            self.viewer.display(path)


# -------------------------------------------------------------------------
# Application entry point
# -------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Abbottabad Dataset Explorer")
    parser.add_argument(
        "--root",
        default="/mnt/efs/abbottabad",
        help="Path to the dataset root (EFS mountpoint)",
    )
    args = parser.parse_args()

    root = Path(args.root).expanduser()
    if not root.exists():
        print(f"Error: root path {root} does not exist.")
        sys.exit(1)

    app = QApplication(sys.argv)
    window = Explorer(root)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
