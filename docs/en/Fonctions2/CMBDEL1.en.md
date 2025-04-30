# Cmbdel

## CMBDEL function

The function ** Cmbdel ** combines (crosses) the methods of the variables in arguments and removes empty methods. & Nbsp;

It is enough to list the different variables (or constructions) to cross as arguments to produce a variable with combined methods.

### Syntax: & nbsp;

Q01.CMBDEL (variables)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| & nbsp; | Variables | List of Variables | List of Logical Variables to Combine | Compulsory |

#### NOIKS:

The CMBDEL function, very close to the CMBVAR variable, deletes cases not encountered (empty methods) of the result.In fact, it is ideal to cross the region variable by the DEPARTMENT variable: only the departments of the regions will appear (while CMBVAR would list all the departments for each of the regions \!).

#### Examples:

\ _CMBDEL (S1; S3; S4)

or & nbsp;

S1.CMBDEL (S3; S4)

The Resulting Variable has in modalities the crossing of the modalities of the three variables in arguments.

& nbsp;

If the Sex Variable Designates Men and Women and the Age Variable Designates Age Groups, then the Crossing of These Two Variables Will Give the Details of the Age Groups for Men and then For Women.

& nbsp;

See also: & nbsp;

[Combine The Methods of Several Variables] (<combination themodalites of the days1.md>)

[Combinations] (<combine thevariables1.md>)