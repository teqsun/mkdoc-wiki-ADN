import re
from pathlib import Path

# Dossier contenant les fichiers à corriger
DOSSIER = Path("docs")

# Expression régulière : corrige **mot ** en **mot**
pattern = re.compile(r'\*\*(.*?)\s+\*\*')

# Fonction de traitement ligne par ligne
def corriger_balises_markdown(texte):
    return pattern.sub(lambda m: f'**{m.group(1).strip()}**', texte)

# Appliquer la correction à tous les fichiers .md
for fichier in DOSSIER.rglob("*.md"):
    contenu = fichier.read_text(encoding="utf-8")
    contenu_corrigé = corriger_balises_markdown(contenu)
    fichier.write_text(contenu_corrigé, encoding="utf-8")

print("✅ Correction terminée sans modification de structure.")
