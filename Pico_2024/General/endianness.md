# Enidaness

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/872cb0d2-cacf-457e-9f82-7e87ca5ed7e6)

Tại đây mình thử start docker và chạy thử lệnh `nc` 

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/749a4645-8fa8-42e9-9f2f-dfdd12ec7380)

Tại đây mình đã nắm được phần input đầu tiên. Mình thử code đổi sang **little endian** và sử dụng **pwntools** để gửi kết quả

```
import pwn

p = pwn.remote ("titan.picoctf.net", "61634")

p.recvuntil("Word: ".encode())
word = p.recvline().decode().replace('\n', '').encode().hex()

little = bytearray.fromhex(word)
little.reverse()
little_result = ''.join(f"{n:02X}" for n in little)

p.sendlineafter("Enter the Little Endian representation:".encode(),little_result.encode())

print(p.recvline().decode())
print(p.recvline().decode())

```
Tại đây mình có output bị treo. Mình thử xem lại file source code của bài **endianess**

```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>
#include <time.h>

char *find_little_endian(const char *word)
{
    size_t word_len = strlen(word);
    char *little_endian = (char *)malloc((2 * word_len + 1) * sizeof(char));

    for (size_t i = word_len; i-- > 0;)
    {
        snprintf(&little_endian[(word_len - 1 - i) * 2], 3, "%02X", (unsigned char)word[i]);
    }

    little_endian[2 * word_len] = '\0';
    return little_endian;
}

char *find_big_endian(const char *word)
{
    size_t length = strlen(word);
    char *big_endian = (char *)malloc((2 * length + 1) * sizeof(char));

    for (size_t i = 0; i < length; i++)
    {
        snprintf(&big_endian[i * 2], 3, "%02X", (unsigned char)word[i]);
    }

    big_endian[2 * length] = '\0';
    return big_endian;
}

char *generate_random_word()
{
    printf("Welcome to the Endian CTF!\n");
    printf("You need to find both the little endian and big endian representations of a word.\n");
    printf("If you get both correct, you will receive the flag.\n");
    srand(time(NULL));

    int word_length = 5;
    char *word = (char *)malloc((word_length + 1) * sizeof(char));

    for (int i = 0; i < word_length; i++)
    {
        word[i] = (rand() % 26) + 'a';
    }

    word[word_length] = '\0';
    return word;
}

int main()
{
    char *challenge_word = generate_random_word();
    printf("Word: %s\n", challenge_word);
    fflush(stdout);

    char *little_endian = find_little_endian(challenge_word);
    size_t user_little_endian_size = strlen(little_endian);
    char user_little_endian[user_little_endian_size + 1];
    bool correct_flag = false;

    while (!correct_flag)
    {
        printf("Enter the Little Endian representation: ");
        fflush(stdout);
        scanf("%10s", user_little_endian);
        for (size_t i = 0; i < strlen(user_little_endian); i++)
        {
            user_little_endian[i] = toupper(user_little_endian[i]);
        }

        if (strncmp(user_little_endian, little_endian, user_little_endian_size) == 0)
        {
            printf("Correct Little Endian representation!\n");
            fflush(stdout);
            correct_flag = true;
        }
        else
        {
            printf("Incorrect Little Endian representation. Try again!\n");
            fflush(stdout);
        }
    }

    char *big_endian = find_big_endian(challenge_word);
    size_t user_big_endian_size = strlen(big_endian);
    char user_big_endian[user_big_endian_size + 1];

    bool final_flag = false;
    while (!final_flag)
    {
        printf("Enter the Big Endian representation: ");
        fflush(stdout);
        scanf("%10s", user_big_endian);
        for (size_t i = 0; i < strlen(user_big_endian); i++)
        {
            user_big_endian[i] = toupper(user_big_endian[i]);
        }

        if (strncmp(user_big_endian, big_endian, user_big_endian_size) == 0)
        {
            printf("Correct Big Endian representation!\n");
            fflush(stdout);
            final_flag = true;
        }
        else
        {
            printf("Incorrect Big Endian representation. Try again!\n");
            fflush(stdout);
        }
    }

    FILE *flag = fopen("flag.txt", "r");
    if (flag == NULL)
    {
        printf("Flag not found. Please run this on the server\n");
        fflush(stdout);
        exit(0);
    }

    char flag_content[100];
    fgets(flag_content, sizeof(flag_content), flag);
    printf("Congratulations! You found both endian representations correctly!\n");
    fflush(stdout);
    printf("Your Flag is: %s\n", flag_content);
    fflush(stdout);
    exit(0);

    return 0;
}
```
Tại đây ta còn thấy 1 phần nữa từ bài endianess là big endian. Mình code thêm phần đó vào script của mình

```
import pwn

p = pwn.remote ("titan.picoctf.net", "61634")

p.recvuntil("Word: ".encode())
word = p.recvline().decode().replace('\n', '').encode().hex()

little = bytearray.fromhex(word)
big_result = ''.join(f"{n:02X}" for n in little)
little.reverse()
little_result = ''.join(f"{n:02X}" for n in little)

p.sendlineafter("Enter the Little Endian representation:".encode(),little_result.encode())



p.sendlineafter("Enter the Big Endian representation: ".encode(),big_result.encode())


p.recvuntil(b'\n')
p.recvline()
print(p.recvline().decode())
```

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/94955464-af10-4aad-a169-920ff76854f9)

Flag: `picoCTF{3ndi4n_sw4p_su33ess_28329f0a}`
