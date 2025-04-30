# Split

## Split Function

The ** Split ** Function Applied to a Literal Variable Cuts The Texts Cited in As Many 'Details' As there are delimited parts encouraged in the Responsses.

Whatever the variable treated, it is automatically converted into a literal variable, and the result is always a literal variable.

### Syntax: & nbsp;

Q01.Split (delimiters; expected share)

Gold

\ _Split (Q01; Delimiters; expected share)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| &#49; | Delimiters | Character Chain | Delimitors to use to cut the chain at the input | Compulsory |
| &#50; | ExpedpartCountCount | Whole | Optional Number of Expedted Parts: Allows You To Force The Number of Details in the Result Variable. | \ -1 Default |

### EXAMPLES:

Q01A.SPLIT (""; 5)

Returns a literal variable dimensioned with 5 details and whose methods correspond to the different 'words' (separated by whites) encountered in the original data.

& nbsp;

Q01A.SPLIT ("")

Same as before, but the number of details depends directly on the maximum number of words encourage in the data.

& nbsp;

See also: [Treat the Literal Variables] (<Trellious Little Little.md>)