# HW10｜Wiki 更新與批次複核紀錄

## 既有資料的歷史紀錄（2026-11-16）
現有 `raw/S1–S5.md` 在正式訪談前已建立，GitHub commit 歷史顯示五份來源摘要分別提交。既有 Wiki 亦記載 S1–S2、S3–S4、S5 的 2＋2＋1 整理規劃；**不能據此宣稱已在 Antigravity 或其他 Coding Agent 實際擷取原始全文**。

## 正式需求核准（2026-11-17）
使用者在 ChatGPT 對話逐題完成 10 題需求訪談，並明確核准 `REQUIREMENTS.md`。這是**修改既有專案的授權**，不是事後捏造的訪談紀錄。

## 本次依核准需求進行的三批 Wiki 文件複核（2026-11-17）
以下是**GitHub 檔案複核／修訂**，不是重新下載五篇來源全文的 Agent ingest。

| 批次 | 對照來源 | 實際更新的 Wiki 檔案 | Git commit |
|---|---|---|---|
| 1 | S1–S2（RAG、Embedding） | `concepts/rag.md`、`concepts/embedding.md`：補首次中英術語與原始 URL | [58dc23dd](https://github.com/Ting-liu0103/calm-event-helper/commit/58dc23dd9bca7721126c0ad5da6fc92d8a1412f8) |
| 2 | S3–S4（FAISS、Embedding 模型） | `concepts/faiss.md`、`concepts/pipeline.md`：補 Chunking 說明、來源邊界與 URL | [e2514995](https://github.com/Ting-liu0103/calm-event-helper/commit/e2514995d99dbe9d2c376317cc472ebc1c13a133) |
| 3 | S5（Retriever / Generator）及全域索引 | `concepts/quality.md`、`index.md`：補來源衝突規則、來源 URL 與完整索引 | [3194cd92](https://github.com/Ting-liu0103/calm-event-helper/commit/3194cd92d5d5614fc25b2065b1939a56e27ca107) |

**本次實際檢查：** 從 GitHub 重新讀取更新後檔案，執行來源 URL 字串、來源卡存在性、概念頁引用與 HTML 投影片引用的程式化靜態比對。詳細結果見 `RUN_LOG.md`。

**仍待完成：** Coding Agent 的實際逐批 ingest 操作證據（若課堂要求）；原始網頁逐項人工忠實度核對；瀏覽器、手機版與獨立 AI Reviewer 驗收。
