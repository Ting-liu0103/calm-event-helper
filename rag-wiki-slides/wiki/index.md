# RAG Wiki｜概念索引與來源追溯

這是以五份公開來源摘要建立的**檔案式 Wiki**，不是特定線上平台或 Coding Agent 自動擷取全文的證明。內容以繁體中文解說，首次專業術語附中英對照。

| 概念 | 概念頁 | 來源 |
|---|---|---|
| 檢索增強生成（Retrieval-Augmented Generation, RAG） | [RAG 是什麼](concepts/rag.md) | [S1][S5] |
| 嵌入向量（Embedding）、語意搜尋（Semantic Search） | [向量與語意搜尋](concepts/embedding.md) | [S2][S4] |
| 向量索引（Vector Index）與 FAISS | [向量索引](concepts/faiss.md) | [S3] |
| 檢索器（Retriever）與生成器（Generator） | [完整流程](concepts/pipeline.md) | [S1][S2][S3][S5] |
| 有根據的回答（Grounded Answer）與品質 | [品質與限制](concepts/quality.md) | [S1][S5]＋教學延伸 |

## 來源原始網址
- [S1] Lewis et al. (2020)：https://arxiv.org/abs/2005.11401
- [S2] Sentence Transformers：https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html
- [S3] FAISS：https://github.com/facebookresearch/faiss
- [S4] Google EmbeddingGemma：https://huggingface.co/google/embeddinggemma-300m
- [S5] Hugging Face RAG：https://huggingface.co/docs/transformers/model_doc/rag

## 查詢示例
- RAG 與直接問 LLM 差在哪？→ `concepts/rag.md`
- Embedding 如何協助語意搜尋？→ `concepts/embedding.md`
- FAISS 會自行產生回答嗎？→ `concepts/faiss.md`
- 文件如何切分、檢索並回答？→ `concepts/pipeline.md`
- 找到文件就一定能回答正確嗎？→ `concepts/quality.md`

## 更新與檢查
詳見 [wiki/log.md](log.md)；來源摘要見 [raw/](../raw/)，證據卡見 [cards/](../cards/)。
