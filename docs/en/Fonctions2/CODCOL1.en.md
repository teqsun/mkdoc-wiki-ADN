# Codcol

## Codcol function

The ** CODCOL ** function allows the caller to modify the codes associated with the columns of the variable.

& nbsp;

The argument is the vector of codes (example: 4 5 99) to be included in the codes of the variable.

### Syntax: & nbsp;

Q01.Codcol (values; selection)

Gold

\ _Codcol (Q01; values; selection)

& nbsp;

|& nbsp;|** Name ** |** Type ** |** Description ** |** Note ** |
|--- |--- |--- |--- |--- |
|&#49;|Values ​​|Numbers List |Codes values ​​|Compulsory |
|&#50;|Selection |List of values ​​|List of affected positions |Different by default |


#### Remarks :

The Codcol Function Keeps All The Other Properties of the Original Variable

### EXAMPLES:

S1.Codcol (97 99; 11 12) Affects Codes 97 and 99 to Columns 11 and 12. & Nbsp;

& nbsp;

See also: [Properties variables] (<modify Proproprietesdesvariable.md>)