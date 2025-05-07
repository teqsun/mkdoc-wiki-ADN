# Styles et Cellules

## Introduction

Un Style est un ensemble de propriétés visuelles qui définissent l'apparence des éléments dans votre application. Dans ce système, les styles peuvent être appliqués à des cellules individuelles, des collections de cellules, des lignes ou des colonnes de tableaux de données, permettant ainsi une mise en forme riche et cohérente des informations présentées.

Les styles sont particulièrement utiles pour :
- Mettre en évidence des informations importantes
- Différencier visuellement différents types de données
- Améliorer la lisibilité des tableaux de résultats
- Créer des rapports professionnels avec une mise en forme cohérente
- Appliquer des formatages conditionnels basés sur les valeurs des données

Ce document fournit des exemples concrets pour vous aider à comprendre comment utiliser efficacement le système de styles dans vos applications.

## Partie 1 : les Styles

### Création et manipulation de styles

```python
# Création d'un style complet avec commentaires explicatifs
style = Style()
style.Bold = True                       # Mettre le texte en gras
style.Italic = False                    # Ne pas mettre le texte en italique
style.Underlined = True                 # Souligner le texte
style.FontName = "Calibri"              # Définir la police
style.FontSize = 12                     # Définir la taille de la police à 12 points
style.Foreground = Color(0, 0, 255)     # Texte en bleu
style.Background = Color(230, 230, 230) # Fond gris clair
style.Format = "#,##0.00"               # Format pour afficher les nombres avec 2 décimales
style.HorizontalAlignment = HorizontalAlignment.Right  # Aligner le texte à droite
style.VerticalAlignment = VerticalAlignment.Center     # Centrer verticalement
style.WrapText = True                   # Autoriser le retour à la ligne automatique
style.Border = Border(PenStyle(PenWeight.Thin, Color(0, 0, 0))) # Bordure fine noire
style.Indentation = 1                   # Ajouter une indentation
```

### Styles avec bordures complexes

```python
# Création d'une bordure simple (identique sur tous les côtés)
simpleBorder = Border(PenStyle(PenWeight.Medium, Color(0, 0, 0)))  # Bordure moyenne noire partout

style = Style()
style.Border = simpleBorder

# Création d'une bordure avec différents côtés
leftRight = PenStyle(PenWeight.Thin, Color(0, 0, 0))     # Bordure fine noire
topBottom = PenStyle(PenWeight.Medium, Color(0, 0, 0))   # Bordure moyenne noire

complexBorder = Border(leftRight, topBottom, leftRight, topBottom)  # Ordre: gauche, haut, droite, bas

complexStyle = Style()
complexStyle.Border = complexBorder
```

## Partie 2 : les Cellules

Une cellule est l'unité fondamentale d'affichage et de stockage des données dans ce système. Elle associe une valeur (Content) à un style visuel qui définit son apparence. Les tableaux de données sont généralement composés de cellules modifiables organisées en lignes et colonnes.

Chaque cellule peut contenir différents types de données (texte, nombres, dates, etc.) et possède ses propres propriétés de mise en forme. Cette combinaison permet de créer des visualisations riches et informatives où les données et leur présentation visuelle travaillent ensemble pour transmettre l'information de manière optimale.

Les cellules peuvent également être regroupées en collections pour appliquer des styles communs à plusieurs éléments, simplifiant ainsi la gestion des grands ensembles de données.

### Création et manipulation de cellules

```python
# Création d'une cellule avec du texte
textCell = Cell("Texte d'exemple")

# Création d'une cellule avec un nombre
numberCell = Cell(42.5)
numberCell.Format = "#,##0.00"
numberCell.HorizontalAlignment = HorizontalAlignment.Right

# Cellule avec une mise en forme avancée
formattedCell = Cell("Important")
formattedCell.Bold = True
formattedCell.Foreground = Color(255, 0, 0)  # Rouge
formattedCell.Background = Color(255, 255, 200)  # Jaune pâle
formattedCell.Border = Border(PenStyle(PenWeight.Thin, Color(0, 0, 0)))
```

### Application de styles à des cellules

```python
# Création d'un style
style = Style()
style.FontName = "Calibri"
style.FontSize = 11
style.Bold = True
style.Foreground = Color(0, 80, 120)  # Bleu foncé

# Application du style à une cellule
cell = Cell("Texte avec style")
cell.ApplyStyle(style, True)  # True = remplacer le style existant

# Fusion d'un style avec le style existant d'une cellule
existingCell = Cell("Style existant") 
existingCell.Bold = True

additionalStyle = Style()
additionalStyle.Italic = True
additionalStyle.Foreground = Color(0, 100, 0)  # Vert foncé

existingCell.ApplyStyle(additionalStyle, False)  # False = fusionner avec le style existant
```

## Partie 3 : les Glyphes

Les glyphes sont des éléments graphiques additionnels qui peuvent être attachés à une cellule pour enrichir l'information qu'elle présente. Un glyphe combine un contenu (texte ou symbole) avec son propre style, indépendamment du style principal de la cellule.

Les glyphes sont particulièrement utiles pour :
- Indiquer des tendances (↑ ou ↓ pour montrer une évolution)
- Afficher des variations (pourcentages de croissance ou de diminution)
- Attirer l'attention sur certaines valeurs (astérisques, symboles d'alerte)
- Ajouter des informations contextuelles (unités, statuts, annotations)
- Créer des indicateurs visuels sans modifier la valeur principale

Par exemple, dans un tableau financier, une cellule pourrait afficher "1250" comme valeur principale, accompagnée d'un glyphe "↑ +15%" en vert pour indiquer une augmentation par rapport à la période précédente. Les glyphes permettent ainsi d'enrichir considérablement l'information présentée dans les cellules sans surcharger leur contenu principal.

### Cellules avec glyphes

```python
# Création d'une cellule avec une valeur
cell = Cell(12500)
cell.Format = "#,##0"

# Ajout d'un glyphe pour indiquer une augmentation
upArrowStyle = Style()
upArrowStyle.Foreground = Color(0, 128, 0)  # Vert
cell.AddGlyph("↑", upArrowStyle)

# Ajout d'un pourcentage comme second glyphe
percentStyle = Style()
percentStyle.Foreground = Color(0, 128, 0)  # Vert
percentStyle.Bold = True
cell.AddGlyph("+15%", percentStyle)
```

## Partie 4 : Collections de cellules

Les collections de cellules permettent de manipuler simultanément plusieurs cellules, simplifiant considérablement le travail sur des ensembles de données. Elles sont basées sur la classe `AbstractCellCollection` qui fournit des méthodes et propriétés communes pour interagir avec des groupes de cellules.

Ces collections vous offrent la possibilité de :
- Appliquer un style unique à plusieurs cellules en une seule opération
- Travailler sur des sous-ensembles spécifiques d'un tableau de données (lignes, colonnes, zones)
- Modifier les valeurs ou les formats d'un groupe de cellules
- Gérer efficacement la mise en forme de grands volumes de données

Par exemple, vous pouvez accéder aux cellules d'un en-tête de colonne (`table.Columns.Cells`), à une ligne spécifique (`table.Rows["Total"].Cells`), ou même à une intersection précise (`table.Columns[1, 2].Rows["Total"].Cells`). Cette flexibilité vous permet de cibler exactement les cellules que vous souhaitez modifier, rendant votre code plus lisible et plus efficace.

Les propriétés de style appliquées à une collection sont automatiquement propagées à toutes les cellules contenues dans cette collection, ce qui permet de maintenir une cohérence visuelle sans avoir à manipuler chaque cellule individuellement.

### Mise en forme d'un groupe de cellules

```python
# Dans cet exemple, 'cells' est une collection de cellules (par ex. obtenue via t.Cells)
cells.Bold = True  # Mettre toutes les cellules en gras
cells.Foreground = Color(0, 0, 128)  # Texte en bleu foncé
cells.Format = "#,##0.00"  # Formater tous les nombres
```

### Bordures sur des lignes et colonnes

```python
# Application d'une bordure sur les en-têtes de colonnes
headerRow = table.Columns.Cells
headerRow.Border = Border(PenStyle(PenWeight.Thick, Color(0, 0, 0)))
headerRow.Background = Color(240, 240, 240)
headerRow.Bold = True

# Bordure fine sur toutes les cellules d'une ligne
dataRow = table.Rows["Total"].Cells
dataRow.Border = Border(PenStyle(PenWeight.Thin, Color(0, 0, 0)))
dataRow.Background = Color(255, 250, 205)  # Jaune pâle
```

## Partie 5 : Cellules composées (Usage avancé)

Les cellules composées représentent un concept avancé mais essentiel dans le travail avec des tableaux de données complexes. Une cellule composée contient plusieurs sous-cellules, chacune avec son propre contenu et style.

### Choix architectural : calculs dans les cellules vs calculs dans les lignes/colonnes

Le système offre deux approches pour gérer les calculs et l'organisation des données :

1. **Approche traditionnelle** : Les calculs sont présentés au niveau des lignes ou des colonnes, et les cellules contiennent simplement les valeurs résultantes. Cette approche est plus appropriée dans la plupart des cas.

2. **Approche par cellules composées** : Les calculs sont intégrés dans les cellules elles-mêmes via les sous-cellules. Cas avantageux : fusion de tableaux complexes, simplification visuelle, calculs complexes entre plusieurs calculs.

Le choix entre ces deux approches dépend de votre cas d'utilisation spécifique. Il est également possible de combiner les deux approches dans différentes parties d'une même application.

### Structure et fonctionnement

Une cellule composée utilise la propriété `SubCells` qui est une collection de cellules filles. Chaque sous-cellule possède :
- Son propre contenu
- Son propre style
- Un identifiant de groupe (Group) pour la retrouver facilement

### Accès aux sous-cellules

Dans la très grande majorité des cas, vous accéderez simplement aux sous-cellules existantes pour lire leurs informations ou modifier leur contenu et leur style :

```python
# Accès aux sous-cellules par nom
cell.SubCells["Valeur"].Content = 125000
cell.SubCells["Valeur"].Format = "#,##0"
cell.SubCells["Évolution"].Foreground = Color(0, 128, 0)  # Vert
cell.SubCells["Évolution"].Bold = True

# Accès aux sous-cellules par index
cell.SubCells[0].FontSize = 12
cell.SubCells[1].HorizontalAlignment = HorizontalAlignment.Right
```

Cette approche permet de travailler efficacement avec des cellules complexes sans avoir à comprendre les mécanismes sous-jacents de création et de disposition des sous-cellules.

### Usage typique

Un cas d'utilisation courant consiste à parcourir les cellules d'un tableau pour appliquer conditionnellement des styles aux sous-cellules en fonction de valeurs présentes dans d'autres sous-cellules :

```python
# Application d'un style conditionnel basé sur les valeurs d'une autre sous-cellule
for cell in table.Cells:
    # Vérification si la sous-cellule "TEST" contient "+"
    if cell.SubCells["TEST"].Content.AsString().Contains("+"):
        # Application d'un style à la sous-cellule "VALUE"
        cell.SubCells["VALUE"].Foreground = Color(0, 128, 0)  # Vert
        cell.SubCells["VALUE"].Bold = True
    else:
        # Style différent si condition non remplie
        cell.SubCells["VALUE"].Foreground = Color(255, 0, 0)  # Rouge
```

Cette approche permet de créer des visualisations conditionnelles riches où l'apparence d'une partie de la cellule dépend de la valeur d'une autre partie.