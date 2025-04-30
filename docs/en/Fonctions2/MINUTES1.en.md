# MINUTES

## Minute Function

The ** minutes ** Function Translates has variable of Digital variable.

& nbsp;

Arguments

* The variable to be translated
* The Type of Conversion:
* If True, Returns The Total Duration expressly in Number of Minutes
* If False, Simply Returns the "minute" Component of the Duration expressd

& nbsp;

Return Value

A digital variable similar to the temporal variable to be converted, whose digital values ​​depend on the arguments specific

### Syntax: & nbsp;

Q01.Minates (TotalCount; Navalue)

Gold

\ _Minutes (Q01; Totalcount; Navalue)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| &#49; | Totalcount | Boolean | If True, account for the full duration (Decimal number possible) If False, Simply Extracts The Component "minutes" | True by Default |
| &#50; | Navalue | Number | Value to be for unanswered | Without Default |

### EXAMPLES:

Duration.minates (False)

Returns a digital variable that represents the "minute" component of the variable duration.

& nbsp;

Duration.minates (True)

Returns a digital variable which represents the total duration expressed in number of minutes.

& nbsp;

See also: [Manipulate the temporal and duration variables] (<manipulativevariablestemporelle1.md>)