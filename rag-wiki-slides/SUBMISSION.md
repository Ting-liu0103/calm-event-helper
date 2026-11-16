# HW10 繳交內容（可貼作業系統）

**繳交標題：** 長庚 B1228011 AI四 劉姮廷 RAG 入門 Wiki 與 HTML 教學簡報

## 1. LLM Wiki 主題與簡短介紹
本次主題是「RAG 入門：從搜尋文件到 Grounded Answer」。我希望讓沒有接觸過 RAG 的同學理解：為什麼語言模型要先檢索外部資料、Embedding 與語意搜尋如何協助找到文件、FAISS 的角色，以及 Retriever 和 Generator 如何合作。我將 5 份公開來源整理成繁體中文概念頁，並且標記 [S1]–[S5]，避免只依靠模型的印象產生教學內容。

## 2. LLM Wiki 連結或成果
- Wiki 展示頁：https://ting-liu0103.github.io/calm-event-helper/rag-wiki-slides/wiki/
- Wiki 原始檔與概念索引：https://github.com/Ting-liu0103/calm-event-helper/tree/main/rag-wiki-slides/wiki
- 來源與整理紀錄：https://github.com/Ting-liu0103/calm-event-helper/tree/main/rag-wiki-slides/raw
- AGENTS.md：https://github.com/Ting-liu0103/calm-event-helper/blob/main/rag-wiki-slides/AGENTS.md

資料共 5 份：RAG 原始論文、Sentence Transformers 語意搜尋文件、FAISS 官方文件、Google EmbeddingGemma 模型卡、Hugging Face RAG 文件。分三批（2＋2＋1）整理，建立 Wiki 概念頁、索引和 log。這裡的 ingest 是**將來源摘要整理進 Git 管理的檔案式 Wiki**，不是聲稱已經由特定線上平台自動抓取全文。

## 3. 教學 HTML 簡報連結
https://ting-liu0103.github.io/calm-event-helper/rag-wiki-slides/slides/

簡報共 12 張，內容依序介紹 RAG 的動機、基本定義、Embedding、FAISS、完整流程、假設案例、限制、作業 graph 與互動測驗。每個有事實性主張的頁面都附來源代號，自製示例也有另外標註。

## 4. Loop / Graph 流程
我採用 Graph 管理整體順序，Loop 處理局部修改：

**來源整理 → Wiki 檢索 → 覆蓋率檢查 → 證據卡 → 教學大綱 → 人工確認 → 逐頁稿 → 忠實度檢查 → HTML 渲染 → 程式／畫面檢查 → Git 提交。**

覆蓋率不足就退回檢索，不能用模型常識硬補；證據卡有問題就重做該張卡；單頁內容不忠於來源，就只修那一頁；HTML 版面或操作出錯則只退回渲染。逐頁稿最多局部重試 2 次，整體最多 3 輪。這樣可以讓錯誤在最接近源頭的節點被發現，不需要每次重做整份簡報。

流程規格：https://github.com/Ting-liu0103/calm-event-helper/blob/main/rag-wiki-slides/.agents/workflows/topic-slides.md

## 5. 一次實際執行與檢查紀錄
本次已建立 5 份 raw 來源摘要、5 張證據卡、5 個 Wiki 概念頁、12 頁教學大綱與 HTML 簡報，並提交 GitHub。實際對照內容時，發現三個容易混淆的地方：

- 「語意相似」不等於「內容一定正確」，因此在 S2 證據卡及簡報第 5 頁加入提醒。
- FAISS 是向量搜尋工具，不會自行產生回答，因此在 S3 證據卡與 Wiki 中區分搜尋和生成。
- 校園活動雨備只是教學假設案例，因此在簡報第 8 頁明確標註，不當成真實 Wiki 查詢結果。

已透過 GitHub 檔案檢查確認 HTML 包含 12 張 slide、5 個來源代號、前後翻頁控制與互動測驗。另有 `python3 scripts/lint.py` 可供重複執行結構檢查。**目前尚未完成外部瀏覽器視覺實測及獨立新對話 AI 審查**，所以不將這兩項寫成已通過。

詳細報告：https://github.com/Ting-liu0103/calm-event-helper/blob/main/rag-wiki-slides/report.md

## 6. 反思與調整
我發現最容易出問題的是「Wiki 整理 → 逐頁稿」之間的資訊轉換。模型很容易把相似度當成正確性，或把檢索工具說成生成工具。原本是在 HTML 完成後才整體檢查，這次改成先製作**每篇來源獨立的證據卡**，再讓逐頁稿只使用對應卡片，將忠實度檢查往前移到產生 HTML 之前。

Graph 也從原本簡單的「取得資料→整理→生成→檢查」改成有明確的覆蓋率、證據卡、逐頁稿與渲染關卡。內容出錯時只退回有問題的節點，版面出錯時則只修 HTML，不再讓排版階段順便改寫知識。這讓流程更容易追蹤，也比較能看出 AI 改了什麼。

## AI 使用說明
本次使用 ChatGPT 協助整理來源摘要、設計 Wiki 結構、撰寫 HTML/CSS/JavaScript、規劃 Graph 與檢查腳本。我負責確認主題方向、檢視來源與簡報內容，並需在正式提交前自行完成頁面操作與人工驗收。程式與內容均保留於 GitHub，可查看修改紀錄。

---

**提交前需自行補上的證據：** GitHub Pages 實際開啟截圖、Wiki 內容或 Coding Agent ingest 截圖、執行 `python3 scripts/lint.py` 的終端輸出、若有進行則附獨立 AI 審查對話。上述未完成項目不應冒稱已通過。
