# Fitrow

## Fitrow Function

The **Fitrow** Function Allows You To Align The Lines from one variable to another.

& nbsp;

Argument 2 corresponds to the recognition mode application to carry out this alignment.

### Syntax: & nbsp;

Q01.Fitrow (variable; matchmode)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
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

Fitrow is a kind of Dynamic SELOW.& Nbsp;

The Fitcol and Fitrow Functions Operate Exactly On The Same Mode, But the First Apps to the "Columns" Dimension and the Second To The "Line" Dimension of the Variable in Argument 1.

This allows a fine control during the interaction of two variables (operator, fix, flt etc.), alignment of methods, alignment of columns, etc.

### EXAMPLES:

Q01.Fitrow (Q02; "T")

Creates a new variable whose lines are the same as those of Q02 but with the data of Q01.

& nbsp;

& nbsp;

& nbsp;

See also: & nbsp;

[Treat the Logical Variables (Modalities)] (<trelligableslogicalsmoda1.md>)

[Combinations] (<combination Thevariables1.md>)

[Dimensions management] (<GERERLESDIMENSESDESSEDAIRAIBLE1.MD>)