from collections import Counter

# Fonction pour calculer l'indice de coïncidence (IC) d'un texte
def calculate_ic(text):
    # Supprimer les caractères non alphabétiques et convertir en majuscules
    text = ''.join(filter(str.isalpha, text)).upper()
    
    # Calculer l'IC en utilisant la formule : IC = Σ(frequences_lettres * (frequences_lettres - 1)) / (N * (N - 1))
    frequencies = Counter(text)
    N = len(text)
    ic = sum(f * (f - 1) for f in frequencies.values()) / (N * (N - 1))
    
    return ic

# Fonction pour trouver la longueur probable de la clé Vigenère
def find_key_length(ciphertext, max_key_length=20):
    ic_values = {}
    
    # Calculer l'IC pour différentes longueurs de clé
    for key_length in range(1, max_key_length + 1):
        subtexts = ['' for _ in range(key_length)]
        for i, char in enumerate(ciphertext):
            subtexts[i % key_length] += char
        
        ic_values[key_length] = calculate_ic(''.join(subtexts))
    
    # Trouver la longueur de clé probable en se basant sur l'IC
    probable_key_length = max(ic_values, key=ic_values.get)
    return probable_key_length

# Fonction pour casser le chiffrement Vigenère en devinant la clé
def vigenere_crack(ciphertext, key_length):
    key = ''
    
    # Découper le texte chiffré en blocs de la longueur de la clé
    blocks = ['' for _ in range(key_length)]
    for i, char in enumerate(ciphertext):
        blocks[i % key_length] += char
    
    # Pour chaque bloc, deviner la lettre de la clé en utilisant l'indice de coïncidence
    for block in blocks:
        max_ic = 0
        probable_shift = 0
        for shift in range(26):
            shifted_text = ''
            for char in block:
                if char.isalpha():
                    shifted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
                    shifted_text += shifted_char
                else:
                    shifted_text += char
            ic = calculate_ic(shifted_text)
            if ic > max_ic:
                max_ic = ic
                probable_shift = shift
        key += chr((26 - probable_shift) % 26 + ord('A'))
    
    return key

# Exemple d'utilisation :
ciphertext = "YSRJN YHBVU WYPSF DZRYE APHHT EFMZH PFWHN YSRSK"
probable_key_length = find_key_length(ciphertext)
probable_key = vigenere_crack("fichier_chiffre.txt", 5)
print("Longueur probable de la clé :", probable_key_length)
print("Clé probable :", probable_key)

