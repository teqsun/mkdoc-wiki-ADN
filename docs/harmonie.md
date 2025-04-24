# HARMONIE – Recodages & Mode Batch

Documentation technique pour le module HARMONIE.

## 📚 Sommaire

- [🔄 Recodages](#-recodages)
  - [🔧 Exemple de recodage simple](#-exemple-de-recodage-simple)
  - [📘 Structure d’un fichier de règles](#-structure-dun-fichier-de-règles)
- [📦 Mode Batch](#-mode-batch)
  - [📁 Exemple de fichier batch](#-exemple-de-fichier-batch)
  - [🧪 Cas d’usage typique](#-cas-dusage-typique)
- [🛠 Options avancées](#-options-avancées)
- [📌 Notes importantes](#-notes-importantes)

---

## 🔄 Recodages

Le module permet d’appliquer des règles de recodage à des ensembles de variables issues d’enquêtes ou de bases de données. Ces règles sont définies dans des fichiers `.yml` ou `.json`.

### 🔧 Exemple de recodage simple

```python
# Exemple fictif en pseudo-code
harmonie.recode("sexe", mapping={"1": "Homme", "2": "Femme"})
