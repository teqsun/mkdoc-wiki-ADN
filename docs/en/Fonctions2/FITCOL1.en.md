# Fitcol

## Fitcol Function

The ** Fitcol ** function allows you to align the columns from one variable to another.

& nbsp;

Argument 2 corresponds to the recognition mode application to carry out this alignment.

### Syntax: & nbsp;

Q01.Fitcol (variable; matchmode)

& nbsp;

|& nbsp;|** Name ** |** Type ** |** Description ** |** Note ** |
|--- |--- |--- |--- |--- |
|&#49;|Variable |Variable |Reference variable |Compulsory |
|&#50;|Matchmode |Character |Applied recognition mode |Compulsory |

& nbsp;

The modes of recognition:

* C (code): Search codes
* E (exact): Complete Search (code + text)
* T (text): Text Search
* S (simplified): Research by simplified text (ignore accents, whites etc.)
* N (Number): Simply aligns the size without too into account any alignment
* R (Repeat): Repeat the Modalities of the first variable to agree with the variable reference

#### Remarks :

Fitcol is a kind of dynamic saltcol. & Nbsp;

The Fitcol and Fitrow Functions Operate Exactly On The Same Mode, But the First Apps to the "Columns" Dimension and the Second To The "Line" Dimension of the Variable in Argument 1.

This allows a Fine Control During the Interaction of Two Variables (Operator, Fix, FLT etc.), Alignment of Methods, Alignment of Columns, etc.

#### Examples:

Q01.FitMod (Q02; "T")

CREATES A NEW VARIABLE WHOSE COLUMNS Are the Same As Those of Q02 But with the data of q01.

& nbsp;

& nbsp;

See also: & nbsp;

[Treat the Logical Variables (Modalities)] (<trelligableslogicalsmoda1.md>)

[Combinations] (<combine thevariables1.md>)

[Dimensions management] (<GERERLESDIMENSESDESSEDAIRAIBLE1.MD>)