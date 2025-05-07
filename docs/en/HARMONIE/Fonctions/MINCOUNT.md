# Mincount

## Mincount Function

The Min **Count** Function Creates A Filter from a Multi-Answer variable and at least number of quotas.& Nbsp;

### Syntax: & nbsp;

Q01.Mincount (argument; list; mode)

Or

\ _Mincount (Q01; argument; list; mode)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| & nbsp; | argument | Whole | minimum number of quotes | compulsory |
| & nbsp; | List | List | List of Terms Considered | & nbsp; |
| & nbsp; | Fashion | Boolean | Exclusively on the basis of the selection If True | & nbsp; |

### EXAMPLES:

Q2.Mincount (2)

CREATE A FILTER SELECTING Individuals who cited at Least 2 Responses.

& nbsp;

Q2.Mincount (2; 1 2 3; True)

CREATE A FILTER SELECTING Individuals HAVING CITED AT LEAST 2 Responses from the methods 1, 2 or 3 exclusively.

& nbsp;

& nbsp;

See also: & nbsp;

Count () & nbsp;

Maxcount ()

& nbsp;

[Labels Management] (<GERERLIBELSLIBALESTHESTEXTES1.MD>)

[Properties variable] (<modify the owner ofvariable.md>)

[Combination the variables] (<combination thevariables1.md>)