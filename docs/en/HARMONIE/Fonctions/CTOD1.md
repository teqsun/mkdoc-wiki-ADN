# Ctod

## CTOD Function

The CTOD Function Transforms A Digital Variable Into A Logical Variable (Discreet) .just list the lower terminals of the different slices to new variable, each modality of which corresponds to a slice.

#### Syntax n ° 1: Creation of Constant WorkForce Classes

Q01.ctod (nb; factor)

Gold

\ _CTOD (Q01; NB; Factor)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| &#49; NB | Whole | Number of Classes To Create | Compulsory |
| &#50; | Factor | Whole | If N, The Terminals Are Multiple N | \ -1 Default |

#### notice:

If the basic variable is dimensioned, the Terminals are Determined by the First item and Applied to All Items.

### & nbsp;

### & nbsp;

#### Syntax n ° 2: Creation of classes by indication of the lower terminals & nbsp;

Q01.CTOD (Boundaries)

Gold

\ _CTOD (Q01; Boundaries)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| & nbsp; | Boundaries | Numbers List | List of Lower Classes To Create | Compulsory |

#### Syntax n ° 3: Creation of A Modality by Value Encountered (Distribution)

Q01.CTOD ()

Gold

\ _Ctod (Q01)

### EXAMPLES:

S2.CTOD ()

Determines the Distribution of the Values ​​encouraged (Creates a slice by Value encountered).

& nbsp;

Age.ctod (0 25 50)

Create the "Less Than 25" Slices, "From 25 to Less Than 50" and "50 and more".

& nbsp;

Age.ctod (4)

Create The Quartiles.

& nbsp;

Age.ctod (0 50)

CREATE A SLICE LESS THAN 50 AND A "50 AND MORE" SLICE.

& nbsp;

See also: [Manipulate The Digital Variables] (<manipulatingsnurablesnumerics1.md>)