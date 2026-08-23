# -*- coding: utf-8 -*-
"""Regenerate the four version*.md source documents from content.py.

The markdown files described the pre-cleanup resumes (mixed stacks, projects
that no longer exist), so they contradicted the site. Generating them from the
same dict keeps every artifact telling one story.
"""
import io, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import VERSIONS
from gen_latex import build as build_latex, JOBS, ACHIEVEMENTS

REPO = os.path.abspath(os.environ.get("REPO", "."))

FILES = {"version1": ("version1_mern.md", "MERN Stack Developer"),
         "version2": ("version2_java.md", "Java Full Stack Developer"),
         "version3": ("version3_python.md", "Python Full Stack Developer"),
         "version4": ("version4_combined.md", "Software Engineer (Generalist)")}
ORDER = ["version1", "version2", "version3", "version4"]

GAPS = {
 "version1": ["Add automated testing depth: Jest and React Testing Library unit"
              " coverage, plus Supertest for Express route integration tests.",
              "Mention a managed deployment target for Node services (AWS ECS,"
              " Elastic Beanstalk, or Render) alongside Docker.",
              "Add server-side rendering and caching specifics for Next.js"
              " (ISR, route handlers, edge caching)."],
 "version2": ["Add unit and integration testing with JUnit 5, Mockito, and"
              " Testcontainers.",
              "Mention a cloud runtime for Spring services (AWS ECS, Elastic"
              " Beanstalk, or Kubernetes).",
              "Add API contract documentation with OpenAPI/Swagger and"
              " versioning strategy."],
 "version3": ["Add testing depth with pytest, pytest-asyncio, and factory"
              " fixtures for DRF/FastAPI endpoints.",
              "Mention Celery observability (Flower, task retries, dead-letter"
              " handling) and worker autoscaling.",
              "Add type safety and validation specifics: mypy, Pydantic models,"
              " and schema versioning."],
 "version4": ["Add a system design artifact: a short architecture write-up or"
              " diagram for the transaction platform.",
              "Mention SLOs, error budgets, and on-call/incident response"
              " practice alongside Prometheus and Grafana.",
              "Add infrastructure-as-code exposure (Terraform or Helm) to"
              " strengthen the platform story."]}


def strip(s):
    """Markdown wants literal characters, and bold as **...**."""
    s = s.replace("&amp;", "&").replace("&middot;", u"·")
    return s.replace("<strong>", "**").replace("</strong>", "**")


def main():
    for i, ver in enumerate(ORDER, start=1):
        data = VERSIONS[ver]
        fname, role = FILES[ver]
        o = []
        o.append("# Resume Version %d: %s\n" % (i, role))
        o.append("> Single-stack by design. This version mentions only the"
                 " technologies relevant to the target role.\n")

        o.append("\n## 1. Professional Summary\n")
        o.append(strip(data["summary"]) + "\n")

        o.append("\n## 2. Technical Skills\n")
        for lb, ct in data["skills"]:
            o.append("* **%s:** %s\n" % (strip(lb), strip(ct)))

        o.append("\n## 3. Experience\n")
        for job, bullets in zip(JOBS, data["exp"]):
            o.append("### %s\n" % job["role"])
            o.append("**%s**\n" % strip(job["company"].replace("\\&", "&")))
            o.append("*%s | %s*\n" % (job["dates"].replace("--", "–"),
                                      job["place"]))
            for b in bullets:
                o.append("* %s\n" % strip(b))
            o.append("\n")

        o.append("## 4. Projects\n")
        for t, d, st in data["projects"]:
            o.append("### %s\n" % strip(t))
            o.append("*Stack: %s*\n" % strip(st))
            o.append("%s\n\n" % strip(d))

        o.append("## 5. Education\n")
        o.append("### Bachelor of Technology (B.Tech.)\n")
        o.append("**Kanpur Institute of Technology** | *Kanpur, UP*\n")
        o.append("*07/2019 – 05/2023*\n")

        o.append("\n## 6. Certifications\n")
        for c in data["certs"]:
            o.append("* %s\n" % strip(c))

        o.append("\n## 7. Achievements\n")
        for a in ACHIEVEMENTS:
            o.append("* %s\n" % a)

        o.append("\n## 8. ATS Score Estimate\n")
        o.append("* **%s/100** — keyword coverage is concentrated on a"
                 " single stack, so role-matched screens score higher and"
                 " nothing dilutes the match.\n" % data["ats"])

        o.append("\n## 9. Missing Skills Recommendations\n")
        for g in GAPS[ver]:
            o.append("* %s\n" % g)

        o.append("\n## 10. Complete LaTeX Resume Code\n")
        o.append("```latex\n")
        clean = dict(data)
        clean["title"] = data["title"].replace("&amp;", "&").replace("&middot;", u"·")
        clean["summary"] = data["summary"].replace("&amp;", "&")
        clean["skills"] = [(a.replace("&amp;", "&"), b.replace("&amp;", "&"))
                           for a, b in data["skills"]]
        clean["projects"] = [tuple(x.replace("&amp;", "&") for x in p)
                             for p in data["projects"]]
        clean["exp"] = [[b.replace("&amp;", "&") for b in g] for g in data["exp"]]
        o.append(build_latex(clean, "0c4f6b"))
        o.append("```\n")

        path = os.path.join(REPO, fname)
        io.open(path, "w", encoding="utf-8").write("".join(o))
        print("wrote %s" % fname)


if __name__ == "__main__":
    main()
