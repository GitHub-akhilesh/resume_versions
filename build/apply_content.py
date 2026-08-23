# -*- coding: utf-8 -*-
"""Rewrite every resume sheet in index.html with role-pure content.

The page renders each version in five template styles, and the styles use four
different markup dialects for skills and projects. Everything is replaced
positionally inside each sheet so a missing target is a hard error, never a
silent no-op.
"""
import io, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import VERSIONS

SRC = sys.argv[1] if len(sys.argv) > 1 else "index.html"

def sheets_end(src):
    """Where the last resume sheet stops.

    The page used to end its sheets with four inline <script type="text/plain">
    LaTeX payloads. Those were unreferenced and held pre-cleanup content, so
    they were removed; the canvas close tag is the boundary now. The old marker
    is still honoured so this works on an unmigrated page.
    """
    for marker in ("</div><!-- /canvas -->", '<script type="text/plain" id="latex-version1"'):
        i = src.find(marker)
        if i != -1:
            return i
    raise ValueError("cannot find the end of the resume sheets")


def norm(s):
    return s.replace("&amp;", "&").replace("&middot;", u"·")

errors = []

def replace_positional(blk, pattern, builders, what, block_name,
                       allow_fewer=False):
    """Replace the i-th match of `pattern` with builders[i](match).

    With allow_fewer, surplus markup slots are deleted rather than treated as
    an error -- that is how a version drops from six project cards to four.
    """
    matches = list(re.finditer(pattern, blk, re.S))
    if len(matches) != len(builders):
        if not (allow_fewer and len(builders) < len(matches)):
            errors.append("%s: %s -> found %d targets, have %d replacements"
                          % (block_name, what, len(matches), len(builders)))
            return blk
    out, last = [], 0
    for i, m in enumerate(matches):
        out.append(blk[last:m.start()])
        if i < len(builders):
            out.append(builders[i](m))
        last = m.end()
    out.append(blk[last:])
    return "".join(out)


def rewrite_block(blk, name, data):
    ver = name.split("-")[0]
    ats, title = data["ats"], norm(data["title"])
    summary = norm(data["summary"])
    skills = [(norm(a), norm(b)) for a, b in data["skills"]]
    projects = [tuple(norm(x) for x in p) for p in data["projects"]]
    certs = [norm(c) for c in data["certs"]]
    exp = [[norm(b) for b in group] for group in data["exp"]]

    # --- ATS badge, role title, profile summary -------------------------
    blk = replace_positional(blk, r'ATS: \d+%', [lambda m: "ATS: %s%%" % ats],
                             "ats", name)
    blk = replace_positional(blk, r'(?<=class="title">)[^<]*',
                             [lambda m: title], "title", name)
    blk = replace_positional(blk, r'(?<=class="summary-text">)[^<]*',
                             [lambda m: summary], "summary", name)

    # --- Skills: three dialects, whichever this style uses --------------
    line_pat = (r'<div class="skills-line">\s*<strong>[^<]*</strong>\s*'
                r'[^<]*\s*</div>')
    if re.search(line_pat, blk):
        blk = replace_positional(blk, line_pat, [
            (lambda lb, ct: lambda m:
             '<div class="skills-line">\n                    '
             '<strong>%s</strong>\n                    %s\n                </div>'
             % (lb, ct))(lb, ct) for lb, ct in skills],
            "skills-line", name)

    exec_pat = (r'<div class="edu-item">\s*<strong>[^<]*</strong><br>\s*'
                r'[^<]*\s*</div>')
    if 'class="sidebar-skills"' in blk:
        start = blk.index('<div class="sidebar-skills">')
        stop = blk.index('<div class="sec-title">', start)
        head, region, tail = blk[:start], blk[start:stop], blk[stop:]
        region = replace_positional(region, exec_pat, [
            (lambda lb, ct: lambda m:
             '<div class="edu-item">\n                    '
             '<strong>%s</strong><br>\n                    %s\n                </div>'
             % (lb, ct))(lb, ct) for lb, ct in skills],
            "executive-skills", name)
        blk = head + region + tail

    sec_pat = (r'<div class="skills-section">\s*<div class="skills-sec-title">'
               r'[^<]*</div>\s*<div class="skills-container">\s*.*?\s*</div>\s*</div>')
    if 'class="skills-section"' in blk:
        def enhancv(lb, ct):
            chips = "".join('<span class="skill-tag">%s</span>' % s.strip()
                            for s in ct.split(","))
            return lambda m: (
                '<div class="skills-section">\n                    '
                '<div class="skills-sec-title">%s</div>\n                    '
                '<div class="skills-container">\n                        %s\n'
                '                    </div>\n                </div>' % (lb, chips))
        blk = replace_positional(blk, sec_pat,
                                 [enhancv(lb, ct) for lb, ct in skills],
                                 "enhancv-skills", name)

    # --- Experience bullets (two roles, same markup everywhere) ---------
    blk = replace_positional(blk, r'<ul class="bullet-list">\s*.*?\s*</ul>', [
        (lambda g: lambda m: '<ul class="bullet-list">\n                            %s\n                        </ul>'
         % "".join("<li>%s</li>" % b for b in g))(g) for g in exp],
        "bullets", name)

    # --- Projects: card dialect (modern / executive / enhancv) ----------
    # modern nests title+desc in a wrapper div so the stack line pins to the
    # bottom of the flex card; executive/enhancv keep the card flat.
    card_pat = (r'<div class="project-card">\s*(<div>\s*)?'
                r'<div class="project-title">[^<]*</div>\s*'
                r'<div class="project-desc">[^<]*</div>\s*(</div>\s*)?'
                r'<div class="project-stack"><strong>STACK:</strong>[^<]*</div>\s*</div>')
    if 'class="project-card"' in blk:
        def card(t, d, s):
            def build(m):
                if m.group(1):
                    return ('<div class="project-card">\n                    <div>\n'
                            '                        <div class="project-title">%s</div>\n'
                            '                        <div class="project-desc">%s</div>\n'
                            '                    </div>\n'
                            '                    <div class="project-stack"><strong>STACK:</strong> %s</div>\n'
                            '                </div>' % (t, d, s))
                return ('<div class="project-card">\n'
                        '                    <div class="project-title">%s</div>\n'
                        '                    <div class="project-desc">%s</div>\n'
                        '                    <div class="project-stack"><strong>STACK:</strong> %s</div>\n'
                        '                </div>' % (t, d, s))
            return build
        blk = replace_positional(blk, card_pat, [card(*p) for p in projects],
                                 "project-cards", name, allow_fewer=True)

    # --- Projects: grid dialect (classic / minimal) ---------------------
    if '<div class="projects-grid">' in blk and 'class="project-card"' not in blk:
        start = blk.index('<div class="projects-grid">')
        stop = blk.index('<div class="section-title">', start)
        head, region, tail = blk[:start], blk[start:stop], blk[stop:]
        grid_pat = (r'<div class="experience-item">\s*'
                    r'<div class="role-title">[^<]*</div>\s*'
                    r'<div class="meta-line">[^<]*</div>\s*'
                    r'<div class="project-desc">[^<]*</div>\s*</div>')
        def grid(t, d, s):
            return lambda m: (
                '<div class="experience-item">\n'
                '                <div class="role-title">%s</div>\n'
                '                <div class="meta-line">%s</div>\n'
                '                <div class="project-desc">%s</div>\n'
                '            </div>' % (t, s, d))
        region = replace_positional(region, grid_pat,
                                    [grid(*p) for p in projects],
                                    "project-grid", name, allow_fewer=True)
        blk = head + region + tail

    # --- Certifications -------------------------------------------------
    blk = replace_positional(blk, r'(?<=class="cert-list")([^>]*>)\s*.*?\s*(?=</div>)', [
        lambda m: m.group(1) + "\n                        "
        + "<br>\n                        ".join(certs) + "\n                    "],
        "certs", name)
    return blk


def main():
    src = io.open(SRC, encoding="utf-8").read()
    ids = [(m.start(), m.group(1)) for m in
           re.finditer(r'<div id="(version\d-\w+)" class="resume-sheet', src)]
    end = sheets_end(src)

    out, last = [], 0
    for i, (s, name) in enumerate(ids):
        e = ids[i + 1][0] if i + 1 < len(ids) else end
        out.append(src[last:s])
        out.append(rewrite_block(src[s:e], name, VERSIONS[name.split("-")[0]]))
        last = e
    out.append(src[last:])
    result = "".join(out)

    if errors:
        print("FAILED - no file written:")
        for e in errors:
            print("  " + e)
        return 1
    io.open(SRC, "w", encoding="utf-8").write(result)
    print("Rewrote %d resume sheets in %s" % (len(ids), SRC))
    return 0


if __name__ == "__main__":
    sys.exit(main())
