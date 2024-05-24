# rev C 1

Author: 孫逸平

Date: 2024-05-25

Link: https://lotuxctf.com/challenges#rev%20C%201-15

## 題目說明

你逆！

Reverse!


Author：FlyDragon

[main.zip](./src/main,zip)

## Write-up

1. `main.zip` 解壓縮後，是一個 `main.exe` 檔，加上觀察題目感覺是 C 語言。
2. 所以到網路上找 exe to C 的工具解碼。
3. 執行 `main.exe` 後發現要你輸入帳號密碼。
4. 將相關的字串在轉檔後的 .c 檔中查詢。
5. 發現只要密碼是 `I_LOVE_DONUTS` 就會吐 flag 出來。
6. 執行 `main.exe`，帳號亂打，密碼輸入 `I_LOVE_DONUTS`，就得到 flag 了：`LoTuX{ReVers3_cccc}`。
