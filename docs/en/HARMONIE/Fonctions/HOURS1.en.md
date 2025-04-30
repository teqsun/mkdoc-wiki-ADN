# Hours

## HOURS FUNCTION

The ** HOURS ** function translates a variable of digital variable.

The result is a digital variable similar to the temporal variable to be converted, whose digital values ​​depend on the arguments specific

### Syntax: & nbsp;

Q01.hours (TotalCount; Navalue)

Gold

\ _Hours (Q01; Totalcount; Navalue)

& nbsp;

|& nbsp;|** Name ** |** Type ** |** Description ** |** Note ** |
|--- |--- |--- |--- |--- |
|&#49;|Totalcount |Boolean |If true, accounts for the full duration (decimal number possible) if false, simply extracts the component "hours" |True by default |
|&#50;|Navalue |Number |Value to be used for unanswered |Without default |

### EXAMPLES:

Duration.hours (False)

Returns a digital variable which represents the "hour" component of the variable duration.

& nbsp;

Duration.hours (True)

Returns a digital variable which represents the total duration expressed in number of hours.

& nbsp;

See also: [Manipulate the temporal and duration variables] (<manipulativevariablestemporelle1.md>)