# Codcol

## Codcol Function

The ** Codcol ** Function Allows the Caller to Modify the Codes Associated With The Columns of the Variable.

& nbsp;

The Argument is the Vector of Codes (Example: 4 5 99) to be include in the codes of the variable.

### Syntax: & nbsp;

Q01.Codcol (values; selection)

Gold

\ _Codcol (q01; values; selection)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| &#49; | Values ​​| Numbers List | Values ​​codes | Compulsory |
| &#50; | Selection | List of Values ​​| List of Affuted Positions | Different by Default |

#### NOIKS:

The Codcol Function Keeps All The Other Properties of the Original Variable

### EXAMPLES:

S1.Codcol (97 99; 11 12) Affects Codes 97 and 99 to Columns 11 and 12. & Nbsp;

& nbsp;

See also: [Properties variables] (<modify Proproprietesdesvariable.md>)