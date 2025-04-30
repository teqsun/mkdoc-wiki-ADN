# None

## NUE or \ <\> function

The ** none ** function allows you to select individuals who have cited any of the methods listed from the respondents of the selected variable. & Nbsp;

The Argument corresponds to the different selected method.The result variable is a filter, a logical variable with a single modality, selecting individuals that have not breathed to any of the seleled methods.to create a selection, simple the syntax relative to itms selections and or the extend.Modalities/Details.

### Syntax: & nbsp;

Q01.NE (Keys)

Or

\ _None (Q01; Keys)

& nbsp;

|& nbsp;|** Name ** |** Type ** |** Description ** |** Note ** |
|--- |--- |--- |--- |--- |
|& nbsp;|Keys |List of values ​​|List of & nbsp;Elements to be treated |Compulsory |

#### notice:

The "respondents" base of the variable created is the "respondent" base of the variable used.

### EXAMPLES:

S1.NONE (1 2 3) or

S1 \ <\> 1 2 3

CREATE A NEW FILTER VARIABLE SELECTING Individuals that have not breathed to any of the methods 1, 2 or 3.

& nbsp;

S1.GRPMOD (NONE (1 2 3) .FLT (S1) is an equivalent definition.

& nbsp;

See also: & nbsp;

[All] (<all1.md>)

[Exactly] (<exactly1.md>)

[Any] (<ny1.md>)