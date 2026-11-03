# 更新紀錄（只追加）

## [2026-11-03] init | 建立專案骨架
- 建立中文規則、模板、索引、三個主題規劃頁及檢查工具。
- 參考：使用者提供的 LLM Wiki 附件與 Karpathy 原始 Gist。
- 尚未匯入性健康證據、完成專業審閱或部署網站。

## [2026-11-03] ingest | SRC-0001 第一篇文章
- 保存使用者提供的完整PDF、抽取文字及SHA-256紀錄；原始PDF複製前後一致。
- 新增wiki/sources/lin-wu-2018-affirmative-consent.md與wiki/concepts/affirmative-consent.md。
- 更新wiki/topics/sexual-consent.md、wiki/index.md、wiki/gaps.md、raw/source-register.csv、docs/project-status.md與docs/workflows.md。
- AGENTS.md記錄往後每篇先存raw、再整理Wiki與索引的固定約定；AGENT.md維持連到唯一規則入口。
- 類型：2018年倡議評論；法制敘述屬歷史資料，2017調查為二手轉述。未據此更新現行法律、MSM數據或醫療建議。
- 所有實質新增／更新的知識頁為needs-review，未指定審閱者；未發布raw或網站。
- 解析限制：PDF交叉參照警告，成功抽取10頁文字及渲染首頁，保留原檔不改寫。
- lint結果：PASS（本地連結、必要欄位、索引與基本審閱欄位）；原檔SHA-256及來源登錄單一性檢查通過。
