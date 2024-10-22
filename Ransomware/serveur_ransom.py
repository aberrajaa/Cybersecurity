from cryptography.fernet import Fernet
import socket
import os

key = Fernet.generate_key()
print("Your Key is:", key)

with open("keyfile.key", "wb") as key_file:
    key_file.write(key)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 5000))
s.listen()

conn, addr = s.accept()
print(addr, "connected")

msg = conn.recv(2048).decode()
if msg == "key":
    conn.send(key)
    print("Key sent!")
    
conn.close()  
