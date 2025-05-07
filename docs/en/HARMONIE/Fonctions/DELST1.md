# Delst

## DELST function

The **DELST** function removes the subtitles encountered in the methods of the treated variable.

Two working methods are possible: either they are purely and simply deleted, or they are repeated in terms of methods using a separator, while respecting the original hierarchy.

### Syntax: & nbsp;

Q01.DELST (Delimiter)

Or

\ _DELST (Q01; Delimiter)

& nbsp;

|& nbsp;|**Name** |**Type** |**Description** |**Note** |
|--- |--- |--- |--- |--- |
|& nbsp;|DELIMITE |Character chain |Optional separator |default |


#### Remarks :

The DELSTCOL and DELSTTROW functions work exactly on the same mode, but the first applies to the "columns" dimension and the second to the "line" dimension of the source variable.

#### Examples:

BR1.DELST ()

Returns a variable whose subtitles are deleted from the list of methods.

& nbsp;

BR1.DELST (" -")

Returns a variable whose subtitles are deleted from the list of methods, but indicated in each of the methods and separated by the " -" chain.

& nbsp;

See also: [Labels management] (<GERERLESLIBELSESTEXTES1.MD>)