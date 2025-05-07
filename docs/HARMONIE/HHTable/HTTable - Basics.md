# Documentation HTTable

## 1. Introduction

HTTable est une structure de données avancée pour manipuler des tableaux comportant des entêtes hiérarchiques en lignes et colonnes. Elle facilite l'analyse et la transformation de données tabulaires complexes.

### Structure fondamentale

Une HTTable comporte trois parties principales :

1. **Entêtes**  
    - Hiérarchiques et multi-niveaux :
    - Entêtes de colonnes (horizontaux)
     - Entêtes de lignes (verticaux)

2. **Corps du tableau**  
    - Contient les données effectives

3. **Annotations**  
    - Métadonnées associées à la table


### Terminologie essentielle

- **Axe** : Ensemble d'éléments organisés selon une direction (ligne ou colonne)
- **Niveau** : Ligne ou colonne spécifique dans une dimension (un niveau d'entête)
- **Dimension** : Regroupe tous les niveaux de hiérarchie dans une direction (lignes ou colonnes)
- **Calcul** : Valeur dérivée pouvant être placée dans différentes parties de la table
- **Cellule** : Unité fondamentale de stockage des données

## 3. Concepts structurels

### Hiérarchie des concepts

```
HTTable
  ├── ColumnsDimension (tous les niveaux d'entêtes de colonnes)
  │     └── Columns (feuilles de la dimension)
  ├── RowsDimension (tous les niveaux d'entêtes de lignes)
  │     └── Rows (feuilles de la dimension)
  ├── Calculations (peut être en lignes, colonnes ou cellules)
  ├── Annotations (métadonnées)
  └── Body (corps de la table)
```

### Axes et dimensions

La structure d'une HTTable s'articule autour de plusieurs axes et dimensions :

```python
# Dimensions (regroupent tous les niveaux hiérarchiques)
colDim = table.ColumnsDimension  # Tous les niveaux d'entêtes de colonnes
rowDim = table.RowsDimension     # Tous les niveaux d'entêtes de lignes

# Axes des feuilles (niveau le plus bas de la hiérarchie)
cols = table.Columns  # Accès simplifié aux colonnes du corps
rows = table.Rows     # Accès simplifié aux lignes du corps

# Calculs (placés en lignes, colonnes ou cellules)
calcs = table.Calculations
```

### Niveaux des dimensions

Les dimensions contiennent plusieurs niveaux, qui représentent les différentes couches de la hiérarchie :

```python
# Accès aux niveaux d'une dimension (origine 1)
level1 = colDim.Levels[1]  # Premier niveau (racine)
level2 = colDim.Levels[2]  # Deuxième niveau
leafLevel = colDim.Leaves  # Dernier niveau (feuilles)

# Accès avec indexation négative
rootLevel = rowDim.Roots  # Premier niveau (équivalent à Levels[1])
subTitleLevel = rowDim.SubTitles  # Avant-dernier niveau
```

### Entêtes

Les entêtes définissent la structure et organisent les données :

```python
# Accès aux entêtes
colHeader = table.ColumnsHeader
rowHeader = table.RowsHeader

# Nombre de niveaux dans les entêtes
colHeaderLevels = table.ColumnHeaderSize
rowHeaderLevels = table.RowHeaderSize
```

### Corps

Le corps contient les données sans les entêtes :

```python
# Accès au corps (table sans les entêtes)
body = table.Body

# Tailles du corps
bodyRowCount = table.RowCount
bodyColCount = table.ColumnCount

# Tailles de la table complète (avec entêtes)
tableRowCount = table.TableRowCount
tableColCount = table.TableColumnCount
```

## 4. Accès aux données

### Accès par axes et dimensions

L'accès aux données via les axes est le moyen principal de manipuler une HTTable. **Important** : Ces opérations retournent une HTTable qui référence la table parent, permettant ainsi de lire et modifier les données dans une sous-partie de la table d'origine :

```python
# Accès à une colonne (retourne une HTTable liée à la table parente)
firstCol = table.Columns[1]     # Première colonne
colsA_C = table.Columns["A", "B", "C"]  # Sélection par noms

# Accès à une ligne (retourne une HTTable liée à la table parente)
secondRow = table.Rows[2]     # Deuxième ligne
totalsRow = table.Rows["Totals"]  # Sélection par nom

# Accès à un niveau spécifique dans une dimension
prodCategories = table.ColumnsDimension.Levels[1]  # Premier niveau d'entête de colonnes
monthLevel = table.RowsDimension.Levels[2]  # Deuxième niveau d'entête de lignes

# Accès aux éléments d'un niveau spécifique
categoryNames = prodCategories.Texts  # Textes du premier niveau d'entête de colonnes
monthNames = monthLevel.Texts  # Textes du deuxième niveau d'entête de lignes

# Modification via la vue (affecte la table parente)
firstCol.SetAt(1, 1, "Nouvelle valeur")  # Modifie la première cellule de la première colonne
```

### Accès par croisement d'axes

Les croisements d'axes permettent d'accéder à des zones spécifiques :

```python
# Sélection d'une cellule par croisement de coords
cell = table.Rows[3].Columns[2]

# Sélection d'une zone
quarterData = table.Rows["Q1"].Columns["Product A", "Product B"]

# Sélection avec un calcul spécifique 
revenueForQ1 = table.Rows["Q1"].Calculations["REVENUE"]
```

### Accès et modification des valeurs

HTTable offre plusieurs façons d'accéder et de modifier les valeurs selon les zones (corps, entêtes) et les types de données.

#### Accès aux valeurs

```python
# Accès aux valeurs brutes du corps
colValues = table.Columns[1].Values        # Toutes les valeurs de la première colonne
rowValues = table.Rows[2].Values           # Toutes les valeurs de la deuxième ligne
cellValue = table.Columns[1].Rows[3].Value # Valeur à l'intersection

# Accès typé aux valeurs numériques
colNumbers = table.Columns["Revenue"].Numbers  # En tant que doubles
rowIntegers = table.Rows["Count"].Integers    # En tant qu'entiers

# Accès aux textes (conversion automatique en chaînes)
colTexts = table.Columns[1].Texts             # Textes du corps
headerTexts = table.Columns.Texts             # Textes de l'entête des colonnes (niveau feuilles)
levelTexts = table.ColumnsDimension.Levels[1].Texts  # Textes d'un niveau spécifique d'entête
```

#### Modification des valeurs

La modification des valeurs dépend de la zone ciblée (corps ou entêtes) :

```python
# Modification du corps du tableau
table.Columns[1].Rows[2].Value = 42  # Modifie une cellule spécifique du corps
table.Columns["Q1", "Q2"].Value = 0  # Met à zéro toutes les cellules des colonnes Q1 et Q2

# Modification des entêtes
table.Columns.Value = "Trimestre"    # Modifie le texte de l'entête des colonnes (niveau feuilles)
table.Rows.Texts = ["A", "B", "C"]   # Modifie les textes de l'entête des lignes (niveau feuilles)
table.ColumnsDimension.Levels[1].Value = "Année"  # Modifie un niveau spécifique d'entête

# Distribution de valeurs multiples
table.Columns[1].Values = [10, 20, 30, 40]  # Affecte ces valeurs aux 4 premières lignes 
table.Rows["Total"].Values = [100, 200, 300]  # Affecte ces valeurs aux 3 premières colonnes

# Pour les grandes sélections, les valeurs se répètent si la collection est plus petite
table.Columns["Q1", "Q2", "Q3", "Q4"].Values = [0, 1]  # Affecte alternativement 0 et 1
```

#### Manipulation des cellules (style + valeur)

Les cellules permettent d'accéder et de modifier à la fois les valeurs et leur mise en forme :

```python
# Accès aux cellules
colCells = table.Columns["Revenue"].Cells     # Collection de cellules
firstCell = table.Columns[1].Rows[1].Cell     # Une cellule spécifique

# Modification du contenu et du style
cell = table.Columns[1].Rows[2].Cell
cell.Content = "Nouveau contenu"   # Valeur de la cellule
cell.Bold = True                   # Mise en gras
cell.Italic = True                 # Mise en italique
cell.Foreground = Color.Red        # Couleur du texte
cell.Background = Color.LightGray  # Couleur de fond
cell.Format = "#,##0.00"           # Format d'affichage (nombres)
cell.HorizontalAlignment = HorizontalAlignment.Right  # Alignement

# Création d'une cellule formatée
formattedCell = Cell("Valeur importante")
formattedCell.Bold = True
formattedCell.Foreground = Color.Blue
table.Columns[1].Rows[3].Cell = formattedCell
```


## 5. Manipulations des dimensions et axes

### Extraction et sélection

```python
# Extraction d'une sous-table à partir d'axes
revenueByQuarter = table.Columns["Revenue"].Rows["Q1", "Q2", "Q3", "Q4"]

# Extraction d'un niveau de dimension
productLevel = table.ColumnsDimension.Levels[1].Extract()

# Extraction de toutes les colonnes correspondant à un motif
europeColumns = table.Columns["Europe*"]  # Utilise des patterns
```

### Ajout et suppression

```python
# Ajout d'un niveau d'entête
tableWithNewHeader = table.ColumnsDimension.AppendLevel(["Cat1", "Cat1", "Cat2", "Cat2"])

# Ajout d'une colonne (à la fin)
tableWithNewCol = table.Columns.Append("Nouvelle colonne")

# Ajout d'une ligne (au début)
tableWithNewRow = table.Rows.Prepend("Nouvelle ligne")

# Suppression d'une colonne
tableWithoutFirstCol = table.Columns.Remove(1)

# Suppression de plusieurs lignes
tableWithoutRows = table.Rows.Remove("Ligne A", "Ligne C")
```

### Réorganisation des entêtes

```python
# Réorganisation d'un entête de colonne 
# (positif = depuis racine, négatif = depuis feuilles)
newColOrder = table.ColumnsDimension.ReorganizeHeader(2, 1, -1)  # Niveaux 2, 1, puis feuilles

# Redimensionnement d'un entête (ajoute ou supprime des niveaux)
threeRowLevels = table.RowsDimension.ResizeHeader(3)  # Force 3 niveaux d'entête

# Réécriture complète d'un entête avec différents types d'éléments
newHeader = table.ColumnsDimension.RewriteHeader([
    "Région",  # Texte littéral
    "*",       # Conserve tous les niveaux existants
    "[NAME]"   # Valeur d'annotation
])

# Réécriture avec format
newHeader2 = table.ColumnsDimension.RewriteHeaderUsingFormat("-1;-2;\"EXTRA\"")
```

### Déplacement d'éléments

```python
# Déplacer des éléments en haut
tableWithUSFirst = table.Columns.MoveToTop("US")

# Déplacer des éléments à la fin
tableWithTotalLast = table.Rows.MoveToBottom("Total")

# Déplacer avant/après
tableWithMoved = table.Rows.Move("Q2", MoveKinds.Before)  # Options: Before, After, First, Last
```

## 6. Opérations avancées

### Fusion de tables

```python
# Fusion horizontale (ajoute des colonnes)
merged1 = HTTable.MergeColumns(
    [table1, table2], 
    useSmartMerge=True,
    annotationsKeys=["SOURCE"]
)

# Fusion verticale (ajoute des lignes)
merged2 = HTTable.MergeRows([table1, table2])

# Fusion "intelligente" qui harmonise d'abord les dimensions
harmonizedTables = HTTable.Harmonize(TableDirections.Vertical, [table1, table2])
mergedHarmonized = HTTable.MergeColumns(harmonizedTables)
```

### Découpage de tables

```python
# Découpage par dimension
northTable, southTable = table.Columns.SplitByDelimiters("|")

# Découpage en parties égales (ici en trois parties)
parts = table.Rows.SplitBySizes([5, 5, 5])  # 5 lignes par partie

# Découpage avancé respectant la hiérarchie
pages = table.RowsDimension.AdvancedSplit(maxItemsPerPage=20, tolerance=2)

# Découpage par valeurs
q1, q2, q3, q4 = table.Rows.SplitOnValues("Quarter")
```

### Transposition

```python
# Transformer lignes en colonnes et vice-versa
transposed = table.Transpose()
```

### Agrégation

```python
# Agrégation avec opération Sum (options : Sum, Count, Min, Max, etc.)
totalRow = table.Rows.Aggregate(Aggregator.Sum, AggregatorModes.Last, "Total")

# Ajout d'une ligne de total
withTotalRow = table.Rows.AppendTotal()

# Réductions rapides
sumTable = table.Columns.Sum()
avgTable = table.Columns.Mean()
```

### Tri

```python
# Tri des lignes par une colonne
sortedByRevenue = table.Rows.Sort(criteria="Revenue", ascendant=True)

# Tri avancé respectant la hiérarchie
sortedHierarchy = table.RowsDimension.AdvancedSort(
    criteria="Revenue", 
    ascendant=False, 
    sortGroups=True
)
```

### Filtrage

```python
# Extraction selon une condition
positiveValues = table.Rows.ExtractIf(lambda item: item.AsDouble() > 0)

# Suppression des éléments vides
nonEmptyTable = table.Columns.RemoveEmpty()

# Filtrage rapide "WHERE" style
filteredTable = table.Where("Country", "France")
multiFilter = table.Where(["Revenue", "Margin"], value => value > 1000, any=True)
```

## 7. Manipulation des calculs

### Types de placements

Les calculs peuvent être positionnés de différentes façons :

- **AxisPlacement.InRows** : Calculs en lignes
- **AxisPlacement.InColumns** : Calculs en colonnes
- **AxisPlacement.Cells** : Calculs dans les cellules
- **AxisPlacement.None** : Aucun calcul

```python
# Vérifier si la table a des calculs
hasCalcs = table.HasCalculations

# Définir le placement des calculs
table.CalculationsPlacement = AxisPlacement.InColumns

# Déplacer les calculs
table = table.Calculations.MoveToCells()
table = table.Calculations.MoveTo(AxisPlacement.InColumns)
```

### Accès aux calculs

```python
# Accès à un calcul par nom (quand ils sont en lignes ou colonnes)
revenueTable = table.Calculations["REVENUE"]
marginTable = table.Calculations["MARGIN"]

# Accès à un calcul par indice
firstCalc = table.Calculations[1]

# Liste des noms de calculs
calcNames = table.Calculations.Names
```

### Calculs en cellules

Lorsque les calculs sont placés dans les cellules, chaque cellule peut contenir plusieurs sous-cellules, une par calcul.

```python
# Déclarer des calculs en cellules avec un nom par défaut
table.AssumeInCellsCalculation("VALUE")

# Accéder aux sous-cellules
foreach cell in table.Cells:
    if cell.HasSubCells:
        valueCalc = cell.SubCells["VALUE"].Content
        cell.SubCells["VALUE"].Bold = True  # Mise en forme
```

### Opérations entre tables avec calculs

```python
# Addition de tables
sumTable = table1.CalcSumWith(table2)

# Division (par exemple pour calculer des pourcentages)
percentTable = marginTable.CalcDivisionWith(revenueTable)

# Autres opérations disponibles
minTable = table1.CalcMinWith(table2)
avgTable = table1.CalcMeanWith(table2, table3)
```

## 9. Exemples pratiques

### Exemple 1 : Construction et manipulation d'une table de ventes

```python
# Création d'une table avec entêtes
salesTable = HTTable.Create(["Q1", "Q2", "Q3", "Q4"], ["Product A", "Product B", "Product C"])

# Modification des valeurs
for r in range(1, 5):  # Lignes (trimestres)
    for c in range(1, 4):  # Colonnes (produits)
        salesTable.SetAt(r, c, r * c * 100)  # Valeurs de vente fictives

# Ajout d'un niveau d'entête pour grouper les produits
salesTable = salesTable.ColumnsDimension.PrependLevel(["Hardware", "Hardware", "Software"])

# Ajout d'une ligne de total
salesTable = salesTable.Rows.AppendTotal()

# Extraction d'une sous-table pour l'analyse
hardwareData = salesTable.Columns["Hardware"].Extract()
```

### Exemple 2 : Analyse multidimensionnelle

```python
# Table de départ avec dimensions Région > Pays et Année > Trimestre
salesData = HTTable.FromFile("sales_data.xlsx")

# Réorganisation des entêtes pour placer Année au plus haut
newDimOrder = salesData.ColumnsDimension.ReorganizeHeader(2, 1, -1)  # Année, Région, Trimestre

# Extraction des données européennes de 2022
europe2022 = newDimOrder.Columns["2022"].Columns["Europe*"].Extract()

# Ajout d'une colonne de croissance (%)
withGrowth = europe2022.Columns.AppendHeader("Growth %")

# Calcul de la croissance (en utilisant les tables précédentes)
for r in range(1, europe2022.RowCount + 1):
    current = europe2022.GetAt(r, 2)  # Q2
    previous = europe2022.GetAt(r, 1)  # Q1
    growth = (current - previous) / previous * 100 if previous != 0 else 0
    withGrowth.SetAt(r, withGrowth.ColumnCount, growth)

# Tri des pays par croissance
sortedByGrowth = withGrowth.Rows.Sort("Growth %", ascendant=False)
```

### Exemple 3 : Utilisation des calculs et fusions

```python
# Création d'une table avec plusieurs calculs
revenueData = HTTable.Create(["Q1", "Q2", "Q3", "Q4"], ["US", "Europe", "Asia"])
costData = HTTable.Create(["Q1", "Q2", "Q3", "Q4"], ["US", "Europe", "Asia"])

# Remplissage avec des données
# [Code omis pour brevité]

# Fusion des tables avec annotations
financialTable = HTTable.MergeCalculations(
    [revenueData, costData],
    useSmartMerge=True,
    outputCalculations=AxisPlacement.InColumns
)

# Renommage des calculs
financialTable.Calculations.Names = ["REVENUE", "COST"]

# Calcul de la marge directement via une opération de table
marginTable = financialTable.Calculations["REVENUE"].CalcSubtractWith(
    financialTable.Calculations["COST"]
)

# Ajout du calcul de marge à la table principale
withMargin = HTTable.MergeCalculations(
    [financialTable, marginTable],
    outputCalculations=AxisPlacement.InColumns
)

# Extraction des données par région et calcul
usFinancials = withMargin.Columns["US"]
europeProfitability = withMargin.Columns["Europe"].Calculations["MARGIN"]
```