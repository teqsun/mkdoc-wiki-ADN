# Delprefix

## Delprefix Function

The **DELPREFIX** function detects the prefix common to all the methods of the treated variable, then deletes it.

It is possible to clean the texts (deletion of white and unwanted characters at the head/end of text, etc.) that results.

It is also possible to affect the prefix deteted as the variable resulting.

& nbsp;

This function is generally called after a merger (on modality or dimension) to adjust the texts of the variable obtained.

### Syntax: & nbsp;

Q01.DelPREFIX (Cleantext; Modifytitle; PartDelimiter)

Gold

\ _DelPrefix (Q01; Cleantext; Modifytitle; Partdlimiter)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| &#49; | Cleantext | Boolean | Auto Cleaning of Text If True | True by Default |
| &#50; | Modifytitle | Boolean | The prefix deteted will be added to the title if true | True by Default |
| &#51; | Partdepilimiter | Character | When there is, the separator simplifies the detection of the common prefix | Different by Default |

& nbsp;

### EXAMPLES:

Q01.DelPrefix (True; True;)

Here the Common Prefix is ​​"*** to What Extent, WOULD YOU RETURN TO The Different Countries Mention Above. (***"

& nbsp;

| With this definition the wording of the method of the variable Q01 | Become: |
| --- | --- |
| To what extent, would you return to the differenties mentioned above.(Germany) to what extent, would you return to the differenties mentioned above.(Austria) to what extent, would you return to the differenties mentioned above.(Belgium) to what extent, would you return to the different country mentioned aboo.(Denmark) to What Extent, Wow you Return to the Different Countries Cited Above.(Finland) to What Extent, Would You Return to the Different Counties Mentioned Above.(France) to What Extent, Would Go Back to the Different Counties Mentioned Above.(Greece) | Germany Austria Belgium Denmark Spain Finland France Greece |

#### notice:

If the label ends with a parenthesis ")", it is deleted.

& nbsp;

See also: & nbsp;

[Treat the Literal Variables] (<Trellious Little Little.md>)

[Labels Management] (<GERERLIBELSLIBALESTHESTEXTES1.MD>)