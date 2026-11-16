# RAG Wiki｜知識索引

這是以 5 份來源摘要進行的**檔案式 LLM Wiki 整理成果**，不是線上平台的 ingest 統計。概念頁附 [S1]–[S5] 來源代號，適合 Coding Agent 檢索。

| 概念 | Wiki 頁 | 來源 |
|---|---|---|
| RAG 定義 | [RAG 是什麼](concepts/rag.md) | S1、S5 |
| Embedding / 語意搜尋 | [向量與語意搜尋](concepts/embedding.md) | S2、S4 |
| FAISS | [向量索引](concepts/faiss.md) | S3 |
| RAG 工作流程 | [Retriever + Generator](concepts/pipeline.md) | S1、S2、S3、S5 |
| 限制與檢查 | [品質與限制](concepts/quality.md) | S1、S5；教學延伸 |

## 查詢示例
- 問：RAG 與直接問 LLM 差在哪？ → `concepts/rag.md`
- 問：為什麼語意搜尋不只是關鍵字比對？ → `concepts/embedding.md`
- 問：FAISS 會不會自己回答？ → `concepts/faiss.md`
- 問：檢索到了文件還會出錯嗎？ → `concepts/quality.md`

來源全文未重新散布；請從 `raw/` 的原始網址開啟。
