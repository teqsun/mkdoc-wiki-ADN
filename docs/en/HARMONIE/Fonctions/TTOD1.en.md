# Ttod

## Ttod Function

The ** ttod ** Function is the Counterpart of the Dtot Function: It Translates A Literal Variable (Text) Into A Logical Variable With Modalities.& Nbsp;

It is possible to create a multi-answer variable by indicating the responsibilities.& Nbsp;

Finlly, Breakage can be taken into account or ignored.

& nbsp;

Argument 1: If True, The Breakage (Capital Letters/Tiny) is important, if false it is ignored.

Argument 2 (Optional): The Responses of Responses Used in the Texts, Between Double-Quotes.

### Syntax: & nbsp;

Q01.ttod (ignorecase; delimiters)

Or

\ _Ttod (q01; ignorecase; delimiters)

& nbsp;

|& nbsp;|** Name ** |** Type ** |** Description ** |** Note ** |
|--- |--- |--- |--- |--- |
|&#49;|Ignorecase |Boolean |Insensitive to the True Casse (Pass the Labels of the Modalities in Capotles) |False by default |
|&#50;|Delimiters |Character chain |Separator to use for multi-answers |Different by default |

### EXAMPLES:

Q01A.TTOD (True; ";")

Created a modality by text encountered in the responses, ignoring the breakage, and considering that the semicolon is a response delimiter.This example therefore produces a multi-answer variable.

& nbsp;

See also: [Treat the Literal Variables] (<Trellious Little Little.md>)