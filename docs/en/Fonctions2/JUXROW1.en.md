# Juxrow

## JUXROW function

The Function ** Juxrow ** juxtapos The variables in arguments on the dimension of the lines.& Nbsp;

The variable that do not have lines are automatically adapted.& Nbsp;

& nbsp;

IMPORTANT: The modalities of the resulting variable obey the principle of the harmonization of dimensions.

& nbsp;

It is there is possible to juxtapose any variables on the lines: The Function is responsible for harmonizing Everything if necessary.

& nbsp;

The Juxrow Function is the Equivalent of the Juxcol Function on the Dimension of the Columns.

### Syntax: & nbsp;

\ _JUXROW (selection)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| & nbsp; | selection | selection of variables | Expression of selection of variables (ex: '$ "s?"') or list of variables separated by a ";"; ";"| Compulsory |

### EXAMPLES:

\ _JUXROW (Q1: Q2: Q3)

\ _JUXROW ("Q \*")

#### notice:

A variable having a line dimension has a column dimension.

In Other Words, Only A Doubly Dimensioned Variable has lines and columns.a Simplely Dimensioned Variable Never has lines.& Nbsp;

In the case of juxtaposition of several simple valids, the columns items recover a wording constituted by the variable part of the title of variables of origins.While the common part becomes the title of the & nbsp;

New variable.

To juxtapossa variables without too into account the wording, it is necessary to use the functions [notxt] (<notxt1.md>), clrcol or clrrow must beforehand.

See also: & nbsp;

[Dimensions management] (<GERERLESDIMENSESDESSEDAIRAIBLE1.MD>)

[Combination the variables] (<combination thevariables1.md>)