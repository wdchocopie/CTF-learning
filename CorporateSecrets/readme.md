# CorporateSecrets
----
**Scenario:** Phân tích file và trả lời câu hỏi. Dưới đây là thông tin của file

**Dữ liệu được cung cấp:** File .zip và password. Bên trong là 1 file .ad1

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/c1b8d39a-f211-4a37-95b0-0a8bfd3a5e08)

**Tool sử dụng:**
* Kit của ZimmermanTools
* FTK imager
* Vmware:
* * Kali Linux
  * Windows 10 x64


----
# Câu hỏi

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/b27a82be-37e8-4ce9-a494-3e4500d183c3)

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/754c2be4-5b4d-4dbd-ba1f-d87492dc3805)

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/b3c11262-89e8-4af1-abaa-c85ffa9af7c3)

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/8b63c8c6-5d0f-42be-8710-b050c37764bc)

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/0606cb59-9127-44ea-8a43-85d9bea034d0)

----
# Câu 1
Trước khi vào bài thì mình sẽ tiến hành mở file được cấp trong bài bằng **FTK Imager** và tiến hành extract ra cho dễ làm việc

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/e1e45b67-b15b-4166-8923-c3e617409b64)

Trước tiên, để làm được bài này, ta cần hiểu **Registry** trên Windows là gì

Registry là một cơ sở dữ liệu dùng để lưu trữ thông số kỹ thuật của Windows. Nó ghi nhận tất cả các thông tin và cài đặt cho những phần mềm bạn cài trên máy, các thiết bị phần cứng, hồ sơ người dùng, cấu hình hệ điều hành và nhiều thông tin khác nữa.

Vậy để tìm thông tin của bản build thì chúng ta lên google search

`build number registry location`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/d567f236-a1df-48eb-b91c-e4d17700365c)

Ta có vị trí là `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion`. Bây giờ tìm kiếm tiếp theo là vị trí của file Registry để mình có thể tiến hành mở nó

`window registry location`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/791c180f-5684-4f45-878b-fc9fe6bc1307)

Vậy ta sẽ sử dụng **Registry Explorer** \(gọi tắt là RE\) để mở và tìm value của nó từ thư mục `C:\Windows\System32\config\SOFTWARE `

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/3f0f1ab8-591e-4c6a-8ebb-62032f44c307)

Sau đó tìm kiếm keyword là `CurrentVersion`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/4f307dcd-2185-47e0-8f13-32e3b692de70)

Và tìm vào thông tin bản build

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/7746a8fe-8818-4116-a144-24709ee28efe)

Thử nhập `16299` vào ô điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/75dab5e3-6a58-48df-b8c3-1469e10fbd3f)

----
# Câu 2

Tiếp tục google nhanh 

`check user registry`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/deb9980d-efbc-4cf2-985f-5528f4b53b63)

Ta có đường dẫn `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList`. Mình sẽ thử tìm kiếm nó trên **RE**

`ProfileList`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/e553664b-151c-4a29-9936-872c21baae57)

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/31ee99e7-42bb-41a6-94b5-0c54d033c621)

Tại dây ta thấy số user = `6`. Thử nhập vào ô điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/3a4e5035-262a-481c-a61e-331cb7338ac8)

----
# Câu 3

Trước tiên chúng ta phải hiểu **CRC64** là gì. Dựa theo gemini:

**CRC64** là một thuật toán kiểm tra tính toàn vẹn dữ liệu được sử dụng để xác định xem dữ liệu có bị thay đổi hay bị lỗi hay không. Nó hoạt động bằng cách tính toán một giá trị 64 bit dựa trên dữ liệu đầu vào. Nếu dữ liệu bị thay đổi, giá trị CRC64 cũng sẽ thay đổi.

Có 3 loại CRC64:
* ISO
* ECMA (Chính)
* XZ

Trước tiên mình sẽ tìm xem file `fruit_apricot.jpg` trong các thư mục của user.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/fd68e0c2-0b7e-4a83-a14b-d05658727ba7)

Tiến hành upload file này lên [Toolkitbay](https://www.toolkitbay.com/tkb/tool/CRC-64)

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/381faadf-79a8-4044-9b74-172c61750111)

Thử nhập `ED865AA6DFD756BF`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/32d97e39-909c-4182-99f4-c19d11a1fdc1)

----
# Câu 4

Chúng ta với câu này cần hiểu **Logical size** là gì. Về cơ bản đây là size mà dữ liệu chiếm. Thông thường logical size < physical size (là size chiếm dụng trên ổ đĩa)

Bây giờ mình sẽ tìm file `strawberry.jpg"`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/5e7e0cbf-84e3-4327-be97-ecb09b5c4674)

Mở mục properties ra

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/41c5eb09-8340-40cc-b911-73c25aa9ffe0)

Ta thử nhập size dựa trên số byte `72448` xem

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/3d10f501-e8ec-441e-a2cf-00e29558e04e)

----
# Câu 5

Lại Google nhanh

`registry check architecture windows`

Và tại trang [này](https://qtechbabble.wordpress.com/2016/08/15/determine-x86-or-x64-architecture-from-windows-registry/), Ta có

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/51d566ee-25bf-4e35-a6f8-ae0ad1186cf8)

Quay lại **RE**, mình tiến hành mở file registry SYSTEM

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/ea25bc28-1300-4903-9245-9a3adee590f5)

Tìm kiếm

`Environment`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/c1e34b68-6a13-4fa9-a2a2-a8a82a304836)

Tại đây ta có phần **PROCESSOR_ARCHITECTURE** là `AMD64`. Thử nhập vào ô điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/8b39e761-0a76-48d6-95d2-9708eb83f4b1)

----
# Câu 6

Để tìm các mục ở Recycle bin thì chúng ta cần lục trong directory `$Recycle.Bin`. Do chúng ta đang mở file bằng Windows nên sẽ không thể mở thư mục này. Mình sẽ mở nó bằng **FTK Imager**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/ddb86ddb-e4d7-4155-a15f-b5d906950cc9)

Tiến hành lục từng folder 1 thì mình tìm được ảnh trong 1 folder có mã `***-1005`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/c9e8cd76-b4aa-4a44-8060-63c1d508f045)

Những mã này còn được gọi là SID. Mình sẽ đối chiếu vối thông tin có được từ Registry của Profilelist

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/668d2c86-fb90-4543-b53c-d3899c4b89b0)

Ta có user là `hansel.apricot`. Thử nhập vào ô flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/809d9a73-4014-47d9-b249-35fd05b317d4)

----
# Câu 7

Lại tìm file có tên `vegetable` trong thư mục user

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/602d8570-f002-4018-80d8-42edd5ccf728)

Tại đây nó không hiện đuôi cuối của file. Mình sẽ tiến hành check nó bằng lệnh `file` của linux

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/c11d8096-1eb6-4122-81ae-739f35272e84)

Lên google nhanh đuôi cuối của file 7zip

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/9834d64e-5e69-412c-b70d-57e931e31141)

Nhập `7z` vào

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/8478b21b-8cec-4545-8210-7c11ee802e38)

----
# Câu 8

Do đầu bài hơi khó hiểu nên mình thử xem thử hint mà đề bài cho 

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/8493c350-421f-4070-8681-c7911695d0fd)

Dựa vào đây chúng ta sẽ lục tung các thứ có trong browser của user đó. Mình thử vào xem thư mục `Appdata` thì thấy

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/2da43443-2e75-47c4-be8c-8304963cf710)

Tại đây là thư mục chứa thông tin của trình duyệt Firefox. Tại đây mình search google cách đọc lịch sử của firefox từ file

`firefox read history file`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/bf1760f7-40bf-4b2a-a07f-f8e7baee70bc)

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/cc13a5cc-52e1-4a31-b1a7-e398445522da)

Mình sẽ sử dụng [sqlite online](https://sqliteviewer.app/) và gửi file `place.sqlite` lên. Trong mục `moz_places` có thông tin cho chúng ta

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/2fc2a772-aa29-499b-a0c5-b75c751bd4be)

Thử nhập `VSCO`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/f4ca99df-67c3-4bf2-841e-15e2e9ff2290)

----
# Câu 9

Lại google nhanh

`device name registry`

Và tại trang [này](https://superuser.com/questions/1539088/find-hostname-of-an-windows-image)

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/10840334-6d9b-4e28-b7b6-aa3c755a5ce3)

Vào tìm trong Registry SYSTEM

`ComputerName`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/a650335e-a55b-4ef4-803f-df83fd06b44b)

Thử nhập `DESKTOP-3A4NLVQ`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/48114f08-d434-4a1c-82fa-ac20e91bbe64)

----
# Câu 10

Với câu này ta cần hiểu SID là gì. SID là viết tắt của Security Identifier \(Số nhận dạng bảo mật\), là một mã định danh duy nhất được sử dụng trong hệ thống Windows để xác định các đối tượng bảo mật, bao gồm người dùng, nhóm, máy tính và các dịch vụ. SID được sử dụng để kiểm soát truy cập tài nguyên và đảm bảo an ninh cho hệ thống.

Dựa theo tài liệu từ [Microsoft](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-identifiers), ta có cấu trúc của nó như hình bên dưới

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/9afc2e7b-268c-41d8-976c-db61643b06f3)

Dựa theo các thông tin vừa tìm được, quay lại với những gì ta tìm được ở phần `Profilelist`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/ed046ab9-acfb-42c8-b6d6-810d75984317)

Tại đây ta thấy trừ đoạn -\*\*\*\* \(* =  1 số\) thì trước đó chính là mã SID của máy tính theo cấu trúc ta vừa tìm hiểu bên trên. Thử nhập `S-1-5-21-2446097003-76624807-2828106174` 

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/3360079d-413d-4bd4-b16b-9aeaf372bd08)

----
# Câu 11

Trước khi tính những browser khác thì trước hết tại windows sẽ chắc chắn có `Internet Explorer` và với windows 10 sẽ có thêm `Edge`

Và dựa theo thông tin đã biết thì trên hệ thống này có thêm `firefox`

Tiếp theo mình thử ra ngoài và search với từ khóa `exe` để tìm xem có cái gì giống với browser không

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/6f5f556b-57ff-4127-894c-007a210c1fde)

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/b7f98534-8aab-4026-bcc4-9f5f496015c7)

Dựa theo 2 hình ảnh trên ta thây được thêm `tor` và `chrome`. Tổng là `5`. Nhập vào ô điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/3c9cf4f6-14c7-4355-9ca2-ad6b058dd61a)

----
# Câu 12

Với câu này, trước tiên mình sẽ vào thử folder của user `tim.apple`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/3f7ec2d5-a2ef-4c81-b9fc-5623e2d3fbfb)

Tại đây mình mò thử từng file. Mình vào thử file `Document` trước

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/c1229760-8807-4797-adfe-f3d7fd6e12bd)

Tại đây mình thấy có 1 file là `secret.odt`. Mình thử mở file ra

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/e9c7b6be-5ffc-425a-aa36-7e251ef40a17)

Thường mình vẫn thói quen là dùng `CTRL + A` để xem xem có chữ cùng màu với nền hay không

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/1db5ea05-4d33-42b8-8087-ecd92fb87526)

Vậy là có. Mình thử nhập `4` vào ô điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/4e212ba1-6ccc-4740-add9-940187177077)

----
# Câu 13

Vừa tìm được ở câu 12. Nhập `Jim Tomato`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/6afc8ff7-20e2-45ad-9dee-920709bc79a3)

----
# Câu 14

Lại google nhanh

`last logged in registry check`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/15dc070f-750d-48f7-9cc5-d69fd4adccf8)

Tìm kiếm trên file Registry SYSTEM trên **RE**

`Winlogon`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/88742e32-9db0-4800-95f2-bdb54929a26a)

Nhập `jim.tomato`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/766f77a7-9694-4191-8474-31d5c9b3ea66)

----
# Câu 15

Nhìn dạng câu này lại giống với mấy câu trước. Mình sẽ lục thử như các câu trước là ở trong lịch sử browser của Tim

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/f75e1c8c-b967-493b-962b-2291c9f70f53)

Tại đây mình tìm được browser firefox. Lại tương tự như câu trước mình sẽ mở lịch sử truy cập

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/996f6e7e-3ce3-42bd-82da-f77ef5d6130d)

Thử nhập `secretary` 

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/90664795-8f03-44b6-b417-456cf69b3414)

----
# Câu 16

Dựa vào các câu vừa làm, ta có SID của user này là `1004`. Thử nhập

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/38bcbf90-e35c-4eac-804f-a24c867c90e7)

----
# Câu 17

Câu này quay lại thư mục gốc, Tìm kiếm 

`tor`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/fa37d9eb-a25b-4e28-a434-3d8a5dad1161)

Vậy đường dẫn của ta là `C:\Program1`. Thử nhập vào ô điền flag 

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/2f8680d5-a5c2-4203-9252-9ac89336dea0)

----
# Câu 18

Câu này chắc chắn là dựa vào lịch sử của trình duyệt. Mình thử vào folder `/jim.tomato/appdata` xem ta có trình duyệt gì

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/1e8b9708-20cb-41ba-939b-b9c7be008655)

Ta có trình duyệt của google thì đây là của chrome. Lên google nhanh

`chrome history view file`

Trong [foxton forensics](https://www.foxtonforensics.com/browser-history-examiner/chrome-history-location), ta có các thông tin sau

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/ca27d6c3-a3e1-4d45-81f3-f2ae3d7f88c9)

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/6debbf60-527b-41ed-8f36-50d1a9bf632a)

Bây giờ tìm trong file data của chrome và mở nó bằng **sqlite online**. Filter trong mục URLs

`youtube`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/95c46739-7feb-4a55-8b2a-59ae2cad04a4)

Thử nhập `https://www.youtube.com/watch?v=Y-CsIqTFEyY`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/13edf72a-58e2-4074-9a69-c2d2f615ccdc)

----
# Câu 19

Quay về thư mục gốc, Mình thử tìm kiếm

`LibreCAD`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/75d6efd2-e659-4128-a112-7069c37d9b3d)

Thử mở file location của file `.exe`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/ff95303b-5b9e-4edb-96e0-a47aaf76e0ee)

Thử nhập `miriam.grapes` 

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/1df77bc0-0966-4e27-9be5-a074eaf698c1)

----
# Câu 20

Google nhanh `registry log in count` và ở trang [này](https://boncaldoforensics.wordpress.com/2018/08/01/4n6-quick-01-windows-users-list-login-count/) thì người ta có đề cập tới mục sau

> Sometimes you might need to find what user accounts exist on a system, and other times it could just help narrow down your work. Regardless, it is always beneficial to know as much case background information as possible. All Windows user account names, SIDs (Security Identifiers), login counts, creation dates, last password change dates, groups, and much more can be found in the Windows Registry SAM (Security Account Manager) file.

Mình ném thử file `SAM` vào **RE**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/0e9ada38-62dc-4b53-acf8-a49259259629)

Theo hướng dẫn từ trên thì kiểm tra phần bookmark > user

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/e93b942b-d9db-4668-b0e8-91d862ceb3ae)

Tại đây ta thấy phần total login count là `10`. Thử nhập vào 

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/1fcac611-91cf-436b-9fcf-b063986af540)

----
# Câu 21

Lại google nhanh

`find dhcp registry`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/92732e61-f0f5-4583-a374-93f052d95b15)

Thử tìm kiếm trong **RE** với file registry của SYSTEM

`Interfaces`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/99a44cbd-5672-4d8c-b356-da0474e12dfe)

Thử nhập `fruitinc.xyz`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/c1370db3-7e65-4e0d-97d1-6e41d8fbe2bc)

----
# Câu 22

Trước tiên mình thử tìm trong `/user/tim.apple/Pictures/Saved Picture` vì đó thường là nơi lưu trữ ảnh

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/26db7dae-ea3a-4d6c-ae3b-393cf33c4d98)

Kiểm tra nó bằng **exiftool** hoặc vào file properties ta sẽ có

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/b20be757-47d2-47a1-afc3-86b2951ae796)

Đổi nó ra giờ UTC ta sẽ có flag `04/05/2020 03:49`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/e6ea8a8c-9dc0-429b-bb24-7b2dcd7741f4)

----
# Câu 23

Lại google nhanh

`check how many time app open windows registry`

Và tại [Stack Overflow](https://stackoverflow.com/questions/10527756/count-the-number-of-times-the-program-has-been-launched), ta có

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/1812102f-7a50-459b-b027-c627e3d2ed30)

Do cái này nằm ở `HKEY_CURRENT_USER`, Ta lại google tiếp

`user registry key file`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/38c71dc4-bd27-4b57-bdc3-e5005bf597ef)

Vào **RE**, Import Registry từ user `jim.tomato` và tìm kiếm `UserAssist`. 

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/a8bfcf00-abfb-46d7-b24d-57cb64899c4e)

Dựa vào thông tin từ câu trước, ta thấy có 1 trình duyệt có icon của tor nhưng đặt tên là `firefox.exe`. Mình thử tìm kiếm nó

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/c96c6e15-e09f-4436-be90-9a7dc4680d97)

Do ta đã biết tor nằm ở thư mục `Program1` nên số lần run counter là `2`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/5ed83615-363e-4516-8673-92719cabfbb6)

----
# Câu 24

Trước tiên là mình tìm file nào giống với file được mô tả trong user `miriam.grapes`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/f7467915-e050-4a0f-a9d4-5b68bbc52e8f)

Tại đây ta có file `samplePhone.jpg` nhưng vì yêu cầu của bài nó nói rằng đây là file PNG nên mình nghĩ có lẽ file đã được ẩn đi. Mình thử dùng **binwalk** bên kali linux

`binwalk  --dd=".*" samplePhone.jpg`

Sau khi extract thành công, mình thử list các file trong thư mục vừa extract ra được

`ls`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/db113be2-4b09-496e-b72d-0de938247e9f)

Mình thử dùng lệnh sau để kiểm tra định dạng của file

`file *`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/965d439d-ce7a-49f3-91df-1c85b1294fe5)

Dùng nốt lệnh tạo mã SHA1 hash cho ảnh

`sha1sum 174A`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/992f91be-303a-4e50-9869-39624a78e0d4)

Nhập `537fe19a560ba3578d2f9095dc2f591489ff2cde` vào ô điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/12be7d03-5851-4c31-aa11-044d55d06c61)

----
# Câu 25

Google nhanh

`last open docx registry windows`

Và tại trang [StackkExchange](https://security.stackexchange.com/questions/89150/possible-to-find-out-the-last-person-to-open-a-file-on-windows-without-specialis), ta có thông tin sau

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/2d00fde9-5ea0-4767-8faa-f55dc38dee61)

Bây giờ thì mở từng file registry của từng user trong **RE**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/13d52747-cf5e-4afd-be27-c742f00a30af)

Tại đây ta sẽ chỉ thấy 4 user có file `.DAT`. Mình sẽ tìm tiếp với từ khóa

`recentdocs`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/c71e4f07-611d-48db-82aa-d5c4b82f8524)

Kiểm tra từng file

`jim.tomato`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/8af33e7a-6044-4e3d-b53f-bbb76ed123de)

`miriam.grapes`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/b076bc09-abb5-43d1-ab72-b92d933b7879)

`tim.apple`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/c8294ff6-5f22-48fa-bd58-d3869f56a966)

`admin`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/1481f23a-1e0e-427f-b386-7c8e06cec5ba)

Vậy là chỉ có của `jim.tomato` là có file `.docx` mở lên. Mình đổi thời gian về thời gian UTC thì ta có flag `2020-04-11 23:23:36`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/ba8c5c66-f900-4700-8631-25677fb269dd)

----
# Câu 26

Với câu này chỉ là trích xuất xem có bao nhiêu bản ghi từ file hệ thống. Mình sẽ sử dụng [mftdump](https://github.com/mcs6502/mftdump) để xem

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/7d5a5441-fea0-449f-8779-f8740b813ca5)

Tại đây ta thấy số cuối cùng là `219903` nhưng do cái này nó đếm bắt đầu từ số `0` nên tổng số ta sẽ có là `219904`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/55bf542d-922d-4029-bba4-7e88be398e9b)

----
# Câu 27

Tiếp tục tìm trong folder của `tim.apple`, ta thấy 

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/6d3e972c-efb3-4cba-90ec-984c15ce6d41)

Lại tiến hành kiểm tra lịch sử của Firefox

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/69037224-7ce2-4a84-ae07-31eb0c58fe48)

Có vẻ không có gì liên quan nên mình thử kiểm tra xem còn trình duyệt nào khác không

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/1ac115d9-8a15-4bf5-8c81-3856c2ca8f2b)

Thử mở của Google lên và kiểm tra lịch sử

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/cec1f613-2b38-4aae-b777-af0227ada9dd)

Ta thấy từ khóa `stinky` phù hợp với yêu cầu đề bài

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/ff78d27e-39d3-4489-9b3b-bc50549d68b4)

----
# Câu 28

Lại google tiếp

`startup items registry`

Và tại trang [này](https://lazyadmin.nl/it/windows-10-startup-folder-location/), Ta thấy

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/5dadbbe9-8e95-4d62-be8a-5b60a4ae8ff5)

Giờ chỉ cần mở file Registry của admin trong **RE** rồi tìm theo đường dẫn `Microsoft\Windows\CurrentVersion\Run`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/e819557e-b044-4b7e-8e8e-42bb8beee96c)

Ta xác minh dược nó là `OneDrive`. Thử nhập vào ô điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/132d24b7-6484-41d9-91fb-8edfa4c1a1b5)

----
# Câu 29

Với câu này, ta cần hiểu thế nào là **prefetch**.

> A Prefetch file will contain information about which files are loaded as a part of the running application, a count of the number of times executable files run, and a timestamp indicating the last time any of these programs run.

Dựa vào các ý ở đây, Chúng ta sẽ tìm các file prefetch trong hệ thống windows. Lại tiếp tục google

`prefetch file in windows location`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/9735d8e3-3ded-4652-9e09-6a42dc76d8c5)

Vào thử thư mục đó và mình thử tìm kiếm từ khóa `firefox`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/a2c09c74-9f0b-4a51-b283-e15df7ef5f08)

Tại đây mình sẽ dùng PEcmd để xem từng file 1

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/43e3c190-88c6-44f4-ac59-33cc17f091c7)

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/4fe52898-9809-43eb-8ba7-4ba0757ad3b9)

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/525285ba-9d7f-4840-af3f-b964d09d7879)

Vậy flag của chúng ta là `FIREFOX.EXE-A606B53C.pf/21`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/553326bc-e6d4-4c86-b921-5909a560bf85)

----
# Câu 30

Lại google nhanh

`registry check last ip connected`

Trong [Super User](https://superuser.com/questions/1338775/where-is-ip-address-of-my-ethernet-settings-stored-in-registry)

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/7a8c8f07-0942-4203-a367-2b2303a86df1)

Mở file Registry SYSTEM và kiểm tra theo đường dẫn `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/e30074e1-600e-4128-ae21-8f1a9c4c3ff6)

Tại đây ta thấy giá trị trong ô **DHCPIP Address** là `192.168.2.242`. Nhập thử

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/0de039f6-0b5d-40e2-ac47-98ce7393373c)

----
# Câu 31

Lại google nhanh

`taskbar window location icons`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/bf955191-48f2-46c6-93ea-3ef24a18556c)

Chúng ta đi check từng user theo đúng đường dẫn `%AppData%\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar`

`admin` - 4 icons

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/9e750398-84d9-477b-b28f-2759cde65f69)

`hansel.apricot` - 2 icons

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/066adfcf-a3df-480d-bfc0-f477593cb288)

`jim.tomato` - 2 icons

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/3eeaf5a2-8804-4561-abc8-30a1646c0438)

`miriam.grapes` - 2 icons

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/b1ce5e09-7f5f-4c50-a762-a233f89e9652)

`suzy.strawberry` - 2 icons

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/d88150fd-e79f-49ae-8de6-19e5cf2de858)

`tim.apple` - không có folder đó

Vậy flag cần tìm là `admin`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/967bb681-64f2-4f34-8f6a-6035b9039e41)

----
# Câu 32

Mình sử dụng MFTEcmd để tạo 1 file `.csv` về các thông tin có trong đó

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/04502345-fe9f-477f-b686-c0891bd7edc7)

Tiếp theo mình mở thử file vừa tạo và tìm kiếm tới đúng mã `164885`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/b233bf27-9c8a-4d10-87ea-d8e8031b20af)

Quay lại và tìm `7zg` trong file prefetch

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/9dc8e309-14aa-4b19-8259-53769a46bab6)

Và chạy Pecmd với file này

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/e7fab387-1285-44d1-98c7-df0b4707f2d2)

Thử nhập `04/12/2020 02:32:09`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/f6f362df-70e8-42d4-9d9b-41d3fdf6c776)

----
# Câu 33

Chúng ta có thể hiểu LSN (Logfile Sequence number) là một số được sử dụng để xác định vị trí của một bản ghi cụ thể trong tệp nhật ký. Và với các thông tin từ các bài trước liên quan tới MFT thì ta có thể xác định được LSN cũng nằm ở trong file này

Tiếp tục ở trong file output vừa có được, mình tìm kiếm `fruit_Assortment.jpg`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/c7a8861f-3feb-4a86-824c-bf9276eb5929)

Theo đòng này chúng ta sẽ tìm được LSN của file

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/aadf0d94-5911-489f-863d-f50affe5cc19)

Thử nhập `1276820064`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/65cadef5-25d8-449d-bb2d-5e60a1c9fc8a)

----
# Câu 34

Trước tiên mình tiến hành tìm file `.docx` được đề cập trong bài

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/c58c7a52-599b-412d-a877-635831d119c4)

Mình thử mở nó lên

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/28fb428f-78e4-4fbc-bd32-42f48b869dc0)

Có lẽ file `.docx` này đã bị ẩn đi ở trong file ta đang nhìn thấy. Mình thử đổi nó thành file zip và xuất nó ra

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/35338ce3-a4d7-451c-962a-e8e300499c1d)

Tại đây có 1 file lạ là file `file.xml`. Mình tiến hành mở nó lên

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/9876473e-900a-4aa9-8d23-c7bd4e0f299d)

Có vẻ như cái này không dúng dạng file lắm. Mình thử kiểm tra bằng lệnh `file`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/837c4e5b-6a57-4da6-baee-5870e5b7ac52)

Đổi lại tên cho đúng định dạng `.docx` và mở nó ra

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/b3d80815-2958-434b-adc3-57674c6b857d)

Vậy Flag là `Customer data is not stored securely`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/e4343b41-ca1b-46dc-a3af-5f8b20e7213c)

----
# Câu 35

Thực sự với câu này hoàn toàn không hiểu đề bài. Dựa theo đoán mò và từ hint thì ta có đáp án này

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/bab4454f-c9bf-4766-abe3-b9630c6721a8)

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/01343371-7b3c-4def-adde-3c8d68ed0e1e)

----
# End Of Challenge Check

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/e5ca5761-1a30-43a4-9a60-72bd6d9d9351)

**--End--**
