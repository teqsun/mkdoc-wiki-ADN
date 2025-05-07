# Juxrow

## JUXROW function

The function **juxrow** juxtaposes the variables in arguments on the dimension of the lines. & Nbsp;

The variables that do not have lines are automatically adapted. & Nbsp;

& nbsp;

IMPORTANT: The modalities of the resulting variable obey the principle of the harmonization of dimensions.

& nbsp;

It is therefore always possible to juxtapose any variables on the lines: the function is responsible for harmonizing everything if necessary.

& nbsp;

The juxrow function is the equivalent of the juxcol function on the dimension of the columns.

### Syntax: & nbsp;

\ _JUXROW (selection)

& nbsp;

|& nbsp;|**Name** |**Type** |**Description** |**Note** |
|--- |--- |--- |--- |--- |
|& nbsp;|Selection |Selection of variables |Expression of selection of variables (ex: '$ "s?"') Or list of variables separated by a ";"; "|Compulsory |


#### Examples:

\ _JUXROW (Q1: Q2: Q3)

\ _JUXROW ("Q \*")

#### notice:

A variable having a line dimension has a column dimension.

In other words, only a doubly dimensioned variable has lines and columns.A simply dimensioned variable never has lines. & Nbsp;

In the case of juxtaposition of several simple valids, the columns items recover a wording constituted by the variable part of the title of variables of origins.While the common part becomes the title of the & nbsp;

new variable.

To juxtapose variables without taking into account the wording, it is necessary to use the functions [notxt] (<notxt1.md>), clrcol or clrrow must beforehand.

See also: & nbsp;

[Management dimensions] (<reurlesdimensesdesdesdairaible1.md>)

[Combine the variables] (<combine thevariables1.md>)