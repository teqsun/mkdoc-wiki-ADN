# Datetime

## Datetime function

The **DateTime function** has built a new temporal variable, from a given date in the form of a character string.

### Syntax: & nbsp;

\ _Datetime (level; value; format)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| &#49; | Level | Character Chain | Target Level | Compulsory |
| &#50; | Value | Character Chain | The Value of The Date to Decode | Compulsory |
| &#51; | Format | Character Chain | Date Decoding Format | Default |


#### Remarks :

Attention \!In the expression of the format, the breakage is important: respect the capital letters and the tiny \!

| Y | Year |
| --- | --- |
| M | MONTH |
| D | Days |
| H | hours |
| M | minutes |
| S | Seconds |
| F | Second fractions |

### EXAMPLES:

\ _DateTime ("Units"; "4/10/1957"; "D/M/Yyy")

Created the variable of October 4, 1957.

& nbsp;

(Consult the Functions \ _now or Sys to Create a variable that corresponds to the current date)

& nbsp;

See also: [Manipulate the temporal and duration variables] (<manipulativevariablestemporelle1.md>)