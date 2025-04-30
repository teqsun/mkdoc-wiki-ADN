# Breakcol

## Breakcol function

The ** BREAKCOL ** function defines leaps of pages or spacings on the column dimension of the treated variable.

### Syntax: & nbsp;

Q01.BREAKCOL (selection; value; BreakBeFore; Spacebreak)

Or

\ _Breakcol (Q01; selection; value; Breakbefore; Spacebreak)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| &#49; | Selection | List of Values ​​| Elements Positions To Modify | Compulsory |
| &#50; | Value | Boolean | by Default, Adds the page Jump. | True by Default |
| &#51; | BreakBeFore | Boolean | by Default, The Jump is before selection | True by Default |
| &#52; | Spacebreak | Boolean | True: Replacing Jumping Page by Spacing | False by Default |


#### Examples:

S1.BREAKMOD (3; True; True; True)

CREATE A SPACING IN FRONT OF THE 3RD ELEMENT OF THE COLUMN DIMENSION, visible in the tables.

& nbsp;

See also: & nbsp;

[Present the variables in the tables] (<pretenderlesvariableables whilestAb1.md>)