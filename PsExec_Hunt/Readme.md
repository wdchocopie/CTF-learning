# PsExec Hunt - Week 2
----
Tool sử dụng trong bài: 
* Wireshark

Scenario: Hệ thống phát hiện xâm nhập (IDS) của chúng tôi đã đưa ra cảnh báo, cho biết hoạt động chuyển động ngang đáng ngờ liên quan đến việc sử dụng PsExec. Để ứng phó hiệu quả với sự cố này, vai trò của bạn với tư cách SOC là phân tích lưu lượng mạng đã ghi lại được lưu trữ trong tệp PCAP.

Material trong bài:
* File zip -> 1 file PCAP
* Password giải nén: cyberdefenders.org

Link -> [Cyberdefend](https://cyberdefenders.org/blueteam-ctf-challenges/psexec-hunt/)

----
# Các câu hỏi

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/3ee413e1-c21a-469f-a3f6-b8c0b7ae8210)

**Tạm dịch:**
1. Xác định địa chỉ IP của máy mà kẻ tấn công ban đầu có được quyền truy cập
2. Tìm hostname của máy mà kẻ tấn công đã tấn công đầu tiên hay không
3. Username được kẻ tấn công sử dụng để xác thực
4. Tên service được thực thi trên target
5. Network share được PsExec sử dụng để cài đặt dịch vụ trên máy mục tiêu?
6. Network share mà PsExec dùng để giao tiếp
7. Hostname của máy mà kẻ tấn công đã cố gắng xâm nhập vào

----
# Kiến thức cần tìm hiểu

**PsExec**: là một công cụ tiện ích cho phép quản trị viên hệ thống điều khiển máy tính từ xa từ microsoft. Khác với RPD và telnet, nó không cần tải thêm chương trình nào khác. Ngoài ra thay vì dùng chuột thì nó sẽ gửi command line về máy chủ.

Thông thường PsExec hay sử dụng SMB Protocol và chạy ở port 445. Cách bảo mật thường sử dụng là username / password hoặc là NTLM

**IDS**(Intrusion Detection System): là một công cụ hỗ trợ bảo mật hệ thống và cảnh báo khi có xâm nhập. Thường được tích hợp vào các hệ thống bảo mật khác, IDS giúp bảo vệ thông tin hệ thống, giúp phát hiện và cảnh báo xâm nhập.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/71ca3d61-6511-4754-9f54-912a9f0b4b22)

----
# Câu 1
Dựa theo những thông tim vừa tìm hiểu được về PsExec thì mình sẽ tiến hành filter SMB2 và NTLM

`smb2 and ntlmssp`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/b0eb6b5c-f280-4475-83ee-907306b33a23)

Tại đây ta thấy packet số 130 là `NTLMSSP_NEGOTIATE` với ip source là `10.0.0.130`. Dựa vào kiến thức đã có từ bài [PoisonCredential](https://github.com/wdchocopie/CTF-learning/tree/main/PoisonCredential) thì ta có thể xác định luôn đây là ip cần tìm.

Thử nhập nó vào ô điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/c026ed3c-c0e4-4641-ba1c-70df5f895a2b)

**Dữ kiện bổ sung**

Tại đây ta sẽ có thêm 1 dữ kiện nữa là ip đang đóng vai trò server của mô hình NTLM là `10.0.0.133`.

----
# Câu 2
Vẫn dựa theo kiến thức về NTLM thì mình cần tìm packet có chứa các thông tin sau
* Giao thức SMB2
* NTLMSSP
* Bước challenge (do nó sẽ chứa thông tin của máy)
* Từ ip 10.0.0.133 (theo mô hình bài PoisonCredential thì cái này là từ phía server được kết nối tới)

Vậy ta có filter là

`smb2 and ntlmssp.challenge.target_info and ip.src==10.0.0.133`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/6f906888-b0ca-4476-b4bb-6b60a953b6f7)

Nhìn kĩ vào packet thì ta thấy

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/829c9726-cef9-4668-9cd1-e1d212f4dab5)

Chúng ta có tên hostname là `Sales-PC`. Mình thử nhập vào ô điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/003ea58e-e497-47f6-a331-511425768a7e)

----
# Câu 3
Vẫn dựa vào kiến thức về NTLM, ta cần tìm
* Giao thức SMB2
* NTLMSSP
* Bước authentication (tại bước này sẽ chứa username người dùng của client)
* Từ IP 10.0.0.130 (client/ attacker)
* Tới IP 10.0.0.133 (server)
* Auth username

Filter của ta là

`smb2 and ntlmssp.auth.username and ip.src==10.0.0.130 and ip.dst==10.0.0.133`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/2467ab9e-e748-476f-acc2-1d0d7b996f9b)

Ta thấy luôn username cần tìm trong mục info là `ssales`. Mình thử nhập vào chỗ điền flag.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/780f924a-d145-445d-b052-0e09a7b8d058)

----
# Câu 4
Lại tiếp tục dựa theo kiến thức về NTLM, ta có thể khái quát những gì cần filter
* Giao thức SMB2, có chứa filename
* ip source: 10.0.0.130
* ip destination: 10.0.0.133

Ta có filter

`smb2.filename and ip.src==10.0.0.130 and ip.dst==10.0.0.133 `

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/a315ff73-c377-405b-ba06-ff835b65e966)

Ta thấy 1 file **.exe** tên `psexesvc` trong phần info. Khi mình tiến hành mở kiểm tra chi tiết thì ta có tên file như sau

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/71962c96-414b-4fa2-8582-dc171d2f9b8b)

Vậy thì `psexesvc` có vẻ là tên của file này do theo yêu cầu flag là tên file chứ không bao gồm đuôi của nó. Mình thử nhập vào.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/24e44bc1-4fe2-4f4c-bf75-61bb25752695)

----
# Câu 5
**Bổ sung kiến thức**
Dưới đây là cấu trúc của SMB2 Header

`+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|     0xFE      |      'S'      |      'M'      |      'B'      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|          Header Length        |           (padding)           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                          NT_Status                            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|            Opcode             |            (padding)          |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|       :S:C:P:R|               |               |               |    Flags
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                          Chain Offset                         |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                        Command Sequence-                      |
+-+-+-+-+-+-+                                     +-+-+-+-+-+-+-+
|                             Number                            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                           Process ID                          |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                            Tree ID                            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                                                               |
+-+-+-+-+                    User ID                    +-+-+-+-+
|                                                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                                                               |
+-+-+-+-+                                               +-+-+-+-+
|                                                               |
+-+-+-+-+                   Signature                   +-+-+-+-+
|                                                               |
+-+-+-+-+                                               +-+-+-+-+
|                                                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ `

Ta sẽ tập trung vào trong phần Tree ID. TreeID thường hay dùng để nhận diện share resource. Tóm tắt sơ qua thì nó sẽ có dạng `buffercode / sharename(\\host\sharename)` 

Và với yêu cầu đề bài này thì nói lại sẽ là đi tìm sharename mà PsExec dùng để tải service lại về náy. Ta quay lại check packet 144 mà vừa check ở câu 4. Trong mục SMB2 -> SMB2 Header -> Tree Id, ta có những thông tin như sau.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/39197247-0212-4ba5-920d-7c998f811d35)

Sharename trong này là `ADMIN$` và cũng có thể là flag. Mình nhập thử vào và kết quả.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/5bf691d4-c1f4-411f-9e17-6b05c2b8e603)

**Bổ sung thêm thông tin**

Khi sharename có dạng \[tên$\] thì nó sẽ tạo hidden share (theo [hatoffsecurity](https://hatsoffsecurity.com/2018/01/11/smb-tree-connect-response-details/)) và khi bạn về \\servername\ thì cũng sẽ không thấy phần hidden share.

----
# Câu 6
Vẫn lọc như câu số 4, ta có:

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/7a1e0be5-0683-480f-a73d-cdc46f336955)

Mình sẽ tập trung vào tìm sharename của những request liên quan tới stdin/out/err (standard in / out / error). Check thử packet số 499 với vị trí như câu 5, ta thấy

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/15da7bba-6d09-4170-9113-db52125008c8)

Mình thấy được sharename `IPC$`, thử nhập vào nơi điền flag.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/0a529565-8e23-438b-b153-42aeebfe050c)

----
# Câu 7
Để tiến hành lấy được hostname, mình sẽ filter như sau

`ntlmssp.challenge.target_info`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/6102f242-709e-4012-af13-d22a6731484b)

Sau khi filter xong, mình vào kiểm tra phần conversation

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/b2a7d96b-81ca-400b-8869-8786ffbd4b93)

Tại đây mình thấy số lượng packet mà địa chỉ `10.0.0.130` và `10.0.0.131` giao tiếp với nhau nhiều hơn nên mình sẽ tiến hành fiter tiếp

`ntlmssp.challenge.target_info and ip.addr==10.0.0.131 and ip.addr==10.0.0.130`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/11ea9a07-4eea-4e21-a873-07206982cd9c)

Tiến hành kiểm tra bất kì packet nào có protocol là SMB2, mình đều thấy có dòng này

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/d2339d6d-2ffd-4cee-b819-a8be1a901bd7)

Mình dự đoán đây là flag mà mình cần tìm, mình tiến hành nhập nó vào ô điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/2cc6c888-76a6-495b-89ed-cb843fc91aa7)

**Bổ sung cách tìm flag**
Chúng ta cũng có thể tìm flag bằng cách sử dụng thêm tool bên ngoài là Network Miner (với điều kiện đổi file từ Pcapng -> pcap)

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/246c18d6-a44a-46a7-a04a-727b59b81b47)

----
# End of challenge check

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/9fb19a3a-8267-491a-832a-33f1259e4142)


--End--
