import random 
from sympy import mod_inverse
from Crypto.Util import number


###
def calcul_n(phi):
	p=number.getPrime(64)
	q=number.getPrime(64)
	phi=(p-1)*(q-1)
	n=p*q
	return n
###	



def calculer_d(e,phi_n):
	d = pow(e,-1,phi_n)
	return d
	
def fonction(e,n,m):
	if(m<(2**(2*64))):
		return pow(m,e,n)
		
		
def code(chaine,dictionnaire):	
	result = ""
	for caractere in chaine:
		if caractere in dictionnaire:
			result += str(dictionnaire[caractere])
	return result
	
	
def decode(chaine, dictionnaire):
    decode = ""
    for i in range(0, len(chaine), 2):
        entier = int(chaine[i:i+2])  
        caractere = dictionnaire.get(entier)
        if caractere is not None:
            decode += caractere
    return decode

def chiffrement_RSA(chaine, n, e, dictionnaire):
    codage = int(code(chaine, dictionnaire))
    return fonction(e, n, codage)

def dechiffrement_RSA(decodage, d, dictionnaire):
    decoder = fonction(d, n, decodage)
    chaine = str(decoder)
    return decode(chaine, dictionnaire)



   
   
mon_dico_code = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19, 'k': 20, 'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r': 27, 's': 28, 't': 29, 'u': 30, 'v': 31, 'w': 32, 'x': 33, 'y': 34, 'z': 35}

mon_dico_decode = {
    10: 'a',
    11: 'b',
    12: 'c',
    13: 'd',
    14: 'e',
    15: 'f',
    16: 'g',
    17: 'h',
    18: 'i',
    19: 'j',
    20: 'k',
    21: 'l',
    22: 'm',
    23: 'n',
    24: 'o',
    25: 'p',
    26: 'q',
    27: 'r',
    28: 's',
    29: 't',
    30: 'u',
    31: 'v',
    32: 'w',
    33: 'x',
    34: 'y',
    35: 'z'
}

p = number.getPrime(64)  
q=number.getPrime(64)
phi_n=(p-1)*(q-1)
n=p*q
e=(2**16)+1
d=calculer_d(e,phi_n)

# Utilisez le même dictionnaire pour le codage et le décodage
resultat_chiffre = chiffrement_RSA("bonjourcavaettoi", n, e, mon_dico_code)
resultat_dechiffre = dechiffrement_RSA(resultat_chiffre, d, mon_dico_decode)

print(resultat_chiffre)
print(resultat_dechiffre)

