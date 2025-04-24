import pandas as pd
import yaml
from datetime import datetime

log_lines = []

with open("batch_config.yml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

for bloc in config["batch"]:
    fichier_csv = bloc["fichier"]
    fichier_regles = bloc["recodages"]

    log_lines.append(f"[{datetime.now()}] Traitement de {fichier_csv} avec {fichier_regles}")

    df = pd.read_csv(fichier_csv)

    with open(fichier_regles, "r", encoding="utf-8") as f:
        regles = yaml.safe_load(f)

    recodages = regles.get("recodages", {})
    for colonne, mapping in recodages.items():
        if colonne in df.columns:
            df[colonne] = df[colonne].astype(str).map(mapping).fillna(df[colonne])
            log_lines.append(f"  → Recodé : {colonne}")
        else:
            log_lines.append(f"  ⚠️ Colonne manquante : {colonne}")

    sortie = fichier_csv.replace(".csv", "_recode.csv")
    df.to_csv(sortie, index=False)
    log_lines.append(f"  ✅ Exporté : {sortie}\n")

# Sauvegarde du fichier de log
with open("log.txt", "w", encoding="utf-8") as log_file:
    log_file.write("\n".join(log_lines))

print("📄 Log généré : log.txt")
