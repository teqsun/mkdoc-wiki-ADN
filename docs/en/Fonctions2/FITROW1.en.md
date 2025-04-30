# Fitrow

## Fitrow Function

The ** Fitrow ** Function Allows You To Align The Lines from one variable to another.

& nbsp;

Argument 2 corresponds to the recognition mode application to carry out this alignment.

### Syntax: & nbsp;

Q01.Fitrow (variable; matchmode)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| &#49; | Variable | Variable | variable reference | Compulsory |
| &#50; | Matchmode | Character | Applied Recognition Mode | Compulsory |

& nbsp;

The Modes of Recognition:

* C (code): Search codes
* E (exact): Complete Search (code + text)
* T (text): Text Search
* S (simplified): Research by simplified text (ignore accents, whites etc.)
* N (Number): Simply aligns the size without too into account any alignment
* R (Repeat): Repeat the Modalities of the first variable to agree with the variable of & nbsp;

#### NOIKS:

Fitrow is a kind of Dynamic SELOW.& Nbsp;

The Fitcol and Fitrow Functions Operate Exactly On The Same Mode, But the First Apps to the "Columns" Dimension and the Second To The "Line" Dimension of the Variable in Argument 1.

This allows a Fine Control During the Interaction of Two Variables (Operator, Fix, FLT etc.), Alignment of Methods, Alignment of Columns, etc.

### EXAMPLES:

Q01.Fitrow (Q02; "T")

CREATES A NEW VARIABLE WHOSE LINES Are the Same As Those of Q02 But with the data of q01.

& nbsp;

& nbsp;

& nbsp;

See also: & nbsp;

[Treat the logical variables (modalities)] (<TrelligableslogicalsModa1.md>)

[Combinations] (<combination Thevariables1.md>)

[Management dimensions] (<reurlesdimensesdesdesdairaible1.md>)