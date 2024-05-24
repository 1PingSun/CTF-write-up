# ZongZi

Author: 孫逸平

Date: 2024-05-25

Link: https://lotuxctf.com/challenges#ZongZi-30

## 題目說明

🐉🚣

Author：FlyDragon

[ZongZi](./src/ZongZi)

## Write-up

1. 利用 cat 查看檔案內容：`cat Zongzi`。
2. 猜測其為 obj 檔。
3. 發現包含兩物件，一物件名稱為 text。
4. 將該物件提取出來另存。
5. 打開後發現長的很 flag，但內容看不清楚。
6. 經過各種測試及爬文後，發現保留 v 值以及 f 值第一筆資料的第一項、第二筆資料的第一項、第三筆資料的第一項
7. 利用 3D 預覽等應用程式開啟後，就看到 flag 了：`LoTuX{Dr4gon_b0at_fest1val!}`。
