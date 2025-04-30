# Grpcol

## GRPCOL Function

The ** grpcol ** function allows you to group the columns with a variable. & Nbsp;

The arguments corresponds to the different desired groups.the result variable has as many columns as there are groupings.to create a group, Simply use the syntax Relating to items selections and or the extended selection of modalities/details.

### Syntax: & nbsp;

Q01.GRPCOL (Keys)

Gold

\ _GRPCOL (Q01; Keys)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| & nbsp; | Keys | List of values ​​| List of & nbsp; Elements to be treated | Compulsory |


#### Remarks :

The grouping operator is: & nbsp;

* Now for variable logical,
* Sum for Digital Variables.

#### Examples:

S1.GRPCOL (1 2; 1; 2; -1)

CREATES A NEW VARIABLE WHOSE COLUMNS Are:

\- The group of columns 1 and 2 of S1

\- The first column of S1

\- The second column of S1 & nbsp;

\- The Last of S1.

& nbsp;

S1.GRPCOL (1 2; 1; 2; $ o)

Creates a new variable whose columns are:

\- The group of columns 1 and 2 of S1

\- The first column of S1

\- The second column of S1 & nbsp;

\- No-cited columns

& nbsp;

See also: [Management dimensions] (<GERERLESDIMENSESDESSEVARIAIA1.MD>)