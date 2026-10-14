# Resume Builder

A good resume comes from details: what you did, how you did it, and what came of it. It's hard to give AI all of that in one chat, and you'd have to do it again for every job.

This project keeps it all in one place. AI interviews you once, writes your resume from your answers, and tailors a new version for each job you apply to.

## Getting started

Open this project in StashBase and tell the Agent:

1. **"Set me up."** It asks for your current resume first. No resume? Your LinkedIn profile works too: open your profile on LinkedIn, click More, then Save to PDF. If you have a GitHub, it reads your repositories too, so it doesn't have to ask what's already there. Then it asks a few basics, like your major and the job you want, and writes a question list just for you in `context/experience.md`.
2. **Answer the questions.** Either write under them in `context/experience.md`, or say **"Interview me"** and the Agent asks them one at a time in Chat, saving each answer as you go. Rough notes are fine, and you can skip what you can't answer. Start with the ones marked ⭐.
3. **"Write my resume."** It turns your answers into experience notes, writes `output/resume.md`, reviews it the way a recruiter would, exports a PDF, and tells you what's still missing. Say "Interview me" again to fill those gaps.
4. **"Tailor it for this job:"** and paste the job description. It writes a resume for that job in `output/applications/`, picking from everything you've done, not just what's on your base resume. Ask for a cover letter if you need one.

The template comes with an example: a computer science student looking for a backend internship. Look around before you run setup.

## Make it yours

* **Your basics and resume settings** are in `context/profile.md`: the job you want, paper size, and page limit.
* **Everything you've done** is in `context/experience.md`. The more detail, the better each resume gets. Add to it anytime, tell the Agent, or say "Interview me about…" something new.
* **Your old resume, LinkedIn PDF, and other material** go in `materials/`. The Agent reads them but never changes them.
* **The look of your resume** is set in `templates/`. The Agent only fills in content, so every PDF has the same size and style.
* **The Agent's persona and rules** are in `AGENTS.md`.

## PDF export

The Agent exports with `scripts/build.py`, which turns your Markdown into HTML with the template, prints it to PDF, and checks the page count in one step. You need Python 3, Chrome or Edge, and an Agent that can run local commands. If the resume runs over your page limit, the Agent cuts content, never the font size, until it fits.

You can run it yourself too: `python3 scripts/build.py output/resume.md`.

If export doesn't work, open the HTML file next to your resume in a browser, choose Print, and save as PDF with headers and footers turned off.

## Files

* `AGENTS.md`: the AI's persona, how it writes for you, and the task index.
* `CLAUDE.md`: points Claude Code to `AGENTS.md`.
* `context/profile.md`: your basics, the job you want, resume settings, and preferences.
* `context/experience.md`: your question list at first, then your experience notes.
* `materials/`: your old resume, LinkedIn PDF, and anything else that shows what you've done.
* `workflows/setup.md`: reading your materials and GitHub, the basic questions, and how the question list is written.
* `workflows/interview.md`: asking your open questions one at a time in Chat.
* `workflows/resume.md`: how your notes and base resume are written, the recruiter review, and the resume format.
* `workflows/tailor.md`: tailoring a resume to a job description, and writing cover letters.
* `workflows/export.md`: running the build script and checking the page count.
* `scripts/build.py`: turns a resume or cover letter into HTML and PDF.
* `templates/resume.html`, `templates/cover-letter.html`: the fixed page size and style.
* `output/resume.md`: your base resume, with its HTML and PDF.
* `output/applications/`: one folder per job, with the job description, resume, and cover letter.
