# Tabmod

## Tabmod function

The ** Tabmod ** function applies an external recodification table to a variable.

& nbsp;

The name of the table is indicated by a character string, according to the principle of identifying external tables.

& nbsp;

This function plays a particular role because it allows you to carry out all current operations on the methods (extractions, groups ...) by analysis of text file content, in CSV format.The definition is thus independent of studies and can be used in successive waves, with updates that will be taken into account automatically in the absence of variable storage. & Nbsp;

The result is always a logical, multi-answer or discreet variable.

& nbsp;

The treated variable can be digital or logical.

If the variable is digital, the codes indicated represent the digital values ​​to be used and are not necessarily present in the data.

If the variable is logical, the codes indicated correspond to methods and must be available, therefore at most to the number of methods.

The zero value (0) is authorized to generate empty methods.

& nbsp;

The columns of the read table follow the structure described below.

& nbsp;

The Code column contains the terms of methods to be grouped on the same line.

This is a simple list.

.17 & nbsp;& nbsp;The modality corresponds to the occurrences of code 17

.17 & nbsp;19 & nbsp;& nbsp;The modality corresponds to the occurrences of codes 17 or 19

.17 to 21 & nbsp;& nbsp;The modality corresponds to the occurrences of codes 17, 18, 19, 20 or 21 & nbsp;

& nbsp;

The Wording Column Indicates The Texts (Forced) or not (Resumption of the Initial Label).

To recover an initial label, put a "#".

& nbsp;

If the study includes several languages, the title of the column is supplemented by the International Code of the Language, in parentheses.Example: Long (FR), shorts (GB).

& nbsp;

The insertion of subtitles is authorized.In this case, only the labels columns are filled. & Nbsp;

The number of "\ &" which prioritizes the subtitles must be respected.

& nbsp;

The Tabcol and Tabrow functions work exactly on the same mode, but the first applies to the "columns" dimension and the second to the "line" dimension of the source variable.

### Syntax: & nbsp;

Q01.TABMOD (Table Expression; Indentation)

Or

\ _TABMOD (Q01; Table Expression; Indentation)

& nbsp;

|& nbsp;|** Name ** |** Type ** |** Description ** |** Note ** |
|--- |--- |--- |--- |--- |
|&#49;|Table Expression |Character chain |Descriptive codes table |Compulsory |
|&#50;|Indentation |Character |& nbsp;|Default space |


#### Examples:

\ _TABMOD (Q02A; "Countries")

Returns a variable which is the result of the application of the recodification table to the Q02A variable.

#### NOIKS:

The TABMOD function removes the spaces at the end of the labels.

& nbsp;

& nbsp;

See also: [Utilities \ & Miscellaneous] (<Tools \ _misc1.md>)