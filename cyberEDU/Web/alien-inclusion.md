# alien-inclusion

Author: 孫逸平

Date: 2024-05-22

Link: https://app.cyber-edu.co/challenges/82a11560-3621-11eb-861a-3777b029f577?tenant=cyberedu

## 題目說明

Keep it local and you should be fine. The flag is in /var/www/html/flag.php.

## Write-up

1. 打開題目後看到原始碼，透過觀察發現 GET 的 `start` 參數必須有內容，且透過將 POST 的 `start` 設為路徑，即可讀取該路徑之檔案。另題目說 flag 藏在 `/var/www/html/flag.php`。
2. 透過 postman 將方法設定為 POST，網址路徑為 `/?start=123`，body 新增 start 參數為 `/var/www/html/flag.php`，並發送請求就獲得 flag 了。

## 防護說明與建議

### 本題 CWE

* CWE-98: Improper Control of Filename for Include/Require Statement in PHP Program ('PHP File Inclusion')

### 建議防護與修補

* 輸入驗證：透過白名單限制可讀取之路徑，避免機密檔案洩露。

## 心得

在解這題時，我原本沒有考量到要如何同時存在 GET 和 POST，幸好 postman 的操作還算方便，我就嘗試在網址後方加入參數，並在 body 新增參數，就同時傳送 GET 和 POST 的參數了，過程還算順利，為什麼有同學說很難？
