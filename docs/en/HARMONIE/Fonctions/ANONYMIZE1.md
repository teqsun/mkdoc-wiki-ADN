# Anonymize

## Anonymize Function

The Function **Anonymize** Cleans a variable by Removing the Non -Cited Methods in Relation to a Given Universe.& Nbsp;

Optionally, an "other" modality can be created.

### Syntax: & nbsp;

Q01.Anonymize (Universe; Createothers)

Gold

\ _Anonymize (Q01; Universe; Createothers)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| &#49; | Universe | Universe Application | Compulsory |
| &#50; | Createothers | Boolean | Creates the "Others" Modality If True | True by Default |

### EXAMPLES:

Department. Anonymize (Region 1)

Returns a variable Department which includes only the Department of the Region 1. The other Department are groupd in a "other" methods.

& nbsp;

DEPARTMENTS.ANONYMIZE (Region 1; FALSE)

Returns a variable Department which Only Includes The Department of the Region 1. The other Department are Simply Deleted.

& nbsp;

See also: & nbsp;

[Universe, Targets and Sub-Populations] (<UniverscibleSets-Populations.md>)

[Combination the variables] (<combination thevariables1.md>)