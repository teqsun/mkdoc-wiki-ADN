# DELPREFIXROW

## Fonction DELPREFIXROW

La fonction **DELPREFIXROW** détecte le préfixe commun à toutes les lignes de la variable traitée, puis le supprime

Il est possible de nettoyer les textes (suppression des blancs et caractères indésirables en tête/fin de texte etc.) qui en résultent.

Il est également possible d'affecter le préfixe détecté au titre de la variable qui en résulte.

&nbsp;

Cette fonction est généralement appelée après une fusion (sur modalité ou sur dimension) pour ajuster les textes de la variable obtenue.

#### Syntaxe :&nbsp;

Q01.DELPREFIXROW(CleanText; ModifyTitle; PartDelimiter)

ou

\_DELPREFIXROW(Q01; CleanText; ModifyTitle; PartDelimiter)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | CleanText | Booléen | Nettoyage auto du texte si TRUE | TRUE par défaut |
| &#50; | ModifyTitle | Booléen | Le préfixe détecté sera ajouté dans le titre si TRUE | TRUE par défaut |
| &#51; | PartDelimiter | Caractère | Lorsqu'il existe, le séparateur simplifie la détection du préfixe commun | NUL par défaut |


&nbsp;

Voir aussi :&nbsp;

[Traiter les variables littérales](<Traiterlesvariableslitterales.md>)

[Gestion des libellés](<Gererleslibelleslestextes1.md>)
