# An unusual sighting

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/25d8dbb1-ecf6-4928-9125-47af102c7942)

Trước tiên là mình tải file về và xem nó cho mình dữ kiện gì

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/02a9f809-36e9-4797-afc7-9fe032fa9dde)

Tại đây nó cho mình 2 file như file log của bài. Mình tiến hành kết nối tới **docker** của challenge bằng **netcat**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/b31848d0-97a3-4fdf-88a2-d8289e6102c5)

Với câu này, mình nhìn vào file **sshd.log**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/d44bc6ce-0922-4ad4-b013-c0520d010256)

Tại đây ta thấy có máy tính connnect vào địa chỉ `100.107.36.130:2221`. Mình thử nhập vào

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/65d4770f-4c01-4137-afb6-37bc4268db63)

Ở ngay dưới file có đoạn như sau

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/ee90b1f2-84c9-45d0-90cb-21687e075a08)

Thử nhập `2024-02-13 11:29:50` vào ô trả lời

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/94d2c09f-c24a-4e9c-8b56-8a2ec052be95)

Tại đây ta biết rằng thời gian hoạt động của công ty này là từ **09:00 -> 19:00**. Mình sẽ xem phần nào có lịch sử login ngoài thời gian đó

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/afd43d74-0e6c-4731-b30c-1c82289b5dac)

Thấy có 1 đoạn nó hiển thị `2024-02-19 04:00:14`. Thử gửi nó về server 

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/33cdf0b7-0a71-4db4-98ae-153e6d11dcaa)

Ở ngay dưới đó chúng ta có fingerprint của kẻ tấn công

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/2227adc9-58b2-4cf0-8e04-4fbee2119408)

Thử nhập `OPkBSs6okUKraq8pYo4XwwBg55QSo210F09FCe1-yj4` vào

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/cecb6ed1-a153-4c52-8352-0c6401245591)

Với câu hỏi này, mình sẽ qua file **Bash_history.txt**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/4b351feb-df95-4e6e-b977-c7a1e6d38834)

Tại thời điểm 04:00, có 1 command được thực thi là `whoami`. Thử nhập vào

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/51e858eb-ad13-485b-8902-68d5e0df9618)

Với câu này mình sẽ tới câu lệnh nào thực thi cuối cùng trước 9h

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/45596c79-1e12-4c9d-974c-7b91d877ec8c)

Thử nhập `./setup` vào

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/04889e41-1304-4bbf-8381-0ca353552d3c)

Flag: `HTB{B3sT_0f_luck_1n_th3_Fr4y!!}`
