# Reformat

## Reformat function

The ** Reformat ** function rewrites a literal variable using a regular expression.

& nbsp;

Arguments:

\- Regex & nbsp;: the regular expression that identifies what to deal with

\- Format & nbsp;: the rewriting format (use $ 1, $ 2 etc. to use regex subgroups)

### Syntax: & nbsp;

Q01.REFORMAT (expression; format)

Or

\ _REFORMAT (Q01; Expression; Format)

& nbsp;

|& nbsp;|** Name ** |** Type ** |** Description ** |** Note ** |
|--- |--- |--- |--- |--- |
|&#49;|Expression |Character chain |Regular selection expression |Compulsory |
|&#50;|Format |Character chain |Format |Different by default |


#### Remarks :

For more information on regular expressions:

http://lgmorand.developpez.com/dotnet/regex/

& nbsp;

To test and build regular expressions:

http://regexstorm.net/tester

http://www.ultrapico.com/expresso.htm

#### Examples:

Dates.reformat ("(\\\ d \\\ d)/(\\\ d \\\ d)/(\\\ d \\\ d \\\ d \\\ d)") ")

Returns a literal variable which only contains the date in JJ/MM/AAAA format.

& nbsp;

See also: [Treat the literal variables] (<Trellious Little Little.MD>)