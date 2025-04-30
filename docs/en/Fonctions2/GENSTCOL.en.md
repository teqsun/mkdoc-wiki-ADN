# Genstcol

## Function Genscol

The ** Genstcol ** Function Creates Subtitles According to a chosen delimiter.it is the opposite of delstol.

### Syntax: & nbsp;

Q01.Genstcol (Delimiter; Rightlign)

Or

\ _Genstcol (Q01; Delimiter; Rightlign)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| & nbsp; | Delimite | Character Chain | Oblogatorys Separator | & nbsp; |
| & nbsp; | Rightlign | Boolean | True: Start Decoding on the right | & nbsp; |

### & nbsp;

#### Examples:

BR1.Genstcol (",")

Returns a variable whose subtitles are created from the labels of the columns.

& nbsp;

France, Man

France, woman

Spain, man

Spain, woman

& nbsp;

becomes

& nbsp;

France

& nbsp;& nbsp;Man

& nbsp;& nbsp;Women

Spain

& nbsp; & nbsp;

& nbsp; & nbsp; Women