import html
import docx
import scrapy


class BookScraperSpider(scrapy.Spider):
    name = "erin_hanter"

    # Generate list of all 54 URL addresses immediately in the standard start_urls attribute
    start_urls = [
        "https://readukrainianbooks.com/721-na-volju-erin-hanter.html#part1"
    ] + [
        f"https://readukrainianbooks.com/page-{page_num}-721-na-volju-erin-hanter.html"
        for page_num in range(2, 55)
    ]

    custom_settings = {
        "USER_AGENT": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            " (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ),
        "DOWNLOAD_DELAY": 1,
        "CONCURRENT_REQUESTS": 1,  # Load strictly in sequence
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.all_paragraphs = []

    def parse(self, response):
        raw_texts = response.css("div#texts ::text").getall()

        for line in raw_texts:
            text = line.replace("\xa0", " ").strip()
            if text:
                self.all_paragraphs.append(text)

        self.logger.info(
            f"Processed: {response.url} (total paragraphs: {len(self.all_paragraphs)})"
        )

    def closed(self, reason):
        self.save_txt("na_volju.txt")
        self.save_docx("na_volju.docx")
        self.save_fb2("na_volju.fb2")
        self.logger.info("Done! All chapters (1-54 pages) saved.")

    def save_txt(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n\n".join(self.all_paragraphs))

    def save_docx(self, filename):
        doc = docx.Document()
        doc.add_heading("На волю! — Ерін Гантер", level=1)
        for p in self.all_paragraphs:
            doc.add_paragraph(p)
        doc.save(filename)

    def save_fb2(self, filename):
        fb2_header = """<?xml version="1.0" encoding="utf-8"?>
<FictionBook xmlns="http://www.gribuser.ru/xml/fictionbook/2.0" xmlns:l="http://www.w3.org/1999/xlink">
  <description>
    <title-info>
      <genre>children</genre>
      <author>
        <first-name>Ерін</first-name>
        <last-name>Гантер</last-name>
      </author>
      <book-title>На волю!</book-title>
      <lang>uk</lang>
    </title-info>
  </description>
  <body>
    <section>
"""
        fb2_footer = """    </section>
  </body>
</FictionBook>"""

        with open(filename, "w", encoding="utf-8") as f:
            f.write(fb2_header)
            for p in self.all_paragraphs:
                safe_text = html.escape(p)
                f.write(f"      <p>{safe_text}</p>\n")
            f.write(fb2_footer)
