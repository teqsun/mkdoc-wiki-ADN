# Fitmod

## Fitmod Function

The ** Fitmod ** Function Allows you to align the method of one variable on another.

& nbsp;

Argument 2 corresponds to the recognition mode application to carry out this alignment.

### Syntax: & nbsp;

Q01.Fitmod (variable; matchmode)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| &#49; | Variable | Variable | variable reference | Compulsory |
| &#50; | Matchmode | Character | Applied Recognition Mode | Compulsory |

& nbsp;

The Modes of Recognition:

* C (code): codes search
* E (exact): Complete search (code + text)
* T (text): text search
* S (simplified): Research by simplified text (ignores accents, whites etc.)
* N (number): simply aligns the size without taking into account any alignment
* R (Repeat): repeat the modalities of the first variable to agree with the variable of & nbsp;reference

#### NOIKS:

Fitmod is a kind of dynamic selmod.& Nbsp;

The Fitcol and Fitrow Functions Operate Exactly On The Same Mode, But the First Apps to the "Columns" Dimension and the Second To The "Line" Dimension of the Variable in Argument 1.

This allows a Fine Control During the Interaction of Two Variables (Operator, Fix, FLT etc.), Alignment of Methods, Alignment of Columns, etc.

### EXAMPLES:

Q01.FitMod (Q02; "T")

CREATES A NEW VARIABLE WHOSE MODALITIES Are the Same As Those of Q02 But with the data of q01.

& nbsp;

& nbsp;

& nbsp;

See also: & nbsp;

[Treat the logical variables (modalities)] (<TrelligableslogicalsModa1.md>)

[Combinations] (<combination Thevariables1.md>)

[Management dimensions] (<reurlesdimensesdesdesdairaible1.md>)