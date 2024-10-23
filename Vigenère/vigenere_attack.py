import argparse
import string
from collections import Counter
import math

ALPHABET = string.ascii_uppercase

bigram_freqs = {
    'TH': 1.52, 'HE': 1.28, 'IN': 0.94, 'ER': 0.94, 'AN': 0.82, 'RE': 0.68, 'ND': 0.63,
    'AT': 0.59, 'ON': 0.57, 'NT': 0.56, 'HA': 0.56, 'ES': 0.56, 'ST': 0.55, 'EN': 0.55,
    'ED': 0.53, 'TO': 0.52, 'IT': 0.50, 'OU': 0.50, 'EA': 0.47, 'HI': 0.46, 'IS': 0.46,
    'OR': 0.43, 'TI': 0.34, 'AS': 0.33, 'TE': 0.27, 'ET': 0.19, 'NG': 0.18
}

def fitness(text):
    bigrams = [text[i:i+2] for i in range(len(text)-1)]
    bigram_counts = Counter(bigrams)
    total_bigrams = sum(bigram_counts.values())

    score = 0
    for bigram, count in bigram_counts.items():
        if bigram in bigram_freqs:
            score += (count / total_bigrams) * bigram_freqs[bigram]
    return score

def decrypt(ciphertext, key):
    decrypted = []
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        if char in ALPHABET:
            key_char = key[i % key_length]
            decrypted_char = ALPHABET[(ALPHABET.index(char) - ALPHABET.index(key_char)) % 26]
            decrypted.append(decrypted_char)
        else:
            decrypted.append(char)  
    return ''.join(decrypted)

def brute_force_vigenere(ciphertext, max_key_length):
    best_key = ""
    best_score = float('-inf')
    best_plaintext = ""

    for key_length in range(1, max_key_length + 1):
        key = [''] * key_length

        def recursive_search(position):
            nonlocal best_key, best_score, best_plaintext
            if position == key_length:
                key_str = ''.join(key)
                plaintext = decrypt(ciphertext, key_str)
                score = fitness(plaintext)
                if score > best_score:
                    best_score = score
                    best_key = key_str
                    best_plaintext = plaintext
            else:
                for letter in ALPHABET:
                    key[position] = letter
                    recursive_search(position + 1)

        recursive_search(0)

    return best_key, best_plaintext

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Vigenère Cipher Brute Force Attack")
    parser.add_argument('--input', required=True, help="Input file containing ciphertext")
    parser.add_argument('--max-key-length', type=int, default=4, help="Maximum key length to consider for brute-force")

    args = parser.parse_args()

    with open(args.input, 'r') as f:
        ciphertext = f.read().strip().upper()

    key, plaintext = brute_force_vigenere(ciphertext, args.max_key_length)

    print(f"Best key: {key}")
    print(f"Decrypted text: {plaintext}")
