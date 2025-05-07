# Insmod

## Insmod function

The **insmod** function adds an empty modality before the position indicated and attributes a wording to it.

### Syntax: & nbsp;

Q01.insmod (insertionpoint; text)

Or

\ _Insmod (q01; insertionpoint; text)

& nbsp;

|& nbsp;|**Name** |**Type** |**Description** |**Note** |
|--- |--- |--- |--- |--- |
|&#49;|INSERTIONPOINT |Number |Insertion position: The new modality will be inserted before the indicated position.|Compulsory |
|&#50;|Text |Character chain |Optional: Label to use & nbsp;(Avoid during multilingual treatments \!) |& nbsp;|

### EXAMPLES:

S3.insmod (2; "My Wording")

Returns a logical variable whose 2nd modality has the text "my wording".

& nbsp;

See also: & nbsp;

[Treat the Logical Variables (Modalities)] (<trelligableslogicalsmoda1.md>)

[Labels Management] (<GERERLIBELSLIBALESTHESTEXTES1.MD>)