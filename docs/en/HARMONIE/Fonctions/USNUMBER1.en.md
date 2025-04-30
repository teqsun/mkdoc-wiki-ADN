# USNUMBER

## USNUMBER function

The ** USNUMBER ** function allows you to calculate a digital identifier by incrementation.\
It is necessary to specify on which level of response we want to create the variable.

### Syntax: & nbsp;

\ _USNUMBER (Level; firstcordvalue)

& nbsp;

|& nbsp;|** Name ** |** Type ** |** Description ** |** Note ** |
|--- |--- |--- |--- |--- |
|&#49;|Level |Character chain |Name of the level to be identified |Different by default |
|&#50;|FIRSTRECORDVALUE |Whole |First value |&#49;By default |


#### Examples:

\ _USNUMBER ("Units"; 1001)

Creates a digital variable that starts at 1001 for the 1st recording and then increasing from 1 to each new recording.

& nbsp;

See also: & nbsp;

[Utilities \ & Miscellaneous] (<tools \ _misc1.md>)

[Creation of variables (system, random ...)] (<creerdesvariablesdoutepiecesys.md>)