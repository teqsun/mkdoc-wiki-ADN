# Txtcol

## TXTCOL Function

The Function ** TXTCOL ** Modifies the text of one or more 'columns' (dimension 1) of the variable.

This method is useful for modifying a particular text While Letting the Engine Manage Other Texts Useful.

### Syntax: & nbsp;

Q01.txtcol (Key; Value; Delimiter)

Gold

\ _Txtcol (Q01; Key; Value; Delimiter)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| &#49; | Key | Character Chain | Assigned Positions | Compulsory |
| &#50; | Value | Character Chain | Associated Chain1;Associated Chain2 | Chain;Default Chain2 |
| &#51; | Delimite | Character Chain |; | Different by Default |

### EXAMPLES:

It is possible to use variable annotations to modify the texts of the items, in this example, the labels of the items are enriched with the annotation \ [title \]:

Q02c.txtcol ("\*"; "\ [Title \] - #")

& nbsp;

See also: & nbsp;

[Management dimensions] (<reurlesdimensesdesdesdairaible1.md>)

[Labels Management] (<GERERLIBELSLIBALESTHESTEXTES1.MD>)