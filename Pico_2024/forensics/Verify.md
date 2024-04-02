# Verify

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/f6cc7242-e564-4850-aced-de3a421d7580)

Connect vào server

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/b1efd24c-4100-4e8c-ab03-8eef0339a081)

Mình sẽ sử dụng `sha256sum` với tất cả trong directory `files` và grep ra cái ở trong checksum.txt

`sha256sum files/* | grep $(cat checksum.txt)`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/7465989d-fa10-409e-9d14-087c7ccdb1e6)

Quay lại dùng nó với file `decrypt.sh`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/4153898c-45c7-45fe-adba-2a22be7a43fc)

Flag: `picoCTF{trust_but_verify_87590c24}`
