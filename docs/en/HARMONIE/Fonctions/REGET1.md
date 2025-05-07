# Reget

## Reget Function

The **reget function** extracts part of a literal variable using a regular expression.

Very practical to extract the month of a date, the first part of a sentence, etc.

& nbsp;

Arguments:

\- Regex & nbsp;: Regular Extraction Expression.Each Group in Parentheses will be extraced.

\- Delimit: The Delimiter to Use to 'Paste' The Different Parts Extraced (Optional)

### Syntax: & nbsp;

Q01.Ret (expression; delimitis)

Gold

\ _REGET (Q01; Expression; Delimite)

& nbsp;

|& nbsp;|**Name** |**Type** |**Description** |**Note** |
|--- |--- |--- |--- |--- |
|&#49;|Expression |Character chain |Regular selection expression |Compulsory |
|&#50;|DELIMITE |Character chain |separator |"" Default |

#### NOIKS:

For more information on regular expressions:

http://lgmorand.developpez.com/dotnet/regex/

& nbsp;

To test and build Regular expressions:

http://regexstorm.net/tester

http://www.ultrapico.com/expresso.htm

### EXAMPLES:

Dates.reget ("\\ d \\\ d/(\\ d \\ d)/\\ d \\\ d \\ d \\ d")

Returns a literal variable which contains the month (the part in parentheses) from a variable which contains dates in JJ/MM/AAAA format.

& nbsp;

See also: [Regular expressions] (<regular \ _expressions1.md>)