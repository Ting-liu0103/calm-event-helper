# Source Coverage Gate｜來源覆蓋關卡

| ID | 來源類型 | 對應概念 | 原始網址 |
|---|---|---|---|
| S1 | 研究論文 | RAG 動機、定義、檢索與生成 | https://arxiv.org/abs/2005.11401 |
| S2 | 官方技術文件 | Embedding、Semantic Search | https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html |
| S3 | 官方程式庫 | FAISS、向量索引 | https://github.com/facebookresearch/faiss |
| S4 | 官方模型卡 | Embedding 模型例子 | https://huggingface.co/google/embeddinggemma-300m |
| S5 | 官方模型文件 | Retriever、Generator | https://huggingface.co/docs/transformers/model_doc/rag |

**靜態覆蓋判定：** 目前列出 5 份、1 篇論文＋4 份官方文件，覆蓋 5 個主題。這只證明有資料清單，不能取代每一個事實主張的忠實度檢查。

**證據邊界：** RAG 不保證回答正確；語意相似不保證真實；FAISS 只負責向量搜尋；特定 Embedding 模型和 Hugging Face RAG 實作不代表所有系統。文件切分與品質評估的設計建議，需標註為教學延伸而非原始論文的統一規定。
