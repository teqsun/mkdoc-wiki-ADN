# Grpcol

## GRPCOL function

The ** Grpcol ** Function Allows You To Group The Columns with a variable.& Nbsp;

The arguments correspond to the different desired groups.The result variable has as many columns as there are groupings.To create a group, simply use the syntax relating to items selections and/or the extended selection of modalities/details.

### Syntax: & nbsp;

Q01.GRPCOL (Keys)

Or

\ _GRPCOL (Q01; Keys)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| & nbsp; | Keys | List of values ​​| List of & nbsp; Elements to be treated | Compulsory |


#### Remarks :

The grouping operator is: & nbsp;

* Or for logical variables,
* SUM for digital variables.

### EXAMPLES:

S1.GRPCOL (1 2; 1; 2; -1)

Creates a new variable whose columns are:

\- The Group of Columns 1 and 2 of S1

\- The First Column of S1

\- The second column of S1 & nbsp;

\- The last of S1.

& nbsp;

S1.GRPCOL (1 2; 1; 2; $ o)

Creates a new variable whose columns are:

\- The group of columns 1 and 2 of S1

\- The First Column of S1

\- The second column of S1 & nbsp;

\- No-cited columns

& nbsp;

See also: [Dimensions management] (<GERERLESDIMENSESDESSEVARIABLE1.MD>)