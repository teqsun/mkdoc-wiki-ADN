# Documentation Utilitaires de chaînes de caractères

## Introduction aux chaînes de caractères en .NET
Les chaînes de caractères (strings) en .NET sont des objets immuables, ce qui signifie qu'une fois créés, ils ne peuvent pas être modifiés. Toute opération qui semble modifier une chaîne crée en réalité une nouvelle instance.

Les méthodes de la bibliothèque standard de .NET sont complétées par de nombreuses méthodes d'extension de la bibliothèque ADN. En voici la liste.

## Sommaire

- [Manipulation basique des chaînes](#manipulation-basique-des-chaînes)
  - [LengthOf](#lengthof)
  - [Repeat](#repeat)
  - [IsSingleLine](#issingleline)
  - [SingleLine](#singleline)
  - [Truncate](#truncate)
  - [CountStartCharacters](#countstartcharacters)
  - [CountEndCharacters](#countendcharacters)
  - [CountCharacters](#countcharacters)
  - [FixedLength](#fixedlength)
  - [RemoveEmptyStrings](#removeemptystrings)
  - [HasMultiLines](#hasmultilines)
  - [IsMultiLine](#ismultiline)

- [Transformation et formatage de texte](#transformation-et-formatage-de-texte)
  - [RemoveAccents](#removeaccents)
  - [RemoveAllButLettersAndDigits](#removeallbutlettersanddigits)
  - [RemoveAllButDigits](#removeallbutdigits)
  - [ExtractIf](#extractif)
  - [RemoveIf](#removeif)
  - [Capitalize](#capitalize)
  - [Uncapitalize](#uncapitalize)
  - [Pascalize](#pascalize)
  - [Camelize](#camelize)
  - [Underscore](#underscore)
  - [Dasherize](#dasherize)
  - [Minimize](#minimize)
  - [Titleize](#titleize)
  - [Humanize](#humanize)
  - [Ordinalize](#ordinalize)
  - [Initials](#initials)
  - [StripHtml / HtmlToString](#striphtml--htmltostring)
  - [StringToHtml](#stringtohtml)
  - [Clean](#clean)
  - [SafeTrim](#safetrim)
  - [Align](#align)

- [Recherche et comparaison](#recherche-et-comparaison)
  - [ContainsIgnoreCase](#containsignorecase)
  - [ContainsOneOf / ContainsAny](#containsoneof--containsany)
  - [WildcardMatch](#wildcardmatch)
  - [FuzzyCompare](#fuzzycompare)
  - [AlphaNumCompare](#alphanumcompare)
  - [AlphaNumSort](#alphanumsort)
  - [FindCommonPart](#findcommonpart)
  - [FindCommonPartOffset](#findcommonpartoffset)
  - [FindCommonRoot](#findcommonroot)
  - [CompareStrings](#comparestrings)
  - [CompareNames](#comparenames)
  - [AreNamesEqual](#arenamesequal)
  - [StartsWithNoCase](#startswithnocase)
  - [Contains (with comparison)](#contains-with-comparison)

- [Fractionnement et jointure](#fractionnement-et-jointure)
  - [ScanLines](#scanlines)
  - [ScanWords](#scanwords)
  - [Split](#split)
  - [SplitIgnoringLiterals](#splitignoringliterals)
  - [SplitOnSize](#splitonsize)
  - [JoinWith / ToString](#joinwith--tostring)
  - [FromString](#fromstring)
  - [ModifyLines](#modifylines)
  - [Extract](#extract)
  - [GetPart](#getpart)
  - [GetRightPart](#getrightpart)

- [Conversion et parsing](#conversion-et-parsing)
  - [SafeParse (bool, double, int)](#safeparse-bool-double-int)
  - [ParseValue](#parsevalue)
  - [ParseValues](#parsevalues)
  - [ParseIntVector](#parseintvector)
  - [ParseDoubleVector](#parsedoublevector)
  - [ParseStringVector](#parsestringvector)
  - [ReadInteger](#readinteger)
  - [ToEnum](#toenum)
  - [TryToEnum](#trytoenum)
  - [ToObject](#toobject)
  - [ToChar](#tochar)
  - [IsNumber](#isnumber)
  - [IsInteger](#isinteger)
  - [IsBoolean](#isboolean)
  - [IsExpressionTrue / IsExpressionFalse](#isexpressiontrue--isexpressionfalse)
  - [IsIntegerVector](#isintegervector)
  - [IsNumericRange](#isnumericrange)
  - [TryParseNumericRange](#tryparsenumericrange)
  - [IsNumericExpression](#isnumericexpression)
  - [ResolveNumericExpression](#resolvenumericexpression)
  - [TryEvaluateNumericExpression](#tryevaluatenumericexpression)

- [Nommage et identification](#nommage-et-identification)
  - [IsKeyword](#iskeyword)
  - [IsKeywordPath](#iskeywordpath)
  - [IsMetaKeyword](#ismetakeyword)
  - [IsName](#isname)
  - [IsSymbolName](#issymbolname)
  - [ArrangeName / Nameize](#arrangename--nameize)
  - [EnsureUniqueName](#ensureuniquename)
  - [EnsureUniqueNames](#ensureuniqueNames)
  - [EnsureUniqueFileName](#ensureUniqueFileName)
  - [NewUniqueName](#newuniquename)
  - [NewUniqueId](#newuniqueid)
  - [FindRootName](#findrootname)
  - [IsCodeExpression](#iscodeexpression)
  - [GetCodeExpressionValue](#getcodeexpressionvalue)
  - [FormatCodeExpression](#formatcodeexpression)
  - [IsEntityExpression](#isentityexpression)
  - [GetEntityExpressionValue](#getentityexpressionvalue)
  - [FormatEntityExpression](#formatentityexpression)

- [Support d'encodages et internationalisation](#support-dencodages-et-internationalisation)
  - [DetectEncoding](#detectencoding)
  - [FixEncoding](#fixencoding)
  - [Recode](#recode)
  - [ToUtf8](#toutf8)
  - [ToDefaultEncoding](#todefaultencoding)
  - [IsUpper / IsLower](#isupper--islower)
  - [IsUnaccentedLetter](#isunaccentedletter)
  - [IsUnaccentedLetterOrDigit](#isunaccentedletterordigit)

- [Utilitaires pour fichiers et chemins](#utilitaires-pour-fichiers-et-chemins)
  - [AssumeIOCompatible](#assumeiocompatible)
  - [CompareFileNames](#comparefilenames)
  - [ComparePaths](#comparepaths)
  - [NormalizePath](#normalizepath)
  - [MakeValidFileName](#makevalidfilename)
  - [MakePath](#makepath)
  - [IsAbsolutePath](#isabsolutepath)
  - [IsRelativePath](#isrelativepath)
  - [FormatFileSize](#formatfilesize)
  - [CleanUrl](#cleanurl)
  - [IsUrl](#isurl)

- [Expressions et patterns](#expressions-et-patterns)
  - [HasWildcard](#haswildcard)
  - [RemoveWildcards](#removewildcards)
  - [IsWildcard](#iswildcard)
  - [ContainsJoker](#containsjoker)
  - [IsTag](#istag)
  - [IsTagExactly](#istagexactly)
  - [UntagString / UntagStringEx](#untagstring--untagstringex)
  - [UntagText](#untagtext)
  - [UntagObject](#untagobject)
  - [ExtractAnnotations](#extractannotations)
  - [HasAnnotation](#hasannotation)
  - [ParseAnnotation](#parseannotation)
  - [SmartFormat](#smartformat)
  - [LooksLikeSelectionPattern](#lookslikeselectionpattern)
  - [ParseXmlAttributes](#parsexmlattributes)
  - [FormatAsXmlAttributesString](#formatasxmlattributesstring)
  - [ReGet](#reget)
  - [FindMatchingParenthese / FindMatchingClosingChar](#findmatchingparenthese--findmatchingclosingchar)
  - [IsTerminalExpression](#isterminalexpression)

- [Utilitaires spécifiques](#utilitaires-spécifiques)
  - [LooksLikeEmail](#lookslikeemail)
  - [LooksLikeJson](#lookslikejson)
  - [LooksLikeXml](#lookslikexml)
  - [ZipString / UnzipString](#zipstring--unzipstring)
  - [HashString](#hashstring)
  - [BytesToHexa / HexaToBytes](#bytestohexa--hexatobytes)
  - [Shuffle](#shuffle)
  - [Quote / Unquote](#quote--unquote)
  - [AutoQuote](#autoquote)
  - [SlashString / UnslashString](#slashstring--unslashstring)
  - [AutoFormatValue](#autoformatvalue)
  - [GetAutoFormat](#getautoformat)
  - [GetTimeStamp](#gettimestamp)
  - [GetPrettyTimeStamp](#getprettytimestamp)
  - [Inject](#inject)
  - [GenerateRandomString](#generaterandomstring)
  - [ToExcelAddress](#toexceladdress)
  - [IsExcelAddress](#isexceladdress)
  - [FormatExcelText](#formatexceltext)

## Manipulation basique des chaînes

### LengthOf
Retourne la longueur d'une chaîne, ou 0 si la chaîne est null.
```python
length = Strings.LengthOf("hello")  # Retourne 5
length = Strings.LengthOf(None)     # Retourne 0
```

### Repeat
Répète une chaîne un nombre spécifié de fois.
```python
repeated = "abc".Repeat(3)  # Retourne "abcabcabc"
```

### IsSingleLine
Vérifie si une chaîne ne contient pas de retours à la ligne.
```python
result = "hello world".IsSingleLine()    # Retourne True
result = "hello\nworld".IsSingleLine()   # Retourne False
```

### SingleLine
Convertit une chaîne multi-lignes en une seule ligne en remplaçant les retours à la ligne par des espaces.
```python
text = "hello\nworld".SingleLine()  # Retourne "hello world"
```

### Truncate
Tronque une chaîne à une longueur maximale, avec différentes options.
```python
text = "Hello world, how are you today?".Truncate(10)
# Retourne "Hello worl…"

# Avec l'option FinishWord pour compléter le dernier mot
text = "Hello world, how are you today?".Truncate(10, TruncateOptions.FinishWord)
# Retourne "Hello…"
```

### CountStartCharacters
Compte le nombre de caractères spécifiés au début d'une chaîne.
```python
count = "!!Hello".CountStartCharacters("!", "!")  # Retourne 2
```

### CountEndCharacters
Compte le nombre de caractères spécifiés à la fin d'une chaîne.
```python
count = "Hello!!".CountEndCharacters("!", "!")  # Retourne 2
```

### CountCharacters
Compte le nombre d'occurrences des caractères spécifiés dans une chaîne.
```python
count = Strings.CountCharacters("Hello World", "l", "o")  # Retourne 4
```

### FixedLength
Aligne une chaîne à droite ou à gauche pour atteindre une longueur spécifiée.
```python
text = Strings.FixedLength("abc", 5)       # Retourne "  abc"
text = Strings.FixedLength("abc", 5, "0")  # Retourne "00abc"
text = Strings.FixedLength("abc", 5, " ", False)  # Retourne "abc  "
```

### RemoveEmptyStrings
Supprime les chaînes vides d'une liste.
```python
strings = ["a", "", "b", "", "c"]
Strings.RemoveEmptyStrings(strings)  # Modifie la liste : ["a", "b", "c"]
```

### HasMultiLines
Vérifie si une chaîne contient plusieurs lignes.
```python
result = "hello\nworld".HasMultiLines()  # Retourne True
```

### IsMultiLine
Vérifie si une chaîne contient plusieurs lignes (alias de HasMultiLines).
```python
result = "hello\nworld".IsMultiLine()  # Retourne True
```

## Transformation et formatage de texte

### RemoveAccents
Supprime les accents d'une chaîne.
```python
text = "éàçèñ".RemoveAccents()  # Retourne "eacen"
```

### RemoveAllButLettersAndDigits
Supprime tous les caractères qui ne sont ni des lettres ni des chiffres.
```python
text = "Hello, World! 123".RemoveAllButLettersAndDigits()  # Retourne "HelloWorld123"
```

### RemoveAllButDigits
Supprime tous les caractères qui ne sont pas des chiffres.
```python
text = "Hello, World! 123".RemoveAllButDigits()  # Retourne "123"
```

### ExtractIf
Extrait les caractères qui satisfont une condition.
```python
# Extrait seulement les voyelles
text = "Hello World".ExtractIf(lambda c: c in "aeiouAEIOU")  # Retourne "eoo"
```

### RemoveIf
Supprime les caractères qui satisfont une condition.
```python
# Supprime les voyelles
text = "Hello World".RemoveIf(lambda c: c in "aeiouAEIOU")  # Retourne "Hll Wrld"
```

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
Convertit une chaîne en PascalCase.
```python
text = "hello_world".Pascalize()  # Retourne "HelloWorld"
```

### Camelize
Convertit une chaîne en camelCase.
```python
text = "hello_world".Camelize()  # Retourne "helloWorld"
```

### Underscore
Convertit une chaîne en snake_case.
```python
text = "HelloWorld".Underscore()  # Retourne "hello_world"
```

### Dasherize
Convertit une chaîne en kebab-case.
```python
text = "HelloWorld".Dasherize()  # Retourne "hello-world"
```

### Minimize
Minimise une chaîne en supprimant les accents et en ne conservant que les lettres et chiffres, convertis en majuscules.
```python
text = "Hello, World! 123".Minimize()  # Retourne "HELLOWORLD123"
```

### Titleize
Convertit une chaîne en format titre (majuscule pour chaque mot).
```python
text = "hello_world".Titleize()  # Retourne "Hello World"
```

### Humanize
Rend une chaîne plus lisible pour les humains.
```python
text = "hello_world".Humanize()  # Retourne "Hello world"
```

### Ordinalize
Convertit un nombre en forme ordinale.
```python
text = "1".Ordinalize()  # Retourne "1st"
text = "2".Ordinalize()  # Retourne "2nd"
```

### Initials
Extrait les initiales d'une chaîne.
```python
initials = Strings.Initials("Hello World")  # Retourne "HW"
```

### StripHtml / HtmlToString
Supprime les balises HTML d'une chaîne.
```python
text = "<p>Hello <b>World</b></p>".StripHtml()  # Retourne "Hello World"
```

### StringToHtml
Convertit une chaîne en format HTML (remplace les retours à la ligne par des <br/>).
```python
html = "Hello\nWorld".StringToHtml()  # Retourne "Hello<br/>World"
```

### Clean
Nettoie une chaîne en supprimant le HTML, les retours à la ligne, etc.
```python
text = "<p>Hello\nWorld</p>".Clean()  # Retourne "Hello World"
```

### SafeTrim
Supprime les espaces blancs d'une chaîne, retourne une chaîne vide si l'entrée est null.
```python
text = " Hello ".SafeTrim()    # Retourne "Hello"
text = None.SafeTrim()         # Retourne ""
```

### Align
Aligne une chaîne selon une largeur et un alignement spécifiés.
```python
text = "Hello".Align(10, HorizontalAlignment.Left)   # Retourne "Hello     "
text = "Hello".Align(10, HorizontalAlignment.Right)  # Retourne "     Hello"
```

## Recherche et comparaison

### ContainsIgnoreCase
Vérifie si une chaîne contient une sous-chaîne, sans tenir compte de la casse.
```python
result = "Hello World".ContainsIgnoreCase("world")  # Retourne True
```

### ContainsOneOf / ContainsAny
Vérifie si une chaîne contient au moins un des caractères spécifiés.
```python
result = "Hello World".ContainsAny('x', 'y', 'z', 'o')  # Retourne True (contient 'o')
```

### WildcardMatch
Vérifie si une chaîne correspond à un pattern avec jokers (* et ?).
```python
result = Strings.WildcardMatch("te?t", "test")         # Retourne True
result = Strings.WildcardMatch("te*", "test")          # Retourne True
result = Strings.WildcardMatch("te?t", "text")         # Retourne False
result = Strings.WildcardMatch("*est", "test")         # Retourne True
```

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

### AlphaNumSort
Trie une liste de chaînes de façon alphanumérique.
```python
sorted = ["A1", "A10", "A2"].AlphaNumSort()  # Retourne ["A1", "A2", "A10"]
```

### FindCommonPart
Trouve la partie commune au début de plusieurs chaînes.
```python
strings = ["abcdef", "abcxyz", "abcghi"]
common = Strings.FindCommonPart(strings)  # Retourne "abc"
```

### FindCommonPartOffset
Trouve la position de fin de la partie commune à plusieurs chaînes.
```python
strings = ["abcdef", "abcxyz"]
offset = Strings.FindCommonPartOffset(strings)  # Retourne 3
```

### FindCommonRoot
Trouve la racine commune dans une liste de chaînes (utile pour les identifiants).
```python
strings = ["user_profile", "user_settings", "user_account"]
root = Strings.FindCommonRoot(strings)  # Retourne "USER"
```

### CompareStrings
Compare deux chaînes, avec option pour ignorer la casse.
```python
result = Strings.CompareStrings("abc", "ABC", True)  # Retourne 0 (égal)
```

### CompareNames
Compare deux noms d'entités (ignorant la casse).
```python
result = Strings.CompareNames("UserEntity", "userentity")  # Retourne 0 (égal)
```

### AreNamesEqual
Vérifie si deux noms d'entités sont égaux (ignorant la casse).
```python
result = Strings.AreNamesEqual("UserEntity", "userentity")  # Retourne True
```

### StartsWithNoCase
Vérifie si une chaîne commence par une sous-chaîne spécifiée, sans tenir compte de la casse.
```python
result = "Hello World".StartsWithNoCase("hello")  # Retourne True
```

### Contains (with comparison)
Vérifie si une chaîne contient une sous-chaîne avec un mode de comparaison spécifié.
```python
result = "Hello World".Contains("world", StringComparison.OrdinalIgnoreCase)  # Retourne True
```

## Fractionnement et jointure

### ScanLines
Retourne chaque ligne d'un texte sous forme d'énumération.
```python
lines = "Hello\nWorld".ScanLines()  # Retourne ["Hello", "World"]
```

### ScanWords
Analyse une chaîne et retourne les mots sous forme d'énumération.
```python
words = Strings.ScanWords("Hello, World!")  # Retourne des mots ["Hello", "World"]
```

### Split
Divise une chaîne en parties selon des options spécifiées.
```python
parts = "Hello,World".Split(SplitStringOptions())  # Retourne ["Hello", "World"]
```

### SplitIgnoringLiterals
Divise une chaîne mais ignore les délimiteurs qui sont dans des chaînes littérales.
```python
parts = 'Hello,"World,Test",Bye'.SplitIgnoringLiterals(',')
# Retourne ["Hello", "\"World,Test\"", "Bye"]
```

### SplitOnSize
Divise une chaîne en parties de taille égale.
```python
parts = "HelloWorld".SplitOnSize(5)  # Retourne ["Hello", "World"]
```

### JoinWith / ToString
Joint une collection de chaînes avec un délimiteur.
```python
joined = ["Hello", "World"].JoinWith(", ")  # Retourne "Hello, World"
```

### FromString
Divise une chaîne en parties selon des délimiteurs et nettoie chaque partie.
```python
parts = Strings.FromString("Hello, World", ',')  # Retourne ["Hello", " World"]
```

### ModifyLines
Modifie chaque ligne d'un texte à l'aide d'une fonction.
```python
text = Strings.ModifyLines("Hello\nWorld", lambda line: line.ToUpper())
# Retourne "HELLO\nWORLD"
```

### Extract
Extrait une sous-chaîne selon un indice de début et une longueur.
```python
sub = "HelloWorld".Extract(2, 5)  # Retourne "elloW"
```

### GetPart
Extrait une partie spécifique d'une chaîne délimitée.
```python
part = "one.two.three".GetPart('.', 2)  # Retourne "two"
```

### GetRightPart
Extrait la partie droite d'une chaîne délimitée à partir d'une position.
```python
part = "one.two.three".GetRightPart('.', 1)  # Retourne "two.three"
```

## Conversion et parsing

### SafeParse (bool, double, int)
Tente de convertir une chaîne en valeur typée, retourne une valeur par défaut en cas d'échec.
```python
value = Strings.SafeParse("123", 0)      # Retourne 123 (int)
value = Strings.SafeParse("12.34", 0.0)  # Retourne 12.34 (double)
value = Strings.SafeParse("true", False) # Retourne True (bool)
```

### ParseValue
Convertit une chaîne en valeur typée (bool, int, double ou string).
```python
value = Strings.ParseValue("123")    # Retourne 123 (int)
value = Strings.ParseValue("12.34")  # Retourne 12.34 (double)
value = Strings.ParseValue("true")   # Retourne True (bool)
value = Strings.ParseValue("hello")  # Retourne "hello" (string)
```

### ParseValues
Divise une chaîne sur un délimiteur et convertit chaque partie en valeur typée.
```python
values = Strings.ParseValues("123;12.34;true;hello")
# Retourne [123, 12.34, True, "hello"]
```

### ParseIntVector
Convertit une chaîne en tableau d'entiers.
```python
values = Strings.ParseIntVector("1,2,3,4")  # Retourne [1, 2, 3, 4]
```

### ParseDoubleVector
Convertit une chaîne en tableau de nombres à virgule flottante.
```python
values = Strings.ParseDoubleVector("1.1;2.2;3.3")  # Retourne [1.1, 2.2, 3.3]
```

### ParseStringVector
Convertit une chaîne en tableau de chaînes.
```python
values = Strings.ParseStringVector("one,two,three")  # Retourne ["one", "two", "three"]
```

### ReadInteger
Lit un entier depuis le début d'une chaîne.
```python
value = Strings.ReadInteger("123abc", 0)  # Retourne 123
```

### ToEnum
Convertit une chaîne en valeur d'énumération.
```python
value = "Monday".ToEnum(DayOfWeek)  # Retourne DayOfWeek.Monday
```

### TryToEnum
Tente de convertir une chaîne en valeur d'énumération, retourne une valeur par défaut en cas d'échec.
```python
value = "Monday".TryToEnum(DayOfWeek.Sunday)  # Retourne DayOfWeek.Monday
value = "Invalid".TryToEnum(DayOfWeek.Sunday) # Retourne DayOfWeek.Sunday
```

### ToObject
Convertit une chaîne en objet typé.
```python
obj = Strings.ToObject("123")    # Retourne 123 (int)
obj = Strings.ToObject("12.34")  # Retourne 12.34 (double)
obj = Strings.ToObject("true")   # Retourne True (bool)
```

### ToChar
Convertit une chaîne en caractère (prend le premier caractère).
```python
char = "abc".ToChar()  # Retourne 'a'
```

### IsNumber
Vérifie si une chaîne représente un nombre.
```python
result = Strings.IsNumber("123")     # Retourne True
result = Strings.IsNumber("12.34")   # Retourne True
result = Strings.IsNumber("abc")     # Retourne False
```

### IsInteger
Vérifie si une chaîne représente un entier.
```python
result = Strings.IsInteger("123")    # Retourne True
result = Strings.IsInteger("12.34")  # Retourne False
```

### IsBoolean
Vérifie si une chaîne représente une valeur booléenne.
```python
result = Strings.IsBoolean("true")   # Retourne True
result = Strings.IsBoolean("false")  # Retourne True
result = Strings.IsBoolean("123")    # Retourne False
```

### IsExpressionTrue / IsExpressionFalse
Vérifie si une chaîne représente une expression "vraie" ou "fausse" (inclut "yes", "no", "vrai", "faux", etc.).
```python
result = "yes".IsExpressionTrue()   # Retourne True
result = "no".IsExpressionFalse()   # Retourne True
```

### IsIntegerVector
Vérifie si une chaîne représente un vecteur d'entiers.
```python
result = "1,2,3".IsIntegerVector()  # Retourne True
```

### IsNumericRange
Vérifie si une chaîne représente une plage numérique (ex: "1..10").
```python
result = "1..10".IsNumericRange()  # Retourne True
```

### TryParseNumericRange
Tente de convertir une chaîne en plage numérique.
```python
success = "1..10".TryParseNumericRange(out from, out to, out step)
# Success = True, from = 1, to = 10, step = 1
```

### IsNumericExpression
Vérifie si une chaîne représente une expression numérique (vecteur ou plage).
```python
result = "1,2,3".IsNumericExpression()  # Retourne True
result = "1..10".IsNumericExpression()  # Retourne True
```

### ResolveNumericExpression
Résout une expression numérique en séquence d'entiers.
```python
values = "1..5".ResolveNumericExpression()  # Retourne [1, 2, 3, 4, 5]
values = "1,3,5".ResolveNumericExpression()  # Retourne [1, 3, 5]
```

### TryEvaluateNumericExpression
Tente d'évaluer une expression numérique.
```python
success = "1..5".TryEvaluateNumericExpression(out values)
# Success = True, values = [1, 2, 3, 4, 5]
```

## Nommage et identification

### IsKeyword
Vérifie si une chaîne est un mot-clé valide (commence par une lettre ou un underscore, suivi de lettres, chiffres ou underscores).
```python
result = "myVar_123".IsKeyword()  # Retourne True
result = "123var".IsKeyword()     # Retourne False
```

### IsKeywordPath
Vérifie si une chaîne est un chemin de mots-clés valide (mots-clés séparés par des points).
```python
result = "module.class.method".IsKeywordPath()  # Retourne True
```

### IsMetaKeyword
Vérifie si une chaîne est un méta-mot-clé (commence par $).
```python
result = "$variable".IsMetaKeyword()  # Retourne True
```

### IsName
Vérifie si une chaîne est un nom valide (alias de IsKeyword).
```python
result = Strings.IsName("myVariable")  # Retourne True
```

### IsSymbolName
Vérifie si une chaîne est un nom de symbole valide (alias de IsKeyword).
```python
result = "mySymbol".IsSymbolName()  # Retourne True
```

### ArrangeName / Nameize
Arrange une chaîne pour en faire un nom valide.
```python
name = "My Variable 123".Nameize()  # Retourne "MyVariable123"
name = "123Invalid".ArrangeName("_")  # Retourne "_123Invalid"
```

### EnsureUniqueName
S'assure qu'un nom est unique dans une collection, en ajoutant un suffixe numérique si nécessaire.
```python
name = Strings.EnsureUniqueName("File", ["File", "File_1"])  # Retourne "File_2"
```

### EnsureUniqueNames
S'assure que tous les noms d'une liste sont uniques entre eux.
```python
names = Strings.EnsureUniqueNames(["File", "File", "Report"])  # Retourne ["File", "File_1", "Report"]
```

### EnsureUniqueFileName
S'assure qu'un nom de fichier est unique sur le disque, en ajoutant un suffixe numérique si nécessaire.
```python
fileName = Strings.EnsureUniqueFileName("C:\\data\\report.txt")  # Retourne "C:\\data\\report_1.txt" si le fichier existe déjà
```

### NewUniqueName
Génère un nouveau nom unique basé sur un modèle, en ajoutant un suffixe numérique.
```python
name = Strings.NewUniqueName("Item", ["Item", "Item_1"])  # Retourne "Item_2"
```

### NewUniqueId
Génère un nouvel identifiant unique basé sur un GUID.
```python
id = Strings.NewUniqueId()  # Retourne une chaîne unique comme "8f9d5f7b3a2e1c"
```

### FindRootName
Extrait la racine d'un nom (la partie avant le dernier délimiteur).
```python
root = "user_settings_profile".FindRootName()  # Retourne "user_settings"
```

### IsCodeExpression
Vérifie si une chaîne est une expression de code (commence par $).
```python
result = "$123".IsCodeExpression()  # Retourne True
```

### GetCodeExpressionValue
Extrait la valeur numérique d'une expression de code.
```python
value = "$123".GetCodeExpressionValue()  # Retourne 123
```

### FormatCodeExpression
Formate une valeur en expression de code.
```python
expr = Strings.FormatCodeExpression(123)  # Retourne "$123"
```

### IsEntityExpression
Vérifie si une chaîne est une expression d'entité (commence par @).
```python
result = "@Entity".IsEntityExpression()  # Retourne True
```

### GetEntityExpressionValue
Extrait le nom d'une expression d'entité.
```python
name = "@Entity".GetEntityExpressionValue()  # Retourne "Entity"
```

### FormatEntityExpression
Formate un nom en expression d'entité.
```python
expr = Strings.FormatEntityExpression("Entity")  # Retourne "@Entity"
```

## Support d'encodages et internationalisation

### DetectEncoding
Détecte l'encodage d'une chaîne.
```python
encoding = Strings.DetectEncoding(textContent)  # Retourne l'encodage détecté
```

### FixEncoding
Répare l'encodage d'une chaîne en cas de problème.
```python
fixed = problematicText.FixEncoding()  # Tente de corriger les problèmes d'encodage
```

### Recode
Change l'encodage d'une chaîne.
```python
recoded = text.Recode(Encoding.ASCII, Encoding.UTF8)  # Convertit de ASCII à UTF8
```

### ToUtf8
Convertit une chaîne en UTF-8.
```python
utf8Text = nonUtf8Text.ToUtf8()  # Convertit en UTF-8
```

### ToDefaultEncoding
Convertit une chaîne vers l'encodage par défaut.
```python
defaultText = utf8Text.ToDefaultEncoding(Encoding.UTF8)  # Convertit de UTF-8 à l'encodage par défaut
```

### IsUpper / IsLower
Vérifie si une chaîne est entièrement en majuscules ou en minuscules (ignore les caractères non-alphabétiques).
```python
result = "HELLO123".IsUpper()  # Retourne True
result = "hello123".IsLower()  # Retourne True
```

### IsUnaccentedLetter
Vérifie si un caractère est une lettre non accentuée.
```python
result = 'a'.IsUnaccentedLetter()  # Retourne True
result = 'é'.IsUnaccentedLetter()  # Retourne False
```

### IsUnaccentedLetterOrDigit
Vérifie si un caractère est une lettre non accentuée ou un chiffre.
```python
result = 'a'.IsUnaccentedLetterOrDigit()  # Retourne True
result = '1'.IsUnaccentedLetterOrDigit()  # Retourne True
result = 'é'.IsUnaccentedLetterOrDigit()  # Retourne False
```

## Utilitaires pour fichiers et chemins

### AssumeIOCompatible
Remplace les caractères non compatibles avec les fichiers par des underscores.
```python
path = Strings.AssumeIOCompatible("file:name.txt")  # Retourne "file_name.txt"
```

### CompareFileNames
Compare deux noms de fichiers en ignorant la casse et en normalisant les séparateurs de chemin.
```python
result = Strings.CompareFileNames("c:\\folder\\file.txt", "C:/folder/file.txt")  # Retourne 0 (égaux)
```

### ComparePaths
Compare deux chemins (alias de CompareFileNames).
```python
result = Strings.ComparePaths("c:\\folder\\file", "C:/folder/file")  # Retourne 0 (égaux)
```

### NormalizePath
Normalise un chemin en remplaçant les séparateurs de chemin par le séparateur du système.
```python
path = Strings.NormalizePath("C:/folder/file")  # Retourne "C:\\folder\\file" sur Windows
```

### MakeValidFileName
Transforme une chaîne en nom de fichier valide en remplaçant les caractères invalides.
```python
fileName = "file*name?.txt".MakeValidFileName()  # Retourne "file_name_.txt"
```

### MakePath
Crée un chemin à partir d'une collection de segments.
```python
path = Strings.MakePath(["folder", "subfolder", "file.txt"])  # Retourne "folder/subfolder/file.txt"
```

### IsAbsolutePath
Vérifie si un chemin est absolu.
```python
result = Strings.IsAbsolutePath("C:\\folder\\file.txt")  # Retourne True
result = Strings.IsAbsolutePath("folder/file.txt")       # Retourne False
```

### IsRelativePath
Vérifie si un chemin est relatif.
```python
result = Strings.IsRelativePath("folder/file.txt")        # Retourne True
result = Strings.IsRelativePath("C:\\folder\\file.txt")   # Retourne False
```

### FormatFileSize
Formate une taille de fichier en chaîne lisible (KB, MB, etc.).
```python
size = Strings.FormatFileSize(1024 * 1024)  # Retourne "1.0 MB"
```

### CleanUrl
Nettoie une URL en supprimant le slash final.
```python
url = Strings.CleanUrl("http://example.com/")  # Retourne "http://example.com"
```

### IsUrl
Vérifie si une chaîne est une URL.
```python
result = Strings.IsUrl("http://example.com")  # Retourne True
```

## Expressions et patterns

### HasWildcard
Vérifie si une chaîne contient des caractères joker (* ou ?).
```python
result = "file*.txt".HasWildcard()  # Retourne True
```

### RemoveWildcards
Supprime les caractères joker d'une chaîne.
```python
text = "file*.txt".RemoveWildcards()  # Retourne "file.txt"
```

### IsWildcard
Vérifie si un caractère est un joker.
```python
result = '*'.IsWildcard()  # Retourne True
```

### ContainsJoker
Vérifie si une chaîne contient des jokers (alias de HasWildcard).
```python
result = "file*.txt".ContainsJoker()  # Retourne True
```

### IsTag
Vérifie si une chaîne contient des tags de format [TAG].
```python
result = Strings.IsTag("This is a [TAG]")  # Retourne True
```

### IsTagExactly
Vérifie si une chaîne est exactement un tag de format [TAG].
```python
result = "[TAG]".IsTagExactly()  # Retourne True
```

### UntagString / UntagStringEx
Remplace les tags dans une chaîne par leurs valeurs correspondantes dans un dictionnaire.
```python
values = {"NAME": "John", "AGE": 30}
text = Strings.UntagString("Hello [NAME], you are [AGE] years old", values)
# Retourne "Hello John, you are 30 years old"
```

### UntagText
Remplace les tags dans un objet Text par leurs valeurs correspondantes.
```python
values = {"NAME": "John", "AGE": 30}
result = Strings.UntagText(textObject, values)  # Remplace les tags dans l'objet Text
```

### UntagObject
Remplace les tags dans un objet (chaîne ou Text) par leurs valeurs correspondantes.
```python
values = {"NAME": "John", "AGE": 30}
result = Strings.UntagObject("[NAME] is [AGE]", values)  # Retourne "John is 30"
```

### ExtractAnnotations
Extrait les annotations (tags) d'une chaîne.
```python
annotations = Strings.ExtractAnnotations("This is [TAG:format] a test")
# Retourne un dictionnaire avec {"TAG": "format"}
```

### HasAnnotation
Vérifie si une chaîne contient des annotations.
```python
result = Strings.HasAnnotation("This is [TAG] a test")  # Retourne True
```

### ParseAnnotation
Analyse une annotation dans une chaîne.
```python
success = Strings.ParseAnnotation("[TYPE]Value", out name, out value)
# Success = True, name = "TYPE", value = "Value"
```

### SmartFormat
Formate une chaîne avec des valeurs de substitution avancées.
```python
values = {"name": "John", "count": 3}
text = "Hello {name}, you have {count} messages".SmartFormat(values)
# Retourne "Hello John, you have 3 messages"
```

### LooksLikeSelectionPattern
Vérifie si une chaîne ressemble à un pattern de sélection.
```python
result = "[Property] = 'Value'".LooksLikeSelectionPattern()  # Retourne True
```

### ParseXmlAttributes
Parse des attributs XML dans une chaîne.
```python
attributes = Strings.ParseXmlAttributes("set Name=\"Value\" Title=\"Example\"")
# Retourne un dictionnaire avec {"Name": "Value", "Title": "Example"}
```

### FormatAsXmlAttributesString
Formate un dictionnaire en chaîne d'attributs XML.
```python
attributes = {"Name": "Value", "Title": "Example"}
xml = attributes.FormatAsXmlAttributesString("set")
# Retourne "set Name=\"Value\" Title=\"Example\""
```

### ReGet
Extrait des parties d'une chaîne à l'aide d'une expression régulière.
```python
regex = new Regex(@"(\d+)-(\d+)")
text = "ID: 123-456"
result = text.ReGet(regex, "-")  # Retourne "123-456"
```

### FindMatchingParenthese / FindMatchingClosingChar
Trouve la parenthèse/accolade/crochet fermant correspondant à un ouvrant.
```python
index = "function() { return true; }".FindMatchingParenthese(8)  # Retourne 10
```

### IsTerminalExpression
Vérifie si une expression est terminale (identificateur simple ou expression déjà entre parenthèses).
```python
result = "variable".IsTerminalExpression()  # Retourne True
result = "(x + y)".IsTerminalExpression()   # Retourne True
result = "x + y".IsTerminalExpression()     # Retourne False
```

## Utilitaires spécifiques

### LooksLikeEmail
Vérifie si une chaîne ressemble à une adresse email.
```python
result = "user@example.com".LooksLikeEmail()  # Retourne True
```

### LooksLikeJson
Vérifie si une chaîne ressemble à du JSON.
```python
result = '{"name": "John"}'.LooksLikeJson()  # Retourne True
```

### LooksLikeXml
Vérifie si une chaîne ressemble à du XML.
```python
result = "<user>John</user>".LooksLikeXml()  # Retourne True
```

### ZipString / UnzipString
Compresse et décompresse une chaîne.
```python
compressed = Strings.ZipString("texte très long à compresser")
decompressed = Strings.UnzipString(compressed)  # Retourne "texte très long à compresser"
```

### HashString
Hache une chaîne pour créer une version plus courte.
```python
hashed = Strings.HashString("texte à hacher", 8)  # Retourne une chaîne de 8 caractères
```

### BytesToHexa / HexaToBytes
Convertit entre des octets et leur représentation hexadécimale.
```python
hexa = Strings.BytesToHexa(byteArray)  # Convertit des octets en chaîne hexadécimale
bytes = Strings.HexaToBytes("0A1B2C")  # Convertit une chaîne hexadécimale en octets
```

### Shuffle
Mélange une chaîne de manière cryptographique.
```python
shuffled = Strings.Shuffle("Hello World", 1)  # Retourne une version mélangée
```

### Quote / Unquote
Ajoute ou supprime des guillemets autour d'une chaîne.
```python
quoted = "Hello".Quote()          # Retourne "\"Hello\""
unquoted = "\"Hello\"".Unquote()  # Retourne "Hello"
```

### AutoQuote
Ajoute des guillemets autour d'une chaîne si elle n'en a pas déjà.
```python
quoted = "Hello".AutoQuote()        # Retourne "\"Hello\""
quoted = "\"Hello\"".AutoQuote()    # Retourne "\"Hello\"" (inchangé)
```

### SlashString / UnslashString
Échappe ou déséchappe les caractères spéciaux dans une chaîne.
```python
slashed = "Hello\nWorld".SlashString()      # Retourne "Hello\\nWorld"
unslashed = "Hello\\nWorld".UnslashString()  # Retourne "Hello\nWorld"
```

### AutoFormatValue
Formate automatiquement une valeur numérique.
```python
formatted = Strings.AutoFormatValue(123.456)  # Retourne "123.46"
```

### GetAutoFormat
Détermine le format automatique pour une valeur numérique.
```python
format = Strings.GetAutoFormat(123.456)  # Retourne un format comme "0.00"
```

### GetTimeStamp
Génère un horodatage au format chaîne.
```python
timestamp = Strings.GetTimeStamp(True)  # Retourne "20250406123456"
```

### GetPrettyTimeStamp
Génère un horodatage lisible par les humains.
```python
timestamp = Strings.GetPrettyTimeStamp()  # Retourne "2025-04-06_12h34"
```

### Inject
Injecte des valeurs dans une chaîne à partir d'un objet ou dictionnaire.
```python
template = "Hello {name}, you are {age} years old"
data = {"name": "John", "age": 30}
result = template.Inject(data)  # Retourne "Hello John, you are 30 years old"
```

### GenerateRandomString
Génère une chaîne aléatoire.
```python
random = Strings.GenerateRandomString("abcdefghijklmnopqrstuvwxyz", 5, 10)
# Retourne une chaîne aléatoire entre 5 et 10 caractères
```

### ToExcelAddress
Convertit des coordonnées de cellule en adresse Excel.
```python
address = Strings.ToExcelAddress(0, 0)  # Retourne "R1C1"
```

### IsExcelAddress
Vérifie si une chaîne est une adresse Excel valide.
```python
result = Strings.IsExcelAddress("A1:B10")  # Retourne True
```

### FormatExcelText
Formate un texte pour qu'il soit correctement affiché dans Excel.
```python
text = "=SUM(A1:A10)".FormatExcelText()  # Préfixe avec ' pour éviter l'interprétation comme formule
```