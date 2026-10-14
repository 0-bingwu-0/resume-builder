# Export to PDF

Turn a resume or cover letter from Markdown into HTML with a fixed template, then print it to PDF. The template sets the paper size, margins, fonts, and font sizes, so every PDF comes out the same.

## 1. Make the HTML

* Start from [templates/resume.html](../templates/resume.html) for a resume, or [templates/cover-letter.html](../templates/cover-letter.html) for a cover letter.
* Keep the `<style>` block exactly as it is, except the paper size at the top: leave it for A4, or change the two marked lines for Letter, following the paper setting in [profile.md](../context/profile.md). The same size sets both the PDF and how the page looks in StashBase.
* Replace the example content in `<body>` with mine, using the same tags and classes as the example. Put my name in the `<title>` too.
* Save it next to the Markdown file with the same name, like `output/resume.html`.

## 2. Print to PDF

Print with Chrome or Edge in headless mode. Use full paths, and save the PDF next to the HTML with the same name.

macOS:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --no-pdf-header-footer --print-to-pdf="/full/path/output/resume.pdf" "file:///full/path/output/resume.html"
```

Windows (PowerShell):

```powershell
& "C:\Program Files\Google\Chrome\Application\chrome.exe" --headless --no-pdf-header-footer --print-to-pdf="C:\full\path\output\resume.pdf" "file:///C:/full/path/output/resume.html"
```

Without Chrome on Windows, use Edge with the same flags: `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`. On Linux, use `google-chrome` or `chromium`.

If none of these work, tell me to open the HTML file in my browser, choose Print, and save as PDF with headers and footers turned off.

## 3. Check the page count

The number after `/Count` is the page count.

macOS and Linux:

```bash
grep -a -o "/Count [0-9]*" "/full/path/output/resume.pdf"
```

Windows (PowerShell):

```powershell
Select-String -Path "C:\full\path\output\resume.pdf" -Pattern "/Count \d+" -AllMatches | ForEach-Object { $_.Matches.Value }
```

If it's over the page limit in [profile.md](../context/profile.md), cut from the Markdown file, starting with the bullets and entries least relevant to the job, and export again. Never change the template's font sizes, margins, or spacing to make it fit. Cover letters are always one page.

When it fits, tell me where the PDF is and what you cut, if anything.
