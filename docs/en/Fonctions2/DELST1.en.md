# Delst

## DELST function

The ** DELST ** function removes the subtitles encountered in the methods of the treated variable.

Two Working Methods are possible: EITHER they are purely and simply deleted, or they are repeated in terms of methods using a separator, while respecting the original hierarchy.

### Syntax: & nbsp;

Q01.DELST (Delimiter)

Or

\ _DELST (Q01; Delimiter)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| & nbsp; | Delimite | Character Chain | Optional Separator | Default |


#### Remarks :

The DELSTCOL and DELSTTROW functions work exactly on the same mode, but the first applies to the "columns" dimension and the second to the "line" dimension of the source variable.

### EXAMPLES:

BR1.DELST ()

Returns a variable whose subtitles are deleted from the list of methods.

& nbsp;

BR1.DELST (" -")

Returns a variable whose subtitles are deleted from the list of methods, but indicated in each of the methods and separated by the " -" chain.

& nbsp;

See also: [Labels management] (<GERERLESLIBELSESTEXTES1.MD>)