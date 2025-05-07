# Mimax

## Mimax Function

The **Mimax** Function Circumbes A Digital Variable by Applying A Lower and/Or Upper Terminal to it.

& nbsp;

Argument 1: The Minimum Value (Floor)

Argument 2: The maximum value (ceiling)

Argument 3 Optional: True (Default) to Authorize the minimum value, false to exclude it

Argument 4 Optional: True (Default) to Authorize the maximum value, false to exclude it

Optional argument 5: True to bring the values ​​out of area to the terminal, False (by default) to put them to home

### Syntax: & nbsp;

Q01.MIMAX (Minvalue; Maxvalue; Includemini; Includemaxi; Forceinsiderangemode)

Gold

\ _Mimax (Q01; minvalue; Maxvalue; Includemini; Includemaxi; Forceinsiderangemode)

& nbsp;

|& nbsp;|**Name** |**Type** |**Description** |**Note** |
|--- |--- |--- |--- |--- |
|&#49;|Minvalue |Number |Mini value |&#49;By default |
|&#50;|Maxvalue |Number |Maximum value |Maximum default number |
|&#51;|Includemini |Boolean |Default mini inclusive |True by default |
|&#52;|Includemaxi |Boolean |Default, maximum inclusive |True by default |
|&#53;|Forceinsiderangemode |Boolean |By default, the outside intervals are in homeless |False by default |


#### Examples:

AGE.MIMAX (18; 99; True; True; True)

The variable produced represents age between 18 and 99 included.The values ​​initially out of the field are brought back to the nearest terminal.

& nbsp;

AGE.MIMAX (18; 99)

The variable produced represents age between 18 and 99 included.The values ​​initially out of scope are eliminated (without responses).

& nbsp;

See also: [Manipulate The Digital Variables] (<manipulatingsnurablesnumerics1.md>)