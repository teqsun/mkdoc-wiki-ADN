# Mtod

## Mtod function

The ** MTOD ** function transforms a multi-answer variable into a mono-answer variable.Two possibilities are offered: either the "smaller" of the terms mentioned is retained, or the function retains only those who have given a single answer.

& nbsp;

The Optional Argument Makes It Possible to Determine The Work Method:

False (default value): the smallest modality cited is retained

True: only respondents who have cited only one methods are retained

### Syntax: & nbsp;

Q01.mtod (Singleansweronly)

Or

\ _Mtod (Q01; Singleansweronly)

& nbsp;

|& nbsp;|** Name ** |** Type ** |** Description ** |** Note ** |
|--- |--- |--- |--- |--- |
|& nbsp;|Singleansweronly |Boolean |By default, consider all the answers |False by default |


#### Examples:

S6.Mtod ()

\ [or s6.mtod (false) \]

The Resulting Variable is a mono-yearswer Whose Responses Are Only The Smallest Methods mentioned.

& nbsp;

S6.Mtod (True)

The Resulting Variable is a mono-Anwer Whose Answers Are Those of Those Which Have Cited Only One Answer.

& nbsp;

See also: [Treat Logical Variables (Modalities)] (<TrelligablelogiquesModa1.md>)