# As

## As Function

The ** as ** Function Creates A Temporal Variable Usable in Current Definition.

& nbsp;

### Syntax: & nbsp;

Q01.as ("name")

Gold

\ _AS (Q01; "name")

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| &#49; | Name | Character Chain | Name of the Temporary Variable | Compulsory |

#### NOIKS:

The Call to A Temporary Variable is prefixed by the "@" Character

### EXAMPLES:

S2.as ("T1").Fix (@t1.noresp () and s1.mod (1); 99) .as ("T2").Fix (@t2.noresp () and s1.not (1);-1)

In this example, we want to apply 2 cleaning rules to the s2 variable without goong through the creation of intermediate variables.

T1 is a first copy of S2 on which a first cleaning rule is applied.

Then t2 which is a copy of the variable from this first cleaning is used for the application of a second cleaning rule.

& nbsp;

See also: