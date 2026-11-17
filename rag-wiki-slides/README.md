# HW10｜RAG 入門 Wiki × 互動式 HTML 簡報

**長庚大學｜B1228011｜AI四｜劉姮廷**

## 成果
- [Wiki 展示](https://ting-liu0103.github.io/calm-event-helper/rag-wiki-slides/wiki/)
- [12 張互動式 HTML 簡報](https://ting-liu0103.github.io/calm-event-helper/rag-wiki-slides/slides/)

> 以上為預定 GitHub Pages 網址，是否可正常部署、操作及在手機瀏覽，**尚待實測**。

## 需求與流程
- [正式 10 題需求訪談與核准結果](REQUIREMENTS.md)
- [唯一主要 Agent 工作規格](AGENTS.md)
- [來源清單及分批規則](INGEST_LIST.md)
- [Wiki 索引](wiki/index.md)、[概念頁](wiki/concepts/)、[真實複核紀錄](wiki/log.md)
- [Graph 與 Loop](WORKFLOW.md)、[工作流程節點](.agents/workflows/topic-slides.md)
- [教學大綱](outline.md)、[逐頁稿](drafts/slides.md)、[HTML](slides/index.html)
- [Lint 腳本](scripts/lint.py)、[執行紀錄](RUN_LOG.md)、[反思報告](report.md)

## 本機執行靜態 Lint
```bash
cd rag-wiki-slides
python3 scripts/lint.py
```

**注意：** 本次 GitHub connector 讀回的 39 項靜態稽核為 39 PASS、0 FAIL；`python3 scripts/lint.py` 在隔離環境因無法 clone GitHub 專案而**未實際執行**。此腳本也不能證明來源內容忠實、瀏覽器互動、手機版、外部 URL 可達或獨立 AI 審查通過。

## 來源性質
本專案以 1 篇學術論文與 4 份官方技術文件整理 5 份繁中摘要，屬於檔案式 Wiki。**不是**原始全文鏡像，也不應冒稱已由課堂 Coding Agent 完成五份全文 ingest。
