# DELSTCOL

## DELSTCOL Function

The ** DELSTCOL ** Function Removes The Subtitles encourage in the columns of the Variable Treated.

Two Working Methods are possible: EITHER they are purely and simplely deleted, or they are repeated at the level of the columns using a separator, while respecting the original hierarchy.

### Syntax: & nbsp;

Q01.DELSTCOL (Delimite)

Or

\ _DELSTCOL (Q01; Delimiter)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| & nbsp; | Delimite | Character Chain | Separator & Nbsp; Optional | Default |

### EXAMPLES:

Q01.DELSTCOL ()

Returns a variable whose subtitles are deleted from the list of columns.

& nbsp;

BR1.DELSTCOL (" -")

Returns a variable whose subtitles are deleted from the list of columns, but indicated in each of the columns and separated by the " -" chain.

& nbsp;

See also: [Labels management] (<GERERLESLIBELSESTEXTES1.MD>)