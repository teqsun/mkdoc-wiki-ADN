# Codrow

## Codrow Function

The **codrow** function allows the caller to modify the codes associated with the lines of the variable.

& nbsp;

The Argument is the Vector of Codes (Example: 4 5 99) to be include in the lines of the variable.

### Syntax: & nbsp;

Q01.Codrow (values; selection)

Or

\ _Codrow (q01; values; selection)

& nbsp;

|& nbsp;|**Name** |**Type** |**Description** |**Note** |
|--- |--- |--- |--- |--- |
|&#49;|Values ​​|Numbers List |Codes values ​​|Compulsory |
|&#50;|Selection |List of values ​​|List of affected positions |Different by default |

#### NOIKS:

The Codrow function keeps all the other properties of the original variable

### EXAMPLES:

S1.Codrow (97 99; 11 12) Affects Codes 97 and 99 to Lines 11 and 12. & Nbsp;

& nbsp;

See also: [Properties variables] (<modify Proproprietesdesvariable.md>)