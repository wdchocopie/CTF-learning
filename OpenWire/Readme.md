# OpenWire - Week 1
Tool sử dụng trong bài:
* Google
* Wireshark

Scenario: Trong quá trình làm việc với tư cách là nhà phân tích SOC-Tier2, bạn sẽ nhận được báo cáo từ Tier 1 về máy chủ công khai. Máy chủ này đã bị gắn cờ vì thực hiện kết nối ra ngoài tới nhiều IP đáng ngờ. Để phản hồi, bạn bắt đầu giao thức ứng phó sự cố tiêu chuẩn, bao gồm cách ly máy chủ khỏi mạng để ngăn chặn khả năng di chuyển sang bên hoặc đánh cắp dữ liệu và thu thập gói tin từ tiện ích NSM để phân tích. Nhiệm vụ của bạn là phân tích pcap và đánh giá các dấu hiệu của hoạt động độc hại.

Thông tin dược cấp trong bài: 1 file zip có pass giải nén là cyberdefenders.org, bên trong có 1 file pcap

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

Trong đó địa chỉ 134.209.197.3 có kết nối tới cả 3 địa chỉ ip còn lại
