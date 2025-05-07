import os

# Racine du dossier anglais
base_path = "docs/en"

# Parcours récursif de tous les fichiers
for root, dirs, files in os.walk(base_path):
    for file in files:
        if file.endswith(".en.md"):
            old_path = os.path.join(root, file)
            new_name = file.replace(".en.md", ".md")
            new_path = os.path.join(root, new_name)

            # Évite d’écraser un fichier existant
            if os.path.exists(new_path):
                print(f"⚠️ Fichier déjà présent, on ignore : {new_path}")
                continue

            os.rename(old_path, new_path)
            print(f"✅ Renommé : {old_path} → {new_path}")
