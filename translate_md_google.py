import os
import time
from googletrans import Translator

def translate_file(source_path, target_path, translator):
    with open(source_path, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.strip():
        print(f"⚠️ Fichier vide ignoré : {source_path}")
        return

    try:
        translated = translator.translate(content, src="fr", dest="en").text
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(translated)
        print(f"✅ Traduit : {source_path}")
    except Exception as e:
        print(f"❌ Erreur ({source_path}) : {e}")


def translate_all_files(root_dir="docs"):
    translator = Translator()
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".md") and not file.endswith(".en.md"):
                source_path = os.path.join(subdir, file)
                target_path = os.path.splitext(source_path)[0] + ".en.md"

                if os.path.exists(target_path):
                    with open(target_path, "r", encoding="utf-8") as f:
                        if f.read().strip():
                            print(f"⏭️ Déjà traduit, ignoré : {target_path}")
                            continue

                translate_file(source_path, target_path, translator)
                time.sleep(2)  # Pause pour éviter de surcharger l'API

if __name__ == "__main__":
    translate_all_files("docs")
