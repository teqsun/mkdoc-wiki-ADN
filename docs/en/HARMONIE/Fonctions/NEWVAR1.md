# Newvar

## Newvar function

The **Newvar** function generates a logical or digital variable.

### Syntax: & nbsp;

\ _Newvar (nbmod; Level; Dim; Value)

& nbsp;

| & nbsp; | **name** | **type** | **Description** | **Note** |
| --- | --- | --- | --- | --- |
| &#49; | Nbmod | Positive or Zero Integer | If 0 Creation of A Digital Variable If Not Number of Methods to Create | Compulsory |
| &#50; | Level | Character Chain | Target Level Name (The Variable Created Will Be On This Level) | Optional: Default Current Level |
| &#51; | Sun | Scalar or Vector | If Scalar, Number of Columns.if Vector (2 Values) Number of Lines on Number of Columns.& Nbsp; | Optional |
| &#52; | Value | Value | Value of the Response Or Modality.Can be a decimal value If Creation of A continuous variable | Optional |


& nbsp;

#### Examples:

\ _Newvar (0)

Creates a digital variable where all individuals are in homelessness.

& nbsp;

\ _Newvar (5)

Creates a logical variable with 5 modalities where all individuals are in homelessness.

& nbsp;

\ _Newvar (5; "Main \ _US"; null; 2)

Creates a logical variable to 5 modalities in the hand level \ _us where all individuals are in modality 2.

& nbsp;

\ _Newvar (0; null; 3 5; 100)

Creates a digital variable with 3 lines and 5 columns in the current level where all individuals have value 100.

& nbsp;

\ _Newvar (1; "Main \ _US"; null; 1) .txtmod (1; "set")

Creates a logical variable to a single modality bringing together all individuals and having the word "ensemble".It is therefore a filter which selects all individuals of the hand level \ _us.

& nbsp;

\ _Newvar (0; null; 10; 1) .cumcol ()

Creates a digital variable with 10 respective columns filled with values ​​1 to 10

& nbsp;

& nbsp;

See also: & nbsp;

[Manipulate digital variables] (<manipulatingVarirablesnumerics1.md>)

[Creation of variables (system, random ...)] (<creerdesvariablesdoutepiecesys.md>)