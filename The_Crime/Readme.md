# The Crime - Week 2
----
**Scenario**: Chúng tôi hiện đang tiến hành một cuộc điều tra giết người và chúng tôi đã lấy được điện thoại của nạn nhân làm bằng chứng quan trọng. Sau khi tiến hành phỏng vấn các nhân chứng và những người thân cận với nạn nhân, mục tiêu của bạn là phân tích tỉ mỉ thông tin chúng tôi thu thập được và siêng năng truy tìm bằng chứng để xâu chuỗi các sự kiện dẫn đến vụ việc lại với nhau.

**Dữ kiện được cung cấp bởi bài**:
* 1 File nén có password là cyberdefenders.org
* 1 tài liệu liên quan tới [Android forensics](https://github.com/RealityNet/Android-Forensics-References)

**Tool sử dụng trong bài**
* [ALEAPP](https://github.com/abrignoni/ALEAPP/releases/tag/v3.1.9)

Link bài -> [CyberDefend](https://cyberdefenders.org/blueteam-ctf-challenges/the-crime/)

----
# Câu hỏi

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/0471dedc-7e8f-4541-acc7-62d452d62a0a)

**Tạm Dịch**
1. App Trading mà người dùng sử dụng
2. Số tiền mà đối tượng đã nợ
3. Người mà đối tượng đã nợ tiền
4. 20/9/2023, đối tượng đã ở đâu
5. Điều tra xem người này đã đặt vé máy bay tới đâu
6. Địa điểm hẹn gặp bạn của đối tượng

----
# Câu 1
Trước khi tiến hành thì mình sẽ sử dụng ALEAPP để xuất ra các log event từ điện thoại của nạn nhân. Sau đây là kết quả

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/65650ac1-518b-469f-ac44-8034e32b66c8)

Tại đây thì ta có các mục sau:
* Report Home -> Nơi chứa 1 vài thông tin sơ bộ của report
* ADB host
* Call Log
* Chromeium
  * Keyword Search Terms
  * Network Action Predictor
  * Search Terms
  * Web History
  * Web Visit
* Contacts
* Device info
  * Partner Settings
  * Sim_Info_0
  * Setting_Secure_0
* Discord Chat
* Emulated Storage Metadata - Files
* FCM-Dump-com.discord
* Google Search History Maps
* Image Manager Cache
* Installed App
  * App Icons
  * Google Play Links For Apps
  * Installed App (GMS)
  * Package
* Permission
  * Appops.xml
  * Package And Shared User
  * Permission Trees
  * Permissions
  * Runtime Permission_0
* Last Boot Time
* Recent Activity_0
* SMS Messenger
* Usage Stat
  * Os Version
  * UsageStat_0
* Wifi Profiles
  * Wifi Hotspot
  * Wifi Profile
  * Wifi Configuration Store Combined - 0
* Factory Reset

Để tìm xem app trading nào người dùng sử dụng, mình vào phần **App Icons**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/52d814aa-ad01-4107-b279-62cce51190c8)

Tại đây trừ `Olymp Trade` còn lại đều là ứng dụng của Google. Mình thử nhập vào ô điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/342bf1a0-b00e-44c4-9010-3bef557e3824)

----
# Câu 2
Tại dây nó sẽ liên quan tới cuộc gọi / tin nhắn với số điện thoại. Mình thử vào phần **Call Log**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/cebbba4d-3a15-4db8-be76-fd25d2ba65a6)

Tại đây mình có thể xác định được số điện thoại mà mục tiêu đang nợ là `+201172137258`. Mình tiếp tục kiểm tra phần **SMS Messenger**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/4572583f-e230-46f1-af2f-6a169e0e35c0)

Tại đây có đúng 1 tin nhắn của chính số `+201172137258` đồng thời có 1 số tiền là `250000` EGP. Mình thử nhập số này vào ô điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/70a565dc-5759-4736-af1f-0458f67269ae)

----
# Câu 3
Do ta đã tra cứu được ra số diện thoại nên mình sẽ quay lại phần **Contacts** để xem điện thoại của mục tiêu lưu tên người này là ai

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/34aaa449-5a1e-4885-85f7-84d349464c1c)

Ta thấy tên của 1 người là `Shady Wahab`. Mình thử nhập vào ô điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/bd393c87-3c24-4dae-bfc0-71840f2897a7)

----
# Câu 4
Đầu tiên mình thử tìm kiếm những thông tin của GPS mà trong này có. Tại mục **App Icons**, chỉ có duy nhất 1 ứng dụng là Google Map cho phép truy cập vào GPS của máy

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/4582834f-881e-4901-924c-ee5e7e1eb863)

Tiếp đó mình xuống phần **Recent Activity_0** và mình có thấy 1 entry của Google map

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/bcae06d0-5b2c-49db-9981-49fe45c68bcc)

Vậy là ta xác nhận cái activity này được record vào đúng ngày chúng ta cần tìm. Mình sẽ tiến hành xem phần **snapshot_image** của nó

![6](https://github.com/wdchocopie/CTF-learning/assets/81132394/413db77b-8ddb-4d74-9413-4968f15d2190)

Tại đây ta có thể tìm được vị trí là `The Nile Ritz-Carlton`. Mình thử nhập vào ô điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/64326a0d-b7c7-4b2e-8e65-825849f002ab)

----
# Câu 5
Mình sẽ vào ngược lại phần **File Report** và search từ ticket xem có file nào nó liên quan tới vé máy bay không.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/1de59d4d-52c5-43df-a651-ea48aa7ee0b3)

Tại đây mình thấy trong `/storage/emulated/0/Download/` Có 1 file là `Plane Ticket.png`. Mình thử mở nó tại thư mục gốc trong phần `..\data\media\0\Download` có 1 file với tên y hệt. Mình mở nó ra.

![Plane Ticket](https://github.com/wdchocopie/CTF-learning/assets/81132394/e8e9663a-e40e-406a-942e-dd565ec0e084)

Tại đây ta thấy địa điểm đi tới là `Las Vegas`. Mình thử nhập vào ô tìm flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/217669de-9b93-4469-9b21-8ea0f7087789)

----
# Câu 6
Tại đây ta có đầu mối là Discord. Mình thử lướt lên phần **Discord Chats**. 

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/1b1d7a86-8780-4870-a7d8-043a02263e54)

Tại đây ta thấy 2 tin nhắn với nội dung sau:
> Hey mate Some changes have occurred in the plan. I have booked my travel ticket for 01/10 at 9:00 AM. Where am I supposed to meet you?

> What a wonderful news! We'll meet at \*\*The Mob Museum\*\*, I'll await your call when you arrive. Enjoy you flight bro ❤️

Tại đây ta thấy tin nhắn thứ 2 có địa điểm là `The Mob Museum` được ẩn đi (theo format \*\*\[tin nhắn\]\*\*). Thử nhập nó vào ô tìm flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/6b6f12c3-a715-4515-a3f3-9c8752382e30)

----
# End of Challenge check

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/b13c2e85-4838-435f-9c2c-fa8af6828036)

**--End--**
