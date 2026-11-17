# RAG：檢索增強生成（Retrieval-Augmented Generation）

**核心定義：** RAG 將外部文件檢索（retrieval）與語言模型生成（generation）結合，讓模型回答時可以參考檢索得到的上下文。[S1][S5]

**初學者比喻：** 直接問模型像閉卷作答；RAG 像先找資料再作答。這是教學比喻，**不表示 RAG 一定答對**。

**常見誤解：** RAG 不能保證消除幻覺；仍須核對文件是否相關，以及回答是否真正受來源支持。

## 來源對照
- [S1] Lewis et al. (2020), *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*：https://arxiv.org/abs/2005.11401
- [S5] Hugging Face Transformers, RAG model documentation：https://huggingface.co/docs/transformers/model_doc/rag

**資料邊界：** S5 描述特定 RAG 模型的介面，不能推論為所有 RAG 系統的唯一實作。
