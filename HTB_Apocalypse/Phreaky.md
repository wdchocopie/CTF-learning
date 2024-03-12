![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/07164d67-981f-46f5-9d62-62d4ccd43445)# Phreaky

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/846c5e0b-0eaa-44f7-b017-61edad4a01e6)

Mình download file pcap về, chạy thử **Network miner** 

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/6af128f6-20ff-4d32-8d08-9b35c9e61758)

Tại đây mình thấy có khá nhiều file **zip**. Mình thử vào xem thử 1 cái

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/b78573f1-240c-4aec-908c-003a3a831413)

Tại đây nó có 1 file bên trong là `phreakplan.pdf.part1`. Mình sẽ sử dụng pcap để xem có tìm được các gói đấy không

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/85aedd50-57c4-4c54-80b6-8da041d69588)

Mình chỉ thấy các file **.eml** nên mình thử xuất hết ra, tiến hành đọc thử 1 file

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/02f4e6e1-2f72-4e06-bb0c-68e24c6ca1a7)

Có vẻ trong này chứa **base64** của file **zip** và chứa cả password. Mình tiến hành đổi mã base64 qua file và xuất file ra

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/59417ffb-a92b-4bf0-8458-ae24b122d569)

Cuối cùng mình ghép hex của các file vào với nhau. Mình có 1 file cuối cùng là pdf. Mở thử và lướt xuống cuối

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/15b117e9-63b9-4265-b86a-cb5b9fc5d1f9)

Flag: `HTB{Th3Phr3aksReadyT0Att4ck}`

**--End--**
