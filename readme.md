# Simple weather api
Ensemble de script pour éxécuté des réquètes mongodb dans une base de données sur le covid en France

## Fonctionnalité principales
- Script python pour exécuté des requétes mongodb
- sauvegarder les résultats dans un fichier json
- Afficher des statistiques sur la base de données via Python avec des requétes MongoDB

## Instruction d'installation
- Créer une base de données mongodb, puis importer dans une collection les données du fichier `./db_covid.json`
- Pour installer les packages nécesaire `pip install pymongo matplotlib`

## Configuration requise
- Serveur et outil MongoDB
- Python 3.12.1
- pip

## Exemple d'utilisation

### Requête pour afficher le total cumulé du nombre de cas confirmés, de décès, et de personnes guéries en France

`python ./requests/req1.py`