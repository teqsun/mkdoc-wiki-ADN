# Juxtol

## JUSCOL FUNCTION

The function ** juxtol ** juxtaposes the variables in arguments on the dimension of the columns.

The variable that do not have columns are automatically adapted.& Nbsp;

& nbsp;

IMPORTANT: The modalities of the resulting variable obey the principle of the harmonization of dimensions.

& nbsp;

It is therefore always possible to juxtapose any variables on the columns: the function is responsible for harmonizing everything if necessary.

& nbsp;

The Juxcol Function is the Equivalent of the Juxrow Function on the Dimension of the Lines.

### Syntax: & nbsp;

\ _Juxcol (selection)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| & nbsp; | selection | selection of variables | Expression of selection of variables (ex: '$ "s?"') or list of variables separated by a ";"; ";"| Compulsory |

### EXAMPLES:

\ _JUXCOL (Q1: Q2: Q3)

\ _Juxcol ("Q \*")

#### Noticed :

In the case of juxtaposition of Several Simple Variables, the Columns Items Recover a wording constituted by the variable part of the title of variables of origins.while the common part Becomes the title of the & nbsp;

New variable.

To juxtapossa variables without too into account the wording, it is necessary to use the functions [notxt] (<notxt1.md>), clrcol or clrrow must beforehand.

& nbsp;

See also: & nbsp;

[Dimensions management] (<GERERLESDIMENSESDESSEDAIRAIBLE1.MD>)

[Combination the variables] (<combination thevariables1.md>)