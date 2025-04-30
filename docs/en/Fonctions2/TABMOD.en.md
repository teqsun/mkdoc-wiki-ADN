# Tabmod

## Tabmod Function

The ** Tabmod ** Function Applied An External Recodification Table To A Variable.

& nbsp;

The Name of the Table is indicated by a character String, According to the Principle of Identifying External Tables.

& nbsp;

This Function Plays a Particular Role Becuse It Allows You To Carry Out All Current Operations On The Methods (Extractions, Groups ...) by Analysis of Text File Content, in CSV Format.The Definition is Thus Independent of Studies and can be used in successive waves, with updates that willAutomatically in the absence of variable storage.& Nbsp;

The result is always a logical, multi-answer or discreet variable.

& nbsp;

The treated variable can be digital or logical.

If the variable is digital, the codes indicate the digital values ​​to be used and are not necessary present in the data.

If the variable is logical, the codes indicated correspond to methods and must be available, therefore at most to the number of methods.

The Zero Value (0) is Authorized to Generate Empty Methods.

& nbsp;

The Columns of the Read Table Follow The Structure Described Below.

& nbsp;

The Code column contains the terms of methods to be grouped on the same line.

This is a simple list.

.17 & nbsp; & nbsp; modality corresponds to the occurrences of code 17

.17 & nbsp; 19 & nbsp; & nbsp; modality corresponds to the occurrences of codes 17 or 19

.17 to 21 & nbsp; & nbsp; modality corresponds to the occurrences of codes 17, 18, 19, 20 or 21 & nbsp;

& nbsp;

The Wording Column Indicates The Texts (Forced) or not (Resumption of the Initial Label).

To recover an initial label, put a "#".

& nbsp;

If the Study Includes Several Languages, The Title of the Column is supplemented by the International Code of the Language, in Parentheses. Example: Long (FR), Shorts (GB).

& nbsp;

The insertion of subtitles is authorized.in this case, only the labels columns are daughter.& Nbsp;

The Number of "\ &" Which Prioritizes The Subtitles Must Be Respected.

& nbsp;

The Tabcol and Tabrow Functions Work Exactly On The Same Mode, but the first apps to the "columns" dimension and the second to the "Line" dimension of the Source Variable.

### Syntax: & nbsp;

Q01.TABMOD (Expression table; indentation)

Or

\ _TABMOD (Q01; Expression table; indentation)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| &#49; | Expression table | Character chain | Description Codes Table | Compulsory |
| &#50; | indentation | Character | & nbsp; | Default Space |


#### Examples:

\ _TABMOD (Q02A; "Countries")

Returns a variable that is the result of the application of the recodification table to the q02a variable.

#### NOIKS:

The Tabmod Function Removes The Spaces At the End of the Labels.

& nbsp;

& nbsp;

See also: [Utilities \ & Miscellaneous] (<Tools \ _misc1.md>)