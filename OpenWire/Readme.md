# OpenWire - Week 1
**Tool sử dụng trong bài**:
* Google
* Wireshark

**Scenario**: Trong quá trình làm việc với tư cách là nhà phân tích SOC-Tier2, bạn sẽ nhận được báo cáo từ Tier 1 về máy chủ công khai. Máy chủ này đã bị gắn cờ vì thực hiện kết nối ra ngoài tới nhiều IP đáng ngờ. Để phản hồi, bạn bắt đầu giao thức ứng phó sự cố tiêu chuẩn, bao gồm cách ly máy chủ khỏi mạng để ngăn chặn khả năng di chuyển sang bên hoặc đánh cắp dữ liệu và thu thập gói tin từ tiện ích NSM để phân tích. Nhiệm vụ của bạn là phân tích pcap và đánh giá các dấu hiệu của hoạt động độc hại.

**Thông tin dược cấp trong bài**: 1 file zip có pass giải nén là cyberdefenders.org, bên trong có 1 file pcap

Link -> [CyberDefend](https://cyberdefenders.org/blueteam-ctf-challenges/openwire/)

----
# Các câu hỏi

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/7bade7fc-513e-4766-8f7e-c315f77c850c)

Tạm dịch:
1. Tìm địa chỉ của C2 server.
2. Tìm port bị Exploit.
3. Tên Serive có lỗ hổng.
4. Tỉm địa chỉ của C2 server thứ 2.
5. Tìm tên Reverse shell.
6. Java Class được gọi trong file XML để khai thác lỗ hổng.
7. Tìm mã CVE của lỗ hổng này.
8. Java method và Class cho phép kẻ tấn công chạy mã độc.

----
# Kiến thức cần tìm

**C2 - Command and control**: là một máy chủ hoặc hệ thống có nhiệm vụ định hướng, điều khiển và theo dõi các hoạt động của phần mềm độc hại hoặc các cuộc tấn công mạng.

Dưới đây là 2 mô hình ứng dụng của C2

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/aa9f7aa4-8ad4-4d6b-adde-88d4312fdee2)

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/64ceded6-afe8-4583-9a5a-028862edd391)

**OpenWire**: là 1 đạng Cross-language wire protocol cho phép kết nối tới ActiveMQ từ nhiều ngôn ngữ và nền tảng.

**Wire protocol**: là binary và stream-oriented protocol

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/4385f857-f93d-4f82-9476-f14b48d13d5d)

**CVE**(Common Vulnerabilities and Exposures): là một danh sách các lỗ hổng bảo mật và các mở rộng của phần mềm và hệ thống máy tính.

----
# Câu 1

Để kiểm tra xem địa chỉ IP của C2 server, mình sẽ tiến hành vào phần Statistic -> Conversation

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/62eecc29-6e9f-4a40-9e2c-10d7b44b370d)

Ở đây ta thấy có 4 địa chỉ ip:
* 84.239.49.16
* 134.209.197.3
* 128.199.52.72
* 146.190.21.92

Trong đó địa chỉ **134.209.197.3** có kết nối tới cả 3 địa chỉ ip còn lại. Đựa theo phỏng đoán theo scenario (This server has been flagged for making outbound connections to multiple suspicious IPs - có thể hiểu rằng server của chúng ta đang kết nối tới nhiều địa chỉ ip lạ 1 lúc.) thì đây có thể là Server của chúng ta.

Mình cũng để ý thấy packet đầu tiên của file pcap này (như hình ở dưới) là địa chỉ **146.190.21.92** gửi packet về server.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/7096f1b1-3001-4013-96dd-646a158c525e)

Kết hợp thêm dữ kiện số lượng packet lớn từ **146.190.21.92** gửi về server.Từ đó chúng ta có thể kết luận được C2 Server là `146.190.21.92`. Thử nhập địa chỉ này vào chỗ nhập flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/7fd02a21-ac47-431c-bef4-72077113a074)

**Bổ sung dữ kiện**

Sau khi mình để ý lại 1 tí thì mình có thấy packet số 11 và số 14 là có request (GET) từ địa chỉ **134.209.197.3** tới **146.190.21.92**. File XML này sẽ truyền dữ liệu và mô tả nhiều loại dữ liệu khác nhau.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/47fdd067-17c8-4f27-9f8f-9f3c49efe511)

  
----
# Câu 2
Để tìm port đang bị Exploit, mình cần xem xem kẻ tấn công sử dụng gì để Exploit server.

Dựa theo tên đề bài và packet số 4 + 5, ta có thể thấy protocol mà kẻ tấn công sử dụng lần này là OpenWire

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/4ef581b2-0ebb-4192-bd55-7281ad9f3ee6)

Bằng cách Google cực nhanh hoặc xem ngay trong packet, ta có thể thấy ngay port nó sử dụng là `61616`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/cc1bbac3-5233-48d4-8a5c-e16838b19b80)

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/eda9576d-57e3-449b-8776-512f741e1651)

Thử nhập `61616` vào ô nhập flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/e72f1af9-7f70-4783-a52a-b809b0ab7c22)

----
# Câu 3
Vẫn bằng vài đường search cơ bản từ google, chúng ta có thể thấy tên service có lỗ hổng này

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/25119f40-7a17-49c3-a39f-d7a6d46644b4)

Mình thử nhập `Apache ActiveMQ` vào ô flag và kết quả là

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/5fcf8241-b41c-42ca-b756-2aba5a3dfb41)

----
# Câu 4
Ta còn 2 địa chỉ ip còn lại là **128.199.52.72** và **84.239.49.16** là chưa động tới. Vậy thì mình sẽ filter địa chỉ ip của server c2 đã tìm thấy đi.

`!ip.src==146.190.21.92 and !ip.dst==146.190.21.92`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/67cf36e8-43c4-4d7f-aff6-13992644d7c8)

Tại đây mình thấy packet số 34 và 38 tương tự như **Dữ kiện bổ sung** ở câu 1 của mình. Xem lại địa chỉ ip thì thấy nó là địa chỉ **128.199.52.72**. Mình thử nhập vào ô điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/79bd8b33-cf14-46ef-ac34-28c4faec50cc)

Hoặc tương tự với đó, mình sẽ follow stream của packet số 11 và thấy trong file XML có cái này

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/753c72bf-ee42-4fb6-85bf-2e14f0547089)

Ta thấy địa chỉ ip đó được curl về 1 file. Và khả năng cao file này là mã độc vì nó cần cấp quyền thực thi (chmod +x). Cũng theo phỏng đoán thì server này cũng có thể là server C2 thứ 2

----
# Câu 5
Theo dữ kiện của phầm **Dữ kiện bổ sung** trong câu 1, phần làm của câu 4, mình sẽ quay lại packet số 11 để follow stream nhằm mục đích xem file XML đã được gửi về.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/1f9ae294-d992-41cc-95ed-60d7d6929879)

Ta có thể thấy lệnh `chmod +x /tmp/docker` tức cấp quyền thực thi cho file tên `docker`. Mình thử nhập vào trong ô nhập flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/17933a11-10ec-468c-abf0-1bd62f81f922)

----
# Câu 6
Tại file XML, có 1 dòng là `<bean id="pb" class="java.lang.ProcessBuilder" init-method="start">`. Trong này có 1 thuộc tính là `java.lang.ProcessBuilder` và với các dữ kiện đã thu thập, nhiều khả năng đây là cái Java class cần tìm. Thử nhập nó nó vào Cyberdefend

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/71e70628-7a18-424b-a594-e193c9df981e)

**Bổ sung thêm dữ kiện**

Class này được sử dụng như để tạo 1 process trên hệ thống của bạn. Và chúng ta có thêm thuộc tính `init-method="start"` thì cái này sẽ tạo và chạy 1 process gì đó. 

Trong này cũng có <bean> - là cái mà [spring Ioc container](https://viblo.asia/p/spring-ioc-inversion-of-control-trong-spring-4P856gJaKY3) quản lí. IoC container sẽ tạo các đối tượng, lắp rắp chúng lại với nhau, cấu hình các đối tượng và quản lý vòng đời của chúng từ lúc tạo ra cho đến lúc bị hủy.

Và tất cả những cái này sẽ build thành 1 process chạy các dòng trong <constructor-arg></constructor-arg>

----
# Câu 7
Google 1 cách nhanh nhất thì ta có thể search như sau

`openwire cve`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/053c49aa-a1f4-49ac-ac54-4097aeaf403f)

Thử nhập `CVE-2023-46604 ` vào

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/ce4c39c9-34f1-44ed-ba69-d6d8cf691cec)

----
# Câu 8
Câu này mamng 1 chút về phần research. Tại trang [trendmicro](https://www.trendmicro.com/en_us/research/23/k/cve-2023-46604-exploited-by-kinsing.html), họ có nói và giải thích qua về lỗ hổng CVE-2023-46604

Hiểu đơn giản về mã này là khi không thể xác thực class type của Throwable thì nó có tạo và thực thi bất kì instance của bất kì class nào. Và trong phần patch diffrent, thì method `validateIsThrowable` đã được thêm vào trong class `BaseDataStreamMarshall `. 

Trong Cyberdefend, họ yêu cầu dạng flag là `class.method` nên chắc flag sẽ là `BaseDataStreamMarshall.validateIsThrowable` nhưng khi nhập thử thì không phải. Mình thử đọc lại phần ảnh trong trang blog trên thì thấy `private Throwable createThrowable`. Vì khi tạo xong mà k xác thực được thì mới xảy ra CVE-2023-46604.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/c37e193d-992c-40c3-b174-1934b44af8f8)

Theo như đầu đề của CyberDefend, mình cần tìm Java method và Class cho phép kẻ tấn công chạy mã độc nên chắc chắn flag phải là `BaseDataStreamMarshaller.createThrowable`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/accaaf03-f0b5-48a3-878a-d56cbd423722)

----
# End of Challenge check

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/0fbf1d93-ba53-4033-ae78-3c51885819b6)

**--End--**
