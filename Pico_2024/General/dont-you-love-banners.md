# dont-you-love-banners

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/a799dabe-622c-40b5-9c68-e2924f0de4ed)

Trước tiên mình tiến hành cho chạy docker của bài 

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/c604211f-008c-4c12-af03-d6c588754b0c)

Connect thử vào địa chỉ đầu tiên với `netcat`

`nc tethys.picoctf.net 60589`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/136b153c-caed-4af2-9857-53f9dcb75256)

Thử connect sang cái thứ 2

`nc tethys.picoctf.net 58750`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/99d27ed4-c51d-494f-868f-c11fcf792364)

Dựa theo thông tin trên đề bài, mình phát hiện ra phần `My_Passw@rd_@1234` là password cho cái này

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/6a276df4-8eb4-477f-80c8-7b1bd64ca980)

Với 1 đường dùng Ai cực nhanh, mình có đáp án là `defcon`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/ec6c6464-9ff0-4f10-9ca5-db74caef07f2)

Tiếp tục google nhanh, mình có đáp án là `John Draper`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/084b9c8d-b198-47bf-9675-f97ba9a7f6ac)

Tại đây mình đã vào được shell của bài. Mình thử kiểm tra trước bằng lệnh ls

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/0f95e5e7-f452-4843-a002-15a49c55671e)

Thử cat file `banner` và `text` ra

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/0ed779e6-c784-4163-a331-8675045c0f6d)

Mình thử tiếp tục tìm bằng cách `ls` những directory quan trọng

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/ec12b3be-2317-41e7-9548-04ac6b293532)

Tại đây mình thử `cat flag.txt`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/cbb369c6-a090-425a-b42d-0d85b1f96af2)

Thử cat file `.py` còn lại

```
cat /root/*.py

import os
import pty

incorrect_ans_reply = "Lol, good try, try again and good luck\n"

if __name__ == "__main__":
    try:
      with open("/home/player/banner", "r") as f:
        print(f.read())
    except:
      print("*********************************************")
      print("***************DEFAULT BANNER****************")
      print("*Please supply banner in /home/player/banner*")
      print("*********************************************")

try:
    request = input("what is the password? \n").upper()
    while request:
        if request == 'MY_PASSW@RD_@1234':
            text = input("What is the top cyber security conference in the world?\n").upper()
            if text == 'DEFCON' or text == 'DEF CON':
                output = input(
                    "the first hacker ever was known for phreaking(making free phone calls), who was it?\n").upper()
                if output == 'JOHN DRAPER' or output == 'JOHN THOMAS DRAPER' or output == 'JOHN' or output== 'DRAPER':
                    scmd = 'su - player'
                    pty.spawn(scmd.split(' '))

                else:
                    print(incorrect_ans_reply)
            else:
                print(incorrect_ans_reply)
        else:
            print(incorrect_ans_reply)
            break

except:
    KeyboardInterrupt
```
Có vẻ như đây là code để chạy khi ta connect `nc` vào địa chỉ thứ 2. Tại đây mình thấy file này tại sao lại phải chạy file `banner` tại thư mục mình đang ở. Dựa theo những gì mình biết thì ta có thể lợi dụng việc chạy file này để mở file `flag.txt` sử dụng symlinks. Mình cũng thử kiểm tra hint đề bài cho

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/48ed76b2-428c-45d0-b326-b40400db87fc)

Mình sẽ xóa file `banner` trước và tiến hành tạo 1 file banner mới là symlinks của file `flag.txt`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/5bf237ff-590b-4fca-817e-9054f26ed146)

Tại đây mình chỉ việc out ra và connect lại địa chỉ thứ 2

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/3fd79e45-928f-487e-b429-005fe9d19bc1)

Flag: `picoCTF{b4nn3r_gr4bb1n9_su((3sfu11y_ed6f9c71}`
