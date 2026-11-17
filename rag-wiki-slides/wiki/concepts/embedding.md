# 嵌入向量（Embedding）與語意搜尋（Semantic Search）

**Embedding：** 將文字表示成數值向量，以便比較不同文字的相似程度。[S2]

**Semantic Search：** 把查詢（query）和文件（document）轉成向量，利用相似度找出可能相關的內容；用詞不完全相同也可能被檢索到。[S2]

**模型實例：** EmbeddingGemma 是 Google 的文字 embedding 模型之一，作為向量表示的具體例子。[S4]

**限制：** 相似度高不代表文件內容真實；找到相關片段也不代表答案已被證實。

## 來源對照
- [S2] Sentence Transformers, Semantic Search：https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html
- [S4] Google, EmbeddingGemma model card：https://huggingface.co/google/embeddinggemma-300m

**資料邊界：** 不應把 EmbeddingGemma 的模型特性套用到所有 embedding 模型。
