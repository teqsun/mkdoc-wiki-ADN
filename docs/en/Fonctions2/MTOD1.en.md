# Mtod

## Mtod Function

The ** Mtod ** Function Transforms A Multi-Answer Variable Into A Mono-Answer Variable.two possibilities are offered: eith the "smaller" of the terms mentioned is retained, or the function retains only those white given a single yearswer.

& nbsp;

The optional argument makes it possible to determine the work method:

FALSE (Default Value): The Smallest Modality Cited is retained

True: Only respondent who have cited only one methods are retained

### Syntax: & nbsp;

Q01.mtod (Singleansweronly)

Or

\ _Mtod (Q01; Singleansweronly)

& nbsp;

| & nbsp; | ** name ** | ** type ** | ** Description ** | ** Note ** |
| --- | --- | --- | --- | --- |
| & nbsp; | Singleansweronly | Boolean | by Default, Consider All The Answers | False by Default |

### EXAMPLES:

S6.Mtod ()

\ [or s6.mtod (false) \]

The Resulting Variable is a mono-yearswer Whose Responses Are Only The Smallest Methods mentioned.

& nbsp;

S6.Mtod (True)

The Resulting Variable is a mono-Anwer Whose Answers Are Those of Those Which Have Cited Only One Answer.

& nbsp;

See also: [Treat Logical Variables (Modalities)] (<TrelligablelogiquesModa1.md>)