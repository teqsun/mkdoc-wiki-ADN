# Setcol

## Setcol function

The **setcol** function allows you to partially modify a dimensioned variable. & Nbsp;

### Syntax: & nbsp;

Q01.setcol (item; value)

Gold

\ _Setcol (variable; item; value)

& nbsp;

|& nbsp;|**Name** |**Type** |**Description** |**Note** |
|--- |--- |--- |--- |--- |
|&#49;|Variable |Variable |All types |Compulsory |
|&#51;|Item |Keys |List of items to modify |Compulsory |
|&#52;|Value |Value or variable |Response to affect (modality number or numerical value depending on the nature of the original variable or a variable) & nbsp;|Compulsory |


& nbsp;

#### Examples:

S1.Setcol (1 2; 10)

The first two S1 items recover the value 10

& nbsp;

S1.Setcol (-1; Q1)

The latest Item of S1 recovers the Q1 values

& nbsp;

S1.Setcol ("France"; Q1)

The Item "France" of S1 recovers the values ​​of Q1

& nbsp;

See also: & nbsp;

[Combine the variables] (<combine thevariables1.md>)

[Temporary variables] (<variablestemporanesshis1.md>)

[Repair a variable] (<fix1.md>)