# Fitcol

## Fitcol Function

The **Fitcol** Function Allows You To Align The Columns from one variable to another.

& nbsp;

Argument 2 corresponds to the recognition mode application to carry out this alignment.

### Syntax: & nbsp;

Q01.Fitcol (variable; matchmode)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
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
* R (Repeat): Repeat the Modalities of the first variable to agree with the variable reference

#### NOIKS:

Fitcol is a kind of dynamic saltcol.& Nbsp;

The Fitcol and Fitrow functions operate exactly on the same mode, but the first applies to the "columns" dimension and the second to the "line" dimension of the variable in argument 1.

This allows a fine control during the interaction of two variables (operator, fix, flt etc.), alignment of methods, alignment of columns, etc.

### EXAMPLES:

Q01.FitMod (Q02; "T")

CREATES A NEW VARIABLE WHOSE COLUMNS Are the Same As Those of Q02 But with the data of q01.

& nbsp;

& nbsp;

See also: & nbsp;

[Treat the Logical Variables (Modalities)] (<trelligableslogicalsmoda1.md>)

[Combinations] (<combination Thevariables1.md>)

[Management dimensions] (<reurlesdimensesdesdesdairaible1.md>)