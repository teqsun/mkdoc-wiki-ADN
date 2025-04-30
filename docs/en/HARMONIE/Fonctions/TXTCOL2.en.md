# Txtcol

## TXTCOL Function

The function ** txtcol ** modifies the text of one or more 'columns' (dimension 1) of the variable.

This method is useful for modifying a particular text While Letting the Engine Manage Other Texts Useful.

### Syntax: & nbsp;

Q01.txtcol (Key; Value; Delimiter)

Gold

\ _Txtcol (Q01; Key; Value; Delimiter)

& nbsp;

|& nbsp;|** Name ** |** Type ** |** Description ** |** Note ** |
|--- |--- |--- |--- |--- |
|&#49;|Key |Character chain |Assigned positions |Compulsory |
|&#50;|Value |Character chain |Associated chain1; Associated chain2 |chain; default chain2 |
|&#51;|DELIMITE |Character chain |;|Different by default |

### EXAMPLES:

It is possible to use variable annotations to modify the texts of the items, in this example, the labels of the items are enriched with the annotation \ [Title \]:

Q02c.txtcol ("\*"; "\ [Title \] - #")

& nbsp;

See also: & nbsp;

[Management dimensions] (<reurlesdimensesdesdesdairaible1.md>)

[Labels Management] (<GERERLIBELSLIBALESTHESTEXTES1.MD>)