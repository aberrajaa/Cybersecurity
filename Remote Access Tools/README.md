# Détection d'Outils de Contrôle à Distance

Ce projet permet de détecter la présence d'outils de contrôle à distance (tels que TeamViewer, AnyDesk, etc.) sur une machine locale. Le programme vérifie si des processus associés à ces outils sont en cours d'exécution et permet d'exporter les résultats en CSV ou JSON. L'exécutable `remote_access_tools.exe` est disponible dans le dossier `executable`.

## Contenu du projet

- **Executable :**  
  - `remote_access_tools.exe` : L'exécutable permettant de lancer la détection des outils de contrôle à distance.
  
- **Dossier `executable` :** Contient l'exécutable `remote_access_tools.exe` qui peut être utilisé directement sur votre système.

## Utilisation

1. **Téléchargement :** Assurez-vous que vous avez téléchargé le dossier contenant l'exécutable.
2. **Exécution :** Ouvrez une fenêtre de terminal ou de commande dans le dossier contenant `remote_access_tools.exe`.
3. **Lancer l'exécutable :** Tapez la commande suivante pour exécuter le programme :
   ```bash
   remote_access_tools.exe
   ```
## Options supplémentaires :
Le programme permet d'exclure certains outils, de voir les outils non détectés, ou d'exporter les résultats en CSV et JSON.
Par exemple, pour exclure certains outils et exporter les résultats, vous pouvez utiliser les options suivantes :
```bash
remote_access_tools.exe --exclude "Chrome Remote Desktop" "TeamViewer" --export-csv results.csv --export-json results.json
```
Export des résultats
CSV : Si l'option --export-csv est utilisée, le programme exportera les outils détectés dans un fichier CSV.
JSON : Si l'option --export-json est utilisée, le programme exportera les résultats au format JSON.

