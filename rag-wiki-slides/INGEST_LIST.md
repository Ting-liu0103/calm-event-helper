# HW10｜來源清單與分批 Ingest 規則

**正式需求已核准：** 至少 5 份，學術論文＋官方技術文件；每批處理 1–2 份，檢查 Wiki、索引、更新紀錄後 commit。

| ID | 類型 | 原始來源與 URL | 用途 |
|---|---|---|---|
| S1 | 研究論文 | Lewis et al. (2020), [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) | RAG 定義與檢索＋生成 |
| S2 | 官方技術教學 | [Sentence Transformers: Semantic Search](https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) | Query/document embedding、語意搜尋 |
| S3 | 官方程式庫文件 | [Meta FAISS](https://github.com/facebookresearch/faiss) | 向量索引與相似搜尋 |
| S4 | 官方模型卡 | [Google EmbeddingGemma](https://huggingface.co/google/embeddinggemma-300m) | Embedding 模型實例 |
| S5 | 官方模型文件 | [Hugging Face RAG](https://huggingface.co/docs/transformers/model_doc/rag) | Retriever / Generator |

## 操作規則
- 每批 1–2 份：檢查來源頁、`raw/S#.md`、`cards/S#.md`、Wiki 概念頁、`wiki/index.md`、`wiki/log.md`。
- **分批複核既有資料**與**從零執行 Coding Agent Ingest**是不同事件。已存在的 `raw/` 為繁中來源摘要，不是原始全文；若未由 Agent 真正執行擷取，不得標示為 Agent ingest 成功。
- 來源矛盾時比較時間、實驗條件與適用範圍，未能解決就標「待查證」。
- 每批通過才 commit；紀錄必須列出實際檢查方法與提交 SHA。不得補寫不存在的歷史紀錄。
