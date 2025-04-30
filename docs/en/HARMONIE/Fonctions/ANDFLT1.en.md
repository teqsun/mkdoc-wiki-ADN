# Andflt

## Function andflt

The Andflt Function Creates A Universe (a Filter) Using A "and Logical" by considering the respondent of each of the arguments (which therefore corresponds to the different variable and or constructions).

#### Syntax n ° 1: & nbsp;

\ _Andflt (selection)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| & nbsp; | selection | selection of variables | Expression of selection of variables (ex: '$ "s?"') or list of variables separated by a ";"; ";"| Compulsory |

#### NOIKS:

A 'Andflt' Produces A Filter (Only One Modality) with the variables in arguments.

### EXAMPLES:

\ _Andflt (S1.Selmod (1 2); S3.Selmod (2); S2)

Gives a universe made up of the intersection (and logic) between respondent to s1 modalities 1 or 2, respondent to s3 modality 2 and respondent to s2.

& nbsp;

See also: & nbsp;

[Universe, Targets and Sub-Populations] (<UniverscibleSets-Populations.md>)

[Combination the variables] (<combination thevariables1.md>)