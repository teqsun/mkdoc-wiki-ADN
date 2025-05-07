# Codify

## Codify Function

The **Codify** Function Affects Codes To The Methods of A Variable.

The codes identify the modalities in a more "stable" manner than the terms numbers, and are used for data exports.

& nbsp;

The expected argument (in addition to the coding variable) is the list of codes to affect.

### Syntax: & nbsp;

Q01.Codify (codes)

Gold

\ _Codify (Q01; Codes)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| & nbsp; | Codes | List of Character Strings | List of Codes to affect | Different by Default |

#### NOIKS:

The Conservation of Codes After Application of Other Recodifications is not Guarantee.

All Modalities must be described

### EXAMPLES:

\ _Codify (S1; 1 2 3 4 99)

Returns a variable whose modalities are identified by codes 1 2 3 4 99 respectly

& nbsp;

See also: & nbsp;

[Treat the Logical Variables (Modalities)] (<trelligableslogicalsmoda1.md>)

[Variable properties] (<modify the Proprities ofVariable.md>)