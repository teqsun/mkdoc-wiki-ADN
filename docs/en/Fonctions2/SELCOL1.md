# Selcol

## Selcol or Collar Function

The **SELCOL** function selects (or groups) columns of the treated variable.

See [Selmod] (<Selmod.md>).

### Syntax: & nbsp;

Q01.Selcol (Share1; Share2; Share3; ...; Reduc)

Gold

Q01.Col (Share1; Share2;

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| & nbsp; | Pares | List of Expressions | Selection/Grouping Expressions Separated by ';' | Compulsory |
| & nbsp; | reduce | Operator & nbsp; | [Reduction operator] (<drads1.md>) | Optional |

& nbsp;

### EXAMPLES:

Q1.Col (1 2 3; Sumna (1 2 3)) & nbsp;

Returns a variable dimensioned at 3 Columns Plus One Last Being the Sum of the 3 Others Without Taking Into Account The Homeless (Sumna).& Nbsp;

& nbsp;

It is possible to use the hugs to extract an item: **q1 {2}** is equivalent to **q1.col (1) .timdim ()**

& nbsp;

See also:

[Dimensions,] (<reurlesdimenssesdesevaliable1.md>)

& nbsp;