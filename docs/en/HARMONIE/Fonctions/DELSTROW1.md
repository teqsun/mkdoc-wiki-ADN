# Delstrow

## Delstrow function

The **DELSTTROW** function removes the subtitles encountered in the lines of the treated variable.

Two working methods are possible: either they are purely and simply deleted, or they are repeated at the lines using a separator, while respecting the original hierarchy.

### Syntax: & nbsp;

Q01.DELSTTROW (DELIMITER)

Or

\ _Delstrow (Q01; Delimiter)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| & nbsp; | Delimite | Character Chain | Separator. | Default |


#### Examples:

Q01.DELSTCOL ()

Returns a variable whose subtitles are deleted from the list of columns.

& nbsp;

BR1.DELSTCOL (" -")

Returns a variable whose subtitles are deleted from the list of columns, but indicated in each of the columns and separated by the " -" chain.

& nbsp;

See also: [Labels management] (<GERERLESLIBELSESTEXTES1.MD>)