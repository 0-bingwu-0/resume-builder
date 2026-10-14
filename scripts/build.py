#!/usr/bin/env python3
"""Turn a resume or cover letter from Markdown into HTML and PDF.

Usage:
    python3 scripts/build.py output/resume.md
    python3 scripts/build.py output/applications/acme-backend-intern/cover-letter.md
    python3 scripts/build.py output/resume.md --no-pdf

Writes the HTML and PDF next to the Markdown file with the same name, then
prints the page count and the page limit. A file whose name contains "cover"
is built as a cover letter; anything else as a resume.

The look comes from templates/. Only the paper size changes, following the
Paper setting in context/profile.md. Uses only the Python standard library.
"""
import argparse
import html
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "templates"
PROFILE = ROOT / "context" / "profile.md"

BROWSERS = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]
BROWSER_COMMANDS = ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser",
                    "microsoft-edge", "chrome", "msedge"]


def read_settings():
    """Paper size and page limit from profile.md."""
    text = PROFILE.read_text(encoding="utf-8") if PROFILE.exists() else ""
    paper = re.search(r"\*\*Paper:\*\*\s*(\w+)", text)
    pages = re.search(r"\*\*Pages:\*\*\s*(\d+)", text)
    return (paper.group(1) if paper else "A4"), (int(pages.group(1)) if pages else 1)


def inline(text):
    """Escape HTML, then turn **bold**, *italic*, and [text](url) into tags."""
    text = html.escape(text.strip(), quote=False)
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", text)
    return text


def row(text, left_class):
    """A `left | right` line as a two-sided row. The right side is optional."""
    left, _, right = text.partition(" | ")
    spans = f'<span class="{left_class}">{inline(left)}</span>'
    if right.strip():
        spans += f'<span class="right">{inline(right)}</span>'
    return f'<div class="row">{spans}</div>'


def bullet_list(items, indent):
    pad = " " * indent
    lines = [f"{pad}<ul>"]
    lines += [f"{pad}  <li>{inline(item)}</li>" for item in items]
    lines.append(f"{pad}</ul>")
    return lines


def header(name, contact):
    return [
        "  <header>",
        f"    <h1>{inline(name)}</h1>",
        f'    <p class="contact">{inline(contact)}</p>',
        "  </header>",
    ]


def build_resume(md):
    name, contact, sections = "", [], []
    entry = None  # the ### entry being filled, if any

    for raw in md.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("# "):
            name = line[2:]
        elif line.startswith("## "):
            sections.append({"title": line[3:], "items": []})
            entry = None
        elif not sections:
            contact.append(line)
        elif line.startswith("### "):
            entry = {"kind": "entry", "head": line[4:], "sub": None, "bullets": []}
            sections[-1]["items"].append(entry)
        elif line.startswith(("- ", "* ")):
            items = sections[-1]["items"]
            if entry is not None:
                entry["bullets"].append(line[2:])
            elif items and items[-1]["kind"] == "ul":
                items[-1]["bullets"].append(line[2:])
            else:
                items.append({"kind": "ul", "bullets": [line[2:]]})
        elif entry is not None and entry["sub"] is None and not entry["bullets"]:
            entry["sub"] = line
        else:
            sections[-1]["items"].append({"kind": "p", "text": line})
            entry = None

    body = header(name, " ".join(contact))
    for section in sections:
        items = section["items"]
        plain = items and all(item["kind"] == "p" for item in items)
        body.append("")
        body.append('  <section class="skills">' if plain else "  <section>")
        body.append(f"    <h2>{inline(section['title'])}</h2>")
        for item in items:
            if item["kind"] == "entry":
                body.append('    <div class="entry">')
                body.append("      " + row(item["head"], "org"))
                if item["sub"]:
                    body.append("      " + row(item["sub"], "role"))
                if item["bullets"]:
                    body += bullet_list(item["bullets"], 6)
                body.append("    </div>")
            elif item["kind"] == "ul":
                body += bullet_list(item["bullets"], 4)
            else:
                body.append(f"    <p>{inline(item['text'])}</p>")
        body.append("  </section>")
    return name, body


def build_cover_letter(md):
    blocks = [b.strip().splitlines() for b in re.split(r"\n\s*\n", md.strip()) if b.strip()]
    name = blocks[0][0].lstrip("# ").strip()
    contact = " ".join(blocks[1]) if len(blocks) > 1 else ""
    body = header(name, contact)
    rest = blocks[2:]
    for i, block in enumerate(rest):
        body.append("")
        if i == len(rest) - 1:
            body.append(f'  <p class="sign">{"<br>".join(inline(l) for l in block)}</p>')
        else:
            body.append(f"  <p>{inline(' '.join(l.strip() for l in block))}</p>")
    return name, body


def make_html(md_path, cover, paper):
    template = (TEMPLATES / ("cover-letter.html" if cover else "resume.html")).read_text(encoding="utf-8")
    md = md_path.read_text(encoding="utf-8")
    name, body = build_cover_letter(md) if cover else build_resume(md)

    head = template.split("<body>")[0]
    title = f"{name} – {'Cover Letter' if cover else 'Resume'}"
    head = re.sub(r"<title>.*?</title>", lambda _: f"<title>{html.escape(title, quote=False)}</title>", head)
    if paper.lower() == "letter":
        head = head.replace("size: A4;", "size: Letter;")
        head = head.replace("--page-width: 210mm; --page-height: 297mm;", "--page-width: 8.5in; --page-height: 11in;")

    html_path = md_path.with_suffix(".html")
    html_path.write_text(head + "<body>\n" + "\n".join(body) + "\n</body>\n</html>\n", encoding="utf-8")
    return html_path


def find_browser():
    for path in BROWSERS:
        if Path(path).is_file():
            return path
    for command in BROWSER_COMMANDS:
        found = shutil.which(command)
        if found:
            return found
    return None


def print_pdf(html_path):
    browser = find_browser()
    if not browser:
        return None
    pdf_path = html_path.with_suffix(".pdf")
    if pdf_path.exists():
        pdf_path.unlink()
    subprocess.run(
        [browser, "--headless", "--disable-gpu", "--no-pdf-header-footer",
         f"--print-to-pdf={pdf_path}", html_path.as_uri()],
        capture_output=True, timeout=120,
    )
    return pdf_path if pdf_path.exists() else None


def page_count(pdf_path):
    counts = re.findall(rb"/Count (\d+)", pdf_path.read_bytes())
    return max(int(c) for c in counts) if counts else 0


def main():
    parser = argparse.ArgumentParser(description="Build HTML and PDF from a resume or cover letter in Markdown.")
    parser.add_argument("markdown", type=Path)
    parser.add_argument("--no-pdf", action="store_true", help="only write the HTML")
    args = parser.parse_args()

    md_path = args.markdown.resolve()
    if not md_path.is_file():
        sys.exit(f"Not found: {md_path}")
    cover = "cover" in md_path.stem.lower()
    paper, limit = read_settings()
    if cover:
        limit = 1

    html_path = make_html(md_path, cover, paper)
    print(f"HTML: {html_path}")
    if args.no_pdf:
        return

    pdf_path = print_pdf(html_path)
    if not pdf_path:
        print("No PDF: couldn't find or run Chrome, Edge, or Chromium. "
              "Open the HTML in a browser, choose Print, and save as PDF with headers and footers off.")
        sys.exit(3)
    pages = page_count(pdf_path)
    print(f"PDF: {pdf_path}")
    print(f"Pages: {pages} (limit {limit}, paper {paper})")
    if pages > limit:
        print(f"Over the limit by {pages - limit}. Cut content from the Markdown and run again.")
        sys.exit(2)


if __name__ == "__main__":
    main()
