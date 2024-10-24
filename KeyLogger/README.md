# Keylogger Éducatif

## Description

`keylogger.py` est un script Python qui enregistre les frappes de touches sur un clavier à l'aide de la bibliothèque `pynput`. Les données sont enregistrées dans un fichier texte nommé `keylog.txt`. Ce script est conçu à des fins d'apprentissage uniquement.
## Fonctionnalités

- Enregistre chaque touche pressée, y compris les touches spéciales.
- Les frappes sont enregistrées avec un horodatage dans le fichier `keylog.txt`.
- Le script s'arrête lorsque la touche `Échap` est pressée.

## Prérequis

- Python 3.x
- Bibliothèque `pynput`

Vous pouvez installer la bibliothèque `pynput` en utilisant pip :
```bash
pip install pynput
```

## Utilisation

1.Téléchargez keylogger.py sur votre machine.
2.Ouvrez une invite de commande ou un terminal.
3.Naviguez jusqu'au répertoire où keylogger.py est situé.
4.Exécutez le script avec la commande suivante :

```bash
python keylogger.py
```

Pour arrêter l'enregistrement, appuyez sur la touche Échap.

## Sortie
Les frappes seront enregistrées dans le fichier keylog.txt dans le même répertoire que le script. Chaque entrée sera horodatée et ressemblera à ceci :

2024-10-23 12:00:00: Key a pressed
2024-10-23 12:00:01: Special key Key.esc pressed

## Avertissement

Ce script est destiné uniquement à des fins éducatives. L'utilisation de logiciels de keylogging à des fins malveillantes est illégale et contraire à l'éthique. Veuillez utiliser ce script de manière responsable et respectueuse des lois en vigueur.
