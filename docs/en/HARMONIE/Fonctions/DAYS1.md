# Days

## Days Function

The **Days** Function Translates has variable variable in Digital variable.

### Syntax: & nbsp;

Q01.DAYS (TotalCount; Navalue)

Or

\ _Days (Q01; Totalcount; Navalue)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| &#49; | Totalcount | Boolean | If True, account for the full duration (Decimal number possible) If False, Simply Extracts The Component "Days" | True by Default |
| &#50; | Navalue | Number | Value to be for unanswered | Without Default |

### EXAMPLES:

Duration.Days (False)

Returns a digital variable which represents the "day" component of the Duration variable.

& nbsp;

Duration.Days (True)

Returns a digital variable which represents the total duration expressd in number of days.

& nbsp;

See also: [Manipulate the temporal and duration variables] (<manipulativevariablestemporelle1.md>)