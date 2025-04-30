# Copyfrom

## Copyfrom function

The ** Copyfrom function ** copies the properties of a "donor" variable in the treated variable.

& nbsp;

The properties to be copied are defined using the 1st argument:

* Title & nbsp;: the title
* Short \ _title: the short title
* How: the comments
* Universe: the universe associated with the variable
* Weight: the weight associated with the variable
* Labels: the modalities
* Columns: columns & nbsp;
* ROWS: the lines

### Syntax: & nbsp;

Q01.copyfrom (argument; fartymask)

Or

\ _Copyfrom (Q01; Argument; Propertymask)

#### Examples:

Q2r.copyfrom (Q2; short \ _Title)

The short title of the Q2R variable is awarded the same text as the short title of the Q2 variable.

& nbsp;

|& nbsp;|** Name ** |** Type ** |** Description ** |** Note ** |
|--- |--- |--- |--- |--- |
|&#49;|Argument |Variable |Source variable |Compulsory |
|&#50;|Propertymask |Character chain |Copy elements separated by a space |Universe Weight Labels Columns Rows & Nbsp;Title Short \ _Title & nbsp;How |


& nbsp;

See also: & nbsp;

[Labels management] (<GERERLESLIBELLESLESTEXTES1.MD>)

[Variable properties] (<modify the Proprities ofVariable.md>)

[Combine the variables] (<combine thevariables1.md>)