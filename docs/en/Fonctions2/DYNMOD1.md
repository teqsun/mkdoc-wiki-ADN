# Dynmod

## DYNMOD FUNCTION

Based on Reference Table which WHOTS A SET OF CODIFIED ELEMENTS, CREATES DYNAMIC Groupings with Hierarchy, All Controlled in External Tables.

### Syntax: & nbsp;

Q01.DYNMOD (Table; Index; MatchMode; sorters; Groupers; Codecolumn; TextColumn)

Gold

\ _DYNMOD (Q01; Table; index; matchmode; sorters; grouprs; codecolumn; textcolumn)

& nbsp;

|& nbsp;|**Name** |**Type** |**Description** |**Note** |
|--- |--- |--- |--- |--- |
|&#49;|Table |Character chain |Descriptive codes table (Tamod) |Compulsory |
|&#50;|Index |Character chain |Table of methods to be built |Compulsory |
|&#51;|Matchmode |Character chain |Locating by code or position or text.Default code |"Code"/Default position/text |
|&#52;|Sorters |Character chain |List of table names used to sort |"" Default |
|&#53;|Grouprs |Character chain |List of table names used to group |"" Default |
|&#54;|Codecolumn |Character chain |Name of the column indicating the codes of ref |Compulsory |
|&#55;|Textcolumn |Character chain |Name of the column indicating the texts of Ref |"" Default |

### EXAMPLES:

& nbsp;

See also: [Use of External Tables] (<usedablesexternes1.md>)