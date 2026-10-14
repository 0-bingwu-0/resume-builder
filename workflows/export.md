# Export to PDF

Turn a resume or cover letter from Markdown into HTML with a fixed template, then print it to PDF. The template sets the paper size, margins, fonts, and font sizes, so every PDF comes out the same. [scripts/build.py](../scripts/build.py) does all of this in one command. Your job is the Markdown; don't hand-edit the HTML.

## 1. Run the build script

Run it from the project folder with the Markdown file's path:

```bash
python3 scripts/build.py output/resume.md
```

On Windows, use `python` or `py` instead of `python3`.

It writes the HTML and PDF next to the Markdown file with the same name, like `output/resume.html` and `output/resume.pdf`. A file whose name contains `cover` is built from [templates/cover-letter.html](../templates/cover-letter.html), anything else from [templates/resume.html](../templates/resume.html). It reads the paper size and page limit from [profile.md](../context/profile.md), finds Chrome, Edge, or Chromium, prints the PDF, and reports the page count:

```text
Pages: 1 (limit 1, paper A4)
```

The script only understands the formats in [resume.md](resume.md#format) and [tailor.md](tailor.md#cover-letter). If something looks wrong in the PDF, fix the Markdown, not the script or the HTML.

## 2. Check the page count

If the script says it's over the limit, cut from the Markdown file, starting with the bullets and entries least relevant to the job, and run it again. If it fits but the last page ends well short of the bottom, add back the next most relevant bullets from my notes and run it again. Never change the template's font sizes, margins, or spacing to make it fit. Cover letters are always one page.

When it fits, tell me where the PDF is and what you cut, if anything.

## If the script can't run

If there's no Python, write the HTML by hand: start from the matching template, keep the `<style>` block exactly as it is except the two paper-size lines marked at the top (change them for Letter), and replace the example content in `<body>` with mine, using the same tags and classes. Put my name in the `<title>` too. Then print with Chrome or Edge in headless mode, using full paths:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --no-pdf-header-footer --print-to-pdf="/full/path/output/resume.pdf" "file:///full/path/output/resume.html"
```

On Windows, the browser is at `C:\Program Files\Google\Chrome\Application\chrome.exe` or `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`. On Linux, use `google-chrome` or `chromium`. Check the page count with `grep -a -o "/Count [0-9]*" resume.pdf`; the number is the page count.

If the script says it couldn't find a browser and none of the above works, tell me to open the HTML file in my browser, choose Print, and save as PDF with headers and footers turned off.
