# Elliot Secrets - Week 3
----
**Dữ liệu được cung cấp:**
* 1 file bin

**Flag có dạng: flag{}**

**Tool sử dụng:**
* foremost
* deepsound
* johntheripper
* deepsound2john
* bstrings
* js deob
* dcode.fr (decode base32)

Bài này thuộc dạng blackbox, chủ yếu là đi test.

----
Ở đầu bài mình được phát 1 file **.bin**. Vì mình không chắc nên thử xem lại xem file này là dạng file gì

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/d64d95a9-15e6-4960-b5d1-563288778022)

Mình thấy đấy là file có thể **execute** được. Mình tiến hành chạy thử trên **ParrotOS**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/635e3655-3412-48b2-9bb0-2a515f7927cd)

Và tất nhiên cả có cái gì xảy ra cả. Mình bắt đầu nghĩ theo hướng khác là xem có thể **extract** từ file bin ra hay không

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/fc45efb7-ffb2-49d9-b912-44f4ba1b7554)

Mình cũng thử dùng **IDA** để đọc xem nó làm cái gì

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/bbb92e72-1cca-4a77-bc6b-20fafc363792)

Cũng chả thấy gì. Mình thấy tại đây có vẻ không liên quan tới lệnh thực thi nên mình nghĩ file này có thể recover lại được không. Mình thử dùng **foremost**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/003d529b-b8e0-498f-95e7-f32a6ffa5a06)

Có vẻ như có gì đó, mình thử vào và xem file output

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/1ba0718a-6e04-4dac-aa4c-188e8340dcab)

Mình nghĩ ngay tới tool **steganowav**. Ra và thử

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/b785a212-e6d6-4e0b-b7e8-6e9c09a74079)

Có vẻ cũng không được. Mình thử với deepsound

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/6a5ff584-1958-41d7-81ca-dbd24191c8eb)

Tại đây mình thấy nó yêu cầu nhập mật khẩu. Mình sẽ dùng deep2john.py để convert về hash, xong đó bruteforce4 bằng johntheripper sử dụng wordlist rockyou.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/06b11b82-4bbe-4e85-a3df-fb22cec3e320)

Dùng johntheripper

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/50d5799b-f8f8-48b5-b80d-8e1d38645afe)

Tại đây ta có mật khẩu là `ragerocks123`. Mình thử nhập trong deepsound

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/41bff41a-9faf-45b9-8fe8-372a299ece9f)

Tại đây mình thấy 1 file **.pdf**. Mình thử mở ra

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/29d54515-32ca-4a6b-9954-ddb5fa6af32f)

Trông ảnh các thứ có vẻ bình thường. Mình thử xem source của nó (hoặc dùng bstrings) thì thấy

**Source**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/8e4e34be-49a1-40e8-8b13-a44169cb3d66)

**Bsrings**

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/bb0abec4-3b7a-4d7f-ac91-c6e3950cfe71)

**Đoạn code**

````
(function(_0x5404ee,_0x2cdba5){var _0x3442dd=_0x4e5d,_0x77d06d=_0x5404ee();while(!![]){try{var _0x33a91a=-parseInt(_0x3442dd(0xd6))/0x1+parseInt(_0x3442dd(0xd4))/0x2*(-parseInt(_0x3442dd(0xd3))/0x3)+parseInt(_0x3442dd(0xd7))/0x4*(parseInt(_0x3442dd(0xcf))/0x5)+parseInt(_0x3442dd(0xd5))/0x6+-parseInt(_0x3442dd(0xd2))/0x7+-parseInt(_0x3442dd(0xd0))/0x8+parseInt(_0x3442dd(0xd1))/0x9;if(_0x33a91a===_0x2cdba5)break;else _0x77d06d['push'](_0x77d06d['shift']());}catch(_0x142ac7){_0x77d06d['push'](_0x77d06d['shift']());}}}(_0x332f,0x64602));function _0x332f(){var _0x5a8230=['5149970qizzvf','2571elyeGX','822OMCzAm','2273928XOxnwk','805808WvDmTX','3008qiexeb','3715JjkQes','3050328gjTDQp','15736050JyNZQN'];_0x332f=function(){return _0x5a8230;};return _0x332f();}function _0x4e5d(_0x32d94b,_0x5f23f1){var _0x332fe1=_0x332f();return _0x4e5d=function(_0x4e5d6f,_0x129a63){_0x4e5d6f=_0x4e5d6f-0xcf;var _0x5a016c=_0x332fe1[_0x4e5d6f];return _0x5a016c;},_0x4e5d(_0x32d94b,_0x5f23f1);}function hi(){var _0x570375=_0x1c47;console[_0x570375(0x16c)]('I'),console[_0x570375(0x16c)]('Z'),console[_0x570375(0x16c)]('W'),console[_0x570375(0x16c)]('G'),console[_0x570375(0x16c)]('C'),console[_0x570375(0x16c)]('Z'),console[_0x570375(0x16c)]('3'),console[_0x570375(0x16c)]('3'),console['log']('I'),console[_0x570375(0x16c)]('F'),console[_0x570375(0x16c)]('Z'),console[_0x570375(0x16c)]('G'),console[_0x570375(0x16c)]('K'),console[_0x570375(0x16c)]('V'),console[_0x570375(0x16c)]('K'),console[_0x570375(0x16c)]('M'),console[_0x570375(0x16c)]('N'),console[_0x570375(0x16c)]('5'),console[_0x570375(0x16c)]('Z'),console[_0x570375(0x16c)]('X'),console[_0x570375(0x16c)]('I'),console[_0x570375(0x16c)]('P'),console[_0x570375(0x16c)]('3'),console[_0x570375(0x16c)]('?');}

````
Mình thử lên và deobfuscate nó.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/97f6738b-81fe-4406-b5d4-13b871a6d12e)

Ta sẽ được đoạn code sau

````
function hi() {
  var _0x570375 = _0x1c47
  console[_0x570375(364)]('I')
  console[_0x570375(364)]('Z')
  console[_0x570375(364)]('W')
  console[_0x570375(364)]('G')
  console[_0x570375(364)]('C')
  console[_0x570375(364)]('Z')
  console[_0x570375(364)]('3')
  console[_0x570375(364)]('3')
  console.log('I')
  console[_0x570375(364)]('F')
  console[_0x570375(364)]('Z')
  console[_0x570375(364)]('G')
  console[_0x570375(364)]('K')
  console[_0x570375(364)]('V')
  console[_0x570375(364)]('K')
  console[_0x570375(364)]('M')
  console[_0x570375(364)]('N')
  console[_0x570375(364)]('5')
  console[_0x570375(364)]('Z')
  console[_0x570375(364)]('X')
  console[_0x570375(364)]('I')
  console[_0x570375(364)]('P')
  console[_0x570375(364)]('3')
  console[_0x570375(364)]('?')
}
````

Tại đây mình rút các vallue mà console print ra ta sẽ được

`IZWGCZ33IFZGKVKMN5ZXIP3?`

Mình thử dùng cyberchef để decode

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/fb77c480-7682-4be0-be27-27fc97391e76)

Nhìn qua có vẻ là dạng **base**. Mình sẽ test thử **Base 64** và **Base 32**

`base64`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/55d2fcf2-792e-4122-8096-5e4abf91fa42)

`base 32`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/ef3a3fdf-4b04-4818-af49-d469436bc273)

Vì flag có dạng `Flag{}`, mình đổi kí tự vừa tìm được thành `Flag{AreULost?}`. Thử nhập flag vào

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/b7c51aa3-79c5-4c55-bc40-e6fecdd20226)

----
# End of challenge check

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/5a191b5b-de69-41c2-915e-8bf068b858d9)

**--End--**
