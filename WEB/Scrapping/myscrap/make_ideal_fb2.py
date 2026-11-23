import base64
import html
from pathlib import Path
import re
import urllib.request
import xml.etree.ElementTree as ET


def fetch_cover_base64(img_url):
    """Loads cover using direct link and encodes in Base64."""
    try:
        req = urllib.request.Request(
            img_url,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                ),
                "Referer": "https://readukrainianbooks.com",
            },
        )
        img_data = urllib.request.urlopen(req, timeout=10).read()
        b64_data = base64.b64encode(img_data).decode("ascii")
        print(f"Cover loaded successfully ({len(img_data)} bytes).")
        return b64_data, "image/jpeg"
    except Exception as e:
        print(f"Failed to load cover ({e}), building without it.")
        return None, None


def merge_broken_paragraphs(paragraphs):
    """Joins sentences broken at web page boundaries."""
    if not paragraphs:
        return []

    merged = [paragraphs[0]]
    end_chars = (".", "!", "?", "…", '"', "»", "”", ":", ";", ")")

    for current in paragraphs[1:]:
        prev = merged[-1]
        if not prev.endswith(end_chars) and current and current[0].islower():
            merged[-1] = f"{prev} {current}"
        else:
            merged.append(current)

    return merged


def is_chapter_title(text):
    """Determines chapter titles for the table of contents."""
    patterns = [
        r"^Пролог$",
        r"^Епілог$",
        r"^Громадянство$",
        r"^Розділ\s+\d+.*$",
        r"^Глава\s+\d+.*$",
        r"^\d{1,2}$",
    ]
    return any(re.match(p, text.strip(), re.IGNORECASE) for p in patterns)


def build_fb2(txt_file, output_fb2, cover_url):
    with open(txt_file, "r", encoding="utf-8") as f:
        raw_paragraphs = [
            line.strip() for line in f.read().split("\n\n") if line.strip()
        ]

    print(f"Paragraphs read: {len(raw_paragraphs)}")
    paragraphs = merge_broken_paragraphs(raw_paragraphs)
    print(f"Paragraphs after merging: {len(paragraphs)}")

    cover_b64, cover_mime = fetch_cover_base64(cover_url)

    sections = []
    current_title = "Початок"
    current_body = []

    for p in paragraphs:
        if is_chapter_title(p):
            if current_body:
                sections.append((current_title, current_body))
            current_title = f"Розділ {p}" if p.isdigit() else p
            current_body = []
        else:
            current_body.append(p)

    if current_body:
        sections.append((current_title, current_body))

    print(f"Chapters in the table of contents: {len(sections)}")

    coverpage_xml = ""
    binary_xml = ""
    if cover_b64:
        coverpage_xml = """      <coverpage>
        <image l:href="#cover.jpg"/>
      </coverpage>\n"""
        binary_xml = f"""  <binary id="cover.jpg" content-type="{cover_mime}">
{cover_b64}
  </binary>\n"""

    fb2_header = f"""<?xml version="1.0" encoding="utf-8"?>
<FictionBook xmlns="http://www.gribuser.ru/xml/fictionbook/2.0" xmlns:l="http://www.w3.org/1999/xlink">
  <description>
    <title-info>
      <genre>children</genre>
      <author>
        <first-name>Ерін</first-name>
        <last-name>Гантер</last-name>
      </author>
      <book-title>На волю!</book-title>
{coverpage_xml}      <lang>uk</lang>
    </title-info>
  </description>
  <body>
"""

    with open(output_fb2, "w", encoding="utf-8") as f:
        f.write(fb2_header)
        for title, body_paragraphs in sections:
            f.write("    <section>\n")
            f.write(f"      <title><p>{html.escape(title)}</p></title>\n")
            for p in body_paragraphs:
                f.write(f"      <p>{html.escape(p)}</p>\n")
            f.write("    </section>\n")
        f.write("  </body>\n")
        f.write(binary_xml)
        f.write("</FictionBook>")

    # Check XML validity
    ET.parse(output_fb2)
    print(f"XML is valid! File {output_fb2} is ready for PocketBook.")


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    build_fb2(
        txt_file=base_dir / "na_volju.txt",
        output_fb2=base_dir / "na_volju_ideal.fb2",
        cover_url="https://readukrainianbooks.com/uploads/posts/books/7/2/1/na-volju-erin-hanter.jpg",
    )
