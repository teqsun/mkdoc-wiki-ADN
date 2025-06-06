# TXTMOD

## TXTMOD Function

The **txtmod** Function modified the text of one or more methods of the variable.& Nbsp;

This method is useful for modifying a particular text While Letting the Engine Manage Other Texts Useful.

The TXTCOL function modifies an item column and the TXTROW function modifies an item line.

### Syntax: & nbsp;

Q01.TXTMOD (Key; Value; Delimiter)

Gold

\ _TXTMOD (Q01; Key; Value; Delimiter)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| &#49; | Key | Character Chain | Assigned Positions | Compulsory |
| &#50; | Value | Character Chain | Associated Chain1;Associated Chain2 | Chain;Default Chain2 |
| &#51; | Delimite | Character Chain | LABELS SEPARATOR | Different by Default |


#### Examples:

S1.TXTMOD (1; "respondent")

Returns A Logical Variable Whose 1st Modality has the text "respondent".

& nbsp;

Size.ctod (3) .txtmod (1; "small/medium/large"; "/")

Returns a logical variable to 3 modalities with the labels respectively small, medium and large.

& nbsp;

Q1.TXTMOD ("\*"; "\ [code \]")

Replacements The Wording of All The Terms With Their respective code.

& nbsp;

We can also use \ [name \], \ [title \], \ [Title: S \], \ [Filter \], \ [comment \] ...

& nbsp;

See also: & nbsp;

[Treat the logical variables (modalities)] (<TrelligableslogicalsModa1.md>)

[Labels management] (<GERERLESLIBELLESLESTEXTES1.MD>)