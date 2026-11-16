#!/usr/bin/env python3
"""HW10 reproducible offline structural linter. Run from project root or anywhere."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors, notes = [], []
def check(ok, message):
    (notes if ok else errors).append(("PASS" if ok else "FAIL") + " | " + message)

source_ids = {f"S{i}" for i in range(1, 6)}
raw = sorted((ROOT / "raw").glob("S*.md"))
check(len(raw) >= 5, f"at least five raw sources: {len(raw)}")
for sid in sorted(source_ids):
    p = ROOT / "raw" / f"{sid}.md"
    check(p.is_file(), f"{sid} raw file")
    if p.exists():
        s = p.read_text(encoding="utf-8")
        check(bool(re.search(r"https://\S+", s)), f"{sid} original URL")
        check("## 摘要" in s and "## 證據邊界" in s, f"{sid} summary and evidence boundary")
    check((ROOT / "cards" / f"{sid}.md").is_file(), f"{sid} evidence card")

for name in ["AGENTS.md", "SKILL.md", "REQUIREMENTS.md", "sources.md",
             "outline.md", "drafts/slides.md", "wiki/index.md", "wiki/log.md",
             ".agents/workflows/topic-slides.md", "report.md",
             "slides/index.html", "wiki/index.html"]:
    check((ROOT / name).is_file(), name + " exists")

concepts = list((ROOT / "wiki/concepts").glob("*.md"))
check(len(concepts) >= 5, f"wiki concept pages: {len(concepts)}")
wiki = (ROOT / "wiki/index.md").read_text(encoding="utf-8")
for sid in source_ids:
    check(sid in wiki, f"{sid} in wiki index")

deck = (ROOT / "slides/index.html").read_text(encoding="utf-8")
nslides = len(re.findall(r'<section\s+class="slide(?: active)?"', deck))
check(8 <= nslides <= 15, f"HTML slide count: {nslides}")
check(bool(re.search(r'<html\b', deck)) and "</html>" in deck, "HTML root")
check(all(x in deck for x in ['id="prev"', 'id="next"', 'ArrowRight', 'ArrowLeft']), "navigation controls")
check("data-correct" in deck, "quiz interaction")
check("教學假設案例" in deck, "example clearly identified")
refs = set(re.findall(r"\[S\d+\]", deck))
check(refs.issubset({f"[{x}]" for x in source_ids}), "slide citation IDs are defined")
check(len(refs) == 5, f"slide source coverage: {len(refs)}/5")
check("來源：" in deck, "slide source labels")

print("\n".join(notes + errors))
print(f"\nSUMMARY: {len(notes)} passed, {len(errors)} failed")
if errors:
    sys.exit(1)
print("Note: structural checks do NOT prove factual faithfulness, URL reachability, mobile layout or independent AI review.")
