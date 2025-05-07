# Rematch

## Rematch Function

The **Rematch** Function Returns A Filter Which Indicates Whother the Literal Variable Tested Checks The Regular Expression in Argument.

This fun is very Practical to check the right Writing of Complex Codes, Emails, Addes, etc.

& nbsp;

Arguments:

\- Regex & nbsp;: The Regular Expression Tested

### Syntax: & nbsp;

Q01.ratch (expression)

Or

\ _REMATCH (Q01; expression)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| & nbsp; | Expression | Character chain | Regular selection Expression | Compulsory |

#### NOIKS:

For more information on regular expressions:

http://lgmorand.developpez.com/dotnet/regex/

& nbsp;

To test and build Regular expressions:

http://regexstorm.net/tester

http://www.ultrapico.com/expresso.htm

### EXAMPLES:

Codes.rematch ("\^\\x w+$")

Returns a filter that gives 'True' for individuals who have given an alpha-numeric and 'false' code for tersrs.

& nbsp;

See also: [Regular expressions] (<regular \ _expressions1.md>)