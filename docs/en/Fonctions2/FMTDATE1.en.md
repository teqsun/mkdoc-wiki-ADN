# Fmtdate

## FMTDATE FUNCTION

The ** fmtdate ** Function Transforms A Temporal Variable Into A Literal Variable Using A Digital "Excel" Format.

### Syntax: & nbsp;

Q01.FMTDATE (Format; Noanswersvalue)

Or

\ _FMTDATE (Q01; Format; Noanswersvalue)

& nbsp;

|& nbsp;|** Name ** |** Type ** |** Description ** |** Note ** |
|--- |--- |--- |--- |--- |
|&#49;|Format |Character chain |Display format |"G" by default |
|&#50;|Noanswersvalue |Character chain |Sans-answer values ​​|default |

### EXAMPLES:

Date.ftmdate ("G")

Returns a Literal variable whose texts are in the form "10/12/1815".

& nbsp;

Date.ftmdate ("D")

Returns a literal variable whose texts are in the form "Sunday, December 10, 1815".

& nbsp;

See also: [Manipulate the temporal and duration variables] (<manipulativevariablestemporelle1.md>)