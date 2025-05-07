# Multi

## Multi Function

The **Multi** function creates a multi-answer variable from a list of variables.

Each argument variable corresponds to a form of yes/no for a possible responsibility modality to the final variable.

We will only remember only a particular response value for each of these variables.

### Syntax: & nbsp;

\ _Multi (Key; Sources)

& nbsp;

|& nbsp;|**Name** |**Type** |**Description** |**Note** |
|--- |--- |--- |--- |--- |
|&#49;|Key |Value |Response modality to be retained in the variables in argument |Compulsory |
|&#50;|Sources |List of variables |List of variables to be treated |Compulsory |


& nbsp;

#### Examples:

\ _Multi (2; Q01 \ _1; Q01 \ _2; Q01 \ _3; Q01 \ _4; Q01 \ _5; Q01 \ _6;)

The result is a multi-answer variable to 6 modalities by considering the answer 2

& nbsp;

See also: & nbsp;

[Treat the multi-response variables] (<TrelliousvariablesMulti-Répons1.md>)

[Combine the variables] (<combine thevariables1.md>)