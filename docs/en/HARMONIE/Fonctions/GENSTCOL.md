# Genstcol

## Function Genscol

The **GENSTCOL** function creates subtitles according to a chosen delimiter.It is the opposite of Delstcol.

### Syntax: & nbsp;

Q01.Genstcol (Delimiter; Rightlign)

Or

\ _Genstcol (Q01; Delimiter; Rightlign)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| & nbsp; | Delimite | Character Chain | Oblogatorys Separator | & nbsp; |
| & nbsp; | Rightlign | Boolean | True: Start Decoding on the right | & nbsp; |

### & nbsp;

### EXAMPLES:

BR1.Genstcol (",")

Returns a variable whose subtitles are created from the labels of the columns.

& nbsp;

France, man

France, Woman

Spain, man

Spain, woman

& nbsp;

becomes

& nbsp;

France

& nbsp;& nbsp;Man

& nbsp; & nbsp; Women

Spain

& nbsp;& nbsp;Man

& nbsp; & nbsp; Women