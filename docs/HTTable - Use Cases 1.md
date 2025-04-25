## Navigation et Accès aux Données

```python
# Exploration d'une table avec entêtes hiérarchiques
def ExploreTable(table):
    """Illustration des méthodes d'accès basiques d'une HTTable"""
    
    # Nombre de cellules dans le corps de la table
    tableSize = table.RowCount * table.ColumnCount
    
	# Nb niveaux d'entêtes colonnes / lignes
	nbhc = table.ColumnHeaderSize
	nbhr = table.RowHeaderSize
    
    # Accès aux textes d'entêtes
    columnsLabels = table.Columns.Texts
    rowsLabels = table.Rows.Texts
    
    # Accès au premier niveau de hiérarchie (racines)
    rootColumns = table.ColumnsDimension.Roots.Texts
    rootRows = table.RowsDimension.Roots.Texts
    
    # Accès par indice (positif depuis le début, négatif depuis la fin)
    firstColumn = table.Columns[1]
    lastColumn = table.Columns[-1]
    
    # Accès par nom
    specificColumn = table.Columns["FR"]
	
	# Le résultat comporte autant de lignes qu'il y a de lignes "TOTAL" dans table
    totalRows = table.Rows["TOTAL"]
    
    # Accès croisé (cellule spécifique)
    cell = table.Columns["FR"].Rows["TOTAL"]
    cellValue = cell.Value
    
    # Accès aux valeurs sous forme typée
    numbersInFirstColumn = table.Columns[1].Numbers
    textsInLastRow = table.Rows[-1].Texts
    
    return firstColumn, specificColumn
```

## 2. Extraction et Filtrage

```python
# Sélection et extraction de sous-parties d'une table
def ExtractData(salesTable):
    """Démontre différentes méthodes d'extraction et de filtrage"""
    
    # Extraction de colonnes spécifiques
    franceAndSpain = salesTable.Columns["FR", "ES"]
    
    # Extraction par motif/pattern
    europeanCountries = salesTable.Columns["EU*"]
    
    # Extraction sur le 1er niveau hiérarchique
    genderLevel = salesTable.Columns.Roots[1]
    
    # Extraction par position relative dans une hiérarchie
    # Select "$1" = premier élément sous chaque parent
    firstProductPerCategory = salesTable.Columns["$1"]
    
    # Suppression de colonnes
    withoutFirstColumn = salesTable.Columns.Remove(1)
    
    # Suppression de lignes vides
    withoutEmptyRows = salesTable.Rows.RemoveEmpty()
    
    return franceAndSpain, highValues
```

## Manipulation des Dimensions

```python
# Réorganisation et manipulation des dimensions
def ReshapeTable(table):
    """Montre comment manipuler la structure des dimensions"""
    
    # Transposition (lignes ↔ colonnes)
    transposed = table.Transpose()
    
    # Inversion d'un ordre de dimension ou d'axe
    reversedColumns = table.Columns.Reverse()
    
    # Réorganisation de la hiérarchie des entêtes
    # Les racines (niveau 1) deviennent des feuilles (-1)
    reorganized = table.ColumnsDimension.ReorganizeHeader(-1, 1)
    
    # Déclaration d'un axe personnalisé (alias)
    table.DeclareCustomAxis("COUNTRIES", "R", TableDirections.Vertical)
    
    # Utilisation de l'axe personnalisé
    franceData = table.Axes["COUNTRIES"]["FR"]
    
    # Reshaping (modification profonde de la structure)
    reshaped = table.ReShape(["V1", "H2"], ["H1"])
    
    # Déplacement d'éléments
    withTotalOnTop = table.Rows.MoveToTop("TOTAL")
    
    return True
```

## Fusion et Agrégation

```python
# Fusion et combinaison de tables
def MergeTables(table1, table2):
    """Démontre les opérations de fusion et d'agrégation"""
    
    # Fusion horizontale (ajout de colonnes)
	# "True" pour faire un "SmartMerge" qui identifie les colonnes selon leur texte
	# "False" pour faire une fusion naïve : les tables sont déjà cohérentes
    mergedColumns = HTTable.MergeColumns([table1, table2], True)
    
    # Fusion verticale (ajout de lignes)
	# "True" pour faire un "SmartMerge" qui identifie les colonnes selon leur texte
    # "False" pour faire une fusion naïve : les tables sont déjà cohérentes
    mergedRows = HTTable.MergeRows([table1, table2], True)
    
    # Fusion de calculs (combinaison de mesures)
    # "True" pour faire un "SmartMerge" qui identifie les lignes et les colonnes selon leur texte
	# "False" pour faire une fusion naïve : les tables sont déjà cohérentes
    mergedCalcs = HTTable.MergeCalculations([table1, table2], True)
    
	# Ajoute une ligne "TOTAL" qui calcule la somme des lignes pour chaque colonne 
    withTotal = table1.Rows.AppendTotal("TOTAL")
    
    # Ajoute une colonne "TOTAL" qui calcule la somme des colonne pour chaque ligne
    withTotalColumn = table1.Columns.AppendTotal("TOTAL")    
    
    return True
```

## Découpe de tables (Split) : pour boucler sur les lignes/les colonnes

```python
# Découpe / Split
def SplitTable(table):
    """Démontre les opérations de découpe"""

	# Retourne une table extraite par ligne
    splittedRows = table.Rows.Split()
	
	# Boucle sur chaque ligne de la table	
	for splittedRow in splittedRows:
		# Calcul la valeur maximale de la ligne
		maxi = max(splittedRow.Numbers)
    
    # Division d'une table par délimiteurs : chaque colonne "TOTAL" marquera le début d'une table
    parts = table.Columns.SplitByDelimiters("TOTAL")
    
    # Division en une partie de 2 lignes et une partie de 3 lignes
    pages = table.Rows.SplitBySizes([2, 3])
	
	# Découpe table en 4 parties, aux positions 5, 7, et 11 
    parts = table.Rows.SplitByPositions([5, 7, 11])
	
	return True
```



