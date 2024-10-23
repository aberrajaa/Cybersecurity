# Attaque et Chiffrement Vigenère

Ce projet contient deux scripts Python permettant de chiffrer et de déchiffrer des fichiers à l'aide du chiffre de Vigenère, ainsi que d'effectuer une attaque pour deviner la clé de chiffrement utilisée.

## Contenu du projet

- **vigenere.py** : Ce script permet de chiffrer et de déchiffrer un fichier en utilisant le chiffre de Vigenère avec une clé donnée.
  
- **vigenere_attack.py** : Ce script permet de deviner la longueur de la clé et d'effectuer une attaque par analyse de fréquences pour retrouver la clé utilisée dans un texte chiffré par Vigenère.

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

## Attaque du chiffrement de Vigenère
Le script vigenere_attack.py effectue une attaque par brute force pour retrouver la clé utilisée dans un texte chiffré.
Limitations : L'attaque par force brute devient impraticable avec des clés de plus de 5 lettres en raison du nombre exponentiel de combinaisons possibles.

## Utilisation

```bash
python vigenere_attack.py --input fichier_a_dechiffrer.txt --max-key-length 4
```

NB: Ne fonctionne pas pour les clés de plus de 4 lettres

## Pistes pour des techniques plus rapides
- Analyse de fréquence : Utiliser les fréquences des lettres et des bigrammes pour réduire le nombre de combinaisons possibles.

- Indices de coïncidence : Utiliser cette méthode pour estimer la longueur de la clé avant d'appliquer d'autres attaques.

## Exemples de fichiers
Un exemple de fichier chiffré avec la clé READ est fourni sous le nom fichier_chiffre.txt. Vous pouvez l'utiliser pour tester le déchiffrement ou l'attaque par brute force.
