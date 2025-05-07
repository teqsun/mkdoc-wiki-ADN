# Styles and cells

## Introduction

A style is a set of visual properties that define the appearance of the elements in your application.In this system, styles can be applied to individual cells, cells of cells, lines or columns of data tables, thus allowing a rich and consistent formatting of the information presented.

Styles are particularly useful for:
- highlight important information
- Visually differentiate different types of data
- Improve the readability of results tables
- Create professional relationships with a coherent formatting
- Apply conditional formatages based on data values

This document provides concrete examples to help you understand how to effectively use the styles system in your applications.

## Part 1: Styles

### Creation and manipulation of styles

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

### Styles with complex borders

`` python
# Creation of a simple border (identical on all sides)
Simple Border = Border (Penstyle (Penweight.medium, Color (0, 0, 0))) # Black average border everywhere

Style = Style ()
style.border = simple cover

# Creation of a border with different sides
Leftright = Penstyle (Penweight.thin, Color (0, 0, 0)) # fine black border
Topbottom = Penstyle (Penweight.medium, Color (0, 0, 0)) # Medium black border

Complexborder = Border (Left Right, Top Bottom, Left Right, Topbottom) # Order: Left, High, Right, Bas

complexstyle = style ()
complexstyle.border = Complexborder
`` `

## Part 2: cells

A cell is the fundamental unit for displaying and storing data in this system.It associates a value (content) with a visual style which defines its appearance.Data tables are generally composed of modifiable cells organized in lines and columns.

Each cell can contain different types of data (text, numbers, dates, etc.) and has its own formatting properties.This combination makes it possible to create rich and informative visualizations where the data and their visual presentation work together to transmit information optimally.

The cells can also be grouped into collections to apply styles common to several elements, thus simplifying the management of large data sets.

### Ceal creation and manipulation

`` python
# Creation of a cell with text
textcell = cell ("example text")

# Creation of a cell with a number
Numbercell = Cell (42.5)
Numbercell.format = "#, ## 0.00"
Numbercell. horizontalalignment = horizontalalignment.right

# Cell with advanced formatting
formattedcell = cell ("important")
formattedcell.bold = True
Formattedcell.Foreground = Color (255, 0, 0) # Red
formattedcell.background = color (255, 255, 200) # pale yellow
Formattedcell.border = Border (Penstyle (Penweight.thin, Color (0, 0, 0)))))
`` `

### Application of styles to cells

`` python
# Creation of a style
Style = Style ()
Style.fontname = "Calibri"
Style.Fontsize = 11
style.Bold = True
style.Foreground = color (0, 80, 120) # dark blue

# Application of style to a cell
cell = cell ("text with style")
Cell.Applystyle (style, true) # True = replace the existing style

# Fusion of a style with the existing style of a cell
Existing cell = cell ("existing style")
Existingcell.bold = True

Additionalstyle = style ()
Additionalstyle.Italic = True
Additionalstyle.Foreground = color (0, 100, 0) # dark green

Existingcell.Applystyle (Additionalstyle, False) # False = Merge with the existing style
`` `

## Part 3: Glyphs

Glyphs are additional graphic elements that can be attached to a cell to enrich the information it presents.A glyph combines content (text or symbol) with its own style, regardless of the main style of the cell.

Glyphs are particularly useful for:
- Indicate trends (↑ or ↓ to show an evolution)
- Display variations (growth or decrease percentages)
- draw attention to certain values ​​(asterisks, alert symbols)
- Add contextual information (units, statutes, annotations)
- Create visual indicators without modifying the main value

For example, in a financial table, a cell could display "1250" as a main value, accompanied by a glyph "↑ +15%" in green to indicate an increase compared to the previous period.The glyphs thus make it possible to considerably enrich the information presented in the cells without overloading their main content.

### Cells with glyphs

`` python
# Creation of a cell with a value
Cell = Cell (12500)
Cell.Format = "#, ## 0"

# Addition of a glyph to indicate an increase
Uparrowstyle = style ()
Uparrowstyle.Foreground = color (0, 128, 0) # green
Cell.addglyph ("↑", Uparrowstyle)

# Addition of a percentage as a second glyph
percentstyle = style ()
percentstyle.Foreground = color (0, 128, 0) # green
percentstyle.Bold = True
Cell.addglyph ("+15%", percentstyle)
`` `

## Part 4: Cell collections

The cell collections make it possible to simultaneously handle several cells, considerably simplifying work on data sets.They are based on the `abstractcellcollection 'class which provides common methods and properties to interact with groups of cells.

These collections offer you the possibility of:
- Apply a unique style to several cells in a single operation
- Work on specific subsets of a data table (lines, columns, zones)
- Change the values ​​or formats of a group of cells
- effectively manage the formatting of large volumes of data

For example, you can access the cells of a column header (`table.columns.cells`), a specific line (` table.rows ["Total"]. Cells`), or even at a precise intersection (`table.columns [1, 2] .rows [" Total "]. Cells`).This flexibility allows you to exactly target the cells you want to modify, making your code more readable and more efficient.

The style properties applied to a collection are automatically propagated to all the cells contained in this collection, which makes it possible to maintain visual coherence without having to manipulate each cell individually.

### Formatting a group of cells

`` python
# In this example, 'Cells' is a collection of cells (e.g. obtained via t.cells)
Cells.bold = True # Put all the cells in bold
cells.Foreground = color (0, 0, 128) # text in dark blue
Cells.format = "#, ## 0.00"#Format all numbers
`` `

### Borders on lines and columns

`` python
# Application of a border on column headers
Headerrow = table.columns.cells
Headerrow.border = Border (Penstyle (Penweight.thick, Color (0, 0, 0)))))
Headerrow.BackGround = Color (240, 240, 240)
Headerrow.bold = True

# Fine border on all cells of a line
Datarow = table.rows ["Total"]. Cells
Datarow.border = Border (Penstyle (Penweight.thin, Color (0, 0, 0)))))
Datarow.Background = Color (255, 250, 205) # pale yellow
`` `

## Part 5: compound cells (advanced use)

Compound cells represent an advanced but essential concept in work with complex data tables.A composed cell contains several under-cells, each with its own content and style.

### Architectural choice: Calculations in Vs Calculation cells in lines/columns

The system offers two approaches to manage the calculations and the organization of the data:

1. **Traditional approach**: Calculations are presented at lines or columns, and cells simply contain the resulting values.This approach is more appropriate in most cases.

2. **Approach by compound cells**: the calculations are integrated into the cells themselves via the Sous-Celles.Advantages: fusion of complex tables, visual simplification, complex calculations between several calculations.

The choice between these two approaches depends on your specific use case.It is also possible to combine both approaches in different parts of the same application.

### Structure et fonctionnement

A compound cell uses the subcells' property which is a collection of girls cells.Each sub-cell has:
- its own content
- His own style
- a group identifier (Group) to find it easily

### Access to the Sommelules

In the vast majority of cases, you will simply access the existing sub-cells to read their information or modify their content and style:

`` python
# Access to the Sous-Celles by name
Cell.subcells ["value"]. Content = 125000
Cell.subcells ["value"]. Format = "#,##"
Cell.subcells ["evolution"]. Foreground = color (0, 128, 0) # green
Cell.subcells ["evolution"]. Bold = True

# Access to the Sous-Celles by index
cell.subcells [0] .Fontsize = 12
Cell.subcells [1]. horizontalalignment = horizontalalignment.right
`` `

This approach makes it possible to work effectively with complex cells without having to understand the underlying mechanisms of creation and arrangement of the Sous-Celles.

### Typical use

A common use case is to browse the cells of a table to apply conditionally to the styles to the sub-cells as a function of values ​​present in other sub-cells:

`` python
# Application of a conditional style based on the values ​​of another under-cell
For cell in table.Cells:
# Verification if the "test" in-that contains "+"
If Cell.subcells ["Test"]. Content.assring (). Contains ("+"):
# Application of a style to the "Value" Sub-Celule
Cell.subcells ["value"]. Foreground = color (0, 128, 0) # green
Cell.subcells ["value"]. Bold = True
Else:
# Different style if not fulfilled condition
Cell.subcells ["value"]. Foreground = Color (255, 0, 0) # Red
`` `

This approach makes it possible to create rich conditional visualizations where the appearance of a part of the cell depends on the value of another part.