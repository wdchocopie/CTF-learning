# Webstrike - Week1
Tool sử dụng trong bài: Wireshark
Scenario (tình huống): Một điểm bất thường đã được phát hiện trong mạng nội bộ của công ty chúng tôi khi nhóm dev đã tìm thấy một tệp bất thường trên webserver. Nghi ngờ có mã độc, nhóm mạng đã chuẩn bị một tệp pcap có network traffic quan trọng để phân tích cho nhóm bảo mật. Hãy phân tích gói pcap.
Với bài lần này, ta được cung cấp 1 file **pcap** được nén trong file **zip** với password **cyberdefenders.org**.
Link -> [Cyberdefend](https://cyberdefenders.org/blueteam-ctf-challenges/webstrike/)

----

# Các câu hỏi
![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/5d8a7e98-1536-47c9-b6ad-2218cc47d4a6)

Tạm dịch các câu hỏi:
1. Tìm kiếm địa chỉ IP của người tấn công
2. Tìm kiếm user-agent của kẻ tấn công
3. Tên của webshell đã upload
4. Tìm kiếm directory (thư mục) để chứa file vừa được upload
5. Webshell được gửi tới sử dụng port nào
6. Kẻ tấn công đang cố gắng lấy đi tập tin nào

# Bài làm
## Câu  1
Vì là người tấn công thì thường là người bắt đầu gói tin, nên mình sẽ lấy địa chỉ ip source của package đầu tiên

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/e423f212-d89b-4577-99d8-89b6954aa382)

Mình thử check địa chỉ **117.11.88.124** ở tại vị trí nào bằng [Ip location](https://www.iplocation.net/)

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/3eb8b49f-b59a-4897-a0cf-c481046f9e20)

Tại đây thì mình tìm được thành phố là Tianjin thì mình thử nhập vào ô điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/4ea6b7ee-851a-4d8f-8cb2-ccc190c2fe08)

## Câu 2
Vì câu này hỏi về user-agent, ta sẽ cùng đi tìm hiểu qua user-agent là gì
Về cơ bản, user-agent là thông tin bạn gửi tới server từ trình duyệt của bạn. Có thể hiểu nó là thứ để định danh bạn. Thông thường thông tim bao gồm:
* Phiên bản của trình duyệt
* Hệ điều hành của bên bạn
* Loại thiết bị (vd: Tablet, smartphone, laptop,...)
* 1 vài thông tin khác về client software

Trước tiên chúng ta cùng thử lọc xem cái nào có điều kiện ta cần. Mình sẽ lọc 2 lần với điều kiện thỏa mãn:
* Có source từ 117.11.88.124
* Có user-agent

Vậy ta có câu lệnh để lọc: 
`ip.src==117.11.88.124 && http.user_agent`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/ebf2e91e-f4c8-4657-934a-bd8b6afe7f50)

Mình xem thử 1 package, trong phần transmission control protocol (TCP) -> HyperText transfer protocol (Http) -> user-agent sẽ có đoạn string mình cần tìm 

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/37e1ba2e-1c63-46a5-9a71-1e4f366eae3f)

Theo như trên hình thì mình tìm được là `User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0\r\n` nhưng đuôi \r\n này là cách xuống dòng của window (Theo nguổn [StackOverflow](https://stackoverflow.com/questions/15433188/what-is-the-difference-between-r-n-r-and-n)). Và vì định dạng flag là không có đuôi \r\n nên flag chắc hẳn chỉ có phần `Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0`

Tiện cũng nói thêm về các cách xuống dòng ở trên các hệ điều hành:
* `\r` (Carriage return) là xuống dòng của MacOS từ trước X (Tức là từ đời dòng máy macintosh)
* `\n` (Line feed) là xuống dòng dành cho hệ điều hành macOS X, Unix và những bản phân phối của unix (Ubuntu, Kali linux,....)
* `\r\n` là xuống dòng dành cho Windows
**Với cái này mình có thể xác định được hệ điều hành của client sử dụng là gì**

Vậy mình thử nhập `Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0` vào phần điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/027bbd49-90ac-4b97-b8c1-9b539d25214e)

## Câu 3
Sau khi đọc câu này, mình sẽ thử kiểm tra xem từ file pcap này mình có xuất ra được file nào không bằng cách vào File -> Export object -> HTTP...

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/e54534ba-f1e3-4354-b0c0-0a309b668e3e)

Tại đây mình thấy 2 file đáng ngờ với dạng content là **multipart/form-data** tại package 53 và 63. Mình sẽ tiến hành kiểm tra 2 Package này. Điều cần chú ý ở đây là tại mục Multipart media encapsulation xem có cái gì liên quan tới tên file không

**Package 53**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/6ccc999f-f897-480b-819c-4b6097e99792)

**Package 63**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/46a3cdaf-f773-42f7-bfa0-0980d093bb6b)

Tại đây mình tìm thấy 1 phần khá đáng ngờ là **(application/X-php)**. Cái này còn được gọi là MIME (Multipurpose internet mail extension) dùng để trao đổi file với mail. Tại đây là đang trao đổi với file PHP

Mình sẽ tiến hành kiểm tra 2 mục này của cả 2 package 53 và 63

**Package 53**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/41f1b07a-312b-468b-9012-86fd6a0d99ea)

**Package 63**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/f692d0a2-c3e2-451d-b51a-b3b49dc60d5a)

Tại package 63 có 1 đoạn hiển thị `filename=image.jpg.php`. Mình đoán cái này chính là đáp án với 2 lí do:
* Đoạn này giống như là đang cố gắng lừa người đây là 1 file hình ảnh vậy.
* Dạng của flag là *****.***.***

Mình thử nhập trên chỗ nhập flag là `image.jpg.php`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/029db335-ba29-40da-adb4-8a5c75d43c22)

## Câu 4
