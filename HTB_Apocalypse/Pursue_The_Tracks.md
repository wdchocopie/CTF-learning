![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/135abdf7-54b3-4b7b-8bf5-c6b9360b8658)# Pursue The Tracks

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/34ead616-fdcb-429e-a406-2fab21d55735)

Mình tải file về trước

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/8f100bc0-dfd3-4e63-8f55-d8086c946fb2)

Tại đây mình sử dụng tool từ **Zimmerman** có têm là **MFTECmd**

`MFTECmd -f C:\Users\wdcho\Downloads\temp\forensics_persue_the_tracks\z.mft --csv C:\Users\wdcho\Downloads\temp\forensics_persue_the_tracks\a.csv`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/949e96c1-ad1b-4049-9c53-d39e3ceb9213)

Vậy là mình đã xuất xong thông tin từ file MFT. Mình cũng sẽ kết hợp với cả MFTExplorer để tiện nhìn hơn.

Mình tiến hành khởi động docker, truy cập vào server

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/032211fa-03a4-4847-8339-15292e1d42cc)

Trên explorer, Mình thấy có 2 directory là 2023 và 2024

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/4f68711d-4d0e-46ee-9202-80b2161b98c9)

Thử nhập vào `2023,2024`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/644a097a-c6b5-416b-8c03-420fcf92982b)

Tiếp đến mình lọc theo thời gian xem file nào là file viết gần nhất

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/dcc25d2d-9d26-4778-b32f-02663f864698)

Mình thấy file `Final_Annual_Report.xlsx` được tạo sớm nhất. Thử nhập vào

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/f28ddfc6-1858-495b-9408-51d18a365f63)

Tiếp tục nhìn trên **Explorer**, mình thấy có 1 file có icon như bị xóa đi rồi

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/098b6ac1-ff9e-4d9c-8cda-67a57421b473)

Thử nhập `Marketing_Plan.xlsx` vào

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/00a23538-71d0-47fd-8c47-84c143febf76)

Với cái này, vì trong explorer mình không thấy cột hidden file hay không, mình vào file **.csv** đã extract ra được

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/8ce4d7d6-7705-4f5b-9b21-cf5567edd935)

Mình thử sort theo chữ cái

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/babf407e-8f07-4c0d-b476-19f6cd2e6ce5)

Tại đây mình chỉ thấy 1 file hidden mà không phải là file hệ thống. Mình thử nhập `1`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/909fcdc7-c6c4-40e9-af2e-1362e80311a0)

Ta vừa có tên là `credentials.txt`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/50e59a17-6dab-4e4d-b9e8-6f72adeaab6f)

Với cái này mình tìm thử trong explorer và thấy

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/b20d5237-2811-4bd4-b515-c622e8962e0d)

Thử nhập `Financial_Statement_draft.xlsx` vào

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/ccfed5db-89b9-48e5-b22d-ac12d8c247c6)

Trong file csv của mình, mình sử dụng thuật toán so sánh giữa **Create** và **Modified** 

`=IF(TEXT(T2, "mm/dd/yyyy hh:mm:ss AM/PM") <> TEXT(V2, "mm/dd/yyyy hh:mm:ss AM/PM"), FALSE, TRUE)`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/b3c7072e-50e3-42a6-bd44-1110999cc679)
![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/218e24fb-6b38-4030-97fa-fa6cd0ddf6b2)



Tại đây ta thấy chỉ có `Project_Proposal.pdf` là hiện False không phải file hệ thống.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/70c20eca-521b-4546-9bbc-7e19cb9225f0)

Tìm tiếp ở file **CSV**, ta thấy

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/5f032e76-23a3-43fd-866e-634c2b606b51)

Thử nhập `Annual_Report.xlsx`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/51c63af8-040e-48b1-b72e-c74112ce8551)

Vào lại file CSV, mình thấy

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/90fded13-da25-45d5-a48d-bcc381b8278f)

Thử nhập `57344` 

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/bf0a3c6a-9503-4406-8619-aad758a5ec89)

Flag: `HTB{p4rs1ng_mft_1s_v3ry_1mp0rt4nt_s0m3t1m3s}`
