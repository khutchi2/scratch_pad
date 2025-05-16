#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

def download_all_zips(page_url, output_dir="zips"):
    # Check if output_dir exists
    os.makedirs(output_dir, exist_ok=True)

    # Get the page
    resp = requests.get(page_url)
    resp.raise_for_status()

    # Parse HTML
    soup = BeautifulSoup(resp.text, 'html.parser')

    # Find all <a> tags whose href ends with .zip
    zip_links = [
        link['href'] for link in soup.find_all('a', href=True)
        if link['href'].lower().endswith('.zip')
    ]

    if not zip_links:
        print("No ZIP files found on the page.")
        return

    for href in zip_links:
        # Resolve relative URLs
        zip_url = urljoin(page_url, href)
        local_filename = os.path.join(output_dir, os.path.basename(href))
        print(f"Downloading {zip_url} → {local_filename}")

        # Stream download to avoid loading entire file in memory
        with requests.get(zip_url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

    print("All done!")

if __name__ == "__main__":
    PAGE = "https://www.cia.gov/library/abbottabad-compound/index_device.html"
    download_all_zips(PAGE)
