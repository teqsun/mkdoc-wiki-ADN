# Calcround

## Calcround function

The **Calcround** function creates a digital variable corresponding to the rounded value of the digital variable placed in argument with the number of decimals in parameter.

### Syntax: & nbsp;

Q01.Calcround (Decimals)

Or

\ _Calcround (Q01; Decimals)

& nbsp;

|& nbsp;|**Name** |**Type** |**Description** |**Note** |
|--- |--- |--- |--- |--- |
|& nbsp;|Decimals |Whole |Number of decimals kept, 0 by default |&#48;By default |


#### Examples:

IMC.CALCROUND ()

Creates a new variable corresponding to the value rounded to 0 decimal from the digital variable BMI.

& nbsp;

IMC.Calcround (4)

Creates a new variable corresponding to the rounded value to 4 decimals from the digital variable BMI.

& nbsp;

#### Noticed :

The Calcround () function follows the logic of Excel (Awayfromzero).

& nbsp;

See also: [Manipulate the digital variables] (<manipulatingsnurablesnumerics1.md>)