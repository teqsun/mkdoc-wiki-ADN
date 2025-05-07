import os
import re

# Dossier contenant les fichiers à corriger 
DOSSIER_CIBLE = "docs"

# Regex : corrige les "**Mot **" mal fermés sans toucher aux bons "**Mot**" ou "***"
regex_gras_mal_forme = re.compile(r"\*\*(\w+)\s+\*\*(?!\*)")

def corriger_fichier(fichier):
    with open(fichier, "r", encoding="utf-8") as f:
        contenu = f.read()

    contenu_corrige = regex_gras_mal_forme.sub(r"**\1**", contenu)

    if contenu != contenu_corrige:
        with open(fichier, "w", encoding="utf-8") as f:
            f.write(contenu_corrige)
        print(f"Corrigé : {fichier}")

def parcourir_dossier(dossier):
    for racine, _, fichiers in os.walk(dossier):
        for nom_fichier in fichiers:
            if nom_fichier.endswith(".md"):
                chemin_complet = os.path.join(racine, nom_fichier)
                corriger_fichier(chemin_complet)

if __name__ == "__main__":
    parcourir_dossier(DOSSIER_CIBLE)
    print("✅ Correction terminée.")
