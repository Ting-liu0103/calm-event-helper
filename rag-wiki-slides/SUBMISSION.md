# HW10｜繳交內容草稿（待人工實測後提交）

**繳交標題：** 長庚 B1228011 AI四 劉姮廷｜RAG 入門 Wiki × HTML 教學簡報

## 1. 主題與讀者
本次主題為「RAG 入門：從搜尋文件到有根據的回答（Grounded Answer）」，對象是完全沒接觸過 RAG 的大學生。先由 AI 逐題進行 10 題正式需求訪談，於 2026-11-17 取得使用者明確核准，再依規格**修訂既有** HW10 專案。需求與選項見 [REQUIREMENTS.md](REQUIREMENTS.md)；對話截圖請於正式提交時附上。

## 2. LLM Wiki 與來源
- Wiki 展示：https://ting-liu0103.github.io/calm-event-helper/rag-wiki-slides/wiki/
- Wiki 原始檔：https://github.com/Ting-liu0103/calm-event-helper/tree/main/rag-wiki-slides/wiki
- 來源摘要：https://github.com/Ting-liu0103/calm-event-helper/tree/main/rag-wiki-slides/raw
- 工作規格：https://github.com/Ting-liu0103/calm-event-helper/blob/main/rag-wiki-slides/AGENTS.md

共 5 份公開來源：Lewis et al. RAG 論文、Sentence Transformers 語意搜尋文件、FAISS、Google EmbeddingGemma 模型卡、Hugging Face RAG 文件。**來源性質為 1 篇研究論文＋4 份官方文件**。已在既有檔案式 Wiki 上分三批（2＋2＋1）複核概念與來源對照並提交 Git；這不是重新由課堂 Coding Agent 自動擷取五份原始全文的證明。

## 3. 教學 HTML 簡報
https://ting-liu0103.github.io/calm-event-helper/rag-wiki-slides/slides/

共 12 張，依序介紹 RAG 動機、定義、Embedding、Chunking、FAISS、Retriever、Generator、來源驗證、校園活動假設案例、限制、Graph 與互動測驗。事實性頁面標 [S1]–[S5]；自製案例另行標示。

## 4. Graph / Loop
**需求核准 → 1–2 份來源批次 → Wiki 與索引 → 來源覆蓋 → 證據卡 → 大綱 → 逐頁稿 → 忠實度檢查 → HTML → Lint 與瀏覽器檢查 → 紀錄。**

資料不足退回檢索，證據錯退回卡片，單頁文案錯只修該頁，HTML 互動與 RWD 問題只退回渲染。**每條路徑最多自動修正 3 次**，超限或無法判定時停止並詢問。流程詳見 [WORKFLOW.md](WORKFLOW.md)。

## 5. 真實執行與檢查
本次依核准需求修訂 AGENTS、Wiki 概念頁、12 張 HTML 簡報及 Lint。透過 GitHub connector 重新讀回 20 個相關檔案，使用 JavaScript 執行 **39 項靜態檢查：39 PASS、0 FAIL**。這些檢查涵蓋來源 URL 字串、概念頁引用、來源卡存在、投影片數量與引用、互動程式標記。

**未完成的驗證：** 隔離環境無法 clone GitHub，因此未能執行 `python3 scripts/lint.py`；GitHub Pages 實際開啟、手機版、互動操作、來源忠實度逐項核對、獨立 AI 審查及 Coding Agent 真實 ingest 證據仍待補。不可將靜態檢查寫成上述項目已通過。

詳見 [RUN_LOG.md](RUN_LOG.md) 與 [report.md](report.md)。

## 6. 反思
最容易出錯的是「Wiki → 逐頁文案」：模型可能把向量相似度當成事實正確性，或把 FAISS 說成生成模型。因此把來源 URL、證據邊界與引用檢查移到 Wiki／證據卡階段，減少錯誤傳到 HTML。將內容錯誤與排版錯誤分流處理，避免每次重新生成整份簡報。

## 提交前請補
- 10 題訪談及明確核准的對話截圖。
- 本機執行 `python3 scripts/lint.py` 的真實終端輸出。
- Wiki/簡報實際開啟、翻頁、測驗及手機版截圖。
- 若老師要求，Coding Agent 逐批 ingest 的實際操作紀錄。
- 逐條來源忠實度及獨立 AI 審查紀錄（如有執行）。
