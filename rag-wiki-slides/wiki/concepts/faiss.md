# FAISS 與向量索引（Vector Index）

**FAISS：** 一套對密集向量進行相似搜尋及分群的工具，可用不同索引策略找出接近查詢向量的資料。[S3]

**角色區分：** FAISS 幫忙「找」，不負責生成自然語言回答，也不能判定資料真偽。

**文件切分（Chunking）：** 在 RAG 的常見教學流程中，長文件可先拆成較小的段落（chunks），再各自向量化並建立索引。切分大小會影響上下文保留與檢索表現；**這是系統設計上的教學延伸，並非 S3 規定的單一最佳切分方式**。

## 來源對照
- [S3] Meta AI Research, FAISS 官方程式庫：https://github.com/facebookresearch/faiss
