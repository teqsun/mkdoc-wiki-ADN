# Csvcol

## CSVCOL Function

The **CSVCOL** Function Brings Together The Columns of A Variable Using Textual Groupings Described in an External Table.

The Name of the Table is indicated by a character String, According to the Principle of Identifying External Tables.

& nbsp;

The 1st column indicates the items to remember (and the associated texts) to constitute the result variable.

The columns that follow indicates the items to be groupd.the seized texts can use the 'jokers' (\* and?) To express wider selections.

The resulting variable is a dimensioned variable that a column by line of the table.

### Syntax: & nbsp;

Q01.csvcol (table Expression)

Or

\ _Csvcol (Q01; Expression table)

& nbsp;

|& nbsp;|**Name** |**Type** |**Description** |**Note** |
|--- |--- |--- |--- |--- |
|& nbsp;|Table Expression |Character chain |Character chain describing the name and tab of the Excel workbook containing the external table to use |Compulsory |

### EXAMPLES:

Q01A.CSVCOL ("Countries")

Returns a variable whose columns corresponds to the textual groups listed in the table in argument.

& nbsp;

See also: [Use of external tables] (<Usedablesexternes1.md>)