# Projet de Simulation de Ransomware

Ce projet est une simulation d'un ransomware utilisant le chiffrement de fichiers. Il se compose de deux scripts : un pour le serveur (`server_ransom.py`) et un pour le client (`client_ransom.py`). Le client chiffre les fichiers dans un répertoire spécifique et peut également les déchiffrer avec une clé reçue du serveur.

## Contenu du projet

- `server_ransom.py` : Script serveur qui génère une clé de chiffrement et l'envoie au client.
- `client_ransom.py` : Script client qui chiffre et déchiffre les fichiers à l'aide de la clé reçue du serveur.
- `files_to_encrypt/` : Dossier contenant les fichiers à chiffrer.

## Avertissement

**Ce projet est à des fins éducatives uniquement. Son utilisation sans le consentement explicite des personnes concernées est strictement interdite. L'utilisation inappropriée de ce code peut avoir des conséquences juridiques.**

## Instructions d'utilisation

### 1. Préparation de l'environnement

Assurez-vous d'avoir Python installé sur votre machine. Vous aurez également besoin des bibliothèques nécessaires. Vous pouvez les installer avec la commande suivante :

```bash
pip install cryptography pyfiglet
```
### 2. Démarrer le serveur

Ouvrez un terminal.
Exécutez le script serveur :

```bash
python server_ransom.py
```
Cela générera une clé de chiffrement et écoutera les connexions des clients. La clé sera affichée dans le terminal.

### 3. Chiffrement des fichiers
Ouvrez un autre terminal.
Exécutez le script client :

```bash
python client_ransom.py
```
Ce script se connectera au serveur, récupérera la clé et chiffrera tous les fichiers présents dans le dossier files_to_encrypt. Les fichiers chiffrés auront l'extension .encrypt.

### 4. Déchiffrement des fichiers
Après le chiffrement, pour déchiffrer les fichiers, exécutez à nouveau le script client :

```bash
python client_ransom.py
```
Lorsqu'il demande la clé, entrez la clé affichée par le serveur. Le script tentera de déchiffrer tous les fichiers ayant l'extension .encrypt dans le dossier files_to_encrypt.

## Notes

Soyez prudent avec ce code, car une mauvaise utilisation pourrait entraîner une perte irréversible de données.
