# Set Me Up

Make this project mine. Ask one thing at a time, and wait for each answer before asking the next. Keep each question to a sentence or two.

## 1. My resume first

Start by asking for my current resume, and encourage me to share it: the more you have, the fewer questions I need to answer. If I don't have a resume, ask for my LinkedIn profile instead. On LinkedIn, open your profile, click **More**, then **Save to PDF**. A portfolio or project write-ups help too.

I can paste text in Chat or drop files into `materials/`. If I paste text, save it as a file in `materials/`, like `materials/old-resume.md`. If I have nothing yet, that's fine. Move on.

Read everything in `materials/` before asking anything else.

## 2. My GitHub

If my materials don't include a GitHub link, ask for my username. If I don't have one, move on.

If I do, read my public profile: pinned repositories first, then my most recent repositories with real work in them. Skip forks I haven't committed to and class templates. For each one worth a closer look, read the README, the main languages, and the commit history to see how much of it I wrote. Use `gh` if it's installed, or fetch the pages on github.com. If you can't reach GitHub, tell me and move on.

A README says what a project does, not what I did. In a repository with several contributors, take only what the commits show as mine, and ask me about the rest.

## 3. The basics

Ask only what my materials and GitHub don't already answer:

1. **What's your name?**
2. **Where are you now?** School, year, and major. If you're working, your current role.
3. **What kind of job are you looking for?** The role, the industry, and whether it's an internship or full-time.
4. **Where are you applying?** The country or region.

## 4. My question list

Then, in one go:

* Rewrite [profile.md](../context/profile.md) from my answers, under its headings. Drop the example content. Set the paper to Letter if I'm applying in the US or Canada, and A4 anywhere else. Set pages to 1 unless I have more than about ten years of experience.
* Delete the example resume in `output/` (`resume.md` and its HTML and PDF) and the example folders in `output/applications/`.
* Replace [experience.md](../context/experience.md) with my question list, written as below.
* Tell me it's done in a sentence or two. I have two ways to answer: open `context/experience.md` and write under the questions, starting with the ones marked ⭐, or say "Interview me" and you'll ask them one at a time in Chat. Rough notes are fine either way, and I can skip any I can't answer. When I'm done, I say "Write my resume."

### How to write the question list

Write about 20 questions for my situation and the job I want. Mark the 5–8 that matter most for that job with ⭐.

Group them by section, with one block for each experience. Build on my materials and GitHub: don't ask for what's already there. Ask about what's behind it instead, like what I did myself, why I made a choice, and what came of it.

Sections, in this order:

* **Contact:** email, phone, city, LinkedIn, and GitHub or portfolio, each on its own line to fill in.
* **Education**
* **Each internship or job**
* **Each research position:** lab or thesis work. If I'm a student and my materials show none, ask once in its own block whether I've done any research or have papers, posters, or preprints.
* **Each project**
* **Open source:** contributions to projects I don't own. If my GitHub shows pull requests to other projects, give each its own block. If not, ask once whether I've contributed anywhere.
* **Awards and competitions:** hackathons, coding contests like ICPC or Kaggle, and scholarships, with placement and how many took part.
* **Activities and leadership**
* **Skills:** technical skills, certifications, and languages.
* **What should a recruiter remember about you?**

If I have little experience so far, ask about class projects, competitions, clubs, part-time work, and volunteering. Most people have done more than they think.

Good questions ask for one specific thing at a time:

* What did you build or do yourself, not the team?
* What changed because of it? Users, time saved, money, a ranking, a grade.
* What tools or methods did you use, and why those?
* What was the hardest technical problem, and how did you solve it?

When you found facts on GitHub, put them at the top of that block as bullets under "From GitHub", so I can correct anything wrong. Format each block like this, with a blank line under each question for my answer:

```markdown
## Project: Campus Lost & Found (Jan–Mar 2026)

From GitHub, correct anything wrong:

* Android app in Kotlin with a Firebase backend. github.com/you/lost-and-found
* Two contributors. Your commits are mostly in `matching/` and `functions/`.

⭐ **The matching logic looks like yours. How does it decide two items match?**

**Can you put a number on the result?** Installs, users, items returned.
```
