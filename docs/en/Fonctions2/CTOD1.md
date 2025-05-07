# Ctod

## CTOD Function

The CTOD function transforms a digital variable into a logical variable (discreet).Just list the lower terminals of the different slices to create a new variable, each modality of which corresponds to a slice.

#### Syntax n ° 1: Creation of Constant WorkForce Classes

Q01.ctod (nb; factor)

Gold

\ _CTOD (Q01; NB; Factor)

& nbsp;

|& nbsp;|**Name** |**Type** |**Description** |**Note** |
|--- |--- |--- |--- |--- |
|&#49;|NB |Whole |Number of classes to create |Compulsory |
|&#50;|Factor |Whole |If n, the terminals are multiple n |\ -1 default |


#### Noticed :

If the basic variable is dimensioned, the Terminals are Determined by the First item and Applied to All Items.

### & nbsp;

### & nbsp;

#### Syntax n ° 2: Creation of classes by indication of the lower terminals & nbsp;

Q01.CTOD (Boundaries)

Gold

\ _CTOD (Q01; Boundaries)

& nbsp;

|& nbsp;|**Name** |**Type** |**Description** |**Note** |
|--- |--- |--- |--- |--- |
|& nbsp;|Boundaries |Numbers List |List of lower classes to create |Compulsory |


#### Syntax n ° 3: Creation of a modality by value encountered (distribution)

Q01.CTOD ()

Or

\ _Ctod (Q01)

#### Examples:

S2.CTOD ()

Determines the distribution of the values ​​encountered (creates a tranche by value encountered).

& nbsp;

Age.ctod (0 25 50)

Create the "Less Than 25" Slices, "From 25 to Less Than 50" and "50 and more".

& nbsp;

Age.ctod (4)

Create The Quartiles.

& nbsp;

Age.ctod (0 50)

Create a slice less than 50 and a "50 and more" slice.

& nbsp;

See also: [Manipulate The Digital Variables] (<manipulatingsnurablesnumerics1.md>)