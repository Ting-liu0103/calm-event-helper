# Wiki 建置計畫：先討論、後生成

## 討論階段
對象：完全沒有 RAG 經驗的同學。核心問題：為什麼單純問 LLM 與先找文件再回答不同？教材採「問題 → 概念 → 流程 → 例子 → 限制」順序。

## 五篇資料清單（準備 ingest）
1. Lewis et al. (2020), Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. https://arxiv.org/abs/2005.11401 — RAG 定義、retrieval + generation。
2. Sentence Transformers, Semantic Search. https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html — query/document embeddings 與語意相似搜尋。
3. FAISS 官方專案. https://github.com/facebookresearch/faiss — 向量索引與近鄰搜尋。
4. Google, EmbeddingGemma model card. https://huggingface.co/google/embeddinggemma-300m — 文字 embedding 模型實例。
5. Hugging Face, RAG model documentation. https://huggingface.co/docs/transformers/model_doc/rag — retriever/generator 的架構與模型介面。

## 資料處理規則
- 只整理來源支持的概念，不複製長段原文。
- 每個概念頁至少標示一個來源代號 [S1]–[S5]。
- 如果來源不能支持結論，改寫為「需額外驗證」。
- 注意：這份 GitHub 內容是**可瀏覽的 Wiki 成果草稿與 ingest 清單**；是否已在課堂指定的 LLM Wiki 平台完成實際 ingest，仍須在該平台執行並附上截圖或連結，不能只憑此檔宣稱已完成 ingest。
