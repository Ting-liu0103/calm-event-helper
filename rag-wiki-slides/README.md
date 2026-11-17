# HW10｜RAG 入門 Wiki × 互動式 HTML 教學簡報

**長庚大學｜人工智慧學系四年級｜B1228011 劉姮廷**

本專案以「RAG 入門：從搜尋文件到有根據的回答（Grounded Answer）」為題，面向尚未接觸 RAG 的大學生，將公開文獻與官方技術文件整理為可追溯的繁體中文 Wiki，再製作 12 張互動式 HTML 教學簡報。

## 成果展示

| 成果 | 連結 | 內容 |
|---|---|---|
| RAG 入門 Wiki | [開啟 Wiki](https://ting-liu0103.github.io/calm-event-helper/rag-wiki-slides/wiki/) | 五個概念主題、來源對照及原始網址 |
| 互動式 HTML 簡報 | [開啟 12 張投影片](https://ting-liu0103.github.io/calm-event-helper/rag-wiki-slides/slides/) | RAG 定義、Embedding、FAISS、Pipeline、教學案例、限制與測驗 |
| 成果與反思報告 | [report.md](report.md) | 實際執行、驗證範圍、問題與修正策略 |
| 工作流程 | [WORKFLOW.md](WORKFLOW.md) | Graph、檢查關卡與有限次修正 Loop |

**使用者實測：** Wiki 與簡報均能正常開啟；簡報翻頁及互動測驗可正常使用（2026-11-17 於對話確認）。

## Wiki 如何建立？

內容來源為 **1 篇 RAG 研究論文與 4 份官方技術／模型文件**。專案以檔案式 Wiki 方式組織資料，區分來源摘要、Wiki 概念、證據卡與教學簡報，讓每個概念可追溯至 [S1]–[S5] 原始網址。

| 檔案／資料夾 | 用途 |
|---|---|
| [REQUIREMENTS.md](REQUIREMENTS.md) | 10 題逐題需求訪談及使用者核准結果 |
| [AGENTS.md](AGENTS.md) | Coding Agent 工作規格與資料引用原則 |
| [raw/](raw/) | 5 份來源摘要（非原始全文） |
| [wiki/](wiki/) | Wiki 概念頁、索引與批次複核紀錄 |
| [cards/](cards/) | 5 張證據卡，記錄可支持與不可推論的主張 |
| [outline.md](outline.md)、[drafts/slides.md](drafts/slides.md) | 教學大綱與逐頁文案 |
| [slides/index.html](slides/index.html) | HTML / CSS / JavaScript 互動簡報 |
| [scripts/lint.py](scripts/lint.py) | 可重現的離線靜態檢查程式 |
| [RUN_LOG.md](RUN_LOG.md) | GitHub 修改與測試歷程 |

## 教學與流程特色

- **先釐清需求：** 完成 10 題訪談並獲得核准，再對照規格修訂既有成果。
- **來源可追溯：** 概念頁與事實性投影片以 [S1]–[S5] 標註出處。
- **以初學者為中心：** 繁體中文、首次出現術語附英文、生活化案例與互動測驗。
- **Graph + Loop：** 來源不足退回檢索、主張錯誤退回證據卡或文案、操作錯誤退回 HTML；每條路徑最多自動修正 3 次。

## 驗證摘要

| 項目 | 結果 |
|---|---|
| GitHub 檔案靜態稽核 | **39 項通過，0 項失敗**（來源 URL 字串、引用對應、頁面結構及功能程式標記） |
| Wiki 與 HTML 簡報開啟 | **使用者實測通過** |
| HTML 翻頁與互動測驗 | **使用者實測通過** |
| `python3 scripts/lint.py` 實際執行 | 未執行；已提供可重現腳本 |
| 手機版版面、獨立 AI 逐條內容審查 | 未列入已通過項目 |

以上靜態檢查**不等於**原始來源忠實度審查或 Python Lint 的執行結果。詳見 [成果報告](report.md) 與 [執行紀錄](RUN_LOG.md)。

## 資料與實作範圍

此專案是以可查詢的 Markdown 檔案與 HTML 頁面構成的**檔案式 Wiki**。五份 `raw/` 檔案為依據公開來源整理的摘要，不是原始論文全文，也不代表曾在特定線上平台自動匯入全文。批次更新與提交紀錄見 [wiki/log.md](wiki/log.md)。
