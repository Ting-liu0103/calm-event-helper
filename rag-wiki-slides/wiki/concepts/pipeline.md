# RAG 工作流程（Pipeline）

1. **資料準備：** 取得並整理可使用的文件。
2. **文件切分（Chunking）：** 將長文件分成適合檢索的片段；這是常見系統設計，不是每種 RAG 唯一做法。
3. **嵌入向量（Embedding）：** 將文件片段轉成向量，建立向量索引（Vector Index）。[S2][S3]
4. **使用者提問：** 將問題表示成查詢（Query），供檢索使用。[S2]
5. **檢索器（Retriever）：** 找出可能相關的文件或片段。[S1][S5]
6. **生成器（Generator）：** 結合問題與檢索上下文產生回答。[S1][S5]
7. **有根據的回答（Grounded Answer）：** 在回答中標示資料來源，並檢查主張是否真的受來源支持；此為本作業採用的教學檢查策略，不能保證零幻覺。

**兩階段：** 文件處理及索引建立通常先進行；使用者提問時才執行檢索與生成。具體實作可能不同。

## 來源對照
- [S1] Lewis et al. (2020)：https://arxiv.org/abs/2005.11401
- [S2] Sentence Transformers：https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html
- [S3] FAISS：https://github.com/facebookresearch/faiss
- [S5] Hugging Face RAG model documentation：https://huggingface.co/docs/transformers/model_doc/rag
