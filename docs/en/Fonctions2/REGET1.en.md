# Reget

## Reget Function

The ** Reget Function ** Extracts Part of a Literal Variable Using A Regular Expression.

Very Practical to Extract the Month of A Date, the first part of a sentence, etc.

& nbsp;

Arguments:

\- Regex & nbsp;: Regular Extraction Expression.Each Group in Parentheses will be extraced.

\- Delimit: The Delimiter to Use to 'Paste' The Different Parts Extraced (Optional)

### Syntax: & nbsp;

Q01.Ret (expression; delimitis)

Gold

\ _REGET (Q01; Expression; Delimite)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| &#49; | Expression | Character Chain | Regular Selection Expression | Compulsory |
| &#50; | Delimite | Character Chain | Separator | "" DEFAULT |

#### NOIKS:

For more information on regulating expressions:

http://lgmorand.developpez.com/dotnet/regex/

& nbsp;

To test and build Regular expressions:

http://regexstorm.net/tester

http://www.ultrapico.com/expresso.htm

### EXAMPLES:

Dates.reget ("\\ d \\\ d/(\\ d \\ d)/\\ d \\\ d \\ d \\ d")

Returns a literal variable that contains the month (the part in parentheses) from a variable which contains dates in jj/mm/aaaa format.

& nbsp;

See also: [Regular expressions] (<regular \ _expressions1.md>)