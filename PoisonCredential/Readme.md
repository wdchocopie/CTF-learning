# Poison Credential - Week 1
Tool sử dụng trong bài: Wireshark

Scenario: Nhóm bảo mật của tổ chức bạn đã phát hiện thấy hoạt động mạng đáng ngờ gia tăng. Có những lo ngại rằng các cuộc tấn công LLMNR (Link-Local Multicast Name Resolution) và NBT-NS (NetBios Name Service) có thể đã xảy ra. Những cuộc tấn công này được biết đến với việc khai thác các giao thức này để chặn lưu lượng mạng và có khả năng xâm phạm thông tin xác thực của người dùng. Nhiệm vụ của bạn là điều tra nhật ký mạng và kiểm tra lưu lượng truy cập mạng đã ghi lại.

Thông tin dược cấp trong bài: 1 file **zip** có pass giải nén là `cyberdefenders.org`, bên trong có 1 file **pcap**

Link -> [CyberDefemd](https://cyberdefenders.org/blueteam-ctf-challenges/poisonedcredentials/)

----
# Các câu hỏi

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/081708c9-ae37-44e3-ad9d-c2c6730f06a7)

Tạm dịch các câu hỏi:
1. Xác định truy vấn bị nhập sai của địa chỉ 192.168.232.162
2. Tìm Ip máy có vẻ khả nghi
3. Tìm Ip máy đã nhận mã độc của kẻ tấn công
4. Username đã bị đăng nhập từ người dùng không được ủy quyền (unauthorized user)
5. Hostname của máy bị kẻ tấn công thông qua SMB

----
# Lí thuyết cần tìm hiểu trước khi vào bài
**NetBios**(Network Basic Input/Output System): Là 1 giao thức cho phép các phần mềm nằm trên các máy khác nhau trong cùng mạng LAN giao tiếp với nhau.
**NBNS**(NetBios Name Service): là 1 giao thức sử dụng cho NetBios trên giao thức TCP/IP cho phép bạn chuyển đổi tên trên NetBios thành địa chỉ IP
**LLMNR**(Link-Local Multicast Name Resolution): là 1 giao thức để xử lí tên trên NetBios trên mạng LAN
**SMB**(Server Message Block): Là giao thức chia sẻ file của Windows.

**LLMNR** và **NBT-NS** được sử dụng khi DNS request fail trên hệ thông của Windows. Khi đó 2 giao thức này sẽ đóng vai trò như name resolution dự phòng (fallback name resolution)

**LLMNR** và **NBT-NS** có thể triển khai thành Poisoning attack bằng cách lợi dụng việc client gửi sai SMB share adress, khi này DNS sẽ trả về kết quả không thấy địa chỉ đó. Sau đó hệ thông máy tính của client sẽ tự động đổi qua LLMNR / NBT-NS request và kẻ tấn công có thể lợi dụng điều đó để tạo ra server xác nhận rằng đúng địa chỉ, từ đó có thể lấy credential của người dùng.

**Mô phòng cuộc tấn công**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/32745f68-1906-4805-922a-44f6a1c309aa)

Gửi sai địa chỉ SMB ->  DNS trả về không tìm thấy -> Client gửi request LLMNR/NBT-NS -> Kẻ tấn công lợi dụng nó để kết nối với máy của clients 

----
# Câu 1
Tại câu hỏi này, ta có thể suy đoán như sau:
* Vì scenario đã cung cấp cho chúng ta 2 giao thức là LLMNR và NBT-NS nên khả năng cao sẽ tập trung ở đây
* Cả LLMNR, NBNS và SMB đều sử dụng query-respond mechanism (tạm dịch: cơ chế truy vấn). Nên mình sẽ filter 3 cái này

Vậy thì mình sẽ tiến hành kiểm tra thử từng protocol với địa chỉ ip 192.168.232.162
