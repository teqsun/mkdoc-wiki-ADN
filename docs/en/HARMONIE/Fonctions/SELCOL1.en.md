# Selcol

## Selcol or Collar Function

The ** Selcol ** Function Selects (OR Groups) Columns of the Variable Treated.

See [Selmod] (<Selmod.md>).

### Syntax: & nbsp;

Q01.Selcol (Share1; Share2; Share3; ...; Reduc)

Or

Q01.Col (Share1; Share2;

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| & nbsp; | Pares | List of Expressions | Selection/Grouping Expressions Separated by ';' | Compulsory |
| & nbsp; | reduce | Operator & nbsp; | [Reduction operator] (<drads1.md>) | Optional |

& nbsp;

#### Examples:

Q1.Col (1 2 3; Sumna (1 2 3)) & nbsp;

Returns a variable dimensioned at 3 columns plus one last being the sum of the 3 others without taking into account the homeless (Sumna). & Nbsp;

& nbsp;

It is possible to use the hugs to extract an item: ** Q1 {2} ** is equivalent to ** Q1.COL (1) .timdim () **

& nbsp;

See also:

[Dimensions,] (<reurlesdimenssesdesevaliable1.md>)

& nbsp;