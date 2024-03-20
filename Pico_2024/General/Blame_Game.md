# Blame Game

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/6e6f13ff-ad17-404c-94e7-adbb13adf8b1)

Trước tiên vẫn phải tải file về và giải nén

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/cce84325-15c4-4159-a2d5-ca7f7c5fbd6f)

Mình sẽ thử kiểm tra file `.py` này xem sao

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/da91f4de-17dc-4e57-9645-4154d4dd4615)

Nhìn như có vẻ nó bị thiếu khiến cho python không chạy được. Vậy có lẽ file này đã bị sửa đổi. Mình kiểm tra `git log` trước.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/80e35296-b13d-4455-909e-61e4cd9ae598)

Có vẻ như người ta commit khá nhiều lần. Ngồi check hết thì cũng khá lâu. Mình cũng có dữ kiện là 1 author nào đó đã thay đổi nên mình sẽ thử `git log` với file `message.py`

`git log --follow -p -- message.py`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/b7db42b6-fc0b-40bb-9058-c0670690ef78)


Flag: `picoCTF{@sk_th3_1nt3rn_d2d29f22}`
