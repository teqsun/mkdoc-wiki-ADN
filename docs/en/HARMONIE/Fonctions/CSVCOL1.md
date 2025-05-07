# Csvcol

## CSVCOL Function

The **CSVCOL** function brings together the columns of a variable using textual groupings described in an external table.

The Name of the Table is indicated by a character String, According to the Principle of Identifying External Tables.

& nbsp;

The 1st column Indicates The Items to Remember (and the Associated Texts) to Constitte The Result Variable.

The columns that follow indicates the items to be groupd.the seized texts can use the 'jokers' (\* and?) To express wider selections.

The resulting variable is a dimensioned variable that a column by line of the table.

### Syntax: & nbsp;

Q01.csvcol (expression table)

Or

\ _Csvcol (Q01; Expression table)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| & nbsp; | Expression table | Character chain | Character Chain Describing the name and tab of the Excel Workbook containing the external table to use | Compulsory |

### EXAMPLES:

Q01A.CSVCOL ("Countries")

Returns a variable whose columns corresponds to the textual groups listed in the table in argument.

& nbsp;

See also: [Use of External Tables] (<usedablesexternes1.md>)