# CSVROW

## CSVROW function

The **CSVROW** function includes the lines of a variable using textual groupings described in an external table.

The Name of the Table is indicated by a character String, According to the Principle of Identifying External Tables.

& nbsp;

The 1st column Indicates The Items to Remember (and the Associated Texts) to Constitte The Result Variable.

The columns that follow indicate the items to be grouped.The seized texts can use the 'Jokers' (\* and?) To express wider selections.

The resulting variable is a dimensioned variable that has a line line line.

### Syntax: & nbsp;

Q01.CSVROW (Expression table)

Or

\ _CSVROW (Q01; Table Expression)

& nbsp;

|& nbsp;|**Name** |**Type** |**Description** |**Note** |
|--- |--- |--- |--- |--- |
|& nbsp;|Table Expression |Character chain |Character chain describing the name and tab of the Excel workbook containing the external table to use |Compulsory |


#### Examples:

Q01A.CSVROW ("Countries")

Returns a variable whose lines corresponds to the textual groups listed in the table in argument.

& nbsp;

See also: [Use of external tables] (<Usedablesexternes1.md>)