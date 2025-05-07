# DelPrefixrow

## Delprefixrow function

The function **Delprefixrow** detects the prefix common to all the lines of the treated variable, then deletes it

It is possible to clean the texts (deletion of white and unwanted characters at the head/end of text, etc.) that result.

It is also possible to affect the prefix detected as the resulting variable.

& nbsp;

This function is generally called after a merger (on modality or dimension) to adjust the texts of the variable obtained.

### Syntax: & nbsp;

Q01.DelPREFIXROW (Cleantext; Modifytitle; Partdlimiter)

Or

\ _DelPrefixrow (Q01; Cleantext; Modifytitle; Partdlimiter)

& nbsp;

|& nbsp;|**Name** |**Type** |**Description** |**Note** |
|--- |--- |--- |--- |--- |
|&#49;|Cleantext |Boolean |Auto cleaning of text if true |True by default |
|&#50;|Modifytitle |Boolean |The prefix detected will be added to the title if true |True by default |
|&#51;|PartdepiLimiter |Character |When there is, the separator simplifies the detection of the common prefix |Different by default |


& nbsp;

See also: & nbsp;

[Treat the literal variables] (<Trellious Little Little.MD>)

[Labels management] (<GERERLESLIBELLESLESTEXTES1.MD>)