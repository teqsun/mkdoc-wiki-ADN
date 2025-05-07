# Compound

## Function composed

The function **composes** is essential when it comes to creating a complex criterion from an external table.

& nbsp;

The name of the table is indicated by a character string, according to the principle of identifying external tables.

& nbsp;

The expected table has as many columns as desired knowing that:

\- The Last column Contains the Definitions to be Executed for Each of the Terms.note that the selection of the respondent of the definition is Automatic: No Need to Specify them.

\- The preceding columns take up the texts of the modalities according to the different hierarchical levels needed.

### Syntax: & nbsp;

Q01. Complete (expression)

& nbsp;

|& nbsp;|**Name** |**Type** |**Description** |**Note** |
|--- |--- |--- |--- |--- |
|& nbsp;|Expression |Character chain |Character chain describing the name and tab of the Excel workbook containing the external table to use |Compulsory |


#### Examples:

\ _Ccompose (Q01; "Pdt \! Criterres")

Returns a new variable from the table stored in the Excel "PDT.XLSX" file present in the study directory, in the "Criterres" tab.The result has as many modalities as there are in the table.Respondents of each modality are those of the definitions entered in the last column of each line of the table.

& nbsp;

See also: & nbsp;

[Use of external tables] (<Usedablesexternes1.md>)

[Criteria] (<Creerdescriteresoubannieres1.md>)