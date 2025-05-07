# ANSWERS

## ANSWERS FUNCTION

The Answers Function Applied to A Multi-Answer Variable Returns A Digital Variable Which Contains the Number of Responses Cited for Each of the Individuals of the Original Variable.

### Syntax: & nbsp;

Q01.Aswers (USeductor)

Gold

\ _ANSWERS (Q01; USEREDUCTOR)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| & nbsp; | useductor | Boolean | Take Into Account the Reducer If True (Capped at 1) | False by Default |

#### NOIKS:

It is common to use the [dtoc] (<dtoc1.md>) Function Instead of Answers.& Nbsp;

In this case the reducing is always taken into account, and its values ​​are not capped at 1.

### EXAMPLES:

S6.Answers (True)

Returns a digital variable that contains the number of responsibilities mentioned, for example to calculate an average number of responsibilities.

& nbsp;

See also: [Treat the Multi-Responsion Variables] (<Trellablesvariablesmulti-respondes1.md>)