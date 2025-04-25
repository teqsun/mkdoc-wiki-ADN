# DELPREFIX

## Fonction DELPREFIX

La fonction **DELPREFIX** détecte le préfixe commun à toutes les modalités de la variable traitée, puis le supprime.

Il est possible de nettoyer les textes (suppression des blancs et caractères indésirables en tête/fin de texte etc.) qui en résultent.

Il est également possible d'affecter le préfixe détecté au titre de la variable qui en résulte.

&nbsp;

Cette fonction est généralement appelée après une fusion (sur modalité ou sur dimension) pour ajuster les textes de la variable obtenue.

#### Syntaxe :&nbsp;

Q01.DELPREFIX(CleanText; ModifyTitle; PartDelimiter)

ou

\_DELPREFIX(Q01; CleanText; ModifyTitle; PartDelimiter)

&nbsp;

| &nbsp; | **Nom ** | **Type ** | **Description** | **Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | CleanText | Booléen | Nettoyage auto du texte si TRUE | TRUE par défaut |
| &#50; | ModifyTitle | Booléen | Le préfixe détecté sera ajouté dans le titre si TRUE | TRUE par défaut |
| &#51; | PartDelimiter | Caractère | Lorsqu'il existe, le séparateur simplifie la détection du préfixe commun | NUL par défaut |


&nbsp;

#### Exemples :

Q01.DELPREFIX(TRUE;TRUE;)

Ici le préfixe commun est "***Dans quelle mesure, retourneriez-vous dans les différents pays cités ci-dessus.(***"

&nbsp;

|  Avec cette définition les libellés des modalités de la variable Q01 |  deviennent : |
| --- | --- |
| Dans quelle mesure, retourneriez-vous dans les différents pays cités ci-dessus.(Allemagne) Dans quelle mesure, retourneriez-vous dans les différents pays cités ci-dessus.(Autriche) Dans quelle mesure, retourneriez-vous dans les différents pays cités ci-dessus.(Belgique) Dans quelle mesure, retourneriez-vous dans les différents pays cités ci-dessus.(Danemark) Dans quelle mesure, retourneriez-vous dans les différents pays cités ci-dessus.(Espagne) Dans quelle mesure, retourneriez-vous dans les différents pays cités ci-dessus.(Finlande) Dans quelle mesure, retourneriez-vous dans les différents pays cités ci-dessus.(France) Dans quelle mesure, retourneriez-vous dans les différents pays cités ci-dessus.(Grèce) | Allemagne Autriche Belgique Danemark Espagne Finlande France Grèce |


#### Remarque :

Si le libellé se termine par une parenthèse ")", elle est supprimée.

&nbsp;

Voir aussi :&nbsp;

[Traiter les variables littérales](<Traiterlesvariableslitterales.md>)

[Gestion des libellés](<Gererleslibelleslestextes1.md>)
