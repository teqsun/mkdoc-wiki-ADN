# Juxtol

## JUXCOL function

The function ** juxtol ** juxtaposes the variables in arguments on the dimension of the columns.

The variables that do not have columns are automatically adapted. & Nbsp;

& nbsp;

IMPORTANT: The modalities of the resulting variable obey the principle of the harmonization of dimensions.

& nbsp;

It is therefore always possible to juxtapose any variables on the columns: the function is responsible for harmonizing everything if necessary.

& nbsp;

The Juxcol Function is the Equivalent of the Juxrow Function on the Dimension of the Lines.

### Syntax: & nbsp;

\ _Juxcol (selection)

& nbsp;

|& nbsp;|** Name ** |** Type ** |** Description ** |** Note ** |
|--- |--- |--- |--- |--- |
|& nbsp;|Selection |Selection of variables |Expression of selection of variables (ex: '$ "s?"') Or list of variables separated by a ";"; "|Compulsory |


#### Examples:

\ _JUXCOL (Q1: Q2: Q3)

\ _Juxcol ("Q \*")

#### Noticed :

In the case of juxtaposition of several simple variables, the columns items recover a wording constituted by the variable part of the title of variables of origins.While the common part becomes the title of the & nbsp;

new variable.

To juxtapose variables without taking into account the wording, it is necessary to use the functions [notxt] (<notxt1.md>), clrcol or clrrow must beforehand.

& nbsp;

See also: & nbsp;

[Dimensions management] (<GERERLESDIMENSESDESSEDAIRAIBLE1.MD>)

[Combine the variables] (<combine thevariables1.md>)