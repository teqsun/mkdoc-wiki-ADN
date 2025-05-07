# CSVMod

## CSVMod Function

The **CSVMod** function brings together the methods of a variable using textual groupings described in an external table.

& nbsp;

The Name of the Table is indicated by a character String, According to the Principle of Identifying External Tables.

& nbsp;

The 1st column Indicates The Methods (and the Associated Texts) to be retaineed to constitute the result variable.

The columns that follow indicates the other methods to be group.

& nbsp;

The Resulting Variable is a logical variable that a table line modality.

### Syntax: & nbsp;

Q01.csvmod (Expression table)

Gold

\ _Csvmod (Q01; Expression table)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| & nbsp; | Expression table | Character chain | Character Chain Describing the name and tab of the Excel Workbook containing the external table to use | Compulsory |
| & nbsp; | NOTED | BOOLEAN | ADD the not listed to the table If True | False by Default |

#### NOIKS:

The CSVCOL and CSVROW FURCTIONS WORK EXACTLY ON THE SAME MODE, but the first apps to the "columns" dimension and the second to the "line" dimension of the source variable.

### EXAMPLES:

Q01A.CSVMod ("Countries"; True)

Returns a Logical Variable Whose Methods correspond to the textual groups Listed in the Table in Argument Plus The Responses Not Listed in the Table.

& nbsp;

See also: [Use of External Tables] (<usedablesexternes1.md>)