# Ordcol

## Ordcol Function

The **Ordcol** Function Modifies the Authorizing Officer of the Column Dimension of The Treated Variable.

& nbsp;

The Argument is the Vector of Values ​​(Example: 1 1 1 2 2 2) to be included in the columns of the variable.

### Syntax: & nbsp;

Q01.ordcol (values; selection)

Gold

\ _ORDCOL (Q01; Values; selection)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| &#49; | Values ​​| List of Whole | Vector of the values ​​to be Written (Example: 1 1 1 2 2 2) & nbsp; | Compulsory |
| &#50; | Selection | List of Values ​​| List of Affuted Positions (All IF indefinite) | Default Indefinite |

#### NOIKS:

There is no need to indicate as many values ​​as there are affected elements: The Function Automatically Repeats the List of Values ​​Provided.

Thus, a list of values ​​"1 1 2" will be automatic repeated if there are 8 elements to affect: "1 1 2 1 1" "

### EXAMPLES:

S1.ordrcol (1 1 1 2 2)

COMPLETELY Modifies the Authorizing Officer of the Variable S1 - LONGELESS OF ITS SIZE.

& nbsp;

S1.ORDCOL (1; -1)

Modifies the Value of the Authorizing Officer of the Last Column of the Variable S1.

& nbsp;

See also: [Properties variables] (<modify Proproprietesdesvariable.md>)