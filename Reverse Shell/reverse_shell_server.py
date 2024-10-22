import socket

HOST = '0.0.0.0'  
PORT = 4321

def start_listener():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"Listening on {HOST}:{PORT}...")

    conn, addr = s.accept()
    print(f"Connection from {addr}")

    while True:
        try:
            command = input("Shell> ")
            conn.send(command.encode('utf-8'))

            if command.lower() == "exit":
                conn.close()
                break

            result = conn.recv(4096).decode('utf-8')
            print(result)

        except Exception as e:
            print(f"Erreur: {e}")
            conn.close()
            break

if __name__ == "__main__":
    start_listener()
