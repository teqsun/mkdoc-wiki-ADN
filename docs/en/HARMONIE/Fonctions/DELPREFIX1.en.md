# Delprefix

## Delprefix function

The ** DELPREFIX ** function detects the prefix common to all the methods of the treated variable, then deletes it.

It is possible to clean the texts (deletion of white and unwanted characters at the head/end of text, etc.) that result.

It is also possible to affect the prefix detected as the resulting variable.

& nbsp;

This function is generally called after a merger (on modality or dimension) to add the texts of the variable obained.

### Syntax: & nbsp;

Q01.DelPREFIX (Cleantext; Modifytitle; PartDelimiter)

Or

\ _DelPrefix (Q01; Cleantext; Modifytitle; Partdlimiter)

& nbsp;

|& nbsp;|** Name ** |** Type ** |** Description ** |** Note ** |
|--- |--- |--- |--- |--- |
|&#49;|Cleantext |Boolean |Auto cleaning of text if true |True by default |
|&#50;|Modifytitle |Boolean |The prefix detected will be added to the title if true |True by default |
|&#51;|PartdepiLimiter |Character |When there is, the separator simplifies the detection of the common prefix |Different by default |


& nbsp;

#### Examples:

Q01.DelPrefix (True; True;)

Here the common prefix is ​​"*** to what extent, would you return to the different countries mentioned above. (***"

& nbsp;

|With this definition the wording of the methods of the variable Q01 |become: |
|--- |--- |
|To what extent, would you return to the different countries mentioned above. (Germany) to what extent, would you return to the different countries mentioned above. (Austria) to what extent, would you return to the different countries mentioned above. (Belgium) to what extent, would you return to the different countries mentioned above. (Denmark) to what extent, would you return to the different countries cited above.Different countries mentioned above. (Finland) to what extent, would you return to the different countries mentioned above. (France) To what extent, would go back to the different countries mentioned above. (Greece) |Germany Austria Belgium Denmark Spain Finland France Greece |


#### Noticed :

If the label ends with a parenthesis ")", it is deleted.

& nbsp;

See also: & nbsp;

[Treat the literal variables] (<Trellious Little Little.MD>)

[Labels management] (<GERERLESLIBELLESLESTEXTES1.MD>)