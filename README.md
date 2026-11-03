# 性健康教育 LLM Wiki

以中文AGENTS規則維護知識庫，並衍生筆記、逐頁稿與溫暖教育型HTML簡報。正文只依Wiki已收錄來源，建議文獻分區列示。

- [公開展示](https://sexual-health-wiki-classroom.lucky-pear-8620.chatgpt.site/)
- [展示首頁](site/index.html)
- [中文協作規則](AGENTS.md)
- [繳交說明](docs/assignment-submission.md)

## 使用
直接開啟 index.html 即可瀏覽；需保留 site/assets。公式引擎隨專案保存。無API金鑰、帳號或後端依賴。

## GitHub 上傳與 Pages
建立新的公開Repository，將本資料夾內所有檔案上傳至根目錄並提交。Repository內應直接看見AGENTS.md、index.html與site/，不要再包一層資料夾。
Settings → Pages → Deploy from a branch → main / root → Save。等待部署完成後，複製GitHub顯示的實際網址。
老師允許其他網站發布方式，因此上方公開展示網址也可作為網站成果；仍需另交實際GitHub Repository連結。

## 新增內容
先讀AGENTS.md，依raw → wiki → notes → slides → presentations/site流程。公開包不包含原始全文，來源請循DOI取得。勿將私人全文直接上傳。

## 驗證
執行 python3 scripts/lint_wiki.py。瀏覽器已檢查首頁、翻頁、講稿與公式；未在實體手機或印表機驗證。

## 第三方
KaTeX 0.16.11 採MIT授權，LICENSE隨site/assets/katex保留。教育內容為待審閱課程展示。
