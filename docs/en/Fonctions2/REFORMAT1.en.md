# Reformat

## Reformat Function

The ** Reformat ** Function Rewrites A Literal Variable Using A Regular Expression.

& nbsp;

Arguments:

\- Regex & nbsp;: The Regular Expression that identified what to deal with

\- Format & nbsp;: The Rewriting Format (Use $ 1, $ 2 etc. To use Regex subgroups)

### Syntax: & nbsp;

Q01.REFORMAT (expression; format)

Gold

\ _REFORMAT (Q01; Expression; Format)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| &#49; | Expression | Character Chain | Regular Selection Expression | Compulsory |
| &#50; | Format | Character Chain | Format | Different by Default |

#### NOIKS:

For more information on regulating expressions:

http://lgmorand.developpez.com/dotnet/regex/

& nbsp;

To test and build Regular expressions:

http://regexstorm.net/tester

http://www.ultrapico.com/expresso.htm

### EXAMPLES:

Dates.reformat ("(\\\ d \\ d)/(\\ d \\ d)/(\\ d \\ d \\ d \\ d \\ d)") ")") ")") ")") ")")

Returns a Literal variable which only contains the date in jj/mm/aaaa format.

& nbsp;

See also: [Treat the Literal Variables] (<Trellious Little Little.md>)