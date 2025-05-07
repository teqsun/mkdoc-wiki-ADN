# Ctot

## CTOT Function

The **CTOT** Function Transforms A Digital Variable Into A Literal Variable Using A "Excel" Digital Format.

### Syntax: & nbsp;

Q01.CTOT (format; noanswersvalue)

Gold

\ _CTOT (Q01; Format; Noanswersvalue)

& nbsp;

|& nbsp;|**Name** |**Type** |**Description** |**Note** |
|--- |--- |--- |--- |--- |
|&#49;|Format |Character chain |Digital format to use |default |
|&#50;|Noanswersvalue |Character chain |Text associated with homelessness |default |

### EXAMPLES:

S2.CTOT ("000")

Returns a Literal variable whose text is the age formatted on 3 positions supplemented by 0.

& nbsp;

Delta.ctot ('+00; -00; "="')

Returns a literal variable whose texts are the delta formatted in 2 positions supplemented by 0, signed with the zero value replaced by the sign "=".

& nbsp;

S2.ctot ('0 "Years"'; "-")

Returns a Literal variable whose texts are formed by the formatted age followed by the character thong "years" .The homeless receif the channel "-"

& nbsp;

#### notice:

It is always possible to use the [NATOVAL] (<na2val1.md>) function to contain the behavior of homeless people.

### & nbsp;

& nbsp;

See also: [Manipulate The Digital Variables] (<manipulatingsnurablesnumerics1.md>)