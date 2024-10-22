# Script de Hachage de Fichiers

## Description

`hash_files_script.exe` est un utilitaire permettant de calculer les hachages MD5, SHA1 et SHA256 de tous les fichiers présents sur les disques d'une machine. Le script parcourt de manière récursive chaque disque, calcule les hachages et enregistre les résultats dans un fichier texte.

## Fonctionnalités

- Calcule les hachages MD5, SHA1 et SHA256 pour chaque fichier.
- Scanne de manière récursive tous les disques connectés à la machine.
- Sauvegarde les résultats dans un fichier texte nommé `hash_sortie_machine_<nom_machine>.txt` dans le répertoire de travail actuel.

## Prérequis

- Système d'exploitation Windows (le script est conçu pour fonctionner dans un environnement Windows).

## Installation

1. Téléchargez `hash_files_script.exe`.
2. Placez l'exécutable à l'emplacement désiré sur votre machine.

## Utilisation

1. Ouvrez une invite de commande en mode administrateur.
2. Naviguez jusqu'au répertoire où `hash_files_script.exe` est situé.
3. Exécutez l'exécutable en tapant :
   ```bash
   ./hash_files_script.exe

## Résultats

On obtient un fichier texte avec tous les hashs des fichiers de la machine, qui peuvent être utilisés plus tard avec l'API de VirusTotal pour vérifier si des fichiers malveillants existent sur la machine.

