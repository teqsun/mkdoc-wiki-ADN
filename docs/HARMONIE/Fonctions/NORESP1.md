# NORESP

## Fonction NORESP

La fonction **NORESP** manipule les sans-réponses d'une variable logique en les ajoutant ou en les combinant à une modalité existante. Sa syntaxe est équivalente à celle de la fonction RESP.

#### Syntaxe n°1 :&nbsp;

Q01.NORESP()

ou

\_NORESP(Q01)

&nbsp;

Cette version sans argument retourne simplement les sans-réponses à la variable (bonne méthode pour créer un filtre / un univers \!).

#### Syntaxe n°2 :&nbsp;

Q01.NORESP(InsertionPoint; MarginText)

ou

\_NORESP(Q01; InsertionPoint; MarginText)

&nbsp;

| &nbsp; | **Nom** |**Type**|**Description**|**Remarque** |
| --- | --- | --- | --- | --- |
| &#49; | InsertionPoint | Nombre | Position d'insertion : S'il vaut 0, le marginal est ajouté en tête de variable. S'il est plus grand que le nombre de modalités, le marginal est ajouté en fin.&nbsp; S'il est compris entre 1 et 2 (1.5 par exemple), il est inséré entre la modalité 1 et la modalité 2 (etc.). | Obligatoire |
| &#50; | MarginText | Chaîne de caractères | Optionnel : libellé à utiliser avec @code si on souhaite affecter un code à la nouvelle modalité (à éviter lors des traitements multilingues \!). | Indéfini par défaut |


#### Exemples :

S2.NORESP()

Retourne un filtre qui véhicule les sans-réponses à la variable S2.

&nbsp;

S1.NORESP(99;"@99 SR")

Ajoute les sans-réponses à la variable S1 en dernière modalité libellée "SR" (dans la mesure où la variable S1 à moins de 99 modalités...) et lui affecte le code 99.

&nbsp;

S1.NORESP(0)

Ajoute les sans-réponses à la variable S1 en première modalité.

&nbsp;

S1.NORESP(2.5)

Ajoute les sans-réponses à la variable S1 entre la 2ème et la 3ème modalités.

&nbsp;

Voir aussi : [Critères](<Creerdescriteresoubannieres1.md>)