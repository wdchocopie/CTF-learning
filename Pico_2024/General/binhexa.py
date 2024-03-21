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