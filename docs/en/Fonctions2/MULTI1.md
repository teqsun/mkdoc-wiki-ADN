# Multi

## Multi Function

The **Multi** Function Creates A Multi-Answer variable from a list of variables.

Each argument variable corresponds to a form of yes/no for a possible responsibility modality to the final variable.

We will only remember only a particular responsibility value for each of these variables.

### Syntax: & nbsp;

\ _Multi (Key; Sources)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| &#49; | Key | Value | Response Modality to be Retaineed in the Variables in Argument | Compulsory |
| &#50; | Sources | List of Variables | List of Variables to be treated | Compulsory |

& nbsp;

### EXAMPLES:

\ _Multi (2; Q01 \ _1; Q01 \ _2; Q01 \ _3; Q01 \ _4; Q01 \ _5; Q01 \ _6;)

The Result is a multi-answer variable to 6 modalities by considering the ANSWER 2

& nbsp;

See also: & nbsp;

[Treat the Multi-Responsion Variables] (<Trelliousvariableablesmulti-Répons1.md>)

[Combination the variables] (<combination thevariables1.md>)