# Documentation HTTable

## 1. Introduction

HTTable est une structure de données avancée pour manipuler des tableaux comportant des entêtes hiérarchiques en lignes et colonnes. Elle facilite l'analyse et la transformation de données tabulaires complexes.

### Structure fondamentale

Une HTTable comporte trois parties principales :

1. ** Starts ** - Hierarchical and multi -level:
- column headers (horizontal)
- Streets (vertical)

2. **Corps du tableau** - Contient les données effectives

3. ** Annotations ** - Metadata associated with the table

### Terminologie essentielle

- **Axe** : Ensemble d'éléments organisés selon une direction (ligne ou colonne)
- **Niveau** : Ligne ou colonne spécifique dans une dimension (un niveau d'entête)
- **Dimension** : Regroupe tous les niveaux de hiérarchie dans une direction (lignes ou colonnes)
- **Calcul** : Valeur dérivée pouvant être placée dans différentes parties de la table
- **Cellule** : Unité fondamentale de stockage des données

## 3. Concepts structurels

### Hiérarchie des concepts

`` `
Httable
├ Columnsdimension (all levels of column headers)
│ └ Columns (dimension leaves)
├ ROWSDIMENSION (all levels of line entests)
│ └ └ ROWS (dimension leaves)
├ ─ Calculation (can be in lines, columns or cells)
├ ─ Annotations (metadata)
└ Body (body of the table)
`` `

### Axes and dimensions

La structure d'une HTTable s'articule autour de plusieurs axes et dimensions :

```python
# Dimensions (regroupent tous les niveaux hiérarchiques)
colDim = table.ColumnsDimension  # Tous les niveaux d'entêtes de colonnes
rowDim = table.RowsDimension     # Tous les niveaux d'entêtes de lignes

# Axes des feuilles (niveau le plus bas de la hiérarchie)
cols = table.Columns  # Accès simplifié aux colonnes du corps
rows = table.Rows     # Accès simplifié aux lignes du corps

# Calculations (placed in lines, columns or cells)
Calcs = Table.Calulations
`` `

### dimensions levels

Les dimensions contiennent plusieurs niveaux, qui représentent les différentes couches de la hiérarchie :

`` python
# Access to the levels of a dimension (origin 1)
Level1 = Coldim.levels [1] # First level (root)
Level2 = Coldim.levels [2] # Second level
Leaflevel = COLDIM.Leaves # Last level (leaves)

# Access with negative indexing
rootlevel = rowdim.rooots # first level (equivalent to levels [1])
subtitlelevel = rowdim.subtitles # penultimate level
`` `

### Entêtes

Starts define the structure and organize the data:

```python
# Accès aux entêtes
colHeader = table.ColumnsHeader
rowHeader = table.RowsHeader

# Number of levels in headers
Coloaderlevel = table.columnheadersize
Rowheaderlevel = table.rowheadersize
`` `

### Body

Le corps contient les données sans les entêtes :

```python
# Accès au corps (table sans les entêtes)
body = table.Body

# Body sizes
BodyROWCOUNT = TABLE.ROWCOUNT
bodycolcount = table.columncount

# Full table sizes (with headers)
TableRowcount = table.TableRowCount
COLCUNENT table = table.Tablecolumncount
`` `

## 4. Access to data

### Accès par axes et dimensions

Access to data via axes is the main way to handle a httable.** IMPORTANT **: These operations return a httable which references the parent table, thus making it possible to read and modify the data in a sub-part of the original table:

`` python
# Access to a column (returns a httable linked to the parent table)
Firstcol = table.columns [1] # First column
collans_c = table.columns ["a", "b", "c"] # selection by names

# Access to a line (returns a httable linked to the parent table)
Secondrow = table.rows [2] # second line
totalsrow = table.rows ["total"] # selection by name

# Access to a specific level in a dimension
Prodcategories = table.columnsdimension.levels [1] # First level of column headers
Monthlevel = table.rowsdimension.levels [2] # Second level of headlight headers

# Access to elements of a specific level
Categorynamas = Prodcategories.Texts # Texts of the first level of column headers
MONTHNAMES = MONTHLEvel.Texts # Texts of the second level of headlight headers

# Modification via view (affects the parent table)
Firstcol.setat (1, 1, "new value") # modifies the first cell of the first column
`` `

### Accès par croisement d'axes

Axes crossroads provide access to specific areas:

`` python
# Selection of a cell by co -considerment
Cell = table.rows [3] .columns [2]

# Selection of an area
Quarterdata = Table.rows ["Q1"]. Columns ["Product A", "Product B"]

# Selection with a specific calculation
Returnsforq1 = table.rows ["q1"]. Calculations ["returned"]
`` `

### Access and modification of values

Htable offers several ways to access and modify values ​​according to areas (body, headers) and data types.

#### Access to values

`` python
# Access to the raw values ​​of the body
Colvalues ​​= table.columns [1]. Valuces # All the values ​​of the first column
ROWVALUES = TABLE.ROWS [2]. Values ​​# All the values ​​of the second line
Cellvalue = table.columns [1] .rows [3]. Value # value at the intersection

# Type access to digital values
colnumbers = table.columns ["returned"]. Numbers # as doubles
ROWINTEGERS = TABLE.ROWS ["Count"]. Integers # as a party

# Access to texts (automatic conversion to channels)
coltexts = table.columns [1] .Texts # body texts
HeaderText = table.columns.Text # Texts of the header of the columns (Leaves level)
LevelText = table.columnsDimension.Levels [1]. Texts # texts of a specific header level
`` `

#### Modification of values

The modification of the values ​​depends on the targeted zone (body or headers):

`` python
# Modification of the body of the table
table.columns [1] .rows [2] .Value = 42 # modifies a specific cell of the body
table.columns ["Q1", "Q2"]. Value = 0 # Sets zero all the cells of columns Q1 and Q2

# Modification of headers
table.columns.VALUE = "quarter" # Modifies the text of the header of the columns (Leaves level)
table.Texts.Texts = ["A", "B", "C"] # Modifies the texts of the Start of the lines (Leaves level)
table.columnsdimension.levels [1] .Value = "year" # modifies a specific header level

# Distribution de valeurs multiples
table.Columns[1].Values = [10, 20, 30, 40]  # Affecte ces valeurs aux 4 premières lignes 
table.Rows["Total"].Values = [100, 200, 300]  # Affecte ces valeurs aux 3 premières colonnes

# Pour les grandes sélections, les valeurs se répètent si la collection est plus petite
table.Columns["Q1", "Q2", "Q3", "Q4"].Values = [0, 1]  # Affecte alternativement 0 et 1
```

#### Cell manipulation (style + value)

The cells allow access and modify both the values ​​and their formatting:

`` python
# Access to cells
colcells = table.columns ["income"]. Cells # collection of cells
firstcell = table.columns [1] .rows [1] .cell # a specific cell

# Modification of content and style
Cell = table.columns [1] .rows [2] .cell
Cell.content = "new content" # Value of the cell
Cell.bold = True # Gras
Cell.italic = True # Italic
Cell.Foreground = color.red # text color
Cell.Background = color.LightGray # background color
Cell.Format = "#, ## 0.00"#Display format (Numbers)
Cell. horizontalagly = horizontalalignment.right # alignment

# Creation of a formatted cell
formattedcell = cell ("significant value")
formattedcell.bold = True
formattedcell.Foreground = color.blue
table.columns [1] .rows [3] .cell = formattedcell
`` `

## 5. Manipulations of dimensions and axes

### Extraction and selection

`` python
# Extraction of a subtable from axes
Revenuebyquarter = table.columns ["Back"]. ROWS ["Q1", "Q2", "Q3", "Q4"]

# Extraction of a dimension level
Productlevel = table.columnsdimension.levels [1]. Exact ()

# Extraction of all columns corresponding to a pattern
Europecolumns = table.columns ["Europe*"] # Use patterns
`` `

### Addition and deletion

`` python
# Addition of a header level
TableWithNewheader = Table.Column Dimension.Append Level (["Cat 1", "CAT1", "CAT2", "CAT2"])

# Addition of a column (at the end)
tablewithnewcol = table.columns.Append ("new column")

# Addition of a line (at the beginning)
tablewithnewrow = table.rows.prepend ("new line")

# Suppression d'une colonne
tableWithoutFirstCol = table.Columns.Remove(1)

# Deletion of several lines
tablewithoutrows = table.rows.remove ("line a", "line c")
`` `

### Reorganization of headers

`` python
# Reorganization of a column header
# (positive = from root, negative = from sheets)
Newcolorder = table.columnsdimension.reorganizeheader (2, 1, -1) # Levels 2, 1, then leaves

# Resizing of a header (adds or deletes levels)
Threerowlevel = table.rowsdimension.resizeheader (3) # Force 3 Hell levels

# Complete rewriting of a header with different types of elements
Newheader = table.columnsdimension.rewriteheader ([
"Region", # Literal text
"*", # Keeps all existing levels
"[Name]" # annotation value
])

# Réécriture avec format
newHeader2 = table.ColumnsDimension.RewriteHeaderUsingFormat("-1;-2;\"EXTRA\"")
```

###

`` python
# Move items at the top
tablewithusfirst = table.columns.movetotop ("US")

# Move elements at the end
tablewithtotallast = table.rows.movetobottom ("Total")

# Move before/after
TableWithmoved = table.rows.move ("Q2", Movekinds.before) # Options: Before, After, First, Last
`` `

## 6. Advanced operations

### Table merger

`` python
# Horizontal merger (adds columns)
merged1 = htable.Mergecolumns (
[table1, table2],
USESMARTMERGE = TRUE,
Annotationskeys = ["source"]
))

# Vertical fusion (adds lines)
merged2 = htable.mergerows ([table1, table2])

# "Intelligent" fusion which first harmonizes the dimensions
Harmonizedables = htable.harmonize (Tabledirections. Vertical, [Table1, Table2])
mergedharmonized = httable.mergecolumns (harmonizedable)
`` `

### Tables cutting

`` python
# Dimension cutting
NORTHTABLE, SOUTHTABLE = TABLE.COLUMNS.SPLITBYDELIMITERS ("|")

# Device in equal parts (here in three parts)
shares = table.rows.splitbysizes ([5, 5, 5]) # 5 lines per part

# Advanced cutting respecting the hierarchy
pages = table.rowsdimension.advancedsplit (maxitemsperpage = 20, tolerance = 2)

# Values ​​cutting
Q1, Q2, Q3, Q4 = Table.rows.splitonvalues ​​("Quarter")
`` `

### Transposition

`` python
# Transform lines into columns and vice versa
transposition = table.transpose ()
`` `

### Aggregation

`` python
# Aggregation with SUM operation (Options: Sum, Count, Min, Max, etc.)
TOTALOW = TABLE.ROWS.AGGREGATE (aggregator.sum, aggregatormodes.last, "total")

# Addition of a total line
With Total Row = Table.rows.Append Total ()

# Fast discounts
SumTable = table.columns.sum ()
AVGTable = table.columns.mean ()
`` `

### Tri

`` python
# Sorting lines by a column
sortedbyrecomé = table.rows.sort (criteria = "back", ascendant = true)

# Advanced sorting respecting hierarchy
sortedhierarchy = table.rowsdimension.advancedsort (
Criteria = "Returned",
Ascendant = false,
Sortgroups = True
))
`` `

### Filter

`` python
# Extraction according to a condition
Positivevalues ​​= table.rows. extractive (lambda item: item.asdouble ()> 0)

# Suppression des éléments vides
nonEmptyTable = table.Columns.RemoveEmpty()

# Fast "where" style filter
filmedtable = table.Where ("country", "France")
MultiPilter = Table.Where (["Back", "Margin"], Value => Value> 1000, Any = True)
`` `

## 7. Manipulation of calculations

### Types of investments

Calculations can be positioned in different ways:

- ** Displacement.inrows **: line calculations
- ** Displacement.in columns **: column calculations
- ** axisplacement.cells **: calculations in cells
- ** axisplacement.none **: no calculation

`` python
# Check if the table has calculations
Hascalcs = table. Hascalulations

# Define the placement of calculations
table.

# Move calculations
table = table.Calulations.movetocells ()
Table = table.Calulations.moveto (axisplacement.Incolumns)
`` `

### Access to calculations

`` python
# Access to one name by name (when they are in lines or columns)
Returnable = table.
Margintable = table. Calulations ["Margin"]

# Accès à un calcul par indice
firstCalc = table.Calculations[1]

# List of calculation names
calcnams = table.calulations.names
`` `

### Cell calculations

When the calculations are placed in the cells, each cell can contain several sub-cells, one by calculation.

`` python
# Declare cell calculations with a default name
Table.

# Access the Sous-Celles
Foreach Cell in Table.Cells:
If Cell.Hassubcells:
valuecalc = cell.subcells ["value"]. Content
Cell.subcells ["value"]. Bold = True # formatting
`` `

### Operations between tables with calculations

`` python
# Addition of tables
SumTable = Table1.Calcsumwith (Table2)

# Division (for example to calculate percentages)
percentable = margintable.CalcdivisionWith (Revenible)

# Other operations available
MINTABLE = TABLE1.CALCMINWITH (TABLE2)
AVGTABLE = TABLE1.CALCMEANWITH (TABLE2, TABLE3)
`` `

## 9. Practical examples

### Example 1: Construction and manipulation of a sales table

`` python
# Creation of a table with headers
Salesable = htable.create (["Q1", "Q2", "Q3", "Q4"], ["Product A", "Product B", "Product C"])

# Modification of values
For R in Range (1, 5): # lines (quarters)
For C in Range (1, 4): # columns (products)
Salestable.setat (R, C, R * C * 100) # fictitious sales values

# Addition of a header level to group products
Salesable = Salestable.columnsDimension.Prependlevel (["Hardware", "Hardware", "Software"])))

# Addition of a total line
Salestable = Salestable.rows.Appendtotal ()

# Extraction of a subtable for analysis
hardwaredata = Salestable.columns ["Hardware"]. Extract ()
`` `

### Example 2: Multidimensional analysis

`` python
# Starting table with region dimensions> country and year> quarter
Salesdata = htable.fromfile ("Sales_data.xlsx")

# Reorganization of headers to place year at the highest
Newdimorder = Salesdata.columnsdimension.reorganizeheader (2, 1, -1) # year, region, quarter

# Extraction of European data from 2022
Europe2022 = newdimorder.columns ["2022"]. Columns ["Europe*"]. Extract ()

# Ajout d'une colonne de croissance (%)
withGrowth = europe2022.Columns.AppendHeader("Growth %")

# Calculation of growth (using previous tables)
For R in Range (1, Europe2022.rowcount + 1):
Current = Europe2022.Getat (R, 2) # Q2
Previous = Europe2022.Getat (R, 1) # Q1
Growth = (Current - Previous) / Previous * 100 If Previous! = 0 Else 0
Withgrowth.setat (R, withgrowth.columncount, Growth)

# Sorting from countries by growth
sortedbygrowth = withgrowth.rows.sort ("Growth %", ascendant = false)
`` `

### Example 3: Use of calculations and mergers

`` python
# Creation of a table with several calculations
Revenuedata = htable.create (["Q1", "Q2", "Q3", "Q4"], ["Us", "Europe", "Asia"])))
Costdata = htable.create (["Q1", "Q2", "Q3", "Q4"], ["US", "Europe", "Asia"])))

# Filling with data
# [Omitted code for btern]

# Fusion of tables with annotations
Financialable = htable.Mergecalulations (
[REVEREDATA, Costdata],
USESMARTMERGE = TRUE,
Outputcalulations = axisplacement.Incolumns
))

# Remiummn of calculations
Financialtable.Calulations.names = ["Return", "Cost"]

# Calculation of the margin directly via a table operation
Margintable = Financialtable.Calulations ["Revenue"]. Calcsubtractwith (
Financialtable.Calulations ["cost"]
))

# Addition of margin calculation to the main table
withMargin = htable.Mergecalulations (
[Financialtable, Margintable],
Outputcalulations = axisplacement.Incolumns
))

# Extraction des données par région et calcul
usFinancials = withMargin.Columns["US"]
europeProfitability = withMargin.Columns["Europe"].Calculations["MARGIN"]
```
