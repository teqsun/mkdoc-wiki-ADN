# QSRT

## QSRT Function

The **QSRT** Function Modifies the Automatic Hierarchy Setpoint of the Variable in the Tables (in the properies of the variable generated).

It is therein a setpoint for tables.

### Syntax: & nbsp;

Q01.QSRT (Ascendant; Calculation; Criteria)

Gold

\ _QSRT (Q01; ascendant; Calculation; Criteria)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| &#49; | Ascendant | Boolean | Sorting Sense: Ascendant if True, descendant If False and None to Cancel Sorting | False by Default |
| &#50; | Calculation | Character chain | Optional: Calculation to be for outing in the table | Different by Default |
| &#51; | Criteria | Character Chain | Optional: Label of the Reference Column to be used During Sorting | Different by Default |

#### NOIKS:

In general, when a variable is automatic hierarchical in a table, it is possible to specific a reference modality in a outing criterion by starting the text of the method with a closed hug '}'.

### EXAMPLES:

S6.QSRT (none) & nbsp;

And the modalities of the new variable will no longer be sorted.

#### Attention :

The QSRT () Function Does Not Change the Order of the Methods of the Variable But Causes The Sorting of These in A Table.

& nbsp;

See also: [Properties variables] (<modify Proproprietesdesvariable.md>)

PINMOD () to fix a modality.