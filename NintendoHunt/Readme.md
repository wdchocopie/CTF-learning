# NintendoHunt - Week 4
----
**Scenario**: Bạn đã được thuê làm nhà phân tích SOC để điều tra một vi phạm an ninh tiềm ẩn tại một công ty. Công ty gần đây đã nhận thấy hoạt động mạng bất thường và nghi ngờ rằng có thể có một quy trình độc hại đang chạy trên một trong các máy tính của họ. Nhiệm vụ của bạn là xác định quy trình độc hại và thu thập thông tin về hoạt động của nó.

**Tool sử dụng:**
* Voltality 2
* Strings

**Dữ liệu được cung cấp**
* File **.zip** và password. Bên trong là 1 file **.mem**

----
# Câu hỏi

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/40b4b853-0daa-4ed1-a60a-1a434f9f3e73)

**Tạm dịch câu hỏi**
1. PID của mã độc
2. Mã md5 bên trong mã độc
3. Tên Process là Parent với mã độc
4. Địa chỉ MAC của default gateway
5. Tên của hidden file trong alternative data stream
6. Browser cache được lưu khi user truy cập vào www.13cubed.com

----
# Câu 1

**Hint**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/37286e6d-36fc-4fb1-ad66-7e99fd96944c)

**Tạm dịch:** Chạy `pslist` / `psscan` để show process list

Mình trước tiên kiểm tra file **.mem** bằng `imageinfo`

`vol2 -f memdump.mem imageinfo`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/084f0e9f-afa6-4e97-86b3-f748ee47d900)

Mình sẽ thử xem process bằng `pslist`

`vol2 -f memdump.mem --profile=Win10x64_17134 pslist`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/78953add-3f5f-490d-a748-d01231dbc143)

Tại đây mình thấy có 3 cái `svchost.exe.ex` cùng có PPID là `4824` và từ cái tên cũng không bình thường tí nào. Mình quay lại dùng `grep` để tìm những process nào có cùng PPID `4824`

`vol2 -f memdump.mem --profile=Win10x64_17134 pslist | grep 4824`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/73c6b737-915c-48c4-a6f4-a2d4b9495630)

Tại đây ta thấy có 4 cái `svchost.exe` nhưng có 1 cái không bị terminate. Nhiều khả năng đây là malware do hầu hết malware chạy ngầm và thường không bị terminate. Mình thử nhập PID của cái này là `8560` vào ô điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/d3a2001a-c3aa-432c-9ec3-4282d9f4b7f5)

----
# Câu 2

**Hint**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/3748ee85-d3b9-4408-9e94-d271e35a033f)

**Tạm dịch**:
1. dùng memdump
2. -> dùng strings

Trước tiên mình lên xem thử memdump như thế nào trên [cheatsheet](https://downloads.volatilityfoundation.org/releases/2.4/CheatSheet_v2.4.pdf)

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/35541b6e-a51f-4e7e-a13b-7bdbc6fc4da4)

Mình cũng có nhớ trong phần **Help** của voltality 2 có argument này

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/22b70751-33ae-4797-9f12-5ffb23cdc67e)

Vì ở đây chỉ bảo về mã độc nên mình sẽ dump PID `8560`

`vol2 -f memdump.mem --profile=Win10x64_17134 memdump -D C:\Users\wdcho\Downloads\temp\c82-NintendoHunt -p 8560`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/d4a7104d-0c13-415f-ab4f-11603dab1d01)

Mình thử strings file vừa dump được ra

strings 8560.dmp > 8560.txt

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/2324ef5b-4871-450f-b627-4306adc9aa3b)

Mở file và mình thử lướt qua

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/6521a51d-54d8-426c-919d-1113beb040bc)

Lên cybershef và giải ra

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/8aeefdff-4def-4495-a1ca-04ff4f986a34)

Thử nhập `3a19697f29095bc289a96e4504679680` vào ô điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/c56133a8-277c-4504-961d-9df31f8aa699)

----
# Câu 3
Câu này mình vừa tìm được từ trước là `explorer.exe`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/201e94f6-5dcb-4ae4-b816-34fa2531aca7)

----
# Câu 4

**Hint:**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/47c059da-85f8-456d-8d8b-9e35bc51074e)

**Tạm dịch**
1. Phân tích SOFWARE registry hive
2. Chạy printkey trên voltality
3. print "Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged"
4. print "Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged\010103000F0000F0080000000F0000F0E3E937A4D0CD0A314266D2986CB7DED5D8B43B828FEEDCEFFD6DE7141DC1D15D"

Đối với câu này, mình thử search **Tìm default gateway từ registry** trên mạng. Sau đó mình đã tìm thấy câu trả lời ở [reddit](https://www.reddit.com/r/networking/comments/flnux0/is_it_possible_to_extract_the_mac_of_previously/?rdt=56754)

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/24d287ed-41ba-4106-a791-c3180a99cfe5)

Cái này vừa trùng hợp với hint mà mình nhận được. Mình thử tiến hành dùng `printkey` trên `Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged`

`vol2 -f memdump.mem --profile=Win10x64_17134 printkey -K "Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged"`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/4baf9b9d-2966-4462-968b-067bda19015d)

Tiếp tục vào `Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged\010103000F0000F0080000000F0000F0E3E937A4D0CD0A314266D2986CB7DED5D8B43B828FEEDCEFFD6DE7141DC1D15D`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/38015a4e-89bd-4f4b-8ea3-c600447c599a)

Ta có luôn 1 mã MAC. Mình thử nhập vào ô điền flag `00:50:56:FE:D8:07`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/6f88663f-b7b6-4aae-862d-e5bfbcfb2886)

----
# Câu 5
**Hint**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/32431d92-57a5-4ea8-a936-bcb58b16ab9c)

**Tạm dịch:**
1. Dùng `mftparser`
2. tìm `$DATA`

Với bài này mình nghĩ về file thì nghĩ tới ngay `mft` như bài [Eagle Eye](https://github.com/wdchocopie/CTF-learning/tree/main/Eagle%20Eye)

`vol2 -f memdump.mem --profile=Win10x64_17134 mftparser > mft.txt`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/14df4415-358f-4c83-a4a2-c3b7ab33ae4e)

Do tên file có format `\*\*\*.txt` nên mình sẽ dùng regex tìm thử bằng sublime (hoặc có thể dùng bất kì 1 text editor nào khác có find bằng regex)

`\b\w{3}\.txt\b`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/b15d5ff0-4ec9-461e-b33d-efe58ce2ccbb)

Thử `yes.txt` vào ô điền flag

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/97f98763-ffbe-450a-bf75-86d98e2dba82)

----
# Câu 6
**Hints:**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/0d1a98e7-1537-4cfd-a1f4-ea3739fcc832)

**Tạm dịch:**
1. Dùng `mftparser`
2. Tìm kiếm từ khóa `13cubed`

Do mình đã trích sẵn ra file `mft.txt` nên mình sẽ grep nó thôi

`type mft.txt | grep -i 13cubed`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/9a28c3a7-c7ba-4f4e-b4ee-ee821695f5da)

Tại đây ta có định dạng flag là `Format: ﹡:\﹡﹡﹡﹡﹡\﹡﹡﹡\﹡﹡﹡﹡﹡﹡﹡\﹡﹡﹡﹡﹡\﹡﹡﹡﹡﹡﹡﹡﹡\﹡﹡﹡﹡﹡﹡~﹡.﹡﹡﹡\﹡﹡\#!﹡﹡﹡\﹡﹡﹡﹡﹡﹡~﹡\﹡﹡﹡﹡﹡\﹡﹡﹡﹡﹡﹡﹡﹡\﹡﹡﹡﹡﹡﹡﹡[﹡].﹡﹡﹡` nên khả năng tại ô đầu tiên là ổ. Ta sẽ thử `C:\Users\CTF\AppData\Local\Packages\MICROS~1.MIC\AC\#!001\MICROS~1\Cache\AHF2COV9\13cubed[1].htm`
và `C:\Users\CTF\AppData\Local\Packages\MICROS~1.MIC\AC\#!001\MICROS~1\Cache\IQDBNKYD\13Cubed[1].png` vào ô điền flag

`C:\Users\CTF\AppData\Local\Packages\MICROS~1.MIC\AC\#!001\MICROS~1\Cache\AHF2COV9\13cubed[1].htm`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/d0a7eddd-6335-43d3-a38a-8b7f6b2413f2)

----
# End of challenge check

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/39205ebc-d35d-471e-aa4c-da8c2fb2a411)

**--END--**
