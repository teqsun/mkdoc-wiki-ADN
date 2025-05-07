# BASE

## Function base

The function **Base** Filter (puts to "without response") respondents of the variable by applying validity conditions and adds a modality made up of individuals remaining in no response after application of the filter.Thus making it possible to make the difference between the individuals not concerned and the without response.

### Syntax: & nbsp;

Q01.Base (Filter; Text)

Gold

\ _Base (Q01; Filter; Text)

& nbsp;

|& nbsp;|**Name** |**Type** |**Description** |**Note** |
|--- |--- |--- |--- |--- |
|&#49;|Filter |Universe |Application universe |Compulsory |
|&#50;|Text |Character chain |Optional: Label to use & nbsp;Preceded by @Code if we want to impose a code on the new modality (to be avoided during multilingual treatments \!) |& nbsp;|

### EXAMPLES:

S4.base (s3.selmod (1); "@99 the real sr")

The Variable Obtained is in All Respects Similar To The Variable S4.But Its Data is filtered According to the respondents to S3.Selmod (1) and the Remaining Modality of the Remaining Response is Added with the "Real Sr" label and is affected by code 99.

#### NOIKS:

It is the equivalent of the definition & nbsp ;:

S4.Noresp (99; "Les Rére Sr").FLT (S3.Selmod (1))

& nbsp;

The Basic Function () Applied to Variables of the Logical, continuous or literal type.& Nbsp;

& nbsp;

& nbsp;

See also: & nbsp;

[Universe of Variables] (<UniverscibleSetSous-Populations.md>)

[Combination the variables] (<combination thevariables1.md>)