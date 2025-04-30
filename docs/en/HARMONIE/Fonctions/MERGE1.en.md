# Merge

## Merge Function

The ** Merge function ** sticks the recordings of the variables placed in argument and creates the level which corresponds to it.

Thus, the number of records of the result variable is the sum of the number of records of the variable in argument.

### Syntax: & nbsp;

\ _Merge (levelname; variables)

& nbsp;

|& nbsp;|** Name ** |** Type ** |** Description ** |** Note ** |
|--- |--- |--- |--- |--- |
|&#49;|Levelname |Character chain |Target level name (the level must exist) |Compulsory |
|&#50;|Variables |List of variables |List of variables to merge, generally on different levels.If the level of arrival already exists, then the variables must be consistent with the levels used during the 1st call.|Compulsory |

#### NOIKS:

This Function Makes It Possible to Carry Out A Fusion of "Manual" Studies: You Import The Different Studies in the Form of Full -Fledged Levels (You can use a Renamed Mask to Properly Isolate The Variables) .then You Create the Merged Variables Using Merge.it Will UndoubtedlyFitmod to harmonize the variables in question (your choice, on codes, texts, etc.).

### EXAMPLES:

\ _Merge ("products"; Q1a; Q1b)

& nbsp;

See also: & nbsp;

[Levels] (<Levels1.md>)