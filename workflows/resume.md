# Write My Resume

## First draft

When I say "Write my resume":

1. Read [profile.md](../context/profile.md), [experience.md](../context/experience.md), and everything in `materials/`.
2. Turn [experience.md](../context/experience.md) into my experience notes. For each experience, keep every fact from my answers and materials as short bullet points in my words: what I did, tools, numbers, results, and links. Keep facts you found on GitHub that I didn't correct, and drop the ones I said were wrong. Remove the questions. Move unanswered questions that matter for the job I want to a "Still missing" section at the end, and drop the rest.
3. Write `output/resume.md`, following the rules and format below.
4. Review it, following [Review](#review), and fix what you can.
5. Export it to PDF, following [export.md](export.md).
6. Tell me it's ready in a sentence or two. Then name up to three gaps that would most improve it for the job I want, like a missing number. I can answer any of them, say "Interview me" to go through them in Chat, or just tell you what to change.

## Edits

When I answer a gap or share new details, add them to my experience notes first, then update the resume. When I ask for a change, make it in place. Either way, export again.

## What goes in

My notes hold everything; the resume is a selection. Pick what best shows I can do the job I want, and leave the rest in the notes.

* **Sections:** Contact, then Education, Experience, Projects, Activities, and Skills. If I've been working for a few years, put Experience before Education. No summary or objective unless I ask.
* **Optional sections:** Add these only when I have entries that earn them. Research goes after Experience, for lab or thesis work with a supervisor. Publications goes after Research, for papers, posters, and preprints, with my name as it appears on them. Open Source goes after Projects, for contributions to projects I don't own, with links to merged pull requests or the project. Awards goes before Activities, for competitions, hackathons, and scholarships. A single award fits better as a bullet under Education or the project it came from than as its own section.
* **Order:** Most recent first within each section.
* **Bullets:** Two to four per entry, most relevant first. Start with a verb, say what I did and what came of it, and keep each to one line, two at most. Use numbers wherever I gave them.
* **Technical work:** Name the tool where it did the work ("added a PostgreSQL index"), not as a list tacked on the end. For projects, say what it does and give the result: users, speed, scale, a ranking, or that it's still running. If a project is open source, link the repo. If it was a team project, say what part was mine.
* **Skills:** Group by kind, like Languages, Frameworks, and Tools. List only what I've used in something on the resume or in my notes, and that I could talk about in an interview. Mark something "basic" if my notes say so. No skill bars or percentages.
* **Tense:** Past for things I've finished, present for what I'm still doing.
* **Leave out:** Photo, date of birth, and other personal details, unless my profile says they're expected where I'm applying.
* **Length:** The page limit in my profile.

## Review

Before exporting, read the resume the way a recruiter does: about ten seconds on the first pass, mostly the top third, then the bullets for anything that matches the job. Then check each point below. Fix what you can from my notes. If a fix needs something only I know, add it to the gaps you tell me about instead.

* **Top third:** My strongest match for the job is in the top third of the page, not buried under a long Education entry.
* **Results:** Every bullet says what came of the work. A bullet that only describes a duty ("responsible for…", "worked on…") gets a result from my notes, or gets cut, or becomes a gap.
* **Mine:** Each bullet says what I did myself, not what the team did.
* **True:** Every number, tool, title, and date matches my notes exactly, with nothing rounded up.
* **Skills:** Every skill listed shows up in a bullet or in my notes. The most relevant ones for the job come first in each group.
* **Variety:** No two bullets in a row start with the same verb, and the same word doesn't carry half the page.
* **Consistent:** Dates, places, and punctuation follow one style throughout.

## Format

Keep this format exactly. [scripts/build.py](../scripts/build.py) turns it into HTML, and only understands these lines.

```markdown
# Full Name

email · phone · City, Country · linkedin.com/in/you · github.com/you

## Experience

### Company or school | City, Country
Role or degree | Mon YYYY – Mon YYYY

- What I did and what came of it.

## Publications

- A. Author, F. Name. "Paper Title." *Venue*, YYYY.

## Skills

**Label:** item, item, item
```

Each entry is a `###` line plus the line under it. Text before ` | ` shows on the left, text after it on the right; the right side is optional. For a project, put the link on the right of the `###` line and the tools on the left of the line under it. For research, put the lab or school on the `###` line and my role and supervisor under it. Publications and Awards can be plain bullets under the section heading, without `###` entries. Use `**bold**` and `*italic*` only inside a line, and keep each bullet on one line in the file.
