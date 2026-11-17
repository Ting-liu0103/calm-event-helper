# HW10｜RAG 入門 Wiki × 教學 HTML 簡報

**長庚大學｜B1228011｜AI四｜劉姮廷**

## 成果連結
- [Wiki HTML 展示](https://ting-liu0103.github.io/calm-event-helper/rag-wiki-slides/wiki/)
- [12 張教學 HTML 簡報](https://ting-liu0103.github.io/calm-event-helper/rag-wiki-slides/slides/)
- [完整作業繳交草稿](SUBMISSION.md)

## 對照老師第十週 PPT
| 要求 | 對應檔案 |
|---|---|
| 先討論再生成 | [REQUIREMENTS.md](REQUIREMENTS.md) |
| AGENTS.md | [AGENTS.md](AGENTS.md) |
| 至少 5 篇 ingest | [raw/](raw/) 5 份來源摘要，三批整理紀錄見 [wiki/log.md](wiki/log.md) |
| Wiki 索引 | [wiki/index.md](wiki/index.md) 與 [wiki/concepts/](wiki/concepts/) |
| 證據卡 | [cards/](cards/) |
| 簡報大綱／逐頁稿 | [outline.md](outline.md)、[drafts/slides.md](drafts/slides.md) |
| Loop 規格 | [SKILL.md](SKILL.md) |
| Graph | [.agents/workflows/topic-slides.md](.agents/workflows/topic-slides.md) |
| 檢查腳本 | [scripts/lint.py](scripts/lint.py) |
| 執行與反思 | [report.md](report.md)、[RUN_LOG.md](RUN_LOG.md) |

## 執行靜態檢查
```bash
python3 scripts/lint.py
```

## 實作界線
這是一份**以 5 份公開來源摘要建立的檔案式 LLM Wiki**，不是線上 Wiki 平台自動抓取的全文，也不是已經由 Antigravity 跑過的 Agent 實際紀錄。GitHub Pages 網址是否已部署、手機版與獨立 AI 審查，均須實際驗收。請勿把待測項目寫成已通過。

## 原始參考
- [S1 RAG paper](https://arxiv.org/abs/2005.11401)
- [S2 Sentence Transformers](https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html)
- [S3 FAISS](https://github.com/facebookresearch/faiss)
- [S4 EmbeddingGemma](https://huggingface.co/google/embeddinggemma-300m)
- [S5 Hugging Face RAG](https://huggingface.co/docs/transformers/model_doc/rag)
