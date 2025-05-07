# Seconds

## Second function

The **Seconds** function translates a variable variable in digital variable.

& nbsp;

Arguments

* The variable to be translated
* The type of conversion:
* If true, returns the total duration expressed in number of seconds
* If False, simply returns the "second" component of the duration expressed

& nbsp;

Return Value

A digital variable similar to the temporal variable to be converted, whose digital values ​​depend on the arguments specified

### Syntax: & nbsp;

Q01.Seconds (TotalCount; Navalue)

Gold

\ _Seconds (Q01; Totalcount; Navalue)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| &#49; | Totalcount | Boolean | If True, Counts The Full Duration (Decimal Number Possible) If False, Simply Extracts The Component "Seconds" | True by Default |
| &#50; | Navalue | Number | Value to be for unanswered | Without Default |

### EXAMPLES:

Duration.Seconds (False)

Returns a digital variable which represents the "second" component of the variable duration.

& nbsp;

Duration.Seconds (True)

Returns a digital variable which represents the total duration expressed in number of seconds.

& nbsp;

See also: [Manipulate the temporal and duration variables] (<manipulativevariablestemporelle1.md>)