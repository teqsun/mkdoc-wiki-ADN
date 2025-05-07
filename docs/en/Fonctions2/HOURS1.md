# Hours

## Hours Function

The **Hours** Function Translates A Variable of Digital Variable.

The result is a digital variable similar to the temporal variable to be converted, whose digital values ​​depend on the arguments specific

### Syntax: & nbsp;

Q01.hours (TotalCount; Navalue)

Gold

\ _Hours (Q01; Totalcount; Navalue)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| &#49; | Totalcount | Boolean | If True, account for the full duration (Decimal number possible) If False, Simply Extracts The Component "Hours" | True by Default |
| &#50; | Navalue | Number | Value to be for unanswered | Without Default |

### EXAMPLES:

Duration.hours (False)

Returns a digital variable which represents the "hour" component of the variable duration.

& nbsp;

Duration.hours (True)

Returns a digital variable which represents the total duration expressd in number of hours.

& nbsp;

See also: [Manipulate the temporal and duration variables] (<manipulativevariablestemporelle1.md>)