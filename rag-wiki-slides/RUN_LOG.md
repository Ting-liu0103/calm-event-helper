# HW10｜真實執行與測試紀錄

## 2026-11-17：依使用者正式核准需求修訂既有專案

**GitHub repo：** `Ting-liu0103/calm-event-helper`，目錄 `rag-wiki-slides/`。

| 步驟 | 實際方法 | 實際結果 |
|---|---|---|
| 檢查現有專案 | GitHub connector 讀取 main tree、AGENTS、Wiki、來源卡、HTML、lint 與既有報告 | 確認既有 5 份來源摘要、5 張卡、5 個概念頁、12 張 HTML 投影片 |
| 核對既有提交 | GitHub commits API 查詢 `raw/` 與 `wiki/log.md` 歷史 | `raw/S1–S5.md` 在 2026-11-16 已逐檔提交；不是本次訪談後才產生 |
| 核准需求文件 | GitHub commit `c689df75b88c22e19d4c40080b4ff95e15865d06` | 更新正式訪談結果、AGENTS、Graph、Ingest 規則 |
| Wiki 批次複核 1 | GitHub commit `58dc23dd9bca7721126c0ad5da6fc92d8a1412f8` | 更新 RAG 與 Embedding 概念頁 |
| Wiki 批次複核 2 | GitHub commit `e2514995d99dbe9d2c376317cc472ebc1c13a133` | 更新 FAISS 與 Pipeline 概念頁 |
| Wiki 批次複核 3 | GitHub commit `3194cd92d5d5614fc25b2065b1939a56e27ca107` | 更新品質概念與 Wiki 索引 |
| 簡報對齊 | GitHub commit `908465196c333be35b15d3adb9a89908e2bd2d51` | 保留 12 張，補中英術語與 Wiki 來源入口 |
| Lint 擴充 | GitHub commit `c681c6340f9e8f29141363d01fcc153e23671c39` | 增加來源 URL、概念頁與每頁引用、12 張簡報等檢查 |

## 已執行的靜態稽核（不是 Python lint 執行）

**方法：** 使用 GitHub connector 重新讀取 main 分支共 20 個相關檔案，透過 JavaScript 進行 39 項字串／結構比對。

**結果：39 PASS、0 FAIL。** 比對內容包括：五份 raw 來源網址、五張來源卡存在性、Wiki 索引中的五個原始網址、五個概念頁各自對應的來源 URL、12 張投影片數量、9 張事實性投影片的來源代號、導航／測驗程式標記、需求核准與三次重試規則。

**重要限制：** 39 項是本次 GitHub 讀回的**程式化靜態稽核**，不是 `python3 scripts/lint.py` 的執行結果，也不是實際瀏覽器操作。不能以此宣稱 JavaScript 執行、手機版、外部連結或內容忠實度全部通過。

## 嘗試但未完成的檢查
- 曾嘗試在隔離的 Python/容器環境透過 `git clone` 下載 GitHub 專案並執行 `python3 scripts/lint.py`，但環境無法解析 `github.com`，下載失敗，**Python lint 尚未執行**。
- 因此請使用者於本機 clone 或下載 repo 後，執行 `cd rag-wiki-slides && python3 scripts/lint.py`，保存完整終端輸出。

## 2026-11-17：使用者實際瀏覽器驗收
- 使用者於對話確認：Wiki 與 HTML 簡報**均可正常開啟**，簡報**可正常翻頁與作答**。
- 此為使用者回報的實際人工測試結果，不是自動化測試或遠端瀏覽器錄影；未額外聲稱測過鍵盤左右鍵、全部來源連結或手機版。
- 終端 Python Lint 仍未執行，39 項靜態稽核與瀏覽器實測須分開表述。

## 其他尚未驗證的項目
- 原始來源內容是否逐條支持 Wiki 與投影片的重要主張（靜態字串比對不能取代此項）。
- 鍵盤方向鍵、全部來源連結等細部互動尚未逐項確認（網頁開啟、翻頁及小測驗已由使用者實測通過）。
- 手機版是否有溢出或遮擋，及列印版面。
- 是否有獨立新對話 AI Reviewer 的內容審查。
- 逐頁大綱的獨立人工核准、課堂 Coding Agent 實際 Ingest 證據（若需要）。

## 修正與反思
**已知風險：**「語意相似 ≠ 事實正確」、「FAISS ≠ 生成模型」、「校園活動雨備 ≠ 真實 Wiki 查詢」是既有內容需明確標示的界線。此次在概念頁、流程規則與簡報中補強，並把來源 URL 比對放在渲染之前。

**Loop 狀態：** 已建立最多 3 次的修正規格；本次未發生 3 次自動重試，不能把設計寫成已跑過的失敗循環。
