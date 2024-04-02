# Blast from the past

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/a72591a7-16b2-4635-aec3-0e7cb50246aa)

Trước tiên mình sẽ tiến hành tải file hình ảnh và làm theo hướng đẫn của đầu bài

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/1216418d-bf2b-4697-a607-ee62cc978fd0)

Mình sẽ sử dụng **Exiftool Gui** để sửa `ModifyDate`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/76a9b7fc-8da2-4a90-95d7-041e972422cc)

Tiếp tục lại gửi file về server

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/6532e8f5-f21c-4233-ae38-f12f740b31be)

Tiếp tục thay đổi `DateTimeOriginal`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/1218537f-11a7-4478-9fd2-c154f4efce0b)

Gửi lại hình ảnh về server

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/77c6a9bd-d569-474d-801a-93add4779bc7)

Tiếp tục chỉnh `CreateDate`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/48949b2e-8850-4359-9638-e926cbb1c790)

Lại gửi nó về server

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/ee5bd182-15b5-4b8e-9848-bef90fb12b61)

Chỉnh `SubSecCreateDate`. Tại Exiftool Gui nó cho 1 tùy chọn duy nhất là chỉnh `SubSecTime`, `SubSecTimeOriginal` và `SubSecTimeModified` nên mình sẽ chỉnh cả 3 cái đó.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/1f0ec0ab-b81c-4a7d-9a93-ddac46965aa9)
  
Gửi lại về server và check

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/8cfc590b-1730-4adf-81ed-4ce019ce1a97)

Tìm mục `samsung` và thử thay đổi theo nó

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/9b1fd7b5-5a04-421c-a81d-245ef468ef8e)

Có vẻ nó bị lỗi. Lỗi này khả năng là do không thể thay đổi bằng **Exiftool**. Mình thử đổi qua **HXD**.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/a497b749-c22a-4878-a8b0-e09e5a44f8a3)

Tại đây mình thấy đoạn này có timestamp trùng khớp với timestamp server vừa đọc. Mình sẽ thay đổi nó về

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/cb1d97dc-b82c-47b0-af3f-aff78aba4f90)

Gửi lại hình ảnh về server

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/7904c5ac-0f10-4d0c-a840-aaf11af22042)

Flag: `picoCTF{71m3_7r4v311ng_p1c7ur3_a4f2b526}`
