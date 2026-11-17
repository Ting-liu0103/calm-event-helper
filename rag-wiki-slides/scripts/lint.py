#!/usr/bin/env python3
"""HW10 offline structural/source-reference checks. Does not run browser or factual review."""
from pathlib import Path
from html.parser import HTMLParser
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
results = []
def check(condition, label):
    results.append((bool(condition), label))

URLS = {
    "S1": "https://arxiv.org/abs/2005.11401",
    "S2": "https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html",
    "S3": "https://github.com/facebookresearch/faiss",
    "S4": "https://huggingface.co/google/embeddinggemma-300m",
    "S5": "https://huggingface.co/docs/transformers/model_doc/rag",
}
REQUIRED = [
    "AGENTS.md", "REQUIREMENTS.md", "INGEST_LIST.md", "sources.md",
    "wiki/index.md", "wiki/log.md", "wiki/index.html",
    "outline.md", "drafts/slides.md", "slides/index.html",
    "WORKFLOW.md", "SKILL.md", ".agents/workflows/topic-slides.md",
    "RUN_LOG.md",
]
for name in REQUIRED:
    check((ROOT / name).is_file(), f"required file: {name}")
check(len(list((ROOT / "raw").glob("S*.md"))) >= 5, "at least five source notes")

for sid, url in URLS.items():
    p = ROOT / "raw" / f"{sid}.md"
    card = ROOT / "cards" / f"{sid}.md"
    check(p.is_file(), f"{sid}: raw note")
    check(card.is_file(), f"{sid}: evidence card")
    if p.is_file():
        text = p.read_text(encoding="utf-8")
        check(url in text, f"{sid}: canonical source URL in raw")
        check("## 摘要" in text and "## 證據邊界" in text, f"{sid}: summary and evidence boundary")

concept_sources = {
    "rag.md": ["S1", "S5"],
    "embedding.md": ["S2", "S4"],
    "faiss.md": ["S3"],
    "pipeline.md": ["S1", "S2", "S3", "S5"],
    "quality.md": ["S1", "S5"],
}
for file, sids in concept_sources.items():
    p = ROOT / "wiki/concepts" / file
    check(p.is_file(), f"wiki concept: {file}")
    if p.is_file():
        content = p.read_text(encoding="utf-8")
        for sid in sids:
            check(f"[{sid}]" in content and URLS[sid] in content, f"{file}: [{sid}] and original URL")

wiki = (ROOT / "wiki/index.md").read_text(encoding="utf-8")
for sid, url in URLS.items():
    check(f"[{sid}]" in wiki and url in wiki, f"wiki index: [{sid}] original URL")

req = (ROOT / "REQUIREMENTS.md").read_text(encoding="utf-8")
check("正式需求" in req and "10 題" in req, "approved interview documented")
agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
check("最多自動嘗試 3 次" in agents, "three-attempt stop rule")
check(len(agents) <= 12000, f"AGENTS.md under 12000 chars ({len(agents)})")

class DeckParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.slides = []
        self.current = None
        self.buttons = set()
        self.quiz = 0
        self.links = []
        self.viewport = False
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "section" and "slide" in attrs.get("class", "").split():
            self.current = []
            self.slides.append(self.current)
        if tag == "button":
            if "id" in attrs: self.buttons.add(attrs["id"])
            if "data-correct" in attrs: self.quiz += 1
        if tag == "a": self.links.append(attrs.get("href", ""))
        if tag == "meta" and attrs.get("name") == "viewport": self.viewport = True
    def handle_data(self, data):
        if self.current is not None: self.current.append(data)
    def handle_endtag(self, tag):
        if tag == "section": self.current = None

deck = (ROOT / "slides/index.html").read_text(encoding="utf-8")
p = DeckParser()
p.feed(deck)
check(len(p.slides) == 12, f"12 HTML slides: {len(p.slides)}")
check(p.viewport and "@media(max-width:" in deck, "viewport and responsive CSS present")
check({"prev", "next"}.issubset(p.buttons) and "ArrowRight" in deck and "ArrowLeft" in deck, "navigation code markers")
check(p.quiz >= 2 and "data-correct" in deck and "feedback" in deck, "quiz code markers")
check("../wiki/#sources" in p.links, "source index linked from slides")
check("教學假設案例" in deck, "hypothetical example labelled")
refs = set(re.findall(r"\[S\d+\]", deck))
check(refs == {f"[{s}]" for s in URLS}, f"all 5 source IDs referenced: {sorted(refs)}")
for i, slide in enumerate(p.slides, 1):
    content = " ".join(slide)
    if i not in (2, 8, 10):
        check(bool(re.search(r"\[S[1-5]\]", content)), f"slide {i}: source citation")
    else:
        check(True, f"slide {i}: authored goal/example/workflow exception")
check("href=\"../wiki/\"" in deck, "wiki entry link")
check("</html>" in deck and "</script>" in deck, "HTML closing tags")

for ok, label in results:
    print(("PASS" if ok else "FAIL") + " | " + label)
passed = sum(ok for ok, _ in results)
failed = len(results) - passed
print(f"\nSUMMARY: {passed} passed, {failed} failed")
print("SCOPE: static files, source ID/URL text, HTML markup and JS/CSS markers only.")
print("NOT VERIFIED: source truth, URL reachability, JS runtime, RWD visual layout, Pages deployment, independent AI review.")
sys.exit(1 if failed else 0)
