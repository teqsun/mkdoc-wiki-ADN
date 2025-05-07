# DelPrefixrow

## Delprefixrow Function

The Function **Delprefixrow** Detects The Prefix Common to All The Lines of the Treated Variable, then deletes it

It is possible to clean the texts (deletion of white and unwanted characters at the head/end of text, etc.) that results.

It is also possible to affect the prefix deteted as the variable resulting.

& nbsp;

This function is generally called after a merger (on modality or dimension) to add the texts of the variable obained.

### Syntax: & nbsp;

Q01.DelPREFIXROW (Cleantext; Modifytitle; PartDlimiter)

Gold

\ _DelPrefixrow (Q01; Cleantext; Modifytitle; Partdlimiter)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| &#49; | Cleantext | Boolean | Auto Cleaning of Text If True | True by Default |
| &#50; | Modifytitle | Boolean | The prefix deteted will be added to the title if true | True by Default |
| &#51; | Partdepilimiter | Character | When there is, the separator simplifies the detection of the common prefix | Different by Default |

& nbsp;

See also: & nbsp;

[Treat the Literal Variables] (<Trellious Little Little.md>)

[Labels Management] (<GERERLIBELSLIBALESTHESTEXTES1.MD>)