# Stop Drop and Roll

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/a9b76c56-58f8-43f0-bb82-6f391ff320de)

Đầu tiên mình thử chạy netcat tới server được chỉ định

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/7d10be78-38b1-4066-8447-0a394c367e28)

Theo đầu bài này có vẻ mình sẽ phải nhập khá nhiều lần chơi game này. Mình tiến hành code trên python kết nối tới server, đọc stdout, phân tích và trả về giá trị tương ứng

```
import socket
import time

def handle_message(message):
    commands = message.split(", ")
    responses = []

    for command in commands:
        if "GORGE" in command:
            responses.append("STOP")
        elif "PHREAK" in command:
            responses.append("DROP")
        elif "FIRE" in command:
            responses.append("ROLL")
    if len(responses) != 0:
        return "-".join(responses) + "\n"
    else:
        return ""

def main():
    host = ""  # Replace with the host where netcat is running
    port =   # Replace with the port on which netcat is listening

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print("Connected to netcat")
        time.sleep(0.5)
        s.recv(1000)

        s.sendall(b"y\n")
        time.sleep(1)
        i = 0
     
        while True:
            message = s.recv(32767).decode("utf-8").strip()
            
            i = i + 1
            print(i)
            if not message:
                break
		
            print("Received:", message)
            response = handle_message(message)
            print("Response:", response)
            s.sendall(response.encode("utf-8"))
            
            
            
if __name__ == "__main__":
    main()

```

Chạy chương trình và sau 1 hồi nó trả về kết quả

![image](https://github.com/wdchocopie/CTF-learning/assets/81132394/fd4fc203-fca0-4709-bd47-40a15973282f)

Flag `HTB{1_wiLl_sT0p_dR0p_4nD_r0Ll_mY_w4Y_oUt!}`

**--End--**
