# PW Crack 3
Cơ bản khi mình check bài nó có đoạn này

```
def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()
```

Đoạn này nó sẽ encrypt đoạn password thành md5. Nhiệm vụ của mình là crack trong vùng `pos_pw_list = ["6997", "3ac8", "f0ac", "4b17", "ec27", "4e66", "865e"]`. Để tiện mình tạo script luôn.

```
import hashlib

correct_pw_hash = open('level3.hash.bin', 'rb').read()

def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()

def level_3_pw_check():
    for user_pw in pos_pw_list:
        user_pw_hash = hash_pw(user_pw)
        
        if( user_pw_hash == correct_pw_hash ):
            print(user_pw)
            
            return
    print("That password is incorrect")





pos_pw_list = ["6997", "3ac8", "f0ac", "4b17", "ec27", "4e66", "865e"]
level_3_pw_check()
```

![image](https://github.com/user-attachments/assets/129d63c7-79c9-4ad1-8d53-d976333d8349)

Chạy lại file và ăn flag:

![image](https://github.com/user-attachments/assets/e76f5d94-4f24-4c83-b466-d600032f53cb)

Flag: picoCTF{m45h_fl1ng1ng_2b072a90}
