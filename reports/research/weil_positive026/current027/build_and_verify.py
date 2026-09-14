"""Build and check the frozen prime-current reader and its dependency closure."""

from pathlib import Path
import hashlib
import json
import os
import platform
import re
import subprocess

import fitz


report = Path(__file__).resolve().parent
root = report.parents[3]
manifest = json.loads((report / "source-manifest.json").read_text())
source_rows = manifest["source_files"]
for row in source_rows:
    assert hashlib.sha256((root / row["path"]).read_bytes()).hexdigest() == row["sha256"]

module = (root / source_rows[0]["path"]).read_text()
arithmetic = (report.parent / "inputs/arithmetic.tex").read_text()
positive = (root / "research-candidates/weil_positive026/prime-difference-carrier.tex").read_text()
assert arithmetic.count(r"\begin{proof}") == 39
assert positive.count(r"\begin{proof}") == 5
assert module.count(r"\begin{proof}") == 5
all_source = arithmetic + positive + module
labels = re.findall(r"\\label\{([^}]+)\}", all_source)
assert len(labels) == len(set(labels))
refs = set(re.findall(r"\\(?:eqref|ref)\{([^}]+)\}", all_source))
assert refs <= set(labels), refs - set(labels)
firewall = re.compile(r"\b(agent|worktree|workflow|TODO|reviewer|audit|commit|sprint|"
                      r"task packet|acceptance|candidate|implementation)\b", re.I)
assert not firewall.search(module), firewall.findall(module)
assert "/Users/" not in module and "github.com/" not in module

commands = []
environment = os.environ.copy()
environment.update(TEXINPUTS="../inputs:", SOURCE_DATE_EPOCH="1789430400", FORCE_SOURCE_DATE="1")
command = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "-recorder",
           "-output-directory=build", "candidate.tex"]
pdf_hashes = []
for number in range(1, 4):
    process = subprocess.run(command, cwd=report, env=environment, text=True, capture_output=True)
    (report / f"build/frozen-pass{number}.stdout").write_text(process.stdout)
    (report / f"build/frozen-pass{number}.stderr").write_text(process.stderr)
    commands.append({"command": command, "cwd": str(report), "exit_code": process.returncode,
                     "environment_overrides": {key: environment[key] for key in
                        ("TEXINPUTS", "SOURCE_DATE_EPOCH", "FORCE_SOURCE_DATE")}})
    assert process.returncode == 0, process.stderr + process.stdout[-4000:]
    pdf_hashes.append(hashlib.sha256((report / "build/candidate.pdf").read_bytes()).hexdigest())
assert pdf_hashes[-2] == pdf_hashes[-1], pdf_hashes
log = (report / "build/candidate.log").read_text(errors="replace")
bad_log = re.compile(r"undefined|multiply defined|Overfull|Underfull|Warning:|Fatal error|^!", re.I | re.M)
assert not bad_log.search(log), bad_log.findall(log)

project_inputs = set()
for line in (report / "build/candidate.fls").read_text().splitlines():
    if line.startswith("INPUT "):
        path = Path(line[6:])
        path = (report / path).resolve() if not path.is_absolute() else path.resolve()
        if path.suffix in (".tex", ".sty") and path.is_relative_to(root):
            project_inputs.add(str(path.relative_to(root)))
assert project_inputs == {row["path"] for row in source_rows}, project_inputs

baseline = fitz.open(report.parent / "build-candidate/candidate.pdf")
reader = fitz.open(report / "build/candidate.pdf")
assert len(baseline) == 45 and len(reader) == 54
preserved = []
for index in range(45):
    before, after = baseline[index], reader[index]
    assert before.get_text() == after.get_text(), index + 1
    old = before.get_pixmap(matrix=fitz.Matrix(1.25, 1.25), alpha=False).samples
    new = after.get_pixmap(matrix=fitz.Matrix(1.25, 1.25), alpha=False).samples
    assert old == new, index + 1
    preserved.append({"page": index + 1, "text_identical": True,
                      "raster_sha256": hashlib.sha256(new).hexdigest()})

addition = "\n".join(page.get_text() for page in list(reader)[45:])
assert not firewall.search(addition), firewall.findall(addition)
assert "Arithmetic currents and prime inclusions" in addition
assert "Infinite arithmetic multiplication" in addition
assert "/Users/" not in addition and "github.com/" not in addition
(report / "build/addition.txt").write_text(addition)
(report / "build/reader.txt").write_text("\n".join(page.get_text() for page in reader))
pages = []
for index in range(45, len(reader)):
    page = reader[index]
    assert len(page.get_text()) > (100 if index == len(reader)-1 else 1000)
    for block in page.get_text("blocks"):
        x0, y0, x1, y1 = block[:4]
        assert 0 <= x0 <= x1 <= page.rect.width and 0 <= y0 <= y1 <= page.rect.height
    pages.append({"page": index + 1, "text_characters": len(page.get_text()),
                  "text_inside_page": True})

for utility in ("pdfinfo", "pdffonts"):
    result = subprocess.run([utility, "build/candidate.pdf"], cwd=report,
                            text=True, capture_output=True, check=True)
    (report / f"build/{utility}.txt").write_text(result.stdout)
font_rows = (report / "build/pdffonts.txt").read_text().splitlines()[2:]
assert font_rows and all(row.split()[-5:-2] == ["yes", "yes", "yes"] for row in font_rows)
assert not firewall.search(json.dumps(reader.metadata)), reader.metadata
render_command = ["pdftoppm", "-f", "45", "-l", "54", "-r", "120", "-png",
                  "build/candidate.pdf", "build/page"]
render = subprocess.run(render_command, cwd=report, text=True, capture_output=True)
(report / "build/render.stdout").write_text(render.stdout)
(report / "build/render.stderr").write_text(render.stderr)
commands.append({"command": render_command, "cwd": str(report), "exit_code": render.returncode})
assert render.returncode == 0

(report / "build-commands.json").write_text(json.dumps(commands, indent=2) + "\n")
result = {
    "source_aggregate_sha256": manifest["source_aggregate_sha256"],
    "source_closure_verified": True,
    "project_inputs": sorted(project_inputs),
    "proof_counts": {"inherited": 39, "positiveweight": 5, "current": 5},
    "labels_and_references": "all unique and resolved",
    "manuscript_firewall": "no prohibited prose or paths in the addition and its metadata",
    "final_build_warnings": [],
    "pdf_sha256": pdf_hashes[-1],
    "repeated_pdf_hashes": pdf_hashes,
    "repeated_build_byte_identity": True,
    "page_count": len(reader),
    "preserved_pages": preserved,
    "added_pages": pages,
    "font_embedding": "all fonts embedded, subset, and Unicode-mapped",
    "visual_inspection": "separate record required for rendered pages 45 through 54",
    "mathematical_acceptance": "not established by this verification script",
    "versions": {"python": platform.python_version(), "pymupdf": fitz.VersionBind,
                 "pdflatex": subprocess.check_output(["pdflatex", "--version"], text=True).splitlines()[0]},
}
(report / "verification-results.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({key: value for key, value in result.items()
                  if key not in ("preserved_pages", "added_pages")}, indent=2))
