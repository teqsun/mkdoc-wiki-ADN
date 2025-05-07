# Fmtdate

## FMTDATE Function

The **FMTDATE** function transforms a temporal variable into a literal variable using a digital "Excel" format.

### Syntax: & nbsp;

Q01.FMTDATE (Format; Noanswersvalue)

Or

\ _FMTDATE (Q01; Format; Noanswersvalue)

& nbsp;

|& nbsp;|**Name** |**Type** |**Description** |**Note** |
|--- |--- |--- |--- |--- |
|&#49;|Format |Character chain |Display format |"G" by default |
|&#50;|Noanswersvalue |Character chain |Sans-answer values ​​|default |


#### Examples:

Date.ftmdate ("G")

Returns a literal variable whose texts are in the form "10/12/1815".

& nbsp;

Date.ftmdate ("D")

Returns a literal variable whose texts are in the form "Sunday, December 10, 1815".

& nbsp;

See also: [Manipulate the temporal and duration variables] (<manipulativevariablestemporelle1.md>)