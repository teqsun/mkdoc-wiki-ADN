# Breakmod

## Breakmod Function

The **Breakmod** Function Defines or Spacings On The Methods of the Variable Treated.

### Syntax: & nbsp;

Q01.BREAKMOD (selection; value; BreakBeFore; Spacebreak)

Gold

\ _Breakmod (Q01; selection; Value; Breakbefore; Spacebreak)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| &#49; | Selection | List of Values ​​| Elements Positions To Modify | Compulsory |
| &#50; | Value | Boolean | by Default, Adds the page Jump. | True by Default |
| &#51; | BreakBeFore | Boolean | by Default, The Jump is before selection | True by Default |
| &#52; | Spacebreak | Boolean | True: Replacing Jumping Page by Spacing | False by Default |

### EXAMPLES:

S1.BREAKMOD (3; True; True; True)

CREATE A SPACING IN FRONT OF THE 3RD MODALITY, visible in the tables.

& nbsp;

See also: & nbsp;

[Present the variables in the tables] (<PertERDERLESVARIABLE WHILESTAB1.MD>)