# Attaque et Chiffrement Vigenère

Ce projet contient deux scripts Python permettant de chiffrer et de déchiffrer des fichiers à l'aide du chiffre de Vigenère, ainsi que d'effectuer une attaque pour deviner la clé de chiffrement utilisée. Il repose sur des techniques cryptographiques simples comme l'indice de coïncidence (IC) et la fréquence des lettres.

## Contenu du projet

- **`vigenere.py` :**  
  Ce script permet de chiffrer et de déchiffrer un fichier en utilisant le chiffre de Vigenère avec une clé donnée.

- **`vigenere_attack.py` :**  
  Ce script permet de deviner la longueur de la clé et d'effectuer une attaque par analyse de fréquences pour retrouver la clé utilisée dans un texte chiffré par Vigenère.

## Utilisation

### Chiffrement d'un fichier avec Vigenère

Pour chiffrer un fichier avec une clé donnée :

```bash
python vigenere.py --encrypt --input fichier_en_clair.txt --output fichier_chiffre.txt --key VOTRE_CLE
```

### Déchiffrement d'un fichier avec Vigenère
Pour déchiffrer un fichier chiffré avec une clé connue :

```bash
python vigenere.py --decrypt --input fichier_chiffre.txt --output fichier_dechiffre.txt --key VOTRE_CLE
```

### Attaque du chiffre de Vigenère
Le script vigenere_attack.py permet d'effectuer une attaque par fréquence pour retrouver la clé utilisée dans un texte chiffré. Le script utilise les fréquences des lettres courantes dans la langue anglaise pour deviner la clé lors de l'attaque.

### Exemple de fichiers
Un exemple de fichier chiffré est fourni sous le nom fichier_chiffre.txt. Vous pouvez l'utiliser pour tester le déchiffrement ou l'attaque par fréquence.

