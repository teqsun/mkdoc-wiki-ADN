# Setrow

## Setrow Function

The ** Setrow ** Function Allows You To Partially Modify A Dimensioned Variable.& Nbsp;

### Syntax: & nbsp;

Q01.settttt (item; value)

Gold

\ _Setttttt (variable; item; value)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| &#49; | Variable | Variable | All Types | Compulsory |
| &#51; | Item | Keys | List of items to modify | Compulsory |
| &#52; | Value | Value or variable | Responses to affect (Modality Number or Numerical Value Depending On the Nature of The Original Variable Or A Variable) & Nbsp; | Compulsory |

& nbsp;

### EXAMPLES:

S1.Settttttt (1 2; 10)

The First Two Items Lines of S1 Recover the Value 10

& nbsp;

S1.Settttt (-1; Q1)

The Last Item Lines of S1 Recovers The Values ​​of Q1

& nbsp;

S1.settttt ("France"; Q1)

The item line "France" of S1 Recovers the Values ​​of Q1

& nbsp;

See also: & nbsp;

[Combination the variables] (<combination thevariables1.md>)

[Variable temporary] (<variablestemporanesshis1.md>)

[Repair has variable] (<fix1.md>)