# Resume Versions — Akhilesh Kumar Mishra

A browser-based resume studio: four role-targeted resumes, each rendered in five
templates, with PDF / Word / LaTeX downloads for every combination.

**Live site:** https://github-akhilesh.github.io/resume_versions/

## The four versions

Each version is **single-stack by design** — it names only the technologies that
matter for that role, so a keyword screen sees a focused match instead of a
diluted one.

| Version | Role | Stack it talks about |
|---|---|---|
| `version1` | MERN Stack Developer | React, Next.js, Redux Toolkit, Node.js, Express, MongoDB |
| `version2` | Java Full Stack Developer | Java, Spring Boot, Spring Security, JPA/Hibernate, MySQL/PostgreSQL, Kafka |
| `version3` | Python Full Stack Developer | Python, Django, DRF, FastAPI, Celery, SQLAlchemy, PostgreSQL |
| `version4` | Software Development Engineer | Deliberately polyglot: architecture, scale, reliability, and team leadership |

`version4` is the generalist resume, so a mixed stack is the point there. The
other three never cross over.

## Templates

`Modern Grid`, `Classic`, `Minimal Serif`, `Executive` (two-column) and
`Two Column`. Every template is tuned to print as a **single** Letter page —
that is enforced by the build, not assumed.

## Using the page

- Pick a role and a template in the left panel.
- `PDF` / `Word` / `LaTeX` download the matching prebuilt file.
- `Print` opens the browser print dialog (choose *Save as PDF*) — useful if you
  want the page exactly as rendered.
- `Copy link` gives a deep link to one specific resume, e.g.
  `?role=java&template=executive`.
- Keyboard: `1`–`4` role, `[` / `]` template, `P` print, `+` / `-` / `0` zoom.

## Rebuilding

```
pip install lxml python-docx
python generate_downloads.py
```

That regenerates all 60 files in `downloads/` and refreshes the `version*.md`
sources. It needs Chrome or Edge installed (used headlessly for PDF rendering).

To change resume wording, edit `build/content.py` — the single source of truth —
then run:

```
python build/apply_content.py index.html   # rewrite all 20 sheets in the page
python generate_downloads.py              # rebuild every download
```

`build/apply_content.py` is idempotent, so running it twice is a no-op.

### Build layout

| File | Role |
|---|---|
| `build/content.py` | All resume copy, per version. Edit this. |
| `build/apply_content.py` | Writes that copy into the 20 sheets in `index.html`. |
| `build/render_pdfs.py` | Renders each sheet to a single-page PDF via headless Chrome. |
| `build/gen_latex.py` | Generates `downloads/*.tex`. |
| `build/gen_md.py` | Regenerates the `version*.md` documents. |
| `generate_downloads.py` | Runs the whole pipeline (LaTeX → Word → PDF → markdown). |

A note on PDFs: this used to use Playwright, but `pip install playwright` fails
on Python 3.9 / Windows here because `greenlet` has no matching wheel and needs
a C toolchain. `build/render_pdfs.py` drives the already-installed Chrome with
`--headless --print-to-pdf` instead, flattening each variant into its own
single-sheet page first so the output is deterministic.

### Verifying single-page fit

```
python build/render_pdfs.py shot      # PNGs at exact page size, into build/.cache/shots
```

Each PNG is exactly one Letter page, so anything clipped off the bottom shows up
immediately. (Printing an auto-height sheet and counting PDF pages looks like a
neater check but does not work: Chrome ignores the `@page` margin reset under
`--print-to-pdf`, so sheets that actually fit still report two pages.)

`index.html` and `resume_preview.html` are kept identical — the Word generator
reads the latter.
