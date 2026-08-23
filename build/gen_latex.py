# -*- coding: utf-8 -*-
"""Generate downloads/*.tex from content.py.

The old .tex files were extracted from the markdown files, so they carried the
pre-cleanup cross-stack content (and were missing \\begin{document}, so they
would not compile). Generating them from the same dict that drives the HTML
keeps all three download formats saying the same thing.
"""
import io, os, re, sys
try:
    from html import unescape as html_unescape
except ImportError:                     # Python 2 fallback
    from HTMLParser import HTMLParser
    html_unescape = HTMLParser().unescape

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import VERSIONS

REPO = os.path.abspath(os.environ.get("REPO", "."))
DOWNLOADS = os.path.join(REPO, "downloads")

NAMES = {"version1": "Akhilesh_Mishra_MERN_Stack",
         "version2": "Akhilesh_Mishra_Java_Full_Stack",
         "version3": "Akhilesh_Mishra_Python_Full_Stack",
         "version4": "Akhilesh_Mishra_Software_Engineer"}
# style suffix -> accent colour, mirroring the on-page themes
STYLE_COLORS = {"": "0c4f6b", "_Classic": "0056b3", "_Minimal": "1a1a1a",
                "_Executive": "1e293b", "_Enhancv": "007bb6"}

JOBS = [
    {"role": "Software Development Engineer",
     "company": "CSC e-Governance Services India Ltd. (MeitY, Government of India)",
     "dates": "12/2023 -- Present", "place": "New Delhi, India"},
    {"role": "Freelance Software Engineer",
     "company": "Workforce Telemetry \\& Operations",
     "dates": "06/2023 -- 11/2023", "place": "Remote, India"},
]

ACHIEVEMENTS = ["Graduated with First Class Honors, maintaining top academic rank.",
                "Earned a 4-Star Gold Badge in SQL on HackerRank."]

ESCAPES = [("\\", r"\textbackslash{}"), ("&", r"\&"), ("%", r"\%"),
           ("$", r"\$"), ("#", r"\#"), ("_", r"\_"),
           ("{", r"\{"), ("}", r"\}"),
           ("~", r"\textasciitilde{}"), ("^", r"\textasciicircum{}")]


def tex(s):
    """Escape plain text for LaTeX.

    Entities are decoded first: content.py stores HTML, so &amp; / &mdash; /
    &middot; arrive spelled out and must become real characters before the
    backslash escaping runs (otherwise the & in "&mdash;" gets escaped and the
    entity name is printed verbatim).
    """
    s = html_unescape(s)
    for a, b in ESCAPES:
        s = s.replace(a, b)
    return (s.replace(u"\u00b7", r"$\cdot$")
             .replace(u"\u2014", "---")
             .replace(u"\u2013", "--"))


def rich(s):
    """Escape text that may carry <strong> emphasis, keeping the bold."""
    parts = re.split(r"(<strong>|</strong>)", s)
    out, depth = [], 0
    for p in parts:
        if p == "<strong>":
            out.append(r"\textbf{")
            depth += 1
        elif p == "</strong>":
            if depth:
                out.append("}")
                depth -= 1
        else:
            out.append(tex(p))
    out.append("}" * depth)
    return "".join(out)


PREAMBLE = r"""\documentclass[10pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[margin=0.45in]{geometry}
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{xcolor}
\usepackage{hyperref}
\usepackage{fontawesome5}
\usepackage{enumitem}

\definecolor{primaryblue}{HTML}{%(color)s}
\definecolor{darkgray}{HTML}{333333}

\hypersetup{colorlinks=true, linkcolor=primaryblue, urlcolor=primaryblue}

\pagestyle{empty}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}

\newcommand{\resumesection}[1]{%%
  \vspace{6pt}%%
  {\fontfamily{phv}\selectfont\textbf{\large\MakeUppercase{#1}}}%%
  \vspace{2pt}%%
  \hrule%%
  \vspace{4pt}%%
}

\setlist[itemize]{leftmargin=*,noitemsep,topsep=0pt,parsep=0pt,partopsep=0pt,label=\textbullet}

\begin{document}

\begin{center}
    {\fontfamily{phv}\selectfont\textbf{\Huge AKHILESH KUMAR MISHRA}} \\
    \vspace{3pt}
    {\fontfamily{phv}\selectfont\large\textbf{\textcolor{primaryblue}{%(title)s}}} \\
    \vspace{4pt}
    {\small
    \textcolor{primaryblue}{\faPhone*}~+91 88580 45785 \quad | \quad
    \href{mailto:makhileshkumar1@gmail.com}{\textcolor{primaryblue}{\faEnvelope}~makhileshkumar1@gmail.com} \quad | \quad
    \href{https://linkedin.com/in/akhilesh-kumar-mishra-a46030231}{\textcolor{primaryblue}{\faLinkedin}~linkedin.com/in/akhilesh-kumar-mishra} \quad | \quad
    \href{https://github.com/GitHub-akhilesh}{\textcolor{primaryblue}{\faGithub}~github.com/GitHub-akhilesh}
    }
\end{center}
\vspace{-10pt}
"""


def build(data, color):
    out = [PREAMBLE % {"color": color, "title": tex(data["title"])}]

    out.append("\n\\resumesection{Summary}\n" + tex(data["summary"]) + "\n")

    out.append("\n\\resumesection{Experience}\n")
    for i, (job, bullets) in enumerate(zip(JOBS, data["exp"])):
        if i:
            out.append("\n\\vspace{4pt}\n")
        out.append("{\\textbf{%s}} \\\\\n" % tex(job["role"]))
        out.append("{\\textbf{\\textcolor{primaryblue}{%s}}} \\\\\n" % job["company"])
        out.append("{\\footnotesize\\textcolor{primaryblue}{\\faCalendar*}~%s "
                   "\\quad | \\quad \\textcolor{primaryblue}{\\faMapMarker*}~%s}\n"
                   % (job["dates"], tex(job["place"])))
        out.append("\\begin{itemize}\n")
        for b in bullets:
            out.append("    \\item %s\n" % rich(b))
        out.append("\\end{itemize}\n")

    out.append("\n\\resumesection{Projects}\n")
    for i, (t, d, s) in enumerate(data["projects"]):
        if i:
            out.append("\n\\vspace{4pt}\n")
        out.append("{\\textbf{%s}} \\\\\n" % tex(t))
        out.append("{\\small %s} \\\\\n" % tex(d))
        out.append("{\\footnotesize\\textbf{STACK:} %s}\n" % tex(s))

    out.append("\n\\resumesection{Skills}\n")
    out.append(" \\\\\n".join("\\textbf{%s:} %s" % (tex(lb), tex(ct))
                              for lb, ct in data["skills"]) + "\n")

    out.append("\n\\resumesection{Education}\n")
    out.append("{\\textbf{Bachelor of Technology (B.Tech.)}} \\\\\n")
    out.append("{\\textbf{\\textcolor{primaryblue}{Kanpur Institute of Technology}}} \\\\\n")
    out.append("{\\footnotesize\\textcolor{primaryblue}{\\faCalendar*}~07/2019 -- 05/2023"
               " \\quad | \\quad \\textcolor{primaryblue}{\\faMapMarker*}~Kanpur, UP}\n")

    out.append("\n\\resumesection{Certifications}\n")
    certs = [tex(c.replace("&amp;", "&")) for c in data["certs"]]
    out.append(" \\quad | \\quad ".join(certs[:2]) + " \\\\\n")
    out.append(" \\quad | \\quad ".join(certs[2:]) + "\n")

    out.append("\n\\resumesection{Achievements}\n\\begin{itemize}\n")
    for a in ACHIEVEMENTS:
        out.append("    \\item %s\n" % tex(a))
    out.append("\\end{itemize}\n\n\\end{document}\n")
    return "".join(out)


def main():
    if not os.path.isdir(DOWNLOADS):
        os.makedirs(DOWNLOADS)
    n = 0
    for ver, data in sorted(VERSIONS.items()):
        # No entity prep here: tex() decodes entities itself, so every field
        # gets the same treatment and a new entity cannot be missed.
        for suffix, color in sorted(STYLE_COLORS.items()):
            path = os.path.join(DOWNLOADS, NAMES[ver] + suffix + ".tex")
            io.open(path, "w", encoding="utf-8").write(build(data, color))
            n += 1
    print("Generated %d .tex files" % n)


if __name__ == "__main__":
    main()
