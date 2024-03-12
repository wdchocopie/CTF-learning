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
    host = "94.237.63.83"  # Replace with the host where netcat is running
    port = 41945  # Replace with the port on which netcat is listening

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
