# Qsrtcol

## Qsrtcol Function

The ** QSRTCOL ** Function modified the Automatic Hierarchy Setpoint of the variable Columns in the Tables (in the properies of the variable generated).

It is therein a setpoint for tables.

& nbsp;

### Syntax: & nbsp;

Q01.QSRTCOL (ascendant; anchor; Calculation; Criteria)

Gold

\ _QSRTCOL (Q01; ascendant; anchor; Calculation; Criteria)

& nbsp;

|& nbsp;|** Name ** |** Type ** |** Description ** |** Note ** |
|--- |--- |--- |--- |--- |
|&#49;|Ascendant |Boolean |Sorting sense: ascendant if true, descendant if false and none to cancel sorting |False by default |
|&#50;|Anchor |Digital or expression |Number or wording of the reférence modality & nbsp;|& nbsp;|
|&#51;|Calculation |Character chain |Optional: Calculation to be used for sorting in the table |Different by default |
|&#52;|Criteria |Character chain |Optional: Label of the reference column to be used during sorting |Different by default |

#### NOIKS:

In general, when a variable is automatic hierarchical in a table, it is possible to specific a reference modality in a outing criterion by starting the text of the method with a closed hug '}'.

In the case of a logical variable, the "anchor" parameter allows you to choose the reference modality to apply the outing of columns items.

### EXAMPLES:

Q02C.QSRTCOL (FALSE; 1; PV; 2) & nbsp;

The items are sorted on the basis of the vertical percentages of column n ° 2 of the table and on modality 1 of the q02c variable.

#### Attention :

The qsrtcol () Function does not change the order of the columns of the variable but causes the outing of these in a table.

& nbsp;

See also: [Properties variables] (<modify Proproprietesdesvariable.md>)

PINCOL () To fix a columns.