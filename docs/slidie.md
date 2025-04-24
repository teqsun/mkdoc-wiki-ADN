# SLIDIE – API Python

Cette page documente l’API Python permettant de manipuler les tableaux dans l’outil SLIDIE.

## 📌 Fonctions principales

- Chargement de tableaux depuis un fichier ou une base.
- Requêtage, filtrage et tri des données.
- Export vers différents formats (.xlsx, .csv, .json…).

## 🛠 Exemple de code

```python
from slidie import Table

# Chargement d’un tableau
t = Table("clients.xlsx")

# Filtrage
t_filtered = t.filter("pays == 'France'")

# Export
t_filtered.export("clients_fr.csv")
