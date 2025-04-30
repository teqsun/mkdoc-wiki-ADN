# Redmod

## Redmod function

The ** Redmod ** function allows the caller to modify the reducer (numerical value used to quantify a modality) of the variable.

& nbsp;

The argument is the vector of values ​​(example: 4.5 5.2 7.5) to be included in the methods of the variable.

### Syntax: & nbsp;

Q01.redmod (values; selection)

Or

\ _REDMOD (Q01; values; selection)

& nbsp;

|& nbsp;|** Name ** |** Type ** |** Description ** |** Note ** |
|--- |--- |--- |--- |--- |
|&#49;|Values ​​|Numbers List |Reducer values ​​|Compulsory |
|&#50;|Selection |List of values ​​|List of affected positions |Different by default |


#### Remarks :

The Redmod function keeps all the other properties of the original variable

#### Examples:

S1.REDMOD (1 2 3 4 5)

& nbsp;

See also: [Variables properties] (<modify ProproprietesDesvariable.md>)