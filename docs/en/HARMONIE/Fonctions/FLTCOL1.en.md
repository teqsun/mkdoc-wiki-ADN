# Fltcol

## FLTCOL function

The ** FLTCOL ** Filter function (puts "variables" and creates a column detail that corresponds to the title of the applied filter.The universe applied to the variable is that of those who responded to all the variables and/or constructions in arguments.

### Syntax: & nbsp;

Q01.Fltcol (Filter; Title)

Or

\ _FLTCOL (Q01; Filters; Title)

& nbsp;

|& nbsp;|** Name ** |** Type ** |** Description ** |** Note ** |
|--- |--- |--- |--- |--- |
|& nbsp;|Filter |Definition |Definition of the filter to be applied to variable data |Compulsory |
|& nbsp;|Title |Chain |Title to integrate in column of the result variable |Optional |


#### Examples:

S1.FLTCOL (S2 \> 50; "Over 50 years")

The variable obtained is dimensioned with 1 column and similar to the variable S1.But its data is filtered according to the respondents to S2 \> 50.

& nbsp;