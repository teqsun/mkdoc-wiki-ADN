# Mimax

## Mimax Function

The **Mimax** Function Circumbes A Digital Variable by Applying A Lower and/Or Upper Terminal to it.

& nbsp;

Argument 1: The Minimum Value (Floor)

Argument 2: The maximum value (ceiling)

Argument 3 Optional: True (Default) to Authorize the minimum value, false to exclude it

Argument 4 Optional: True (Default) to Authorize the maximum value, false to exclude it

Optional Argument 5: True to Bring the Values ​​Out of Area to the Terminal, False (by Default) to put them to home

### Syntax: & nbsp;

Q01.MIMAX (Minvalue; Maxvalue; Includemini; Includemaxi; Forceinsiderangemode)

Gold

\ _Mimax (Q01; minvalue; Maxvalue; Includemini; Includemaxi; Forceinsiderangemode)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| &#49; | Minvalue | Number | Mini Value | &#49; by Default |
| &#50; | Maxvalue | Number | Maximum VALUE | Maximum DEFAULT NUMBER |
| &#51; | Includemini | Boolean | Default Mini inclusive | True by Default |
| &#52; | Includemaxi | Boolean | Default, maximum inclusive | True by Default |
| &#53; | forceinsiderangemode | Boolean | by Default, the outside intervals are in homeless | False by Default |

### EXAMPLES:

AGE.MIMAX (18; 99; True; True; True)

The variable produced represents age between 18 and 99 include.the values ​​initially out of the field are Busht back to the nearest terminal.

& nbsp;

AGE.MIMAX (18; 99)

The variable produced represents age between 18 and 99 include.the values ​​initially out of scope are eliminated (without responsibes).

& nbsp;

See also: [Manipulate The Digital Variables] (<manipulatingsnurablesnumerics1.md>)