# Qsrtcol

## Qsrtcol Function

The ** QSRTCOL ** Function modified the Automatic Hierarchy Setpoint of the variable Columns in the Tables (in the properies of the variable generated).

It is therein a setpoint for tables.

& nbsp;

### Syntax: & nbsp;

Q01.QSRTCOL (ascendant; anchor; Calculation; Criteria)

Or

\ _QSRTCOL (Q01; ascendant; anchor; Calculation; Criteria)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| &#49; | Ascendant | Boolean | Sorting Sense: Ascendant if True, descendant If False and None to Cancel Sorting | False by Default |
| &#50; | anchor | Digital or expression | Number or wording of the modality refancement & nbsp; | & nbsp; |
| &#51; | Calculation | Character chain | Optional: Calculation to be for outing in the table | Different by Default |
| &#52; | Criteria | Character Chain | Optional: Label of the Reference Column to be used During Sorting | Different by Default |

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