# Any

## Any Function

The **Any** Function Makes It Possible to select the individuals Having Cited at Least One of the Modalities or Codes Listed.

The Argument corresponds to the different selected method.the result variable is a filter, a logical variable with a single modality, selecting individuals who have responded at least one of the seleled methods.to create a selection, simple the syntax Relating to itms selections and or the extended selection ofModalities/Details.

### Syntax: & nbsp;

Q01.any (Keys)

Gold

\ _ANY (Q01; Keys)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| & nbsp; | Keys | List of values ​​| List of Elements to be treated | Compulsory |

### EXAMPLES:

S1.any (1 2 3)

CREATE A NEW FILTER VARIABLE SELECTING INDIVIDEROIRS With At Least One Of The Modalities 1, 2 OR 3.

& nbsp;

S1.GRPMOD (Any (1 2 3)) OR S1.GRPMOD (1 2 3) Are Equivalent Definitions.

& nbsp;

#### NOIKS:

With S2 Being A continuous variable, the following definitions Return the Same Population:

S2.ANY ($ 45)

S2.ANY (45)

S2 = 45

S2 == 45

& nbsp;

See also: & nbsp;

[All] (<all1.md>)

[Exactly] (<exactly1.md>)

[None] (<none1.md>)