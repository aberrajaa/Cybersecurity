# Projet de Reverse Shell

Ce projet consiste en une implémentation simple d'un reverse shell, comprenant deux scripts : un pour le serveur (`reverse_shell_server.py`) et un pour le client (`reverse_shell_client.py`). Le client se connecte au serveur et exécute des commandes envoyées par celui-ci.

## Contenu du projet

- `reverse_shell_server.py` : Script serveur qui écoute les connexions du client et envoie des commandes.
- `reverse_shell_client.py` : Script client qui se connecte au serveur et exécute les commandes reçues.

## Avertissement

**Ce projet est à des fins éducatives uniquement. Son utilisation sans le consentement explicite des personnes concernées est strictement interdite. L'utilisation inappropriée de ce code peut avoir des conséquences juridiques.**

## Instructions d'utilisation

### 1. Préparation de l'environnement

Assurez-vous d'avoir Python installé sur votre machine.

### 2. Démarrer le serveur

1. Ouvrez un terminal.
2. Exécutez le script serveur :

   ```bash
   python reverse_shell_server.py
   ```
Le serveur écoutera les connexions sur l'adresse IP spécifiée (0.0.0.0, ce qui signifie qu'il écoute sur toutes les interfaces) et le port 4321.
### 3. Exécuter le client
1. Ouvrez un autre terminal.
2. Exécutez le script client :
```bash
python reverse_shell_client.py
```
Le client se connectera au serveur en utilisant l'adresse IP et le port spécifiés dans le script.

### 4. Interaction

Une fois que le client est connecté, vous pouvez envoyer des commandes à partir du terminal du serveur.
Le client exécutera les commandes et renverra les résultats au serveur, qui les affichera.
Pour fermer la connexion, tapez exit dans le terminal du serveur.
