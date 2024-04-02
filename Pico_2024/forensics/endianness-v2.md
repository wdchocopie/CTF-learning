![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/1816a532-3e48-422c-8d29-6a50923c65b9)# Endianess-v2

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/89f3c042-d44e-4b82-88bb-537379e8d577)

Dựa theo thông tin đề bài, mình tiến hành tải file về và kiểm tra nó với **Hxd**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/68c4f842-c79f-4baa-9218-bccd4178aee0)

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/44131693-9f7e-4424-b868-b795916a4ef5)

Dưới đây là thông tin mình rút ra được:
* File này là file jpg (Dựa vào đoạn JFIF bị đảo)
* Trong file này, 4 byte bị đảo chỗ cho nhau theo hình bên dưới
* Dựa vào thông tin bài **endianess** thì sẽ có cả **Big Endian** và **Little Endian**
-> Cấu trúc file là dạng **Big Endian**, 4 byte bị đảo theo quy tắc **Little Endian**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/f0b11062-b3af-42f9-9bfd-1d334c8052eb)

Vậy mình sẽ code 1 python script để nhóm 4 byte 1, thay đổi nó về vị trí ban đầu

```
def reverse_bytes_in_groups(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()

    reversed_data = bytearray(data)

    for i in range(0, len(reversed_data), 4):
        group = reversed_data[i:i+4]
        group.reverse()
        reversed_data[i:i+4] = group

    with open(file_path, 'wb') as file:
        file.write(reversed_data)

file_path = "challengefile" #file_path
reverse_bytes_in_groups(file_path)
```
Mở file lên dưới dạng jpg và ta có

![challengefile](https://github.com/wdchocopie/CTF-learning/assets/81132394/d1bc3c49-e3e8-4f2b-9d1e-fa0016c7492f)

Flag: `picoCTF{cert!f1Ed_iNd!4n_s0rrY_3nDian_f72c4bf7}`
