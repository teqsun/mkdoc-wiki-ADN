# Shorttitle

## Shorttitle function

The ** shorttitle ** function modifies the short title of the variable passed into an argument.

& nbsp;

It is possible to prefix the value by the sign "=" to use a treatment function applied as the input variable.

For more information, see the section on "text treatments"

### Syntax: & nbsp;

Q01.Shorttitle (expression)

Gold

\ _Shorttitle (Q01; expression)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| & nbsp; | Expression | Character chain | Expression to use for fixed the new short title | Compulsory |


#### Remarks :

The Shorttitle Function Keeps All The Other Properties of the Original Variable.if the Short Title is present and for Ease of Reading, it is displayed in the "Variable" View Instatead of the Long Title.

#### Examples:

S2.Shorttitle ("Age")

S2.Shorttitle ("= Trim, Upper")

S2.Shorttitle ("= Upper (@value)")

& nbsp;

See also: [Variables properties] (<modify ProproprietesDesvariable.md>)