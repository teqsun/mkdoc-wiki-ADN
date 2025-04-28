import os

# Dossier où sont tes fichiers de fonctions
FONCTIONS_DIR = "docs/fonctions2"

# Nom du fichier de sortie
OUTPUT_FILE = os.path.join(FONCTIONS_DIR, "index.md")

# Récupérer tous les fichiers .md sauf index.md lui-même
fichiers_md = [
    f for f in os.listdir(FONCTIONS_DIR)
    if f.endswith(".md") and f.lower() != "index.md"
]

# Trier les fichiers
fichiers_md.sort()

# Grouper par première lettre
lettres = {}
for fichier in fichiers_md:
    lettre = fichier[0].upper()
    lettres.setdefault(lettre, []).append(fichier)

# Générer le contenu du fichier index.md
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("# 📚 Index des Fonctions\n\n")
    f.write("## 🔤 Accès rapide\n\n")

    # Menu alphabétique
    for lettre in sorted(lettres.keys()):
        f.write(f"[{lettre}](#{lettre.lower()}) ")
    f.write("\n\n---\n")

    # Sections par lettre
    for lettre, fichiers in lettres.items():
        f.write(f"\n## {lettre}\n\n")
        for fichier in fichiers:
            # Nettoyage du nom du fichier pour affichage
            titre = os.path.splitext(fichier)[0].replace("-", " ").replace("_", " ").upper()
            lien = fichier
            f.write(f"- [{titre}]({lien})\n")
