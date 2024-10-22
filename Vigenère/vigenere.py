from collections import Counter

def vigenere(text, key, mode='encrypt'):
    resultat = []
    extended_key = key * (len(text) // len(key)) + key[:len(text) % len(key)]
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            key_char = extended_key[i].upper()           
            if mode == 'encrypt':
                encrypted_char = chr(((ord(char) - ord('a') + ord(key_char) - ord('A')) % 26) + ord('A'))
                resultat.append(encrypted_char)
            elif mode == 'decrypt':
                decrypted_char = chr(((ord(char) - ord(key_char) + 26) % 26) + ord('A'))
                resultat.append(decrypted_char)
        else:
            resultat.append(char)
    return ''.join(resultat)

def decrypt_file(input_file, output_file, key):
        with open(input_file, 'r') as file:
            encrypted_text = file.read()
        decrypted_text = vigenere(encrypted_text, key, mode='decrypt')
        with open(output_file, 'w') as file:
            file.write(decrypted_text)
        print(f"Le fichier a été déchiffré avec succès et enregistré sous {output_file}.")

def encrypt_file(input_file, output_file, key):
	with open(input_file, 'r') as file:
		decrypted_text = file.read()
	encrypted_text = vigenere(decrypted_text, key, mode='encrypt')
	with open(output_file,'w') as file :
		file.write(encrypted_text)
	print(f"le fichier a été chiffré avec succès et enregistré sous {output_file}.")

def split_text(text, key_length):
    text_blocks = ['' for _ in range(key_length)]
    for i, char in enumerate(text):
        text_blocks[i % key_length] += char
    return text_blocks
	
def vigenere_attack(key_length, table_of_frequency, input_file):
    probable_key = ''
    with open(input_file, 'r') as file:
        cipher_text = file.read()
    
    text_blocks = split_text(cipher_text, key_length)
    
    for block in text_blocks:
        # Calculer les fréquences des lettres dans le bloc
        letter_frequencies = Counter(block.upper())
        block_length=len(block)
        letter_percentages={letter:(count/block_length) * 100 for letter, count in letter_frequencies.items()}
        # Trier les lettres par fréquence décroissante
        sorted_frequencies = sorted(letter_percentages.items(), key=lambda x: x[1], reverse=True)
        
        # Supprimer les lettres non alphabétiques
        sorted_frequencies = [(letter, freq) for letter, freq in sorted_frequencies if letter.isalpha()]
        
        # Déterminer la lettre la plus probable de la clé
        most_common_letter, _ = sorted_frequencies[0]
        
        # Déterminer le décalage pour cette lettre par rapport à 'E' (la lettre la plus fréquente en anglais)
        shift = (ord(most_common_letter) - ord('E')) % 26
        
        # Ajouter la lettre probable de la clé à la clé en cours de construction
        probable_key += chr((26 - shift) % 26 + ord('A'))
    
    return probable_key
	
	

input_file = "fichier_chiffre.txt" 
output_file = "fichier_chiffre.txt" 
cle = "BOOKS" 
#encrypt_file(input_file, output_file, cle)

letter_frequencies = {
    'A': 0.0817,
    'B': 0.0149,
    'C': 0.0278,
    'D': 0.0425,
    'E': 0.1270,
    'F': 0.0223,
    'G': 0.0202,
    'H': 0.0609,
    'I': 0.0697,
    'J': 0.0015,
    'K': 0.0077,
    'L': 0.0403,
    'M': 0.0241,
    'N': 0.0675,
    'O': 0.0751,
    'P': 0.0193,
    'Q': 0.0010,
    'R': 0.0599,
    'S': 0.0633,
    'T': 0.0906,
    'U': 0.0276,
    'V': 0.0098,
    'W': 0.0236,
    'X': 0.0015,
    'Y': 0.0197,
    'Z': 0.0007
}
test = split_text("leonardow",3)
print(test)
#key_length=5
#guessed_key = vigenere_attack(key_length, letter_frequencies, input_file)
#print("Clé probable :", guessed_key)
