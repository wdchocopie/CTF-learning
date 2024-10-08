# PW Crack 5
Giờ 1 chút thay đổi về script. Mình chỉ cần đọc nó từ file, ném nó vào array và chạy

```
import hashlib

correct_pw_hash = open('level5.hash.bin', 'rb').read()
dictionary = open('dictionary.txt', 'r')

def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()

def level_3_pw_check():
    for user_pw in dictionary_array:
        user_pw_hash = hash_pw(user_pw)
        
        if( user_pw_hash == correct_pw_hash ):
            print(user_pw)
            
            return
    print("That password is incorrect")

dictionary_array = []
for line in dictionary:
    dictionary_array.append(line.strip())




    
level_3_pw_check()
```
![image](https://github.com/user-attachments/assets/d873c9e9-8ae0-4c38-a28c-cadec98b22bb)

![image](https://github.com/user-attachments/assets/201fccb6-53a5-4a69-82fa-168b38398375)

Flag: picoCTF{h45h_sl1ng1ng_36e992a6}
