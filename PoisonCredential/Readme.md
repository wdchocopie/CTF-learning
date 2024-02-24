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

**LLMNR** và **NBT-NS** có thể triển khai thành Poisoning attack bằng cách lợi dụng việc client gửi sai SMB share adress, khi này DNS sẽ trả về kết quả không thấy địa chỉ đó. Sau đó hệ thông máy tính của client sẽ tự động đổi qua LLMNR / NBT-NS request và kẻ tấn công có thể lợi dụng điều đó để tạo ra server xác nhận rằng đúng địa chỉ.

**Mô phòng cuộc tấn công**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/32745f68-1906-4805-922a-44f6a1c309aa)

Gửi sai địa chỉ SMB ->  DNS trả về không tìm thấy -> Client gửi request LLMNR/NBT-NS -> Kẻ tấn công lợi dụng nó để kết nối với máy của clients (có thể crack NTLMv2 hashes hoặc tấn công SMB relay)

https://github.com/wdchocopie/CTF-learning/assets/81132394/7f2e2c86-0e45-4909-a6b7-a8702bf347d8

----
# Câu 1
Tại câu hỏi này, ta có thể suy đoán như sau:
* Cả LLMNR, NBNS và SMB đều sử dụng query-respond mechanism (tạm dịch: cơ chế truy vấn). Nên nếu có filter thì mình sẽ filter cái này
* Theo Scenario, ta có thể thấy đây là LLMNR/NBT-NS Attack nên nếu là Victim (machine) thì mình chỉ cần filter 2 giao thức là LLMNR và NBNS.

Vậy thì mình sẽ tiến hành kiểm tra thử từng protocol với địa chỉ ip 192.168.232.162

**LLMNR**
`ip.src==192.168.232.162 and llmnr`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/e3638918-e94f-4e47-83f3-1f7773ab2db2)

**NBNS**
`ip.src==192.168.232.162 and nbns`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/efb4add4-7f57-4aa5-a488-ceec3905ff98)

Tại đây ta thấy ở package 47 của filter NBNS có 1 phần ghi `Name query NB FILESHAARE<20>`, mình thử điền flag là `FILESHAARE`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/6c6bc8ab-da7f-47ae-9a33-bfc0cc932b53)

Bổ sung thêm thông tin dựa vào các package từ wireshark, ta có thể thấy giao thức **NBNS** sẽ tập trung vào name query (respond) còn **LLMNR** sẽ tập trung vào standard query (respond).

----
# Câu 2

Dựa vào những gì mình vừa tìm hiểu bên trên, ta có thể kiếm xem có địa chỉ ip nào respond lại với cái query mình vừa tìm không. Nếu như có thì khả năng cao đó là máy khả nghi

Mình sẽ tiến hành kiểm tra bằng cách filter **LLMNR**

`llmnr`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/900b3d52-0548-4470-bdbc-35be51b2788b)

Tại đây ta thấy package số 53, 54, 71, 72,..... đều từ địa chỉ **192.168.232.215** gửi về. Mình sẽ thử nhập địa chỉ ip này vào nơi điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/0964ae3d-65d7-4aa6-b22e-d4f3cc21e986)

-----

# Câu 3

Để tìm được địa chỉ máy đã nhận respond từ kẻ tấn công, ta đã có thể filter nó với địa chỉ ip **192.168.232.215** với giao thức **LLMNR** 

`llmnr and ip.src==192.168.232.215`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/dd252f49-be3c-4acf-91b8-d8cca3faae2e)

Tại đây ta thấy 2 địa chỉ sau khi filter:
* 192.168.232.162
* 192.168.232.176

Và cả 2 địa chỉ này đều tương ứng với 2 cái query bị sai:
* fileshaare
* prinetr

Vậy thì mình sẽ tiến hành kiểm tra lại xem có package nào đi từ / tới địa chỉ **192.168.232.215** thông qua protocol NBNS (để kiểm tra theo tên)

`(nbns) and (ip.src==192.168.232.215 or ip.dst==192.168.232.215)`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/3bc98de6-86b2-476a-83b1-539ebf953a88)

Tại đây ta thấy:
* Địa chỉ 192.168.232.162 chỉ có 1 package là nhận respond của 192.168.232.215 và không có phản hồi
* Địa chỉ 192.168.232.176 nhận được nhiều package, có `name query respond` và `registeration respond` từ  / tới 192.168.232.176

=> Ta có thể suy ra flag ta cần tìm là **192.168.232.176**

Thử nhập flag vào

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/da337b64-2013-4241-b527-6c0781820ba2)

----
# Câu 4
Ở đây người ta dùng từ **Account compromised** thì tức là attacker đã phát động tấn công SMB relay. Mình sẽ tiến hành lọc các package sử dụng protocol SMB và SMB2
với ip source là 192.168.232.215

`(smb or smb2) and ip.src==192.168.232.215`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/2efc9eff-1092-4461-9077-14d82c1a26d1)

Tại đây ta thấy Package số 242 có đoạn info như sau: `Session Setup Request, NTLMSSP_AUTH, User: cybercactus.local\janesmith`

Mình tiến hành kiểm tra packagae này. Trong mục SMB2 -> SMB2 header -> Security Blob -> GSS-API => simple protected negotiation -> negTokenTarg -> NTLM secure service provider ta có thể thấy phần User name là `janesmith`

Mình thử nhập vào ô flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/ca04bff3-fe6d-4081-9f06-d1596137ffdc)

**Bổ sung thêm kiến thức**: Lí dó mình biết được nó nằm trong trong NTLMSSP vì ở phần info nó đã hiện `NTLMSSP_AUTH`. NTLM là security protocol từ Microsoft để xác mình user's identity (danh tính người dùng) và bảo mật chúng. Vậy nếu muốn tìm thông tin liên quan tới victim thì ta sẽ tìm ở trong này.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/49e49745-9126-48cd-9a2b-d33086de1d12)

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/2bb68606-ef23-4efb-9799-5fd6d932d3f1)

----
# câu 5

Như kiến thức vừa đề cập ở trên và với yêu cầu đề bài, mình sẽ tiến hành filter **SMB2** và **NTLMSSP**

`smb2 and ntlmssp`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/3da0fbce-c90b-43d7-87c6-cc7d40edd1ba)

Tại đây ta thấy 3 package phù hợp với phần filter của ta là package 240, 241, 242. Ta thấy package của 241 là response. Mình sẽ thử kiểm tra Security Blob -> GSS-API -> Simple Protected Negotiation -> negTokenTarg -> Target Info. Tại đây mình thấy có NetBios computer name là `ACCOUNTINGPC`. Mình thử nhập vào phần điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/594b7de1-f707-4e6f-8a2a-70259f9bed90)

----
# End of challenge check

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/6974b614-1dea-449a-b9c6-a9e1cdfb5d5e)

**--End--**
