# Xorflt

## XORFLT function

The **XORFLT** function creates a filter using an "exclusive" or logical "by considering the respondents of each of the arguments (which therefore correspond to the different variables and/or constructions).

### Syntax: & nbsp;

\ _Xorflt (Q01; Q02; ...)

& nbsp;

|& nbsp;|**Name** |**Type** |**Description** |**Note** |
|--- |--- |--- |--- |--- |
|& nbsp;|Selection |Selection of variables |Expression of selection of variables (ex: '$ "s?"') Or list of variables separated by a ";"; "|Compulsory |


#### Remarks :

An 'Xorflt' produces a filter (a single modality) whatever the variables in arguments.

#### Examples:

\ _Xorflt (S1; S3)

The result contains a modality.A respondent is "true" when he is a respondent to one and only one of the arguments.

& nbsp;

See also: & nbsp;

[Universe of variables] (<UniverscibleSetSous-Populations.md>)

[Combine the variables] (<combine thevariables1.md>)