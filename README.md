# 性健康教育平台 LLM Wiki

這是依 Karpathy LLM Wiki 思路建立的繁體中文專案骨架：人選擇來源，AI 把來源整合為可累積的知識頁，再由人審閱後供網頁使用。

## 開始使用
1. 將整個資料夾交給可讀寫檔案的 AI 開發工具，請它先讀 AGENTS.md。
2. 將合法取得、無個資的來源放入私人環境的 raw 對應資料夾。
3. 請 AI：「依 AGENTS.md 匯入這份來源，完成來源摘要、更新主題頁、索引與紀錄；不要把草稿發布。」
4. 查詢範例：「先讀 Wiki，再回答某主題的教育需求；證據不足請列入 gaps。」
5. 維護範例：「執行 lint，檢查來源、連結、衝突與過時內容，列出需要人工審閱的頁面。」

## 檔案配置
| 路徑 | 功能 |
| --- | --- |
| AGENT.md、AGENTS.md | 中文入口與完整協作規則 |
| raw/ | 原始資料，新增後保持不變 |
| wiki/index.md | 知識目錄 |
| wiki/log.md | 只追加的操作紀錄 |
| wiki/sources/ | 來源摘要 |
| wiki/topics/、concepts/ | 主題及概念 |
| wiki/qa/、syntheses/ | 可重用問答與跨來源整合 |
| templates/ | 五種知識頁與教育單元模板 |
| docs/ | 工作流程、專案狀態與後續網頁規劃 |
| scripts/lint_wiki.py | 檢查本地連結、索引與必要欄位 |
| site/ | 待開發網頁的說明，尚無網站程式 |

## 檢查
在專案根目錄執行 `python3 scripts/lint_wiki.py`，只需 Python 3 標準函式庫。

## GitHub 與網站
目前是內容與規則骨架，尚未上傳 GitHub、建置網站或部署。先於私人倉庫整理及審閱，之後只將可公開且已審閱的內容輸出至網頁；不要直接把整個私人知識庫開成公開倉庫。

參考：[Karpathy 的 LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)。本專案非其官方產品；原始參考附件保存於 raw/project/。
