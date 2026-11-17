# RAG 品質、來源差異與限制

**限制：** 即使有外部文件，檢索可能找錯段落、知識庫可能缺少答案、生成模型也可能誤讀或補寫沒有根據的敘述。[S1][S5]

**本作業的教學檢查策略（非來源原文規範）：**
- **檢索相關性（Retrieval Relevance）：** 找到的段落是否與問題相關？
- **答案忠實度（Answer Faithfulness）：** 每個重要主張是否有文件支持？
- **無答案處理（No-answer Handling）：** 資料不足時是否明確說明？

**來源衝突：** 先比較發表時間、實驗條件、模型實作及適用情境。若無法確定，保留兩種說法並標「待查證」，不任意合併。

**適用範圍提醒：** S1 是研究論文，S5 是特定 RAG 模型的技術文件；兩者用途不同，不能把模型介面的限制直接視為所有 RAG 系統的限制。

## 來源對照
- [S1] Lewis et al. (2020)：https://arxiv.org/abs/2005.11401
- [S5] Hugging Face RAG model documentation：https://huggingface.co/docs/transformers/model_doc/rag
