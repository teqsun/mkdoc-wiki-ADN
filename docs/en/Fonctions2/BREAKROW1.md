# Breakrow

## Breakrow function

The **BREAKROW** function defines leaps from pages or spacings on the column dimension of the treated variable.

### Syntax: & nbsp;

Q01.BREAKROW (selection; value; BreakBeFore; Spacebreak)

Or

\ _Breakrow (Q01; selection; Value; Breakbefore; Spacebreak)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| &#49; | Selection | List of Values ​​| Elements Positions To Modify | Compulsory |
| &#50; | Value | Boolean | by Default, Adds the page Jump. | True by Default |
| &#51; | BreakBeFore | Boolean | by Default, The Jump is before selection | True by Default |
| &#52; | Spacebreak | Boolean | True: Replacing Jumping Page by Spacing | False by Default |

### EXAMPLES:

S1.Breakrow (3; True; True; True)

Created a spacing in front of the 3rd element of the line dimension, visible in the tables.

& nbsp;

See also: & nbsp;

[Present the variables in the tables] (<PertERDERLESVARIABLE WHILESTAB1.MD>)