# Milliseconds

## milliseconds Function

The ** milliseconds ** Function Translates has variable variable into a variable digital.

& nbsp;

Arguments

* The variable to be translated
* The Type of Conversion:
* If True, Returns The Total Duration expressly in number of milliseconds
* If False, Simply Returns the "Millisecond" Component of the Expressed Duration

& nbsp;

Return Value

A digital variable similar to the temporal variable to be converted, whose digital values ​​depend on the arguments specific

### Syntax: & nbsp;

Q01.Milliseconds (TotalCount; Navalue)

Gold

\ _Milliseconds (Q01; Totalcount; navalue)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| &#49; | Totalcount | Boolean | If True, account for the full duration (Decimal number possible) If False, Simply Extracts The Component "Milliseconds" | True by Default |
| &#50; | Navalue | Number | Value to be for unanswered | Without Default |

### EXAMPLES:

Duration.milliseconds (False)

Returns a digital variable that represents the "millisecond" component of the variable duration.

& nbsp;

Duration.milliseconds (True)

Returns a digital variable which represents the total duration expressd in number of milliseconds.

& nbsp;

See also: [Manipulate the temporal and duration variables] (<manipulativevariablestemporelle1.md>)