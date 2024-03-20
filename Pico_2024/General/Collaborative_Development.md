# Collaborative Development

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/aec82fda-be44-4ee0-9bc5-d30af865992e)

Tải, giải nén và xem file

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/3ecbf7de-f59c-45f6-a704-2ff6e5da5edd)

Mình sẽ check thử file `flag.py` trước

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/52877fae-fa65-4fd7-9e49-a3f3d9565faa)

Dựa theo đầu bài đã cho có vẻ như cái này được nhiều người làm. Mình thử check phần `log` trước

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/d38a2f41-5f36-4061-b20d-68ca68a37b26)

Có vẻ không có gì. Cái tiếp theo mình nghĩ tới chính là `git branch`

`git branch -a`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/79c68c9e-187b-4f3c-9d28-c5363acbd91d)

Có vẻ có 3 branch. Mình sẽ vào từng cái 1 để xenm

`git switch feature/part-1`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/4782cd29-8304-43d0-8130-5568ffc083d1)

`git switch feature/part-2`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/d7ee3d4e-e637-4bbe-8969-d95a5ce5e3cd)

`git switch feature/part-3`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/175437bf-09df-44ae-a597-47333123cc90)

Ghép cả 3 cái vào ta được

Flag: `picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_2c91ca76}`
