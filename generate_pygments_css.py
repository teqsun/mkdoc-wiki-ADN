from pygments.formatters import HtmlFormatter

# Utilise le thème 'monokai' (ou 'dracula', 'paraiso-dark', etc.)
formatter = HtmlFormatter(style="monokai")
css = formatter.get_style_defs('.codehilite')

# Sauvegarde dans un fichier que MkDocs peut charger
with open("docs/assets/stylesheets/pygments.css", "w") as f:
    f.write(css)
