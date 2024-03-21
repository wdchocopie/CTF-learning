# Binhexa

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/38652362-f481-4e88-82be-7bcbc6d52f55)

Với bài này thì mình thử chạy 1 lần.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/4ae189f7-aad5-47d6-b14d-8ef4d518a72d)

Dựa theo quy tắc này mình lên tools bằng **python 3** sử dụng `pwntools`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/4d6a7ec9-4712-44c9-8152-363023decf28)

```
import pwn

p = pwn.remote ("titan.picoctf.net", "56491")


p.recvuntil("Binary Number 1: ".encode())
bin1 = int(p.recvline().decode() , 2)
#print(bin1)

p.recvuntil("Binary Number 2: ".encode())
bin2 = int(p.recvline().decode() , 2)
#print(bin2)
for i in range (1, 7):
    operation_slice = f"Operation {i}: '"
    #print(operation_slice)
    p.recvuntil(operation_slice.encode())
    operation = p.recvline().decode()[0:1]
    #print(operation)
    if operation == "&":
        bin_final = bin1 & bin2
    elif operation == "|":
        bin_final = bin1 | bin2
    elif operation == "^":
        bin_final = bin1 ^ bin2
    elif operation == ">":
        p.recvuntil("Binary Number ".encode())
        bin_num =  p.recvline().decode()[0:1]
        if bin_num == "1":
            bin_final = bin1 >> 1
        elif bin_num == "2":
            bin_final = bin2 >> 1    
    elif operation == "<":
        p.recvuntil("Binary Number ".encode())
        bin_num =  p.recvline().decode()[0:1]
        if bin_num == "1":
            bin_final = bin1 << 1
        elif bin_num == "2":
            bin_final = bin2 >> 1 
    elif operation == "*":
        bin_final = bin1 * bin2
    elif operation == "+":
        bin_final = bin1 + bin2
    
    result = str(bin(bin_final))[2:]
    #print(result)
    p.sendlineafter("Enter the binary result: ".encode(),result.encode())

print(p.recv().decode())
```

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/74687c05-ca7c-4967-9018-85643b2f775b)

Tại đây mình thấy 1 phần cuối là đổi thành `hex`. Mình sử dụng `hex()` rôi gửi lại là xong

```
import pwn

p = pwn.remote ("titan.picoctf.net", "56491")


p.recvuntil("Binary Number 1: ".encode())
bin1 = int(p.recvline().decode() , 2)
#print(bin1)

p.recvuntil("Binary Number 2: ".encode())
bin2 = int(p.recvline().decode() , 2)
#print(bin2)
for i in range (1, 7):
    operation_slice = f"Operation {i}: '"
    #print(operation_slice)
    p.recvuntil(operation_slice.encode())
    operation = p.recvline().decode()[0:1]
    #print(operation)
    if operation == "&":
        bin_final = bin1 & bin2
    elif operation == "|":
        bin_final = bin1 | bin2
    elif operation == "^":
        bin_final = bin1 ^ bin2
    elif operation == ">":
        p.recvuntil("Binary Number ".encode())
        bin_num =  p.recvline().decode()[0:1]
        if bin_num == "1":
            bin_final = bin1 >> 1
        elif bin_num == "2":
            bin_final = bin2 >> 1    
    elif operation == "<":
        p.recvuntil("Binary Number ".encode())
        bin_num =  p.recvline().decode()[0:1]
        if bin_num == "1":
            bin_final = bin1 << 1
        elif bin_num == "2":
            bin_final = bin2 >> 1 
    elif operation == "*":
        bin_final = bin1 * bin2
    elif operation == "+":
        bin_final = bin1 + bin2
    
    result = str(bin(bin_final))[2:]
    #print(result)
    p.sendlineafter("Enter the binary result: ".encode(),result.encode())

hexa_result = str(hex(bin_final))
p.sendlineafter("Enter the results of the last operation in hexadecimal: ".encode(),hexa_result.encode())
print(p.recv().decode())
```

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/462039ba-af09-4221-aa20-446452d0edec)

Flag: `picoCTF{b1tw^3se_0p3eR@tI0n_su33essFuL_6862762d}`
