# Cmbvar

## Cmbvar Function

The Function **CMBVAR** Combins (Crosss) The Methods of the Variables in Arguments.& Nbsp;

It is enfuch to list the different variable (or constructions) to cross as arguments to produce a variable with combined methods.

### Syntax: & nbsp;

Q01.cmbvar (variables)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| & nbsp; | Variables | List of Variables | List of Variables to combine or an expression of selection of variables (ex: '$ "s?"') | Compulsory |

#### NOIKS:

The Cmbdel Function, very close to the Cmbvar Variable, Deletes Cases Not Encountered (Empty Methods) of the Result.in Fact, It is ideal to cross the Variable Region by the Department Variable: Only the Department of the Regions Will Appear (While Cmbvar Would List all the Department for Each of the Regions\!).

### EXAMPLES:

\ _Cmbvar (S1; S3; S4)

or & nbsp;

S1.CMBVAR (S3; S4)

The Resulting Variable has in modalities the crossing of the modalities of the three variables in arguments.

& nbsp;

If the Sex Variable Designates Men and Women and the Age Variable Designates Age Groups, then the Crossing of These Two Variables Will Give the Details of the Age Groups for Men and then For Women.

& nbsp;

See also: & nbsp;

[Combine The Methods of Several Variables] (<combination themodalites of the days1.md>)

[Combinations] (<combination Thevariables1.md>)