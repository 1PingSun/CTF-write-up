# forum

Author: 孫逸平

Date: 2024-05

Link: https://lotuxctf.com/challenges#forum-29

## 題目說明

作為滲透測試的專家，你一眼就看出這個網站有許多漏洞。

As an expert in penetration testing, you can immediately identify multiple vulnerabilities in this website.


Author：FlyDragon

username : user
password : user
http://lotuxctf.com:20004

## Write-up

1. 打開題目後利用題目提供的帳號密碼登入，發現有三篇文章。
2. 發現這三篇文章的網址分別為 `post1.php`、`post2.php`、`post3.php`。
3. 猜測為 IDOR 漏洞，打開 `post0.php` 發現 1/2 的 flag：`LoTuX{S0_Much`。
4. 看到部分文章的作者為 `admin`。
5. 嘗試回到登入頁面利用 SQli 登入 `admin` 帳號，利用帳號：`admin`；密碼：`' OR 1=1 -- -` 登入，順利成功登入。
6. 在打開第一篇文章並點擊 Edit 後，從彈跳視窗得到 2/2 的 flag：`_vu1ner4biliTy}`。
7. 將兩段 flag 組合後提交，就過關了：`LoTuX{S0_Much_vu1ner4biliTy}`。

## 防護說明與建議

### 本題 CWE

* CWE-639: Authorization Bypass Through User-Controlled Key
* CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')

### 建議防護與修補

* 關於 IDOR：
  * 存取控制：限制使用者可存取之路徑
  * 隨機檔名：將檔名設為隨機等不可預測之名稱
* 關於 SQLi：
  * 輸入驗證：透過黑白名單限制輸入的內容

## 心得

在打這題的時候，過程非常順利，除了在拿到 1/2 的 flag 後還要拿後半段的 flag 很想罵髒話，但 2/2 的 flag 也是很簡單 SQLi 漏洞，本來還打算用 SQLmap 去測，結果手動就成功了！
