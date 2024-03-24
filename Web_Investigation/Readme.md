![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/1ebe072a-00b9-4e15-a4f4-097e0ce862b1)# Web Investigation - Week 5
----
**Scenario:** 
Bạn là nhà phân tích an ninh mạng làm việc tại Trung tâm Điều hành An ninh (SOC) của BookWorld, một hiệu sách trực tuyến mở rộng nổi tiếng với tuyển tập văn học phong phú. BookWorld tự hào về việc cung cấp trải nghiệm mua sắm liền mạch và an toàn cho những người đam mê sách trên toàn cầu. Gần đây, bạn được giao nhiệm vụ củng cố tình hình an ninh mạng của công ty, giám sát lưu lượng truy cập mạng và đảm bảo rằng môi trường kỹ thuật số vẫn an toàn trước các mối đe dọa.

Vào một buổi tối muộn, một cảnh báo tự động được kích hoạt khi số truy vấn cơ sở dữ liệu và mức sử dụng tài nguyên máy chủ tăng đột biến bất thường, cho thấy hoạt động độc hại tiềm ẩn. Điều bất thường này làm dấy lên lo ngại về tính toàn vẹn của dữ liệu khách hàng và hệ thống nội bộ của BookWorld, thúc đẩy một cuộc điều tra ngay lập tức và kỹ lưỡng.

Với tư cách là nhà phân tích chính trong trường hợp này, bạn được yêu cầu phân tích lưu lượng truy cập mạng để phát hiện ra bản chất của hoạt động đáng ngờ. Mục tiêu của bạn bao gồm xác định vectơ tấn công, đánh giá phạm vi của bất kỳ vi phạm dữ liệu tiềm ẩn nào và xác định xem kẻ tấn công có giành được quyền truy cập sâu hơn vào hệ thống nội bộ của BookWorld hay không.

**Tool sử dụng**: 
* Wireshark
* networkminer

**Dữ liệu được cung cấp:**
* 1 file Pcap trong file zip
* Password: cyberdefenders.org

Link -> [Cyberdefend](https://cyberdefenders.org/blueteam-ctf-challenges/web-investigation/)

----
# Câu hỏi

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/e978d463-52a5-4a8a-a04d-8105c0ec37e5)

**Tạm dịch:**
1. Địa chỉ ip của kẻ tấn công
2. Thành phố mà kẻ tấn công đang ở
3. Tên của Vulnerable script
4. URI chứa SQLI của kẻ tấn công (Đầu tiên)
5. URI dùng để đọc database
6. Tên của Table chứa thông tin người dùng
7. Tên của thư mục mà kẻ tấn công có quyền truy cập
8. Tài khoản và mật khẩu dùng để log in
9. Tên script chứa mã độc

----
# Kiến thức cần biết

**SQLI (SQL Injection)**: SQL Injection là một kỹ thuật lợi dụng những lỗ hổng về câu truy vấn của các ứng dụng. Được thực hiện bằng cách chèn thêm một đoạn SQL để làm sai lệnh đi câu truy vấn ban đầu, từ đó có thể khai thác dữ liệu từ database. SQL injection có thể cho phép những kẻ tấn công thực hiện các thao tác như một người quản trị web, trên cơ sở dữ liệu của ứng dụng.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/2aff37b2-0175-44d1-8ab4-1f3d3b0ea793)

- SELECT - truy vấn dữ liệu từ một bảng
- INSERT - thêm dữ liệu vào bảng
- UPDATE - chỉnh sửa dữ liệu đã có
- DELETE - xóa dữ liệu trong một bảng
- DROP - xóa một bảng
- UNION - ghép dữ liệu từ nhiều truy vấn với nhau

- WHERE - bộ lọc SQL được sử dụng khi có điều kiện đi kèm
- AND/OR - kết hợp với từ khóa WHERE để làm truy vấn cụ thể hơn
- LIMIT #1, #2 - Giới hạn lượng dữ liệu trả về #2 bắt đầu từ vị trí #1 (Ví dụ LIMIT 3,2; sẽ trả về 2 dòng dữ liệu thứ 4 và 5.)
- ORDER BY - sắp xếp dữ liệu theo cột

----
# Câu 1

Sau khi tải file Pcap về, mình tiến hành check vào phần conversation

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/13154cb7-19fd-4782-9a35-6184b9571418)

Tại đây mình thấy 1 đoạn có nhiều packet được gửi đi hẳn. Với dữ kiện đầu bài đã cung cấp thì đây là SQLI thì việc giao tiếp nhiều cũng là điều hiển nhiên do kẻ tấn công sẽ gửi rất nhiều Query về để khai thác thông tin từ database

Thực ra tại đây chúng ta chỉ thấy địa chỉ `111.224.250.131` là chỉ connect tới `73.124.22.98` và ta có thể suy ra luôn địa chỉ này là của kẻ tấn công. Mình sẽ tiến hành filter lại để kiểm tra cho chắc ăn

`ip.addr==111.224.250.131 and ip.addr==73.124.22.98`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/77360f5d-976f-4c3e-9f1d-480ec497f70e)

Packet đầu tiên 2 địa chỉ này giao tiếp với nhau là từ phía `111.224.250.131`. Thử nhập địa chỉ này vào ô điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/4455429e-4e84-4e50-a4a1-fe5d1bded008)

----
# Câu 2  

Câu này khá đơn giản thôi. Tiến hành vào trang [Search vị trí của ip](https://www.iplocation.net/ip-lookup) và nhập địa chỉ ip của kẻ tấn công ta vừa tìm được

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/2960bac0-08de-44fd-822b-f6449eb463dc)

Ta thấy phần city nó để là `Shijiazhuang`. Thử nhập nó vào

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/ee1da196-bbcb-4379-8944-69d4d614fd1b)

----
# Câu 3

Với câu này ta chỉ cần tìm xem có file nào gửi các query của SQLI đi. Mình sẽ tiến hành filter ip của kẻ tấn công và http.

`ip.addr==111.224.250.131 and http`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/e9d7f7cd-69cf-43f4-a9b1-ab43b990b95d)

Tại đây ta thấy phần info của packet 426 như là 1 Query. Và có vẻ script đang chạy là `search.php`. Thử nhập vào ô điền flag.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/2f41e878-173f-4fc9-a194-82671b50cc45)

----
# Câu 4

Kéo lên trên 1 tí

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/626e3d26-b104-4c0c-af6a-5c5718803e96)

Tại packet 357, Ta thấy URI có chứa dấu `-` ở cuối cùng. Đây là 1 dấu đặc biệt trong việc khai thác SQL như đã đề cập ở trên. Thử nhập `/search.php?search=book%20and%201=1;%20--%20-`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/f3a3ed5e-908f-4dac-9e8f-6f0ae3b88f85)

----
# Câu 5
Tại câu này, mình sẽ đổi qua **networkminer**. Tại đây mình tìm tới từ khóa là `INFORMATION_SCHEMA.SCHEMATA`. Cơ bản đây là Virtual table chứa thông tin của tất cả các database có trên hệ thống. 

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/54a2fbea-4e76-4319-bc3b-293aa3dba7db)

Thử nhập `/search.php?search=book%27%20UNION%20ALL%20SELECT%20NULL%2CCONCAT%280x7178766271%2CJSON_ARRAYAGG%28CONCAT_WS%280x7a76676a636b%2Cschema_name%29%29%2C0x7176706a71%29%20FROM%20INFORMATION_SCHEMA.SCHEMATA--%20-` vào ô điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/25906f9d-51e9-43b5-a103-dd24f8aa1122)

----
# Câu 6

Dựa theo câu này thì tất cả các thông tin sau đó sẽ sau packet tìm tên của database. Mình tiến hành tìm thử packet đó

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/6eaa430b-0f7f-4d11-9e2d-3a665630c606)

Sau khi lục lọi 1 hồi, mình thấy có packet này gửi request về lấy `address`, email và 1 số thứ khác

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/0c8392f6-b187-46e3-b513-d532e3e229bb)

Nhưng nó đã bị cắt ngắn đi. Cái này là do [`ITEM_LABEL_LENGTH > 240`](https://osqa-ask.Wireshark.org/questions/8166/truncated-uri-in-the-Wireshark-ui/). Mình sẽ copy phần bị cắt qua bên **networkminer**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/73458764-ce71-44f4-8da7-5992b7c50bd8)

Tại đây nếu ta phân tích đoạn `/search.php?search=book%27%20UNION%20ALL%20SELECT%20NULL%2CCONCAT%280x7178766271%2CJSON_ARRAYAGG%28CONCAT_WS%280x7a76676a636b%2Caddress%2Cemail%2Cfirst_name%2Cid%2Clast_name%2Cphone%29%29%2C0x7176706a71%29%20FROM%20bookworld_db.customers--%20-`
* `bookworld` là tên database
* `customers` là tên bảng

Thử nhập `customers` vào ô điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/a20797d5-9cd0-4a67-ab5b-b527db53bfef)

----
# Câu 7

Tại ngay mấy packet sau, ta thấy có vẻ như kẻ tấn công đã truy cập được các file trên hệ thống. 

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/648b17bc-1545-4da7-84bf-4b613ec2f8d5)

Thử lướt xuống dưới ta thấy

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/c69feae5-9c74-4c89-9fd5-d4c9e5c94bb1)

Tại đây ta có thể thấy có 1 thư mục là `/admin/` mà kẻ tấn công đã truy cập. Thử nhập vào ô điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/72ca7376-c65f-4d4a-9f84-db9b7b37bb80)

----
# Câu 8

Ở ngay dưới ta thấy 4 packet có phần `application/x-www-form-urlencoded`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/03a76f1c-a908-49aa-a58f-e7c626572124)

Đây là dạng application (chương trình). Mình thử vào xem cái đầu tiên

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/7f234795-b1f4-40ac-881e-cbbe9502d8cc)

Tại đây nó cho login credential. Tuy vậy nhưng có tới 4 cái. Vậy khả năng 3 cái đầu là bị nhập sai. Mình sẽ kiểm tra cái thứ 4

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/f60a5928-6e8a-4b3d-94a6-316ab9c9804e)

Thử nhập `admin:admin123!`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/d336feba-465b-4192-895a-1ca64414211d)

----
# Câu 9

Trong **networkminer**, Mình để ý thấy sau đoạn log in vào hệ thống thì trong frame 88757 đã được gửi 1 lúc 2 file đi. 

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/a60c8827-9365-4dd9-b023-2755fe6b5b2b)

File `index.php` như được làm nền để che đi cái còn lại. Mình thử vào **Wireshark** để kiểm tra

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/f03e956e-9642-4aa9-a2fd-31f64c0836b7)

Tại đây ta không thấy cả file có tên lạ được gửi đi. Quay trở lại **networkminer**, ta thấy có vẻ file này là dạng **MIME**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/1628f3ae-c3b8-4177-81e9-558da8c4bc51)

Và mình thử mở file này ra

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/79a7fa2f-983b-482b-858e-36b53fff5998)

Ta có thể khẳng định đây là script chứa mã độc. Thử nhập `NVri2vhp.php` vào

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/417561f2-5e7a-423a-97b9-2dcc7c37e923)

----
# End of challenge check

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/a69392ab-07ef-4c50-a066-f264f2295c4c)

**--END--**
