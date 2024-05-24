# Title

Author: 孫逸平

Date: 2024-05-24

Link: https://lotuxctf.com/challenges#ASAP-8

## 題目說明

在一分鐘之內猜到數字並回答數學問題即可得到 100 萬獎金！
※ LoTuX 保有活動最終解釋權，得改發 150 分

Guess a number within a minute and answer some random math questions correctly to win a million-dollar prize!
※ LoTuX reserves the right of final interpretation and may change the reward to 150 points.


Author : FlyDragon

nc lotuxctf.com 10000

[server.py](./src/server.py)

## Write-up

1. 撰寫程式解題：
  ```python
  from pwn import *
  
  host = 'lotuxctf.com'
  port = 10000
  
  conn = remote(host, port)
  
  maxma = 100000000
  minma = 1
  
  line = conn.recvline().decode()
  h = "high"
  l = "low"
  c = "clear"
  number = 1
  while True:
      number = int((maxma + minma) / 2)
      conn.sendline(str(number))
      line = conn.recvline().decode()
      if(h in line.strip()):
          minma = number
      elif(l in line.strip()):
          maxma = number
      elif(c in line.strip()):
          print(number)
          break
  line = conn.recvline().decode()
  print(line.strip())
  
  for _ in range(101):
      line = conn.recvuntil('=').decode()
      a = line.strip()[0:-1].split("+")
      conn.sendline(str(int(a[0]) + int(a[1])))
  
  line = conn.recvline().decode()
  print(line.strip())
  
  print(number, line.strip())
  
  conn.close()
  ```
