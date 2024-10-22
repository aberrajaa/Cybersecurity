# Parser MiniPNG

## Description

Ce script est conçu pour analyser les fichiers MiniPNG, extraire des métadonnées telles que la largeur, la hauteur et le type de pixel, et afficher les commentaires intégrés dans le fichier. De plus, il peut visualiser des images en noir et blanc dans la console et convertir les images au format PPM (Portable Pixmap).

## Fonctionnalités

- Valide le format de fichier MiniPNG.
- Extrait les dimensions de l'image, le type de pixel et les commentaires.
- Affiche les images en noir et blanc dans la console.
- Convertit les images au format PPM pour une utilisation ou une visualisation ultérieure.

## Utilisation

1. **Exigences** :
   - Python 3.x
   - Assurez-vous que vos fichiers MiniPNG sont correctement formatés.

2. **Exécution du script** :
   Pour exécuter le script, utilisez la ligne de commande pour naviguer vers le répertoire contenant `minipng_parser.py` et exécutez la commande suivante :

   ```bash
   python minipng_parser.py <nom_fichier>
   ````
Remplacez <nom_fichier> par le chemin de votre fichier MiniPNG (.mp).

## Exemple
```bash
python minipng_parser.py exemple.mp
```

Cette commande affichera la largeur, la hauteur, le type de pixel et les commentaires du fichier exemple.minipng, et affichera l'image si elle est en noir et blanc. Si l'image est d'un autre type, elle sera convertie au format PPM.
