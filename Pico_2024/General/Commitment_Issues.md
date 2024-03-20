# Commitment Issues

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/2e737138-8b66-47f9-b76e-f0eb51299de9)

Mình download file trước và extract nó ra

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/e5968b3b-c223-45c4-9f73-53cf38253bb4)

Có vẻ đây là 1 repo của git. Mình thử check log của nó bằng lệnh

`git log`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/9db7cf23-6c54-4057-9063-37a9532f40e6)

Tại đây ta thấy 2 log và 1 cái có vẻ như nó đã xoắ đi 1 thông tin gì đó (rất có khả năng là flag). Mình thử xem lại lúc trước nó commit gì

`git show 87b85d7dfb839b077678611280fa023d76e017b8`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/d5cd7c62-6c76-4e80-a269-d51d39999269)

Flag: `picoCTF{s@n1t1z3_ea83ff2a}`
