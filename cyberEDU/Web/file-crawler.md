# Title

Author: 孫逸平

Date: 2024-05-22

Link: https://app.cyber-edu.co/challenges/981dca90-04bf-11ec-920e-fd2fbb634a4c?tenant=cyberedu

## 題目說明

Find the vulnerability and get the flag. The flag is located in a temporary folder.

## Write-up

1. 打開題目後，看到頁面中有一張圖片。
2. 透過開發者管理工具的 Source 分頁查看圖片網址路徑為：`/local?image_name=static/path.jpg`。
3. 猜測將 `image_name` 參數修改即可讀取任何檔案。
4. 因題目描述 flag 儲存在暫存資料夾，故盲猜 flag 位於 `/tmp/flag` 中。
5. 將網址路徑修改成 `/local?image_name=../../../../../../../tmp/flag`，發現仍無法找到檔案。
6. 猜測其透過篩選 `../` 避免路徑遍歷。
7. 但仍可透過將 `../` 修改成 `....//` 繞過驗證。
8. 將網址路徑修改成 `/local?image_name=....//....//....//....//....//....//....//tmp//flag`。
9. 網頁自動下載一個 `local` 檔。
10. 將該檔利用 `cat` 或文字編輯器等工具打開，就得到 flag 了！

## 防護說明與建議

### 本題 CWE

* CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')

### 建議防護與修補

* 使用白名單：利用白名單，只允許使用者讀取已授權之路徑

## 心得

在解這題的時候還算是順利，但我覺得有很多地方都必須盲猜，尤其是無法確定 flag 的路徑，因此很難進行各種排出，需要一個一個比對排查，有點靠運氣的感覺，下次比 CTF 前先去拜拜好了XD。但這種路徑遍歷的感覺好好玩，可以讀取到不被授權的東西。
