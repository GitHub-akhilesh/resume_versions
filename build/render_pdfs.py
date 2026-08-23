# -*- coding: utf-8 -*-
"""Render every resume variant in index.html to a single-page PDF.

Why not Playwright: it needs to build greenlet, which has no wheel for the
Python 3.9 / Windows toolchain on this machine, so `pip install playwright`
fails. Headless Chrome (already installed) does the same job through
--print-to-pdf.

Each variant is first flattened into its own temporary page holding exactly one
sheet. That removes the tab-clicking and JS-timing that the old Playwright path
depended on, so output is deterministic. Chrome cold start dominates the
runtime, so launches run in parallel with isolated profiles and a hard timeout
(a wedged headless Chrome otherwise hangs forever).

Usage:
    python build/render_pdfs.py            # all 20 variants -> downloads/*.pdf
    python build/render_pdfs.py shot       # PNGs at exact page size, for eyeballing
    python build/render_pdfs.py pdf version4-classic

Single-page fit is checked with `shot`: the PNG is exactly one Letter page, so
anything clipped off the bottom is visible. Printing an auto-height sheet and
counting PDF pages does not work -- Chrome ignores the @page margin reset under
--print-to-pdf, so a sheet that fits still spills onto a second page.
"""
import io, os, re, shutil, subprocess, sys, tempfile, threading

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, os.pardir))
WORKERS = 4
LAUNCH_TIMEOUT = 120

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    "/usr/bin/google-chrome", "/usr/bin/chromium-browser",
]

VERSIONS = {"version1": "Akhilesh_Mishra_MERN_Stack",
            "version2": "Akhilesh_Mishra_Java_Full_Stack",
            "version3": "Akhilesh_Mishra_Python_Full_Stack",
            "version4": "Akhilesh_Mishra_Software_Engineer"}
STYLES = {"modern": "", "classic": "_Classic", "minimal": "_Minimal",
          "executive": "_Executive", "enhancv": "_Enhancv"}

_COMMON = """
  html, body { background:#fff !important; margin:0 !important; padding:0 !important;
               height:auto !important; overflow:visible !important; display:block !important; }
  .sidebar, .action-bar, .ats-badge, .open-sidebar-btn, .topbar,
  .toast, .zoom-bar { display:none !important; }
  .preview-area, .canvas { padding:0 !important; margin:0 !important;
               overflow:visible !important; display:block !important; width:100% !important; }
  .resume-wrapper { display:block !important; height:auto !important; }
  .resume-sheet { display:none !important; }
"""

# The fixed Letter sheet is what actually ships.
FIXED = """<style id="flatten">%s
  .resume-sheet.active {
      display:block !important; box-shadow:none !important; border-radius:0 !important;
      width:8.5in !important; height:11.0in !important; padding:0.35in 0.4in !important;
      box-sizing:border-box !important; margin:0 !important; overflow:hidden !important;
      transform:none !important; }
</style>
</head>""" % _COMMON



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


def find_browser():
    for c in CHROME_CANDIDATES:
        if os.path.exists(c):
            return c
    return None


def flatten(src_path, stage, override):
    """Write one standalone single-sheet page per variant. Returns [(name, path)]."""
    src = io.open(src_path, encoding="utf-8").read()
    head = src[:src.index("</head>")]
    ids = [(m.start(), m.group(1)) for m in
           re.finditer(r'<div id="(version\d-\w+)" class="resume-sheet', src)]
    end = sheets_end(src)
    made = []
    for i, (s, name) in enumerate(ids):
        e = ids[i + 1][0] if i + 1 < len(ids) else end
        sheet = re.sub(r'(<div id="%s" class="resume-sheet)( active)?' % name,
                       r'\1 active', src[s:e], count=1)
        path = os.path.join(stage, name + ".html")
        io.open(path, "w", encoding="utf-8").write(
            head + override + "\n<body>\n" + sheet + "\n</body>\n</html>\n")
        made.append((name, path))
    return made


def chrome(browser, profile, args):
    cmd = [browser, "--headless=new", "--disable-gpu", "--no-sandbox",
           "--user-data-dir=" + profile, "--no-first-run",
           "--no-default-browser-check", "--disable-sync", "--disable-extensions",
           "--disable-component-update", "--disable-default-apps",
           "--metrics-recording-only", "--hide-scrollbars"] + args
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        p.communicate(timeout=LAUNCH_TIMEOUT)
        return p.returncode
    except subprocess.TimeoutExpired:
        p.kill()
        p.communicate()
        return -1


def outname(name):
    ver, style = name.split("-")
    return VERSIONS[ver] + STYLES[style]


def pdf_pages(path):
    data = io.open(path, "rb").read()
    n = len(re.findall(br"/Type\s*/Page[^s]", data))
    if not n:
        m = re.search(br"/Count\s+(\d+)", data)
        n = int(m.group(1)) if m else 0
    return n


def run(mode="pdf", only=None, repo=REPO):
    browser = find_browser()
    if not browser:
        print("ERROR: no Chrome or Edge found; cannot render PDFs")
        return 1
    src = os.path.join(repo, "index.html")
    downloads = os.path.join(repo, "downloads")
    shots = os.path.join(HERE, ".cache", "shots")
    for d in (downloads, shots):
        if not os.path.isdir(d):
            os.makedirs(d)

    stage = tempfile.mkdtemp(prefix="resume_stage_")
    profiles = [tempfile.mkdtemp(prefix="resume_prof_") for _ in range(WORKERS)]
    print("Browser: %s | mode: %s" % (browser, mode))
    try:
        variants = flatten(src, stage, FIXED)
        if only:
            variants = [v for v in variants if v[0] in only]
        print("Rendering %d variant(s) on %d workers" % (len(variants), WORKERS))

        results, lock, queue = {}, threading.Lock(), list(variants)

        def work(wid):
            while True:
                with lock:
                    if not queue:
                        return
                    name, path = queue.pop(0)
                url = "file:///" + path.replace("\\", "/")
                if mode == "shot":
                    png = os.path.join(shots, name + ".png")
                    rc = chrome(browser, profiles[wid],
                                ["--screenshot=" + png, "--window-size=816,1056", url])
                    info = (os.path.exists(png), 0, rc)
                else:
                    out = os.path.join(downloads, outname(name) + ".pdf")
                    rc = chrome(browser, profiles[wid],
                                ["--print-to-pdf=" + out, "--no-pdf-header-footer", url])
                    ok = os.path.exists(out) and os.path.getsize(out) > 20000
                    info = (ok, pdf_pages(out) if ok else 0, rc)
                with lock:
                    results[name] = info
                    good = info[0] and (mode == "shot" or info[1] == 1)
                    print("  %s %-22s pages=%s" % ("OK " if good else "BAD",
                                                   name, info[1]))
                    sys.stdout.flush()

        threads = [threading.Thread(target=work, args=(i,)) for i in range(WORKERS)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        if mode == "shot":
            bad = [n for n, (ok, _, _) in results.items() if not ok]
        else:
            bad = [n for n, (ok, pages, _) in results.items()
                   if not ok or pages != 1]
        print("\n%d/%d clean" % (len(results) - len(bad), len(results)))
        if bad:
            print("PROBLEM: " + ", ".join(sorted(bad)))
        return 1 if bad else 0
    finally:
        shutil.rmtree(stage, ignore_errors=True)
        for p in profiles:
            shutil.rmtree(p, ignore_errors=True)


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "pdf"
    sys.exit(run(mode, sys.argv[2:] or None))
