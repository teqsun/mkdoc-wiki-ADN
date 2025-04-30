# Rereplace

## Rereplace function

The ** Rereplace ** Function Replacements Parts of A Literal Variable With Another.

This very powerful function makes it possible to reformulate a text.

& nbsp;

Arguments:

\- Regex & nbsp;: The Regular Expression that identified what to replace

\- Replacement & nbsp;: Which you have to replace ($ 1, $ 2 etc. to use regex groups)

### Syntax: & nbsp;

Q01.rereplace (expression; replacement)

Gold

\ _Rereplace (Q01; expression; replacement)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| &#49; | Expression | Character Chain | Regular Selection Expression | Compulsory |
| &#50; | Replacement | Character Chain | New Channel | Compulsory |

#### NOIKS:

For more information on regulating expressions:

http://lgmorand.developpez.com/dotnet/regex/

& nbsp;

To test and build Regular expressions:

http://regexstorm.net/tester

http://www.ultrapico.com/expresso.htm

### EXAMPLES:

Dates.rereplace ("\\\ d \\ d/(\\ d \\ d)/\\ d \\ d \\ d \\ d"; "\! $ 1")

Returns a Literal variable in which dates in jj/mm/aaaa format are replaced by the month number prefixed by an exclamation mark.

& nbsp;

See also: [Regular expressions] (<regular \ _expressions1.md>)