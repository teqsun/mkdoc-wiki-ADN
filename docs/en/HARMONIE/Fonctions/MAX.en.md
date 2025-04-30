# Max

## Max function

The ** max ** function applies to a list of digital variables/constructions and returns a variable whose values ​​are the maximum of the values ​​encountered in the arguments.

& nbsp;

The base of the result is that of respondent to the 2 variables.

For the homeless people to be "neutralized", and the base encompasses respondents at least one of the variables, use Maxna.

### Syntax: & nbsp;

\ _Max (selection)

& nbsp;

|& nbsp;|** Name ** |** Type ** |** Description ** |** Note ** |
|--- |--- |--- |--- |--- |
|& nbsp;|Selection |Selection of variables |Expression of selection of variables (ex: '$ "s?"') Or list of variables separated by a ";"; "|Compulsory |


#### Examples:

\ _Max (Q04A; Q04B)

Returns a variable that caps q04a and q04b, for those whoswered the two questions.

& nbsp;

\ _Maxna (Q04A; Q04B)

Returns a variable that caps q04a and q04b, for Those whoswered at Least One of the Two Questions.

& nbsp;

See also: [Manipulate The Digital Variables] (<manipulatingsnurablesnumerics1.md>)