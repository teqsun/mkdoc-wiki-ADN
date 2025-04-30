# CSVMod

## CSVMod function

The ** CSVMod ** Function Brings Together The Methods of A Variable Using Textual Groupings Described in an External Table.

& nbsp;

The name of the table is indicated by a character string, according to the principle of identifying external tables.

& nbsp;

The 1st column Indicates The Methods (and the Associated Texts) to be retaineed to constitute the result variable.

The columns that follow indicate the other methods to be regrouped.The seized texts can use the 'Jokers' (\* and?) To express wider selections.

& nbsp;

The Resulting Variable is a logical variable that a table line modality.

### Syntax: & nbsp;

Q01.csvmod (table Expression)

Gold

\ _Csvmod (Q01; Expression table)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| & nbsp; | Expression table | Character chain | Character Chain Describing the name and tab of the Excel Workbook containing the external table to use | Compulsory |
| & nbsp; | NOTED | BOOLEAN | ADD the not listed to the table If True | False by Default |


#### Remarks :

The CSVCOL and CSVROW functions work exactly on the same mode, but the first applies to the "columns" dimension and the second to the "line" dimension of the source variable.

### EXAMPLES:

Q01A.CSVMod ("Countries"; True)

Returns a logical variable whose methods correspond to the textual groupings listed in the table in argument plus the responses not listed in the table.

& nbsp;

See also: [Use of external tables] (<Usedablesexternes1.md>)