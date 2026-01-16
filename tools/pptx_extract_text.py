#!/usr/bin/env python3
"""Extracts plain text from a .pptx (Office Open XML) without external deps.

Usage:
  python tools/pptx_extract_text.py path/to/file.pptx > out.txt
"""

from __future__ import annotations

import re
import sys
import zipfile
from xml.etree import ElementTree as ET


NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
}


def extract_slide_text(pptx_path: str) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []

    with zipfile.ZipFile(pptx_path) as z:
        slide_names = sorted(
            (n for n in z.namelist() if n.startswith("ppt/slides/slide") and n.endswith(".xml")),
            key=lambda s: int(re.search(r"slide(\d+)\.xml$", s).group(1)),  # type: ignore[union-attr]
        )

        for slide_name in slide_names:
            xml_bytes = z.read(slide_name)
            root = ET.fromstring(xml_bytes)
            texts = [t.text or "" for t in root.findall(".//a:t", NS)]
            text = " ".join(x.strip() for x in texts if x and x.strip())
            text = re.sub(r"\s+", " ", text).strip()
            out.append((slide_name, text))

    return out


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python tools/pptx_extract_text.py path/to/file.pptx", file=sys.stderr)
        return 2

    pptx_path = sys.argv[1]
    try:
        slides = extract_slide_text(pptx_path)
    except FileNotFoundError:
        print(f"Not found: {pptx_path}", file=sys.stderr)
        return 2
    except zipfile.BadZipFile:
        print(f"Not a valid .pptx zip: {pptx_path}", file=sys.stderr)
        return 2

    for slide_name, text in slides:
        if not text:
            continue
        print(f"## {slide_name}\n{text}\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
