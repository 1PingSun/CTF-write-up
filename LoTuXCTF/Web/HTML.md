# HTML

Author: 孫逸平

Date: 2024-05-24

Link: https://lotuxctf.com/challenges#HTML-2

## 題目說明

FlyDragon 做了他的第一個網站。 雖然看起來甚麼都沒有，但只要按下 F12 開啟開發者工具就能找到他藏起來的東西！

FlyDragon has created his first website. Although it appears to be empty, if you open the developer tools by pressing F12, you can find the things he has hidden!


Author：FlyDragon

http://lotuxctf.com:20000

> **Hint:**
> 
> 本題共有三段 flag ，可組合成完整答案。
>
> To solve this challenge, you will need to assemble three flag segments.

## Write-up

1. 在原始碼中看到一個 script 標籤，當中有兩個 function，分別會打開 `cat.html` 和 `secret.html`。
2. 打開 `cat.html` 後，在原始碼的 /html/body/div/span/div/span/ 看到一個註解：`<!--flag 2/3: 3nD_h1Dden_-->`，此為 2/3 的 flag。
3. 打開 `secret.html` 檔，在頁面中看到：`flag 1/3: LoTuX{fR0nT_`，此為 1/3 的 flag。
4. 在原始碼中看到一 script 標籤，當中有一 function 可打開 `flag.html`。
5. 打開 `flag.html` 後，就在頁面中看到：`flag 3/3: Mes54ge}`，此為 3/3 的 flag。
6. 將三段 flag 組合後得到 flag：`LoTuX{fR0nT_3nD_h1Dden_Mes54ge}`。

## 防護說明與建議

### 本題 CWE

* CWE-200: Information Exposure

### 建議防護與修補

* 移除敏感資訊

## 心得

每次看到有好幾段 flag 的，看到都會很累。
