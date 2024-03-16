# Character

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/412f6c1e-4702-497f-b125-d6638ffd29c6)

Tại đây mình thử netcat vào server người ta

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/bb097de9-5aad-4be0-bdc2-6bdcbe497e5a)

Có vẻ flag sẽ dài nên mình code 1 đoạn script kết nối tới server của họ 

```
import pwn

p=pwn.remote ("", "")

flag = ""

i = -1

while True:
    i+=1
    p.sendlineafter ("index: ", str(i))
    p.recvuntil(": ")
    flag += p.recvline().strip().decode()
print (flag)
```

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/e52e9d8a-0a7c-44ff-8c41-ec5193506f81)

Flag: `HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_iT_t0oK_qU1t3_l0ng!!}`
