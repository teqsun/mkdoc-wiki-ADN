# Setcol

## Setcol Function

The ** Setcol ** Function Allows You To Partially Modify A Dimensioned Variable.& Nbsp;

### Syntax: & nbsp;

Q01.setcol (item; value)

Gold

\ _Setcol (variable; item; value)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| &#49; | Variable | Variable | All Types | Compulsory |
| &#51; | Item | Keys | List of items to modify | Compulsory |
| &#52; | Value | Value or variable | Responses to affect (Modality Number or Numerical Value Depending On the Nature of The Original Variable Or A Variable) & Nbsp; | Compulsory |

& nbsp;

### EXAMPLES:

S1.Setcol (1 2; 10)

The First Two S1 Items Recover The Value 10

& nbsp;

S1.Setcol (-1; Q1)

The Latest Item of S1 Recovers The Q1 Values

& nbsp;

S1.Setcol ("France"; Q1)

The item "France" of S1 Recovers the Values ​​of Q1

& nbsp;

See also: & nbsp;

[Combination the variables] (<combination thevariables1.md>)

[Variable temporary] (<variablestemporanesshis1.md>)

[Repair has variable] (<fix1.md>)