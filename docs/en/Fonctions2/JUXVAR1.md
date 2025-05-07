# Juxvar

## JUXVAR Function

The Function **JUXVAR** JUSTAPOSES THE METHODS OF THE VARIABLE IN ARGUMENT.& Nbsp;

If the first variable has 3 modalities and the second has 2, then the resulting variable has 5 modalities.& Nbsp;

The Basis of the Variable Obtained is that of respondents with at Least One of the Variables in Argument.

& nbsp;

The juxvar function is equivalent to the operator of juxtaposition "," (the comma).

### Syntax: & nbsp;

\ _JUXVAR (selection)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| & nbsp; | selection | selection of variables | Expression of selection of variables (ex: '$ "s?"') or list of variables separated by a ";"; ";"| Compulsory |

### EXAMPLES:

\ _JUXVAR (S1; S3)

\ [or S1, S3 \]

The Resulting Variable Lists The Modalities of S1 then the Modalities of S3.

Base: respondent to S1 or S3.

& nbsp;

\ _JUXVAR (S1; S3; S4)

\ [or S1, S3, S4 \]

The Resulting Variable Lists The Modalities of S1 then Those of S3 then Those of S4.

Base: respondent to S1, S3 or S4.

#### NOIKS:

It is possible to juxtapose logical variables with Digital Variables: & nbsp;

\ _JUXVAR (S1; S1Q.Title ("Number of Responses CITED"))

In the Event of A Control of the Calculation Displayed, the Tomod Function is more followed.

The Use of this Function with continuous variables is equivalent to juuxcol () and therefore cries details (lines and/or columns)

& nbsp;

See also: & nbsp;

[Treat the Logical Variables (Modalities)] (<trelligableslogicalsmoda1.md>)

[Present the variables in the tables] (<PertERDERLESVARIABLE WHILESTAB1.MD>)

[Criteria] (<Creerdescriteresoubannieres1.md>)

[Combine the variables] (<combine thevariables1.md>)