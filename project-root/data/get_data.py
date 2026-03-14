"""
Download and extract the LIAR dataset.
Source: https://www.cs.ucsb.edu/~william/data/liar_dataset.zip
License: Public research use
"""

import os
import urllib.request
import zipfile

DATA_URL = "https://www.cs.ucsb.edu/~william/data/liar_dataset.zip"
DATA_DIR = os.path.join(os.path.dirname(__file__), "raw")


def download_liar():
    os.makedirs(DATA_DIR, exist_ok=True)
    zip_path = os.path.join(DATA_DIR, "liar_dataset.zip")

    if not os.path.exists(zip_path):
        print(f"Downloading LIAR dataset from {DATA_URL} ...")
        urllib.request.urlretrieve(DATA_URL, zip_path)
        print("Download complete.")
    else:
        print("Archive already exists, skipping download.")

    with zipfile.ZipFile(zip_path, "r") as zf:
        zf.extractall(DATA_DIR)
    print(f"Extracted to {DATA_DIR}/")
    print("Files:", os.listdir(DATA_DIR))


if __name__ == "__main__":
    download_liar()