# Tit2net

## Tit2net Function

The ** Tit2net ** Function Automatically Convers Subtitles Into Subtotals.

& nbsp;

The subtitles act as "heads of chapters" in the dimensions of the variables (methods, details, etc.). After application, each subtitle becomes a grouping of methods, but retains the same hierarchical level in terms of presentation.

### Syntax: & nbsp;

Q01.Tit2net (True; 1; 1)

Gold

\ _Tit2net (Q01; True; 1; 1)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| & nbsp; | Divisor | Boolean | If True, Modify the Divider So that the bases Are the Subtotals Created. | by Default False, no Divider |
| & nbsp; | Levelused | Digital | Subtitle Level from which Start to Create Subtotals | & nbsp; |
| & nbsp; | Standardbase | Digital | If 0, Alos the Standard Base is the basis of the variable.if 1, level 1 subtotals are full-fledged bases, etc. | & nbsp; |

### EXAMPLES:

S1.TT2NET ()

In the resulting variable, the subtitles are "replacement" by subtotals.

& nbsp;

See also: [Treat Logical Variables (Modalities)] (<TrelligablelogiquesModa1.md>)