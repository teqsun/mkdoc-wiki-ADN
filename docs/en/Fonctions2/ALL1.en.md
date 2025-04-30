# All

## All Function

The ** All ** Function Allows You To Select The Individuals Having Cited All The Methods Listed.& Nbsp;

The argument corresponds to the different selected methods.The result variable is a filter, a logical variable with a single modality, selecting the individuals who responded to all the selected methods.To create a selection, simply use the syntax relating to the ITEMS selection method and/or the extended selection method of modalities/details.

### Syntax: & nbsp;

Q01.all (Keys)

Gold

\ _All (Q01; Keys)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| & nbsp; | Keys | List of values ​​| List of Elements to be treated | Compulsory |

### EXAMPLES:

S1.all (1 2 3)

CREATE A NEW FILTER VARIABLE SELECTING Individuals that have cited at the modalities 1 and 2 and 3.

& nbsp;

S1.GRPMOD (All (1 2 3)) is an equivalent definition.

& nbsp;

See also: & nbsp;

[Exactly] (<exactly1.md>)

[Any] (<ny1.md>)

[None] (<none1.md>)