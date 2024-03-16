from pwn import *

p = remote('94.237.57.59', 53689)

flag = ''
idx = 0

while True:
    p.sendlineafter(b'index: ', str(idx).encode())
    p.recvuntil(b': ')
    char = p.recvS(1)

    flag += char
    idx += 1

    if char == '}':
        break

print(flag)
