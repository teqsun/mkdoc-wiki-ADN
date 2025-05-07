# Redelete

## Redelete function

The function **Redelete** removes part of a literal variable using a regular expression.

It's a bit like Reget

& nbsp;

Arguments:

\- Regex & nbsp;: the regular expression that identifies what to delete

### Syntax: & nbsp;

Q01.REDELETE (expression)

Or

\ _REDELETE (Q01; expression)

& nbsp;

|& nbsp;|**Name** |**Type** |**Description** |**Note** |
|--- |--- |--- |--- |--- |
|& nbsp;|Expression |Character chain |Regular expression of selection of modalities |Compulsory |


#### Remarks :

For more information on regular expressions:

http://lgmorand.developpez.com/dotnet/regex/

& nbsp;

To test and build regular expressions:

http://regexstorm.net/tester

http://www.ultrapico.com/expresso.htm

#### Examples:

Dates.Redelete ("\\\ d \\\ d/\\\ d \\\ d/\\\ d \\\ d \\\ d \\\ d")

Returns a literal variable in which the dates in JJ/MM/AAA format are deleted.

& nbsp;

See also: & nbsp;

[Treat the literal variables] (<Trellious Little Little.MD>)

[Regular expressions] (<regular \ _expresses1.md>)