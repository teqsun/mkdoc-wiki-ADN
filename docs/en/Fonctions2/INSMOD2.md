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


#### Examples:

S3.insmod (2; "my wording")

Returns A Logical Variable Whose 2nd Modality has the text "My Wording".

& nbsp;

See also: & nbsp;

[Treat the Logical Variables (Modalities)] (<trelligableslogicalsmoda1.md>)

[Labels Management] (<GERERLIBELSLIBALESTHESTEXTES1.MD>)