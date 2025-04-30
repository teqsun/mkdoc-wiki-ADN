# Character chain utility documentation

## Introduction to characters in .Net
Characters (thongs) in .NET are immutable objects, which means that once created, they cannot be modified.Any operation that seems to modify a chain actually creates a new body.

The methods of the standard .NET library are supplemented by many methods of extension of the DNA library.Here is the list.

## Summary

-[Basic handling of channels] (#manipulation-basic-des-chaînes)
- [Lengthof] (#Lengthof)
- [Repeat] (#Repeat)
- [Issingleline] (#Issingleline)
- [singleline] (#singleline)
- [truncate] (#truncate)
- [COUNTSTARTCHAracters] (#cousstartcharacters)
- [countendcharacters] (#countendcharacters)
- [Countcharacters] (#Countcharacters)
- [Fixedlength] (#Fixedlength)
- [Removeemptystrings] (#RemoveemptyStrings)
- [hasmultilines] (#hasmultilines)
- [ismultiline] (#ismultiline)

-[Transformation and formatting of text] (#Transformation-et-formatage-de-text)
- [Removeaccents] (#Removeaccents)
- [Removeallbutlettersanddigits] (#Removeallbutlettersanddigits)
- [Removeallbutdigits] (#Removeallbutdigits)
- [extractive] (#extractive)
- [Removeif] (#Removeif)
- [Capitalize] (#Capitalize)
- [UNCAPITALIZE] (#UNCAPITALIZE)
- [Pascalize] (#Pascalize)
- [camelize] (#camelize)
- [underscore] (#underscore)
- [dasherize] (#dasherize)
- [minimize] (#minimize)
- [Titleize] (#Titleize)
- [Humanize] (#Humanize)
- [ordinalize] (#ordinalize)
- [initials] (#initials)
-[Striphtml / htmltostring] (#Striphtml--Htmltostring)
- [StringTohtml] (#Stringtohtml)
- [Clean] (#Clean)
- [SAUFTRIM] (#SAFETRIM)
- [align] (#align)

-[Research and comparison] (#Research-and-comparison)
- [containsignorecase] (#containsignorecase)
-[Containsoneof / Containsany] (#Containsoneof--Containsany)
- [Wildcardmatch] (#Wildcardmatch)
- [Fuzzycomompare] (#Fuzzycomompare)
- [AlphanumCompare] (#AlphanumCompare)
- [alphanumsort] (#alphanumsort)
- [FindCommonpart] (#FindCommonpart)
- [FindCommonPartoft] (#FindCommonPartoftst)
- [FindCommonroot] (#FindCommonroot)
- [comparers] (#comparestrings)
- [Comparative] (#Comparative)
- [Arenamesequal] (#Arenamesequal)
- [Startswithnocase] (#Startswithnocase)
-[Contains (with comparison)] (#contains-waits-comparison)

-[splitting and joint] (#fractionation-et-juinture)
- [scanlines] (#scanlines)
- [scanwords] (#scanwords)
- [split] (#split)
- [Splitignoringliterals] (#Splitignoringliterals)
- [Splitonsize] (#Splitonsize)
-[Joinwith / Tostring] (#Joinwith-Tostring)
- [Fromstring] (#fromstring)
- [Modifylines] (#Modifylines)
- [Extract] (#extract)
- [Getpart] (#Getpart)
- [Gertichtpart] (#Gertichtpart)

-[Conversion and Parsing] (#Conversion-et-Parsing)
-[SAFEPARS (Bool, Double, Int)] (#SAFEPARSE-BOOL-DOUBLE-INT)
- [Parsevalue] (#Parsevalue)
- [Parsevalues] (#Parsevalues)
- [Shapetevector] (#Parseintvector)
- [Parsoublevector] (#Parsoublevector)
- [Parsestringvector] (#parsestringvector)
- [Readinteger] (#Readinteger)
- [toenum] (#toenum)
- [Trytoenum] (#Trytoenum)
- [Toobject] (#Toobject)
- [Tochar] (#Tochar)
- [isnumber] (#isnumber)
- [isinteger] (#isinteger)
- [isbolean] (#isbolean)
-[ISEXPRESSTRUE / ISEXPRESSEFALSE] (#ISEXPRESSTRUE--ISEXPRESSEFALSE)
- [isintegervector] (#isintegervector)
- [isnumericrange] (#isnumericrange)
- [Tryparsenumericrange] (#Tryparsenumericrange)
- [isnumericexpression] (#isnumericexpression)
- [resolvenuexpression] (#resolvenuexpression)
- [Tryevaluatémericexpression] (#Tryevaluatémericexpression)

-[Namage and identification] (#NAMME-ET-identification)
- [iskeyword] (#iskeyword)
- [iskeywordpath] (#iskeywordpath)
- [ismetakeyword] (#ismetakeyword)
- [isname] (#isname)
- [Issymbolname] (#Issymbolname)
-[Arrangename / Nameize] (#Arrangename--Nameize)
- [ENSUREUNIENENAME] (#ENSUREUNIENAME)
- [ENSUREUNIENEMENTS] (#ENSUREUNIQUENAMES)
- [ENSUREUNIQUEFILENAME] (#ENSUREUNIQUEFILENAME)
- [NewUuniename] (#NewUuniquename)
- [NewUuniqueid] (#NewUuniqueid)
- [Findrootname] (#findrootname)
- [iscodexpression] (#iscodeexpression)
- [Getcodeexpressionvalue] (#Getcodeexpressionvalue)
- [formatcodeexpression] (#formatcodeexpression)
- [Ientityexpression] (#Ientityexpression)
- [Getentityexpressionvalue] (#getentityexpressionvalue)
- [Formatentyexpression] (#Formatentyexpression)

-[Eacoding support and internationalization] (#support-dencodes and internationalization)
- [detectencoding] (#detectencoding)
- [fixencoding] (#fixencoding)
- [Recode] (#recode)
- [ToutF8] (#ToutF8)
- [Todefaultencoding] (#Todefaultencoding)
-[isupper / islower] (#isupper--islower)
- [isunactenedletter] (#isunaccentedletter)
- [isunactenedletterordigit] (#isunactenedletterordigit)

-[Utilities for files and paths] (#Utilities-Pour-Fichiers-et-Chemins)
- [assumeiocompaitable] (#assumeiocompatible)
- [Comparatefilenames] (#Comparefilenames)
- [Comparepaths] (#Comparepaths)
- [normalizepath] (#normalizepath)
- [Makevalidfilename] (#Makevalidfilename)
- [Makepath] (#Makepath)
- [IsabsolutePath] (#IsabsolutePath)
- [isrelativepath] (#isrelativepath)
- [Formatfilesize] (#FormatfileSize)
- [cleanurl] (#cleanurl)
- [isurl] (#isurl)

-[Expressions and patterns] (#Expressions-and-Patterns)
- [haswildcard] (#haswildcard)
- [Removewildcards] (#Removewildcards)
- [Iswildcard] (#iswildcard)
- [Containsjoker] (#Containsjokeer)
- [Istag] (#istag)
- [Istagexactly] (#isatingxactly)
-[UTAGSTRING / UNTAGSTRENGEX] (#UNTAGSTRING--UTAGSTRIngex)
- [UntagText] (#Untagtext)
- [Untagobject] (#UNTAGOBJECT)
- [Extracts] (#extractations)
- [Hasannotation] (#hasannotation)
- [Parseannotation] (#Parsannotation)
- [smartformat] (#smartformat)
- [LookslikeSectionPattern] (#lookslikesectionpattern)
- [parsexmlattributes] (#parsexmlattributes)
- [Formatasxmlattributesstring] (#Formatasxmlattributessring)
- [Reget] (#reget)
-[FindmatchingParenthese / FindmatchingClosingChar] (#FindMatchingParenthese--FindmatchingClosingChar)
- [isterminallexPression] (#isterminallexPression)

- [Specific utilities] (#-specific utilities)
- [Lookslikeemail] (#lookslikeemail)
- [lookslikejson] (#lookslikejson)
- [lookslikexml] (#lookslikexml)
-[Zipstring / Unzipstring] (#Zipstring--unzipstring)
- [hashstring] (#hashstring)
-[bytestohexa / hexatobytes] (#bytestohexa--hexatobytes)
- [shuffle] (#shuffle)
-[quote / unquote] (#quote-unquote)
- [Succot] (#Autoquote)
-[Slashstring / Unslashstring] (#Slashstring-Unslashstring)
- [AutoFormatvalue] (#AutoFormatvalue)
- [Getautoformat] (#Getautoformat)
- [GettimesTamp] (#GettimesTamp)
- [GetprettyTimesTamp] (#GetprettyTimesTamp)
- [inject] (#inject)
- [generaterandomstring] (#generaterandomstring)
- [toexceladdress] (#toexceladdress)
- [Isexceladdress] (#Isexceladdress)
- [FORMATEXCELTEXT] (#FORMATEXCELTEXT)

## Basic chain manipulation

### Lengthof
Return the length of a chain, or 0 if the chain is null.
`` python
length = strings.lengthof ("hello") # returns 5
length = strings.lengthof (none) # returns 0
`` `

### Repeat
Repeat a chain a specified number of times.
`` python
Repeated = "ABC". Repeat (3) # returns "abcabcabc"
`` `

### Issingleline
Check if a chain does not contain feedback.
`` python
Result = "Hello World" .issingleline () # returns true
Result = "Hello \ nworld" .issingleline () # returns false
`` `

### Singleline
Converts a multi-line chain into a single line by replacing feedback from the line with spaces.
`` python
Text = "Hello \ nworld" .Singleline () # returns "hello world"
`` `

### Truncate
Tronque a chain at a maximum length, with different options.
`` python
Text = "Hello World, How Are You Today?". Truncate (10)
# Return "Hello World ..."

# With the Finishword option to complete the last word
Text = "Hello World, How Are You Today?". Truncate (10, truncateoptions.finishword)
# Return "Hello ..."
`` `

### Countstartcharacters
Count the number of characters specified at the start of a chain.
`` python
Count = "!! hello". COURTSTARTCHAracters ("!", "!") # Return 2
`` `

### CountEndCharacters
Compte le nombre de caractères spécifiés à la fin d'une chaîne.
```python
count = "Hello!!".CountEndCharacters("!", "!")  # Retourne 2
```

### Countcharacters
Count the number of occurrences of the characters specified in a chain.
`` python
Count = Strings.Countcharacters ("Hello World", "L", "O") # returns 4
`` `

### Fixedlength
Align a chain to the right or left to reach a specified length.
`` python
text = thongs.fixedlength ("ABC", 5) # returns "ABC"
Text = strings.fixedlength ("ABC", 5, "0") # returns "00abc"
Text = strings.fixedlength ("ABC", 5, "", false) # returns "ABC"
`` `

### Removeemptystrings
Remove the empty channels from a list.
`` python
strings = ["a", "", "b", "", "c"]
Thongs.removeemptystrings (thongs) # Modifies the list: ["A", "B", "C"]
`` `

### Hasmultilines
Check if a chain contains several lines.
`` python
Result = "Hello \ nworld" .hasmultilines () # returns true
`` `

### Ismultiline
Check if a chain contains several lines (aka of hasmultilines).
`` python
RESULT = "Hello \ nworld" .ismultiline () # Return True
`` `

## Text transformation and formatting

### Removeaccents
Remove the accents from a chain.
`` python
Text = "eàçèñ" .removeaccents () # returns "eacen"
`` `

## Removeallbutlettersanddigits
Remove all characters that are neither letters nor figures.
`` python
Text = "Hello, world! 123" .removeallbutlettersanddigits () # returns "helloworld123"
`` `

### Removeallbutdigits
Remove all characters that are not figures.
`` python
Text = "Hello, world! 123" .removeallbutdigits () # returns "123"
`` `

### Extract
Extract the characters that satisfy a condition.
`` python
# Extract only vowels
Text = "hello world". Extractive (lambda c: c in "aeiouaeiou") # returns "eoo"
`` `

### Removeif
Delete the characters that satisfy a condition.
`` python
# Remove vowels
Text = "hello world" .removeif (lambda c: c in "aeiouaeiou") # returns "hll wrld"
`` `

### Capitalize
Met en majuscule la première lettre d'une chaîne.
```python
text = "hello world".Capitalize()  # Retourne "Hello world"
```

### Uncapitalize
Met en minuscule la première lettre d'une chaîne.
```python
text = "Hello world".Uncapitalize()  # Retourne "hello world"
```

### Pascalize
Converts a chain into Pascalcase.
`` python
Text = "hello_world". Pascalize () # returns "helloworld"
`` `

### Camelize
Converts a chain into camelcase.
`` python
Text = "hello_world" .camelize () # returns "helloworld"
`` `

### Underscore
Convertit une chaîne en snake_case.
```python
text = "HelloWorld".Underscore()  # Retourne "hello_world"
```

### Dasherize
Converts a chain into Kebab-Case.
`` python
Text = "helloworld" .dasherize () # returns "hello-world"
`` `

### Minimize
Minimizes a chain by deleting accents and keeping only letters and numbers, converted into uppercase.
`` python
Text = "Hello, World! 123". Minimize () # returns "helloworld123"
`` `

### Titleize
Converts a chain into title format (capital letters for each word).
`` python
Text = "hello_world" .titleize () # returns "hello world"
`` `

### Humanize
Makes a chain more readable for humans.
`` python
Text = "Hello_World". Humanize () # returns "Hello World"
`` `

### Ordinalize
Converts an ordinal number.
`` python
Text = "1". Ordeinalized () # returns "1st"
Text = "2" .cordinalize () # returns "2nd"
`` `

### Initials
Extract the initials from a chain.
`` python
initials = thongs.initials ("hello world") # returns "hw"
`` `

### Striphtml / HTMLTOSTRING
Remove the HTML tags from a chain.
`` python
Text = "<p> Hello <b> World </b> </p>". Striphtml () # returns "Hello World"
`` `

### StringTohtml
Converts a chain into HTML format (replaces the feedback with the line with <br/>).
`` python
html = "hello \ nworld" .stringtohtml () # returns "hello <br/> world"
`` `

### Clean
Clean a chain by removing HTML, line feedback, etc.
`` python
Text = "<p> hello \ nworld </p>". Clean () # returns "Hello World"
`` `

### SAFETRIM
Removes the white spaces from a chain, returns an empty chain if the entrance is null.
`` python
Text = "Hello". Safetrim () # returns "Hello"
text = none.safertrim () # returns ""
`` `

### align
Align a chain according to a specified width and alignment.
`` python
Text = "Hello". Align (10, horizontalalignment.left) # returns "hello"
Text = "Hello". Align (10, horizontalalignment.right) # Return "Hello"
`` `

## Research and comparison

### Containsignorecase
Check if a chain contains a sub-chain, without taking the breakage into account.
`` python
result = "hello world" .containsignorecase ("world") # returns true
`` `

### Containsoneof / Containsany
Check if a chain contains at least one of the specified characters.
`` python
RESULT = "Hello World" .containsany ('x', 'y', 'z', 'o') # returns true (contains 'o')
`` `

### WildCardmatch
Check if a chain corresponds to a pattern with Jokers (* and?).
`` python
result = thongs.wildcardmatch ("te? t", "test") # returns true
RESULT = thongs.wildcardmatch ("te*", "test") # returns true
RESULT = strings.wildcardmatch ("te? t", "text") # returns false
RESULT = strings.wildcardmatch ("*is", "test") # returns true
`` `

### FuzzyCompare
Compare deux chaînes et retourne un pourcentage de similitude (0 à 100).
```python
similarity = Strings.FuzzyCompare("hello", "hallo")  # Retourne un score comme 80
```

### AlphaNumCompare
Compare deux chaînes de façon alphanumérique (trie "A2" avant "A10").
```python
result = Strings.AlphaNumCompare("A2", "A10")  # Retourne une valeur négative
```

### Alphanum comes out
Sort a list of channels in an alphanumeric manner.
`` python
Sorted = ["A1", "A10", "A2"]. Alphanumsort () # returns ["A1", "A2", "A10"]
`` `

### FindCommonpart
Find the common part at the start of several channels.
`` python
thongs = ["Abcdef", "ABCXYZ", "ABCGHI"]
Common = Strings.findcommonpart (Strings) # Return "ABC"
`` `

### FindCommonPartoft
Find the end position of the common part with several channels.
`` python
thongs = ["abcdef", "abcxyz"]
offset = thongs.findcommonpartoft (thongs) # returns 3
`` `

### FINDCOMMONROOT
Find the common root in a list of channels (useful for identifiers).
`` python
strings = ["user_profile", "user_settings", "user_account"]
root = thongs.findcommonroot (thongs) # returns "user"
`` `

### Comparentrings
Compare two channels, with option to ignore the breakage.
`` python
RESULT = thongs.compastrings ("ABC", "ABC", True) # returns 0 (equal)
`` `

## Comparative
Compare two entities (ignoring the breakage).
`` python
RESULT = thongs.Comparenames ("usenty", "usenty") # Return 0 (equal)
`` `

### AreNamesEqual
Vérifie si deux noms d'entités sont égaux (ignorant la casse).
```python
result = Strings.AreNamesEqual("UserEntity", "userentity")  # Retourne True
```

### Starswithnocase
Check if a chain starts with a specified sub-chain, without taking into account the breakage.
`` python
RESULT = "Hello World". STARTSWITHNOCASE ("Hello") # Return True
`` `

### Contains (with comparison)
Check if a chain contains a sub-chain with a specified mode of comparison.
`` python
RESULT = "Hello World" .contains ("world", thongcompaperison.ordinalignorecase) # Return True
`` `

## Fraction and joint

### Scanlines
Return each line of a text in the form of a list.
`` python
Lines = "Hello \ nworld" .Scanlines () # returns ["hello", "world"]
`` `

### Scanwords
Analysis a chain and returns the words in the form of a list.
`` python
Words = Strings.Scanwords ("Hello, World!") # Return words ["Hello", "World"]
`` `

### Split
Divide a chain into parts according to specified options.
`` python
shares = "hello, world" .Split (splitstringoptions ()) # returns ["hello", "world"]
`` `

### Splitigningliterals
Divides a chain but ignores the delimiters who are in literal chains.
`` python
shares = 'hello, "world, test", bye'.splitignantrals (', ')
# Return ["Hello", "\" World, Test \ "", "Bye"]
`` `

### Splitonsize
Divide a chain into equal size parts.
`` python
shares = "helloworld". SPLITONSIZE (5) # returns ["hello", "world"]
`` `

### Joinwith / Tostring
Joined a collection of channels with a delimiter.
`` python
joined = ["hello", "world"]. Joinwith (",") # returns "hello, world"
`` `

### fromstring
Divide a chain into parts according to delimitors and clean up each party.
`` python
Parts = strings.fromstring ("Hello, world", ',') # returns ["hello", "world"]
`` `

### Modifylines
Modify each line of a text using a function.
`` python
Text = thongs.modifylines ("Hello \ nworld", lambda line: line.tour ())
# Return "Hello \ NWORLD"
`` `

### Extract
Extract a sub-chain according to a start index and a length.
`` python
Sub = "HELLOWORLD". EXTRACT (2, 5) # Return "Ellow"
`` `

### Getpart
Extract a specific part of a delimited chain.
`` python
Part = "one.two.three" .Getpart ('.', 2) # returns "Two"
`` `

### Gertichtpart
Extract the right part from a delimited chain from a position.
`` python
Part = "one.two.three" .Getrightpart ('.', 1) # returns "Two.three"
`` `

## Conversion et parsing

### SAFEPARS (Bool, Double, INT)
Try to convert a chain into typical value, returns a default value in the event of failure.
`` python
Value = thongs.safeparse ("123", 0) # returns 123 (int)
Value = thongs.safeparse ("12.34", 0.0) # returns 12.34 (double)
Value = thongs.safeparse ("True", False) # Return True (Bool)
`` `

### ParseValue
Convertit une chaîne en valeur typée (bool, int, double ou string).
```python
value = Strings.ParseValue("123")    # Retourne 123 (int)
value = Strings.ParseValue("12.34")  # Retourne 12.34 (double)
value = Strings.ParseValue("true")   # Retourne True (bool)
value = Strings.ParseValue("hello")  # Retourne "hello" (string)
```

### PARSEVALUES
Divide a chain on a delimiter and converts each part into typical value.
`` python
values ​​= thongs.parsevalues ​​("123; 12.34; True; hello")
# Returns [123, 12.34, True, "Hello"]
`` `

### Slowing
Converts a chain into a whole table.
`` python
Values ​​= thongs.parseintvector ("1.2,3,4") # returns [1, 2, 3, 4]
`` `

### Parsoublevector
Converts a chain into a floating comma number table.
`` python
Values ​​= thongs.parsedoublevector ("1.1; 2.2; 3.3") # returns [1.1, 2.2, 3.3]
`` `

### PARSESTRINGVECTOR
Converts a chain into a chain table.
`` python
values ​​= thongs.parsestringvector ("One, Two, Three") # returns ["One", "Two", "Three"]
`` `

### Readinteger
Has read an integer since the start of a chain.
`` python
Value = Strings.Radinteger ("123ABC", 0) # Return 123
`` `

### Toenum
Converts a chain into enumeration value.
`` python
Value = "Monday" .toenum (dayofweek) # Return dayofweek.monday
`` `

### Trytoenum
Try to convert a chain into enumeration value, returns a default value in the event of failure.
`` python
Value = "Monday" .Trytoenum (dayofweek.sunday) # returns dayofweek.monday
Value = "Invalid" .Trytoenum (dayofweek.sunday) # returns dayofweek.sunday
`` `

### Toobject
Converts a chain into a typical object.
`` python
Obj = Strings.toobject ("123") # returns 123 (int)
obj = thongs.toobject ("12.34") # returns 12.34 (double)
Obj = Strings.toobject ("True") # Return True (Bool)
`` `

### Tochar
Converts a chain into character (takes the first character).
`` python
Char = "ABC" .tochar () # returns 'a'
`` `

### isnumber
Check if a chain represents a number.
`` python
result = thongs.isnumber ("123") # returns true
RESULT = thongs.isnumber ("12.34") # Return True
result = thongs.isnumber ("ABC") # Return False
`` `

### isinteger
Check if a chain represents an integer.
`` python
RESULT = Strings.isinteger ("123") # Return True
RESULT = Strings.isinteger ("12.34") # Return FALSE
`` `

### ISBOOLEAN
Check if a chain represents a Boolean value.
`` python
RESULT = thongs.isbolean ("True") # Return True
result = thongs.isbolean ("false") # returns true
result = thongs.isbolean ("123") # returns false
`` `

### ISEXPRESSTRUE / ISEXPRESSEFALSE
Check if a chain represents a "true" or "false" expression (includes "yes", "no", "true", "false", etc.).
`` python
RESULT = "yes" .ISxpressruetrue () # Return True
result = "no" .isexpressionfalse () # returns true
`` `

### isintegervector
Check if a chain represents a whole vector.
`` python
RESULT = "1.2,3" .isintegervec () # returns true
`` `

### isnumericrange
Check if a chain represents a digital beach (ex: "1..10").
`` python
result = "1..10" .isnumericrange () # returns true
`` `

### Tryparsenumericrange
Tent to convert a chain into a digital beach.
`` python
Success = "1..10" .Tryparsenumericrange (out from, out to, out step)
# Success = True, from = 1, to = 10, step = 1
`` `

### isnumericexpression
Check if a chain represents a digital expression (vector or beach).
`` python
result = "1.2.3" .isnumericexpression () # returns true
result = "1..10" .isnumericexpression () # returns true
`` `

### Resolvenuexpression
Resolves a digital expression in whole sequence.
`` python
Values ​​= "1..5" .Resolvenuexpression () # returns [1, 2, 3, 4, 5]
Values ​​= "1.3.5" .Resolvenuexpression () # returns [1, 3, 5]
`` `

### Tryevaluatémericexpression
Try to assess a digital expression.
`` python
Success = "1..5". TRYYEVALUATENCEXPRESSPRESSE (OUT VALUES)
# Success = True, values ​​= [1, 2, 3, 4, 5]
`` `

## NAGISSE AND IDENTIFICATION

### Iskeyword
Check if a chain is a valid keyword (starts with a letter or a Underscore, followed by letters, figures or underscores).
`` python
result = "myvar_123" .iskeyword () # returns true
result = "123var" .iskeyword () # returns false
`` `

### iskeywordpath
Check if a chain is a valid keyword path (keywords separated by points).
`` python
result = "module.class.method" .iskeywordpath () # returns true
`` `

### ismetakeyword
Check if a chain is a key metal (starts with $).
`` python
RESULT = "$ variable" .ismtakeyword () # returns true
`` `

### ISNAME
Check if a chain is a valid name (alias of Iskeyword).
`` python
result = thongs.isname ("myvariable") # returns true
`` `

### Issymbolname
Check if a chain is a valid symbol name (alias de Iskeyword).
`` python
result = "mysymbol" .issymbolname () # returns true
`` `

### Arrangename / Nameize
Arrange a chain to make it a valid name.
`` python
name = "variable my variable 123" .nameize () # returns "myvariable123"
name = "123invalid". Arrangename ("_") # returns "_123invalid"
`` `

### ENSUREUNIENAME
Ensures that a name is unique in a collection, adding a digital suffix if necessary.
`` python
Name = thongs.seureunianame ("File", ["File", "File_1"]) # returns "File_2"
`` `

### ENSUREUNIQUENAMES
Ensures that all the names of a list are unique between them.
`` python
Names = thongs.seureunicenumes (["File", "File", "Report"]) # returns ["File", "File_1", "Report"]
`` `

### ENSUREUNIQUEFILENAME
Ensures that a file name is unique on the disk, adding a digital suffix if necessary.
`` python
Filename = Strings.seureuniquefilename ("C: \\ Data \\ Report.txt") # Return "C: \\ Data \\ Report_1.txt" If the file already exists
`` `

### NewUniquename
Generates a unique new name based on a model, adding a digital suffix.
`` python
Name = Strings.Newunicename ("Item", ["Item", "Item_1"]) # Return "Item_2"
`` `

### NewUniqueid
Generates a new unique identifier based on a guid.
`` python
id = thongs.newniqueid () # returns a unique chain like "8F9D5F7B3A2E1C"
`` `

### FINDROOTNAME
Extract the root from a name (the part before the last delimiter).
`` python
ROOT = "User_settings_Profile" .findrootname () # returns "User_settings"
`` `

### iscodeexpression
Check if a chain is an expression of code (starts with $).
`` python
RESULT = "$ 123". ISCODEXPRESSPRESS () # Return True
`` `

### Getcodeexpressionvalue
Extracts the numerical value from an expression of code.
`` python
Value = "$ 123" .Getcodeexpressionvalue () # returns 123
`` `

### Formatcodeexpression
Formats a value in code expression.
`` python
expr = font.formatcodeexpression (123) # returns "$ 123"
`` `

### Ientityexpression
Check if a chain is an expression of entity (starts with @).
`` python
RESULT = "@entity". ISENTITYEXPREST () # Return True
`` `

### Getentityexpressionvalue
Extracts the name from an entity expression.
`` python
Name = "@entity" .gestntyexpressionvalue () # returns "entity"
`` `

### Formatentyexpression
Formats a name in entity expression.
`` python
expr = font.formatentyexpression ("entity") # returns "@entity"
`` `

## Eacoding support and internationalization

### DetectEncoding
Détecte l'encodage d'une chaîne.
```python
encoding = Strings.DetectEncoding(textContent)  # Retourne l'encodage détecté
```

### Fixencoding
Repair the encoding of a chain in the event of a problem.
`` python
Fixed = problemmatictext.fixencoding () # Tent to correct encoding problems
`` `

### Recode
Changes the encoding of a chain.
`` python
Recoded = text.recode (encoding.ascii, encoding.utf8) # convert from ascii to utf8
`` `

### Toutf8
Converts a chain into UTF-8.
`` python
utf8Text = nonutf8Text.toutf8 () # Converted into UTF-8
`` `

### Todefaultencoding
Converts a chain to default encoding.
`` python
DEFAULTTEXT = UTF8TEXT.TODEFAULTENCODING (encoding.utf8) # Convert from UTF-8 to default encoding
`` `

### Isupper / IsLower
Check if a chain is entirely in upper or lower case (ignores non-alphabetic characters).
`` python
RESULT = "Hello123" .SUPPER () # Return True
result = "hello123" .islower () # returns true
`` `

### isunactenedletter
Check if a character is an unchanged letter.
`` python
RESULT = 'a'. isunactenedletter () # returns true
RESULT = 'é'. isunactenedletter () # returns false
`` `

### IsUnaccentedLetterOrDigit
Vérifie si un caractère est une lettre non accentuée ou un chiffre.
```python
result = 'a'.IsUnaccentedLetterOrDigit()  # Retourne True
result = '1'.IsUnaccentedLetterOrDigit()  # Retourne True
result = 'é'.IsUnaccentedLetterOrDigit()  # Retourne False
```

## Utilities for files and paths

### Assumeiocompatible
Replaces characters not compatible with files with underscores.
`` python
path = strings.ssumeiocompatible ("File: name.txt") # returns "file_name.txt"
`` `

### Compared
Compare two file names by ignoring the breakage and normalizing the path separators.
`` python
RESULT = Strings.Comparefilenames ("C: \\ Folder \\ File.txt", "C: /folder/file.txt") # Return 0 (equal)
`` `

### ComparePaths
Compare deux chemins (alias de CompareFileNames).
```python
result = Strings.ComparePaths("c:\\folder\\file", "C:/folder/file")  # Retourne 0 (égaux)
```

### Normalizepath
Normalized a path by replacing the path separators with the system separator.
`` python
path = thongs. Normalizepath ("C:/folder/file") # returns "C: \\ Folder \\ File" on Windows
`` `

### Makevalidfilename
Transform a valid file name by replacing the invalid characters.
`` python
Filename = "File*name? .txt". Makevalidfilename () # returns "File_name_.txt"
`` `

### Makepath
Create a path from a collection of segments.
`` python
path = thongs.makepath (["folder", "subfolder", "file.txt"]) # returns "folder/subfolder/file.txt"
`` `

### Isabsolutepath
Check if a path is absolute.
`` python
RESULT = thongs.isabsolutepath ("C: \\ Folder \\ File.txt") # Return True
result = thongs.isabsolutepath ("folder/file.txt") # returns false
`` `

### isrelativepath
Check if a path is relative.
`` python
result = thongs.isrelativepath ("folder/file.txt") # returns true
result = strings.isrelativepath ("C: \\ Folder \\ file.txt") # Return False
`` `

### FormatFileSize
Formate une taille de fichier en chaîne lisible (KB, MB, etc.).
```python
size = Strings.FormatFileSize(1024 * 1024)  # Retourne "1.0 MB"
```

### Cleanurl
Clean an URL by removing the final slash.
`` python
URL = Strings.Cleanurl ("http://example.com/") # returns "http://example.com"
`` `

### isurl
Check if a chain is an URL.
`` python
result = thongs.isurl ("http://example.com") # returns true
`` `

## Expressions and patterns

### HasWildcard
Vérifie si une chaîne contient des caractères joker (* ou ?).
```python
result = "file*.txt".HasWildcard()  # Retourne True
```

### Removewildcards
Remove the Joker characters from a chain.
`` python
Text = "File*.txt" .removewildcards () # returns "file.txt"
`` `

### Iswildcard
Check if a character is a joker.
`` python
RESULT = '*'. Iswildcard () # Return True
`` `

### ContainsJoker
Vérifie si une chaîne contient des jokers (alias de HasWildcard).
```python
result = "file*.txt".ContainsJoker()  # Retourne True
```

### Istag
Check if a chain contains format tags [TAG].
`` python
Result = thongs.istag ("This is a [tag]") # returns true
`` `

### Istagexactly
Check if a chain is exactly a format tag [TAG].
`` python
RESULT = "[tag]". ISTAGEXActly () # Return True
`` `

### UntagString / UntagStringEx
Remplace les tags dans une chaîne par leurs valeurs correspondantes dans un dictionnaire.
```python
values = {"NAME": "John", "AGE": 30}
text = Strings.UntagString("Hello [NAME], you are [AGE] years old", values)
# Retourne "Hello John, you are 30 years old"
```

### Untagtext
Replaces the tags in a text object with their corresponding values.
`` python
Values ​​= {"name": "John", "Age": 30}
RESULT = thongs.attagtext (textobject, values) # replaces tags in the text text
`` `

### UNTAGOBJECT
Replaces the tags in an object (chain or text) with their corresponding values.
`` python
Values ​​= {"name": "John", "Age": 30}
RESULT = thongs.attagobject ("[name] is [age]", values) # returns "john is 30"
`` `

### extractations
Extract the annotations (tags) from a chain.
`` python
Annotations = Strings.EXTRACTANTIVATIONS ("This is [Tag: Format] A Test")
# Return a dictionary with {"tag": "format"}
`` `

### Hasannotation
Check if a chain contains annotations.
`` python
result = thongs.hasannotation ("This is [tag] a test") # returns true
`` `

### Parseannotation
Analysis an annotation in a chain.
`` python
Success = strings.parseannotation ("[type] value", out name, out value)
# Success = True, name = "Type", value = "value"
`` `

### Smartformat
Formats a chain with advanced substitution values.
`` python
Values ​​= {"name": "John", "Count": 3}
Text = "Hello {name}, you have {Count} messages" .smartformat (values)
# Return "Hello John, you have 3 messages"
`` `

### LOOKSLIKESELECTEPTERN
Check if a chain looks like a selection pattern.
`` python
RESULT = "[Property] = 'VALUE'". LOOKSLIKESELECTEPTERN () # Return True
`` `

### Parsexmlattributes
Sprinkled with XML attributes in a chain.
`` python
attributes = thongs.parsxmlattributes ("set name = \" value \ "title = \" Example \ "")
# Return a dictionary with {"name": "value", "title": "Example"}
`` `

### Formatasxmlattributessring
Format a chain dictionary of XML attributes.
`` python
attributes = {"name": "value", "title": "Example"}
XML = attributes.FormatasxMlattributeString ("set")
# Return "set name = \" value \ "title = \" Example \ ""
`` `

### Reget
Extract from the parts of a chain using a regular expression.
`` python
Regex = New Regex (@"(\ D+)-(\ D+)")
Text = "ID: 123-456"
Result = text.reget (Regex, "-") # returns "123-456"
`` `

### FindmatchingParenthese / FindmatchingClosingChar
Find the parenthesis/hug/closing hook corresponding to an opening.
`` python
Index = "Function () {Return True;}". FindmatchingParenthese (8) # returns 10
`` `

### isterminalelexPression
Check if an expression is terminal (simple identifier or expression already in parentheses).
`` python
RESULT = "variable". TRAYMINALE () # Return True
RESULT = "(x + y)". IsterminalelexPression () # Return True
RESULT = "x + y". TRAYMINALE () # returns false
`` `

# Specific utilities

### Lookslikeemail
Check if a channel looks like an email address.
`` python
Result = "User@example.com" .Lookslikeemail () # Return True
`` `

### Lookslikejson
Check if a chain looks like JSON.
`` python
Result = '{"name": "John"}'. Lookslikejson () # Returns True
`` `

### Lookslikexml
Check if a chain looks like XML.
`` python
RESULT = "<Ueser> John </User>". LOOKSLIKEXML () # Return True
`` `

### ZIastring / UNZIPSTRING
Compresses and decompresses a chain.
`` python
compressed = thongs.zipstring ("very long text to compress")
Decompressed = thongs.unzipstring (compressed) # returns "very long text to compress"
`` `

### Hashstring
Ax a chain to create a shorter version.
`` python
hashed = thongs.hashstring ("text to chop", 8) # Returns a chain of 8 characters
`` `

### bystohexa / hexatobytes
Converts between bytes and their hexadecimal representation.
`` python
hexa = thongs.bytestohexa (bytearray) # converts bytes into a hexadecimal chain
bytes = thongs.Hexatobytes ("0A1B2C") # Converts a hexadecimal chain in bytes
`` `

### Shuffle
Mix a chain in an cryptographic way.
`` python
shuffled = thongs.shuffle ("hello world", 1) # returns a mixed version
`` `

### Quote / Unquote
Add or deletes quotes around a chain.
`` python
quoted = "hello". Quote () # returns "\" hello \ ""
UnquoTed = "\" Hello \ "". Unquote () # returns "Hello"
`` `

###
Add quotes around a chain if it does not already have.
`` python
quoted = "Hello". Autoquote () # returns "\" Hello \ ""
quoted = "\" hello \ "". Autoquote () # returns "\" hello \ "" (unchanged)
`` `

### Slashstring / Unslashstring
Escapes or unscrews special characters in a chain.
`` python
Slashed = "Hello \ nworld" .Slashstring () # Return "Hello \\ NWORLD"
Unslashed = "Hello \\ nworld" .UNSLASHSTRING () # Return "Hello \ NWORLD"
`` `

###
Automatically formats a numerical value.
`` python
Formatied = Strings.Autoformatvalue (123.456) # Return "123.46"
`` `

### Getautoformat
Determines the automatic format for a numerical value.
`` python
Format = Strings.Getautoformat (123.456) # Returns a format like "0.00"
`` `

### GettimesTamp
Generates a horoditing in chain format.
`` python
TIMETAMP = thongs.gettimesTamp (True) # returns "20250406123456"
`` `

### Getprettytimestamp
Generates a horoding readable by humans.
`` python
TIMETAMP = thongs.getprettytimestamp () # returns "2025-04-06_12h34"
`` `

### Inject
Injects values ​​into a chain from an object or dictionary.
`` python
Template = "Hello {name}, you are {age} years old"
Data = {"Name": "John", "Age": 30}
Result = template.inject (data) # returns "hello john, you are 30 old old"
`` `

### Generaterandomstring
Generates a random chain.
`` python
random = strings.generaterandomstring ("ABCDEFGHIJKLMNOPQRSTUVWXZ", 5, 10)
# Returns a random chain between 5 and 10 characters
`` `

### ToExcelAddress
Convertit des coordonnées de cellule en adresse Excel.
```python
address = Strings.ToExcelAddress(0, 0)  # Retourne "R1C1"
```

### Isexceladdress
Check if a channel is an Excel valid address.
`` python
RESULT = thongs.isexceladdress ("A1: B10") # Return True
`` `

### FORMATEXCELTEXT
Format a text so that it is properly displayed in Excel.
`` python
Text = "= Sum (A1: A10)". Formatexceltext () # prefix with 'to avoid interpretation as formula
`` `