# Ordmod

## Order Function

The ** Ordmod ** Function Modifies the Authorizing Officer of the Variable Treated.

& nbsp;

The Argument is the Vector of Values ​​(Example: 1 1 1 2 2 2) to be included in the method of the variable.

### Syntax: & nbsp;

Q01.ordmod (values; selection)

Gold

\ _ORDMOD (Q01; Values; selection)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| &#49; | Values ​​| List of Whole | Vector of the values ​​to be Written (Example: 1 1 1 2 2 2) & nbsp; | can be empty |
| &#50; | Selection | List of Values ​​| List of Affuted Positions (All IF indefinite) | Default Indefinite |

#### NOIKS:

There is no need to indicate as many values ​​as there are affected elements: The Function Automatically Repeats the List of Values ​​Provided.

Thus, a list of values ​​"1 1 2" will be automatically repeated if there are 8 elements to affect: "1 1 2 1 1 2 1"

If the ordmod is used without parameter, the authorizing OFFICER IS DETERMINED Automatically According to the subtitles.& Nbsp;

### EXAMPLES:

S1.ORDMOD (1 1 1 2 2)

COMPLETELY Modifies the Authorizing Officer of the Variable S1 - LONGELESS OF ITS SIZE.

& nbsp;

S1.ORDMOD (1; -1)

Modifies the Value of the Authorizing Officer of the Last Modality of the Variable S1.

& nbsp;

Q2.ordmod ()

If Q2 is a logical variable to 6 modalities in the form:

| Modality of the variable Q2 | Subscribe produced by Q2.ordmod () |
| --- | --- |
| Subtitle 1 | & nbsp; |
| & nbsp;Modality 1 | &#49; |
| & nbsp;Modality 2 | &#49; |
| Subtitle 2 | & nbsp; |
| & nbsp;Modality 3 | &#50; |
| & nbsp;Modality 4 | &#50; |

& nbsp;

& nbsp;

See also: [Properties variables] (<modify Proproprietesdesvariable.md>)