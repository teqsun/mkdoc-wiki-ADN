import re
from pathlib import Path

DOSSIER = Path("docs")  # Répertoire à corriger

def corriger_structure_liste(contenu):
    lignes = contenu.splitlines()
    nouvelles_lignes = []
    for ligne in lignes:
        # Cas d’un élément numéroté suivi d’un texte avec tiret (mauvaise fusion)
        if re.match(r"^\d+\.\s+\*\*.*\*\*\s+-", ligne):
            ligne = ligne.replace("** -", "**\n   -")
        # Sépare correctement les éléments qui ont été fusionnés
        ligne = re.sub(r"(\*\*.*\*\*)\s+-", r"\1\n   -", ligne)
        nouvelles_lignes.append(ligne)
    return "\n".join(nouvelles_lignes)

for fichier in DOSSIER.rglob("*.md"):
    contenu = fichier.read_text(encoding="utf-8")
    contenu_corrige = corriger_structure_liste(contenu)
    fichier.write_text(contenu_corrige, encoding="utf-8")

print("✅ Correction de la structure des listes hiérarchiques terminée.")

