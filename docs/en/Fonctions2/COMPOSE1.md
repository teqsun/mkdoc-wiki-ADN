# Compound

## Function composed

The function **composes** is essential when it comes to creating a complex criterion from an external table.

& nbsp;

The Name of the Table is indicated by a character String, According to the Principle of Identifying External Tables.

& nbsp;

The expected table has as many columns as desired knowing that:

\- The last column contains the definitions to be executed for each of the terms.Note that the selection of the respondents of the definition is automatic: no need to specify them.

\- The preceding columns represent the texts of the modalities according to the different hierarchical levels necessary.

### Syntax: & nbsp;

Q01.Complete (expression)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| & nbsp; | Expression | Character chain | Character Chain Describing the name and tab of the Excel Workbook containing the external table to use | Compulsory |

### EXAMPLES:

\ _Ccompose (Q01; "Pdt \! Criterres")

Returns a New Variable from the Table Stored in the Excel "Pdt.xlsx" File Present in the Study Directory, in the "Criterres" Tab.the Result has as many modalities as there are in the table.resondents of each modality are Those of the Definitions Entered in the Last Column of Each.

& nbsp;

See also: & nbsp;

[USE OF EXTERNAL TABLES] (<usedableSexternes1.md>)

[Criteria] (<Creerdescriteresoubannieres1.md>)