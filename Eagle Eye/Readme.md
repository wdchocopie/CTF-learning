# Eagle Eye - Week 3
----
**Tool sử dụng**
* Voltality 2 \([Cheatsheet](https://downloads.volatilityfoundation.org/releases/2.4/CheatSheet_v2.4.pdf)\)

**Dữ liệu được cung cấp**
* 1 file .raw

----
Mình có 1 dữ kiện đầu tiên là file này có đuôi là `.raw`. Ban đầu mình nghĩ đây là 1 file hình ảnh

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/0d460610-5601-4190-b0df-c0cbac7f60e6)

Sau đó mình thử kiểm tra với lệnh file trên ParrotOS

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/ec7d6794-1628-4849-afd6-d5157f72f178)

Đồng thời cũng check lại file online

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/b96b860b-939b-4c6f-a3cd-a6c75cc54e43)

Tạm thời đến đây mình có thể xác định đây là 1 file memory của windows. Mình sẽ sử dụng voltality để xem xem có đúng không

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/e31247c4-d2df-4137-99d3-5367ecdeb4d1)

Ta có thể check ra được info thế này là ok rồi. Mình sẽ tiến hành check process của nó

`pslist`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/7f48d363-7749-4342-aff5-85a7cdefa701)

Tại process mình không thấy có gì lạ, mình tiến hành kiểm tra MFT([Master File Table](https://www.sciencedirect.com/topics/computer-science/master-file-table#:~:text=Master%20File%20Table%20(MFT),the%20drive%2C%20and%20file%20metadata.))

`mftparser`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/3a02bec0-8411-4e46-a68f-e403f40b3273)

Mình thử tìm có gì liên quan tới flag không nên sẽ sử dụng kèm cả `grep`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/a473a781-7b1c-4748-be4b-db27dfead402)

Có vẻ là có, mình sẽ tìm thử nó bằng cách xuất log ra và find bằng text editor.

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/bebab6a4-0a64-418f-8ae5-485b0b7fc0a8)

Tại đây mình thấy đây giống với chương trình của C++, mình sẽ ném hexcode này và giải mã ra

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/9e1be333-9201-45df-8f76-51d9c781e71b)

Sau đây mình sẽ có 1 đoạn code sau đây

````
#include <iostream>
void flag();
using namespace std;
int main(){

flag();
while(true){
}
return 0;
}

void flag(){
char x[26];
int n=0;
x[n++]='f';
x[n++]='l';
x[n++]='a';
x[n++]='g';
x[n++]='2';
x[n++]=':';
x[n++]='_';
x[n++]='S';
x[n++]='Y';
x[n++]='S';
x[n++]='_';
x[n++]='P';
x[n++]='r';
x[n++]='c';
x[n++]='e';
x[n++]='3';
x[n++]='3';
x[n++]='_';
x[n++]='4';
x[n++]='t';
x[n++]='4';
x[n++]='L';
x[n++]='L';
x[n++]='}';
for (int i =0; i<n;i++){
	(x[n]);
}
}

````
Rút hết các kí tự bên trong ta sẽ có

`flag2:_SYS_Prce33_4t4LL}`

Dựa theo flag này, mình thử tìm các từ khóa liên quan tới part 1 của flag. Sau 1 hồi thử `flag`, `flag1` thì mình tìm được từ khóa sau

`part`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/478912f8-b31f-4d32-8d66-e25aaadd41e2)

ta sẽ có flag 1 `{Don0t_alw4ys_TRust`. Ghép 2 cái này vào ta có flag 

`flag{Don0t_alw4ys_TRust_SYS_Prce33_4t4LL}`

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/043fd1c9-d064-40a7-9ece-aa0ca17a16f5)

----
# End of challenge check

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/f326db43-ac02-46e6-bb0b-534159ff5e84)

**--End--**
