# SansAlpha

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/8c0b9d95-cea3-4bea-9f56-a9e37d6ebcbb)

Trước tiên mình spawn docker và thử connect tới server của họ

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/738b18d7-2d38-4e2b-ac68-e21353d2688a)

Có vẻ đây là 1 dạng Shell Escape nhưng mình không thể sử dụng kí tự. Mình sẽ thử với `$(0)` để thoát khỏi cái shell giả này

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/2f37022d-7392-407b-8acd-5cd82304dc22)

Có vẻ cái này cũng chặn việc thoát ra như vậy. Mình thử 1 vài kí tự khác

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/2fd0704f-c9cb-4a55-92c6-81df8ac9b9a4)

Dựa theo gợi ý của đầu bài

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/e9bd6a88-d532-410c-bef4-9048479599ca)

1 vài chữ cái nói ở đây thì giống với mình test lúc nãy. Tại đây mình nảy ra ý định set variable bằng lệnh trên rồi thử cat flag ra.

```
_1=(~)
${_1:6:1}${_1:12:1}${_1:7:1} */*
```

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/fcae63d5-2039-4567-b928-3b1f71c92910)

Flag: `picoCTF{7h15_mu171v3r53_15_m4dn355_640b6add}`
