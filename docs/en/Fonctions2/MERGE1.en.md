# Merge

## Merge Function

The ** Merge Function ** Sticks the Recordings of the Variable Place in Argument and Creates the Level which corresponds to it.

Thus, the number of records of the result variable is the sum of the number of records of the variable in argument.

### Syntax: & nbsp;

\ _Merge (levelname; variables)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| &#49; | Levelname | Character Chain | Target Level Name (The Level Must Exist) | Compulsory |
| &#50; | Variables | List of Variables | List of Variables to Merge, Generally on Different Levels.if the Level of Arrival Already Exists, then the Variables must be consist with the levels used During the 1st call. | Compulsory |

#### NOIKS:

This Function Makes It Possible to Carry Out A Fusion of "Manual" Studies: You Import The Different Studies in the Form of Full -Fledged Levels (You can use a Renamed Mask to Properly Isolate The Variables) .then You Create the Merged Variables Using Merge.it Will UndoubtedlyFitmod to harmonize the variables in question (your choice, on codes, texts, etc.).

### EXAMPLES:

\ _Merge ("Products"; Q1a; Q1b)

& nbsp;

See also: & nbsp;

[Levels] (<Levels1.md>)