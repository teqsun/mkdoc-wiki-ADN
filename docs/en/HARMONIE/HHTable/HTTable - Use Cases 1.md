## Navigation and access to data

`` python
# Exploration of a table with hierarchical heads
exploretable def (table):
"" "Illustration of basic access methods of a httable" ""

# Number of cells in the body of the table
tablesize = table.rowcount * table.columncount

# Nb column / lines headlamps
NBHC = table.columnheadersize
nbhr = table.rowheadersize

# Access to heading texts
columnslabels = table.columns.texts
ROWSLABELS = TABLE.ROWS.Texts

# Access to the first level of hierarchy (roots)
rootcolumns = table.columnsdimension.rooots.texts
rootrows = table.rowsdimension.rooots.texts

# Access by index (positive from the start, negative from the end)
firstcolumn = table.columns [1]
Lastcolumn = table.columns [-1]

# Name access
Specificcolumn = table.columns ["fr"]

# The result has as many lines as there are "total" lines in table
TOTALOWS = Table.rows ["Total"]

# Crossed access (specific cell)
Cell = table.columns ["fr"]. ROWS ["Total"]
Cellvalue = Cell.VALUE

# Access to values ​​in typical form
Numbersinfirstcolumn = table.columns [1].
textsinlastrow = table.rows [-1] .Texts

Return Firstcolumn, Specificcolumn
`` `

## 2. Extraction and filtering

`` python
# Selection and extraction of table sub-parts
DEF Extractdata (Salestable):
"" Demonstrates different methods of extraction and filtering "" "

# Specific column extraction
franceandpain = Salestable.columns ["FR", "ES"]

# Pattern extraction/pattern
EuropeanCountries = Salestable.columns ["EU*"]

# Extraction on the 1st hierarchical level
genderlevel = Salestable.columns.rooots [1]

# Extraction by relative position in a hierarchy
# Select "$ 1" = first element under each parent
FirstProductPercategory = Salestable.columns ["$ 1"]

# Deletion of columns
Withoutfirstcolumn = Salestable.columns.remove (1)

# Deletion of empty lines
Withoutemptyrows = Salestable.rows.removeempty ()

Return franceandspain, highvalues
`` `

## Manipulation of dimensions

`` python
# Reorganization and manipulation of dimensions
Def Reshapetable (table):
"" "Show how to manipulate the structure of the dimensions" ""

# Transposition (lines ↔ columns)
transposition = table.transpose ()

# Inversion of an order of dimension or axis
Reversedcolumns = table.columns.reverse ()

# Reorganization of the Stout Hierarchy
# Roots (level 1) become leaves (-1)
Reorganized = table.columnsdimension.reorganizeheader (-1, 1)

# Declaration of a personalized axis (alias)
Table.Declarecustomaxis ("Countries", "R", Tabledirections. Vertical)

# Use of the personalized axis
francedata = table.Axes ["Countries"] ["Fr"]

# Reshaping (deep modification of the structure)
reshaped = table.reshape (["v1", "h2"], ["h1"])

# Moving elements
withtotalontop = table.rows.movetotop ("Total")

Return True
`` `

## Fusion and aggregation

`` python
# Fusion and combination of tables
Def Mergetables (table1, table2):
"" Demonstrates the "" "" "" "" melting and aggregation operations

# Horizontal merger (addition of columns)
# "True" to make a "smartmerge" which identifies the columns according to their text
# "False" to make a naive merger: the tables are already consistent
mergedcolumns = httable.mergecolumns ([table1, table2], true)

# Vertical fusion (addition of lines)
# "True" to make a "smartmerge" which identifies the columns according to their text
# "False" to make a naive merger: the tables are already consistent
mergedrows = httable.mergerows ([table1, table2], true)

# Fusion of calculations (combination of measures)
# "True" to make a "smartmerge" that identifies the lines and columns according to their text
# "False" to make a naive merger: the tables are already consistent
mergedcalcs = htable.Mergecalulations ([table1, table2], true)

# Add a "total" line that calculates the sum of the lines for each column
withtotal = table1.rows.amendtotal ("total")

# Add a "total" column that calculates the sum of the column for each line
withtotalcolumn = table1.columns.Appendtotal ("total")

Return True
`` `

## Table cutting (split): to complete on the lines/columns

`` python
# Cutout / Split
Def splittable (table):
"" Demonstrates the cutting operations "" ""

# Return a table extracted by line
Splittedrows = table.rows.split ()

# Loop on each line of the table
For Splittedrow in Splittedrows:
# Calculation The maximum line value
Maxi = max (Splittedrow.Numbers)

# Division of a table by delimitors: each column "Total" will mark the start of a table
shares = table.columns.splitbyDeLimiters ("Total")

# Division in a part of 2 lines and a part of 3 lines
pages = table.rows.splitbysizes ([2, 3])

# Cutting table in 4 parts, in positions 5, 7, and 11
shares = table.rows.splitbyPositions ([5, 7, 11])

Return True
`` `



