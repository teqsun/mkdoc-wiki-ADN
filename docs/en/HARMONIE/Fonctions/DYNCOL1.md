# Dyncol

## Dyncol Function

Based on Reference Table which WHOTS A SET OF CODIFIED ELEMENTS, CREATES DYNAMIC Groupings with Hierarchy, All Controlled in External Tables.

### Syntax: & nbsp;

Q01.DYNCOL (table; index; matchmode; sorters; grouprs; codecolumn; textcolumn)

Gold

\ _DYNCOL (Q01; Table; index; matchmode; sorters; Grouprs; codecolumn; textcolumn)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| &#49; | Table | Character Chain | Description Codes Table | Compulsory |
| &#50; | Index | Character Chain | Table of Methods to Be Built | Compulsory |
| &#51; | Matchmode | Character Chain | Locating by Code OR GOLD Position Text.default Code | "Code"/Default Position/Text |
| &#52; | sorters | Character chain | List of Names Used to Sort | "" Default |
| &#53; | Grouprs | Character Chain | List of Table Names Used to Group | "" Default |
| &#54; | Codecolumn | Character Chain | Name of the column indications the codes of ref | compulsory |
| &#55; | Textcolumn | Character Chain | Name of the column Indicating the Texts of Ref | "" Default |

### EXAMPLES:

& nbsp;

See also: [Use of External Tables] (<usedablesexternes1.md>)