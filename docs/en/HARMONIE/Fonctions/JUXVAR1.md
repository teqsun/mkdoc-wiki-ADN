# Juxvar

## JUXVAR Function

The function **juxvar** juxtaposes the methods of the variables in argument. & Nbsp;

If the first variable has 3 modalities and the second has 2, then the resulting variable has 5 modalities. & Nbsp;

The basis of the variable obtained is that of respondents with at least one of the variables in argument.

& nbsp;

The juxvar function is equivalent to the operator of juxtaposition "," (the comma).

### Syntax: & nbsp;

\ _JUXVAR (selection)

& nbsp;

|& nbsp;|**Name** |**Type** |**Description** |**Note** |
|--- |--- |--- |--- |--- |
|& nbsp;|Selection |Selection of variables |Expression of selection of variables (ex: '$ "s?"') Or list of variables separated by a ";"; "|Compulsory |


#### Examples:

\ _JUXVAR (S1; S3)

\ [or S1, S3 \]

The resulting variable lists the modalities of S1 then the modalities of S3.

Base: respondent to S1 or S3.

& nbsp;

\ _JUXVAR (S1; S3; S4)

\ [or S1, S3, S4 \]

The resulting variable lists the modalities of S1 then those of S3 then those of S4.

Base: respondents to S1, S3 or S4.

#### Remarks :

It is possible to juxtapose logical variables with Digital Variables: & nbsp;

\ _JUXVAR (S1; S1Q.Title ("Number of responses cited"))

In the Event of A Control of the Calculation Displayed, the Tomod Function is more followed.

The use of this function with continuous variables is equivalent to juxcol () and therefore creates details (lines and/or columns)

& nbsp;

See also: & nbsp;

[Treat the logical variables (modalities)] (<TrelligableslogicalsModa1.md>)

[Present the variables in the tables] (<PertERDERLESVARIABLE WHILESTAB1.MD>)

[Criteria] (<Creerdescriteresoubannieres1.md>)

[Combine the variables] (<combine thevariables1.md>)