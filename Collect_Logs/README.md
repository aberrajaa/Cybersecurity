# Analyse de Logs

`find_info_logs.exe` est un outil de recherche qui analyse des fichiers journaux (`.log`, `.txt`, et `.evtx`) à la recherche de domaines, d'URLs et d'adresses IP. Il extrait ces informations et les enregistre dans des fichiers de texte séparés pour une consultation facile.

## Fonctionnalités

- Analyse les fichiers journaux dans un répertoire donné pour identifier :
  - **Domaines** (ex : example.com)
  - **URLs** (ex : https://example.com)
  - **Adresses IP** (ex : 192.168.0.1)
- Prend en charge les formats de fichiers suivants :
  - Fichiers texte (`.log`, `.txt`)
  - Fichiers de journal Windows (`.evtx`)
- Crée trois fichiers de sortie contenant respectivement :
  - Les domaines connectés
  - Les URLs trouvées
  - Les adresses IP interagies

## Installation

1. Téléchargez le dossier Collect_Logs.

## Utilisation

1. Ouvrez une fenêtre de commande (cmd) ou PowerShell en mode administrateur.
2. Naviguez jusqu'au répertoire contenant `find_info_logs.exe`.
3. Exécutez l'exécutable :
   ```bash
   find_info_logs.exe

## Résultats

On obtient 3 fichiers texte avec les noms de domaines, les URL et les IPs rencontrés, qui peuvent servir pour une analyse d'indices de compromission par exemple pour chercher des traces malveillantes sur la machine.
