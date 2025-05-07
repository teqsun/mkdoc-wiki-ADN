# Redelete

## Redelete Function

The Function **Redelete** Removes Part of a Literal Variable Using A Regular Expression.

It's a bit of a rejection

& nbsp;

Arguments:

\- Regex & nbsp;: the regular expression that identifies what to delete

### Syntax: & nbsp;

Q01.REDELETE (expression)

Gold

\ _REDELETE (Q01; expression)

& nbsp;

|& nbsp;|**Name** |**Type** |**Description** |**Note** |
|--- |--- |--- |--- |--- |
|& nbsp;|Expression |Character chain |Regular expression of selection of modalities |Compulsory |

#### NOIKS:

For more information on regular expressions:

http://lgmorand.developpez.com/dotnet/regex/

& nbsp;

To test and build Regular expressions:

http://regexstorm.net/tester

http://www.ultrapico.com/expresso.htm

### EXAMPLES:

Dates.Redelete ("\\\ d \\ d/\\ d \\\ d/\\ d \\ d \\ d \\ d")

Returns a Literal variable in which the dates in jj/mm/aaa format are deleted.

& nbsp;

See also: & nbsp;

[Treat the Literal Variables] (<Trellious Little Little.md>)

[Regular expressions] (<regular \ _expresses1.md>)