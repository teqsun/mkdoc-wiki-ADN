# Seconds

## Second Function

The ** Seconds ** Function Translates has variable variable in Digital variable.

& nbsp;

Arguments

* The variable to be translated
* The Type of Conversion:
* If True, Returns The Total Duration expressly in Number of Seconds
* If False, Simply Returns The "Second" Component of the Duration expressd

& nbsp;

Return Value

A digital variable similar to the temporal variable to be converted, whose digital values ​​depend on the arguments specified

### Syntax: & nbsp;

Q01.Seconds (TotalCount; Navalue)

Gold

\ _Seconds (Q01; Totalcount; Navalue)

& nbsp;

|& nbsp;|** Name ** |** Type ** |** Description ** |** Note ** |
|--- |--- |--- |--- |--- |
|&#49;|Totalcount |Boolean |If true, counts the full duration (decimal number possible) if false, simply extracts the component "seconds" |True by default |
|&#50;|Navalue |Number |Value to be used for unanswered |Without default |

### EXAMPLES:

Duration.Seconds (False)

Returns a digital variable which represents the "second" component of the variable duration.

& nbsp;

Duration.Seconds (True)

Returns a digital variable which represents the total duration expressd in number of seconds.

& nbsp;

See also: [Manipulate the temporal and duration variables] (<manipulativevariablestemporelle1.md>)