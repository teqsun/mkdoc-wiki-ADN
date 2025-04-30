## Navigation and access to data

`` python
# Exploration of A Table With Hierarchical Heads
Exploreable DEF (table):
"" Illustration of Basic Access Methods of A Htable "" "

# Number of Cells in the body of the table
tablesize = table.rowcount * table.columncount

# NB column / Lines Headlamps
NBHC = table.columnheadersize
nbhr = table.rowheadersize

# Access to Heading Texts
columnslabels = table.columns.texts
ROWSLABELS = TABLE.ROWS.Texts

# Access to the First Level of Hierarchy (Roots)
rootcolumns = table.columnsdimension.rooots.texts
rootrows = table.rowsdimension.rooots.texts

# Access by index (positive from the start, Negative from the end)
firstcolumn = table.columns [1]
Lastcolumn = table.columns [-1]

# Name Access
Specificcolumn = table.columns ["fr"]

# The Result has as many lines as there are "total" lines in table
Totalows = table.rows ["Total"]

# Crossed Access (specific cell)
Cell = table.columns ["fr"].ROWS ["Total"]
Cellvalue = Cell.VALUE

# Access to Values ​​in Typical Form
Numbersinfirstcolumn = table.columns [1].
textsinlastrow = table.rows [-1] .Texts

Return Firstcolumn, Specificcolumn
`` `

## 2. Extraction and filtering

`` python
# Selection and extraction of Sub-Party Table
DEF Extractdata (Salestable):
"" Demonstrates Different Methods of Extraction and Filtering "" "

# Specific column extraction
franceandpain = Salestable.columns ["Fr", "es"]

# Extraction/pattern pattern
EuropeanCountries = Salestable.columns ["EU*"]

# Extraction on the 1st hierarchical level
genderlevel = Salestable.columns.rooots [1]

# Extraction by relative position in a hierarchy
# Select "$ 1" = First Element Under Each Parent
FirstProductPercategory = Salestable.columns ["$ 1"]

# Deletion of columns
Withoutfirstcolumn = Salestable.columns.remove (1)

# Deletion of Empty Lines
Withoutemptyrows = Salestable.rows.removeempty ()

Return franceandspain, highvalues
`` `

## Manipulation of Dimensions

`` python
# Reorganization and Manipulation of Dimensions
Def Reshapetable (table):
"" "Show How to manipulate the structure of the dimensions" ""

# Transposition (Lines ↔ Columns)
transposition = table.transposes ()

# Inversion of an order of dimension or axis
Reversedcolumns = table.columns.reverse ()

# Reorganization of the Stout Hierarchy
# Roots (Level 1) Become Leaves (-1)
Reorganized = table.columnsdimension.reorganizeheader (-1, 1)

# Declaration of A Personalized Axis (alias)
Table.Declarecustomaxis ("Countries", "R", tabledirections. Vertical)

# Use of the Personalized Axis
francedata = table.Axes ["Countries"] ["Fr"]

# Reshaping (Deep Modification of the Structure)
reshaped = table.reshape (["v1", "h2"], ["h1"])

# Moving Elements
withtotalontop = table.rows.movetotop ("Total")

Return True
`` `

## Fusion and aggregation

`` python
# Fusion and Combination of Tables
Def Mergetables (table1, table2):
"" Demonstrates the "" "" "" "melting and aggregation operations

# Horizontal Merger (Addition of Columns)
# "True" to make a "smartmerge" which identifies the columns according to their text
# "False" to make a naive merger: the table are already consist
mergedcolumns = httable.mergecolumns ([table1, table2], true)

# Vertical Fusion (Addition of Lines)
# "True" to make a "smartmerge" which identifies the columns according to their text
# "False" to make a naive merger: the table are already consist
mergedrows = httable.mergerows ([table1, table2], true)

# Fusion of Calculations (Combination of Measures)
# "True" to make a "smartmerge" that identified the lines and columns according to their text
# "False" to make a naive merger: the table are already consist
mergedcalcs = htable.Mergecallations ([table1, table2], true)

# Add a "Total" Line that calculates The Sum of the Lines for Each Column
withtotal = table1.rows.amendtotal ("total")

# Add a "Total" column that calculates the sum of the column for each line
withtotalcolumn = table1.columns.Appendtotal ("total")

Return True
`` `

## Table Cutting (split): to complete on the lines/columns

`` python
# Cutout / Split
Def splittable (table):
"" Demonstrates the Cutting Operations "" ""

# Return A Table Extracted by Line
Splittedrows = table.rows.split ()

# Loop on each line of the table
For Splittedrow in Splittedrows:
# Calculation The Maximum Line Value
Maxi = max (Splittedrow.Numbers)

# Division of A Table by Delimitors: Each Column "Total" Will Mark the Start of A Table
Shares = table.columns.splitbydelimiters ("Total")

# Division in a part of 2 lines and a part of 3 lines
pages = table.rows.splitbysizes ([2, 3])

# Cutting Table in 4 parts, in positions 5, 7, and 11
shares = table.rows.splitbypositions ([5, 7, 11])

Return True
`` `