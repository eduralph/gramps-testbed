---
title: Fr:Manuel wiki pour Gramps 6.0 - Les filtres
categories:
- Fr:Documentation
managed: false
source: wiki-scrape
wiki_revid: 111070
wiki_fetched_at: '2026-05-30T18:47:09Z'
lang: fr
---

{{#vardefine:chapter\|14}} {{#vardefine:figure\|0}} ![[_media/Definirfiltre_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Boite de dialogue «Définir un filtre»]] Cette annexe décrit les règles de filtrage actuellement définies dans Gramps. Chacune de ces règles peut être utilisée pour la création de filtres personnalisés.

Ces règles sont présentées ici par catégories.

## Filtre ou Recherche

Il y a deux méthodes pour trouver des données dans Gramps : la recherche et le filtrage. La recherche utilise la barre de recherche en haut des vues en liste. (tels que la vue Individus, la vue Familles, etc ...). Le filtrage peut être utilisé en complément de la recherche ou seul dans les barres inférieures et latérales de Gramplets. **La barre de recherche du haut n'apparaît que si la barre latérale n'est pas présente**. Vous pouvez fermer/afficher les barres de Gramplets latérale et inférieure depuis le menu ou .

La recherche et le filtrage fonctionne différemment et il est utile de connaître ces différences : ![[_media/Barrerechanot_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Barre de recherche]]

- *Recherche* - la barre de recherche en haut des listes explore les données telles qu'elles apparaissent à l'écran dans les lignes et colonnes. La fonction de recherche est probablement celle que vous utiliserez le plus souvent, car c'est la plus simple et la plus rapide, mais elle a certaines limitations (voir ci-dessous).

Par exemple, si dans vos préférences d'affichage des noms vous avez défini "Nom de famille, Prénom" alors vous pouvez chercher des noms comme "Durand, J" dans toutes les lignes qui correspondent. Si vous changez l'affichage des noms (dans les Préférences) alors vous devrez suivre le nouveau format (par exemple, "Jean Durand").

![[_media/GrampletfiltreIndivbarlat_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Filtre dans la barre latérale]]

- *Filtre* - les filtres utilisent un système plus complexe. Il n'est pas limité à ce que vous voyez à l'écran, mais il recherche les données réelles dans tous les champs nom, et pas seulement celles qui apparaissent dans la vue. La saisie de plusieurs mots crée une phrase qui sera recherchée dans plusieurs champ de texte. Chaque mot dans la recherche de nom est utilisé séparément comme s'il s'agissait d'une sous-recherche dans les enregistrements trouvés dans la recherche avec le mot précédent. Et la recherche concerne simultanément *tous* les champs Nom.

Les filtres peuvent être créés et contrôlés depuis le menu , ou depuis un Gramplet spécifique dans les barres inférieure et latérale. Le Gramplet Filtre offre un filtre rapide comme la barre de recherche en haut des listes, mais tous les filtres suivent la distinction décrite ici.

Quelques points complémentaires :

- Le filtre va également regarder dans les noms alternatifs  & multiples  ; la barre de recherche ne regarde que le nom principal (celui affiché). C'est pourquoi si vous filtrez sur "Durand" vous verrez des individus listés qui, apparemment, ne correspondent pas. Mais si vous cherchez dans les détails de cette personne avec l'[éditeur de nom](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Fonctionnement_des_attributs,_adresses,_noms,_et_la_fusion#Noms), vous pourrez voir qu'elle a un nom alternatif contenant "Durand".
- Le filtre permet l'utilisation d'"expressions rationnelles" (voir plus bas). Ainsi vous pouvez trouver tous les noms qui commencent par "B" et finissent par "tin" : "B.\*tin". Vous ne pouvez pas faire cela dans la barre de recherche au dessus des listes.
- La barre de recherche ne trouve que ce qui est affiché. Si un nom ou un texte est trop long pour être visible dans la liste sous la barre de recherche, alors vous ne le trouverez pas. C'est quelque chose qu'il faut garder à l'esprit quand on fait une recherche dans les notes. Le mieux est d'utiliser le Filtre pour les notes et les autres champs avec des textes longs.
- Par défaut, les filtres ne tiennent pas compte de la casse ; "Tin" trouvera "tin", "TIN", ou "TiN". Par contre, les expressions rationnelles sont sensibles à la casse.

### Voir aussi

- [Filtre](wiki:Gramps_Glossary#filter) - définition
- [Filtres](wiki:Filter/fr)
- [Exemples de filtre](wiki:Example_filters/fr) - Filtres imbriqués
- [Étendre les filtres](wiki:Rule_expansions) avec les greffons
- [Pages en relation avec Filtres](wiki::Category:Filters)
- [Migration de vos filtres personnels](wiki:Template:Backup_Omissions) - La sauvegarde de Gramps ne sauve pas vos filtres.

{{-}}

## Expressions rationnelles

Les expressions rationnelles (ou expressions régulières, ou motif, ou sous la forme de l'abbréviation regex) sont des outils rapides et puissants pour décrire du texte qui doit correspondre à un modèle. L'utilisation des regex dans les filtres Gramps est en option.

La recherche par regex est une fonctionnalité avancée désactivée par défaut. Pour les filtres personnalisés, avec chaque règle individuelle vous avez l'option dans la boite de dialogue de la règle. Le Gramplet Filtre propose la même option pour saisir des expressions rationnelles directement dans les champs de recherche.

Par exemple, si vous cherchez un nom de famille commençant par "B", et finissant par "tin" alors vous pourrez utiliser des expressions rationnelles qui décriront ce motif. Ce peut être :

`^B.*tin`

- Le **^B** indique un texte qui commence par B
- Le **.** indique n'importe quel caractère unique (lettre, nombre, ou n'importe quoi)
- Le **\*** indique zéro ou plus caractères comme le précédent (dans ce cas, n'importe quel caractère unique)
- Le **tin** correspond aux lettres exactes t, i, n dans cet ordre.

Les expressions rationnelles sont puissantes avec de multiples options. Nous utilisons le système des expressions régulières du langage Python que nous allons documenter ici. De plus, vous pouvez vous référer aux expressions régulières Python.

*blanc* - Le terme "blanc" est utiliser ci-dessous pour signifier un ou plusieurs caractères que vous ne voyez pas. Par exemple, les tabulations, espaces, passage à la ligne.

Des caractères ont une signification particulière avec les expressions rationnelle. Ce sont :

- **`. ^ $ * + ? { } [ ] \ | ( )`**

Ils peuvent être utilisés comme suit :

- '`.`' correspond à n'importe quel caractères (lettre, nombre ou autre)
- '`^`' correspond au début du texte
- '`$`' correspond à la fin du texte
- '`*`' correspond à zéro ou plusieurs fois l'item précédent
- '`+`' correspond à un ou plusieurs fois l'item précédent
- '`?`' correspond à zéro ou une fois l'item précédent (le rend optionnel)
- '`{`' - début d'un nombre de correspondances
- '`}`' - termine le nombre de correspondances
- '`[`' - début d'un ensemble
- '`]`' - fin d'un ensemble
- '`\`' - le prochain caractère est une séquence particulière
- '`|`' - ou
- '`(`' - début d'un groupe
- '`)`' - fin d'un groupe

Des motifs particuliers commencent avec '`\`' représente un ensemble prédéfini de caractères souvent utiles, comme un ensemble de chiffres, de lettres ou un ensemble de quoi que ce soit non blanc. Les motifs spéciaux prédéfinis suivant sont un sous-ensemble de ceux qui sont disponibles.

- `\d` correspond à n'importe quel le chiffre ; équivalent a la classe `[0-9]`.
- `\D` correspond a n'importe quel caractère qui n'est pas un chiffre ; équivalent à la classe `[^0-9]`.
- `\s` correspond à n'importe quel caractère blanc ; équivalent la classe `[ \t\n\r\f\v]`.
- `\S` correspond à n'importe quel caractère non-blanc ; équivalent la classe `[^ \t\n\r\f\v]`.
- `\w` correspond à n'importe quel caractère alphanumérique ; équivalent à la classe `[a-zA-Z0-9_]`.
- `\W` correspond à n'importe quel caractère de non-alphanumérique ; équivalent a la classe `[^a-zA-Z0-9_]`.

Le quantificateur le plus compliqué est `{m,n}`, où `m` et `n` sont des entiers décimaux. Ces quantificateurs signifient qu'il doit y avoir au moins `m` répétitions, et au plus `n`.

### Trouver toutes les valeurs définies ou les blancs

<span id="regex_all">Pour trouver toutes les valeurs, `(.|\s)*` est adapté : n'importe quel caractère ou caractère "blanc" ; et zéro ou plus de répétitions d'eux.</span>

<span id="regex_null">Pour trouver des chaînes vides (vide ou nulle), `^.{0}$` est adapté : du début de la correspondance `^` pour n'importe quel caractère (sauf le passage à la ligne) `.` apparaissant exactement zéro fois `{0}` avant la fin de la correspondance `$`</span>

### Groupes et ensembles

Les groupes sont encadrés par les opérateurs '`('`, '`)`'. '`(`' et '`)`' ont tout à fait la même signification que dans les expressions mathématiques ; ils regroupent les expressions contenues à l'intérieur d'eux, et vous pouvez répéter les contenus d'un groupe avec un qualifiant de répétition, comme `*, +, ?, ou {m,n}`. Par exemple, `(ab)*` va correspondre à zéro ou plus de répétitions de `ab`.

Les ensembles dont marqués avec les opérateurs '`[`' et '`]`'.

Vous pouvez considérer les groupes comme une listes de possibilités séparés par l'opérateur '`|`', ou chaque possibilité comprend un, plusieurs ou zéro caractères et les ensembles comme une liste de possibilités où chaque possibilité est un seul caractère.

### Exemples

- **`^B.*tin$`** - correspond à tous les textes qui commencent par un '`B`', suivi par n'importe quelle chaîne, finissant avec '`tin`'.
  - correspond : **`Bertin`**, **`Berutin`**, **`Baroutin`**
  - ne correspond pas : **`Berutino`**
- **`^B.*tin`** - correspond à tous les textes qui commencent par un '`B`', suivi par n'importe quelle chaîne, suivi par '`tin`' (qui peut être suivi par autre chose).
  - correspond : **`Bertin`**, **`Berutino`**, **`Baroutin`**, **`Bertingardot`**, **`Batin`**, **`Baratine`**
  - Ne correspond pas : **`Bertoin`**

#### Variations communes d'un nom de famille

Exemple 1  
En utilisant l'expression **`Eri(ch|ck|k|c)(ss|s)on`** les noms suivant sont reconnus :

<!-- -->

    Erikson
    Eriksson
    Ericson
    Ericsson
    Erickson
    Ericksson
    Erichson
    Erichsson

**Explication** : en raison de ce qui suit :

- **`Eri`** = Eri
- **`(ch|ck|k|c)`** = groupe correspondant **`ch`**, **`ck`**, **`k`** ou **`c`**. Il essaie de trouver la plus longue chaîne correspondante en premier
- **`(ss|s)`** = groupe correspondant **`ss`** ou **`s`**. Il essaie de trouver la plus longue chaîne correspondante en premier
- **`on`** = on

<hr>

Exemple 2  
En utilisant l'expression **`Ba(in|yn|m|n)bri(dge|cke|g(g|e|))`** les noms suivant sont reconnus :

<!-- -->

    Bainbricke
    Bainbridge
    Bainbrig
    Bainbrigg
    Bambridge
    Banbrig
    Banbrige
    Baynbrige

**Explication** : en raison de ce qui suit :

- **`Ba`** = Ba
- **`(in|yn|m|n)`** = groupe correspondant **in**, **yn**, **m** ou **n**. Il essaie de trouver la plus longue chaîne correspondante en premier.
- **`bri`** = bri
- **`(dge|cke|g(g|e|))`** = groupe correspondant **dge**, **cke** ou (**g** avec **g**, **g** avec **e** ou **g** avec rien)

<hr>

Exemple 3  
En utilisant l'expression **`n(es|oua|oai|o[iya]|a[iy])r(r|)(on|((e|)au(x|t|d|lt|)))`** les noms suivant sont reconnus :

<!-- -->

    nairaud
    nairault
    naireaud
    nayrault
    nesrau                
    nesrault
    nesreau
    nesreaud
    noirau
    noiraud
    noirauld
    noirault
    noiraut
    noiraux
    noireau
    noireaud
    noireault
    noireaut
    noirraux
    noirreau
    noirreaud
    nouarault
    noyraud
    noyrault 

**Explication** : en raison de ce qui suit :

- **`n`** = n
- **`(es|oua|oai|ensemble1|ensemble2)`** = groupe correspondant **es**, **oua**, **oai**, **set1** ou **set2**
- **`ensemble1`** est **`o[iya]`** = ensemble correspondant à **o** ET **i**, **y** ou **a**. En d'autres termes **oi**, **oy** ou **oa**
- **`ensemble2`** est **`a[iy]`** = ensemble correspondant à **a** ET **i** or **y**. En d'autres termes **ai** ou **ay**
- **`r`** = r
- **`(r|)`** = groupe correspondant **r** ou rien
- **`(on|(sous-groupe 1)`** = groupe correspondant **on** ou **sous-groupe 1**.
- **sous-groupe 1** est un groupe correspondant à (**sous-groupe 2 au sous-groupe 3**)
- **sous-groupe 2** est **(e\|)** = groupe correspondant **e** ou rien
- **`au`** = au
- **sous-groupe 3** est **(x\|t\|d\|lt)** = groupe correspondant **x**, **t**, **d** ou **lt**

#### Tester les expressions rationnelles

Des tests pour les expressions rationnelles peuvent être trouvées par Google®. <https://www.regexr.com/> est simple et pratique.

## Éditeur de filtre personnalisé

Vous pouvez faire de multiples sélections d'individus, évènements, lieux, etc, en utilisant simplement le filtre de la barre latérale dans les vues d'individus, évènements, lieux, etc ; mais noter que l'option "Utiliser les expressions rationnelles" ne marchent que dans des champs particuliers pour chaque vue.

Si le filtre de la barre latérale ne répond pas à vos besoins, vous aurez besoin de fabriquer un filtre personnalisé.

### Dialogue Filtres de 'nom de la catégorie'

![[_media/Filtrepersofam_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Exemple 'Filtres de famille']]

Pour créer un nouveau filtre personnalisé ou voir ceux précédemment créés, allez au menu pour ouvrir la boite de dialogue où le "nom de la catégorie" change en fonction de la catégorie sélectionnée dans le navigateur (barre latérale gauche), soit :

-  Filtres d'individus

-  Filtres de familles

-  Filtres d'évènements

-  Filtres de lieux

-  Filtres de sources

-  Filtres de media

-  Filtres de dépôts

-  Filtres de notes

-  Filtres de citations

Alternativement, dans le Gramplet Filtre de la barre latérale, cliquez le bouton sur la ligne filtre.

Dans la boite de dialogue , les actions suivantes sont disponibles par les boutons du côté droit de la fenêtre :

-  

  
affiche le dialogue et ajoute une nouvelle structure de filtre personnalisé (non encore dénommé).

-  

  
ouvre le dialogue et charge votre filtre personnalisé existant pour le modifier.

-  

  
fait une copie exacte du filtre sélectionné

-  

  
ouvre la fenêtre de résultats contenant la liste des correspondances qui satisfont au test. Si le test du filtre est invalide, c'est une erreur qui s'affiche.

-  

  
supprime le filtre sélectionné de l'ensemble des filtres personnalisés.

{{-}}

### Définir un filtre

![[_media/Filtrepersodefinir_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Définir un filtre]]

L'éditeur de filtre personnalisé génère des filtres selon ses besoins pouvant être utilisés pour trouver des individus dans les rapports, exportations, et autres outils et utilitaires. C'est un outil très puissant pour les analyses généalogiques.

Dans la fenêtre :

- Saisissez le nom de votre nouveau filtre dans le champ .

- Mettez n'importe quel commentaire pour vous aider à identifier ce filtre plus tard dans le champ .

- Ajouter autant de que vous voulez dans la Liste des règles en utilisant le bouton .

- Si un filtre comporte plusieurs règles, choisissez dans la liste déroulante parmi les  :
  - (par défaut)

  - 

  - 

-  Cocher pour inverser la règle de filtrage. Par exemple, inverser la règle **"a un ascendant commun avec I1"** trouvera tous les individus qui n'ont pas d'ascendant commun avec cette personne.

{{-}}

### Dialogue Ajouter une règle

![[_media/Filtrepersoajoutregle_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogue &#39;Ajout d&#39;une règle&#39;]] Pour définir un nouveau filtre, cliquez sur dans la fenêtre pour ouvrir le dialogue .

Le panneau de la partie gauche montre les règles disponibles rangées par catégories dans une arborescence qui peut être déployée.

Pour des détails sur une règle, vous pouvez soit :

- Utilisez le champ de recherche
- Cliquer sur la flèche pour déployer/refermer la catégorie appropriée.
- Sélectionner la règle dans l'arborescence en cliquant sur son nom. La partie droite affiche le nom, la description, et les valeurs à définir pour la règle sélectionnée.

Une fois l'ensemble des règles ajoutées, cliquez le bouton pour ajouter le nouveau filtre. {{-}}

### Fenêtre de résultats du test de filtre

![[_media/Filtrepersotest_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Exemple d&#39;un résultat de test]] A partir de la fenêtre et le bouton , vous obtenez une fenêtre de résultats.

Une fenêtre de résultats valide peut être vide si aucun enregistrement ne correspond au filtre. {{-}}

## Quelles règles de filtre dans quelle catégorie ?

Selon la catégorie affichée, vous disposez d'un ensemble de règles de filtre différent.

\*; Catégorie Tableau de bord : Pas de règles de filtre disponible

\*; Catégorie Individus, Relations et Graphiques : Règles pour filtres citation/source, filtres familiaux, filtres généraux, filtres relationnels, filtres sur les ascendants, filtres sur les descendants, filtre sur les évènements.

\*; Catégorie Famille : Règles pour filtres citation/source, filtres généraux, filtre sur l'enfant, filtre sur la mère, filtre sur le père, filtre sur les évènements.

\*; Catégorie Évènement et Media : Règles pour filtres citation/source et filtres généraux.

\*; Catégorie Lieux : Règles pour filtres citation/source, filtres généraux et filtre sur la position.

\*; Catégorie Géographie (seulement pour le filtre dans la barre latérale ou inférieure) : Règles pour filtres citation/source, filtres familiaux, filtres généraux, filtres relationnels, filtres sur les ascendants, filtres sur les descendants, filtre sur les évènements.

\*; Catégorie Sources, Dépôts et Notes : Règles seulement pour filtres généraux.

\*; Catégorie Citations : Règles pour filtres généraux et filtres sur les sources.

## Filtres généraux

Cette catégorie comprend les règles les plus générales :

\*;A une galerie : cette règle sélectionne les objets principaux avec des media.

\*;A l'identifiant : cette fonction sélectionne les objets principaux ayant exactement l'identifiant Gramps donné. Vous pouvez entrer l'identifiant dans un champ texte, ou bien sélectionner un objet dans la liste en cliquant le bouton . Dans ce cas, l'identifiant apparaîtra dans le champ de saisie de texte après la sélection.

\*;A une note : cette règle sélectionne les objets avec une note.

\*;A une référence de <nombre> : cette fonction sélectionne les objets selon un nombre de référence.

\*;A une citation/source : cette règle sélectionne les objets avec une citation/source.

\*;Correspond au filtre suivant : cette fonction sélectionne les objets par un filtre. Le filtre est choisi par son nom dans un menu.

\*;Dernière modification : cette règle sélectionne les objets modifiés depuis une date précise.

\*;Noms qui contiennent une chaîne : cette fonction sélectionne toutes les objets dont les enregistrements contiennent une sous-chaîne spécifiée. Tous les enregistrements textuels sont recherchés. Une option peut rendre la recherche sensible à la casse, ou correspondante à une expression rationnelle.

\*;Objets marqués : cette règle sélectionne tous les objets qui sont sur la liste de signet.

\*;Objets marqués comme privés : cette règle sélectionne les objets principaux dont les informations sont marquées comme privées.

\*;Tous les objets : cette règle accepte tous les objets de la base de données. Elle n'est pas très utile seule sauf pour tester. Par contre, elle sert en combinaison avec d'autres règles.

## Filtres individus

\*;A une adresse : cette règle sélectionne tous les individus avec une adresse.

\*;A une association : cette règle sélectionne tous les individus associés à quelqu'un dans l'onglet association de l'.

\*;A un enregistrement complet : cette règle sélectionne tous les individus dont les enregistrements sont marqués comme complet. Actuellement, l'information complète de l'individu est marquée manuellement, dans le dialogue .

\*;Est la personne centrale : cette règle sélectionne la personne centrale, souche.

\*;Est une femme : cette fonction sélectionne les femmes.

\*;Est un homme : ce filtre sélectionne les hommes.

\*;Individus dont le nom contient : cette règle sélectionne toute personne dont le nom contient la valeur indiquée, complètement ou en partie. Par exemple, Marta Ericsdotter sera trouvée par la règle sous-chaîne "eric" pour le nom de famille. Des valeurs séparées peuvent être employées pour leprénom, le nom de famille, le suffixe, et le titre. La règle est efficace si et seulement si, toutes les valeurs non vides (partiellement) sont assorties par le nom d'une personne. Pour employer juste une valeur, laissez les autres valeurs vides.

\*;Individus avec des noms incomplets : cette règle sélectionne toutes les personnes ayant des noms incomplets.

\*;Individus probablement en vie : cette règle sélectionne toutes les personnes dont les dates n'indiquent pas leur mort et qui ne sont pas anormalement vieilles, jugeant à leurs données disponibles de naissance et aujourd'hui.

\*;Individus sans date de naissance : cette règle sélectionne les personnes sans date de naissance.

## Filtres événements

Cette catégorie regroupe les fonctions qui utilisent les événements des personnes :

\*; A une naissance : cette règle sélectionne les personnes dont la naissance correspond aux valeurs données pour Date, Lieu, et Description. La correspondance est faite même quand l'événement n'est que partiellement identique. Les correspondances sont insensibles à la casse des caractères. Par exemple, toute personne décédée en France sera sélectionnée par la valeur "fr" pour le lieu. La règle sélectionne l'entrée si et seulement si toutes les valeurs non vides correspondent (partiellement) à la naissance de la personne. Si vous voulez sélectionner sur un seul champ, laissez les autres champs vides.

\*; A un décès : cette règle sélectionne les personnes dont le décès correspond aux valeurs données pour Date, Lieu, Type et Description. La correspondance est faite même quand l'événement n'est que partiellement identique. Les correspondances sont insensibles à la casse des caractères. Par exemple, toute personne ayant obtenu un diplôme en France sera sélectionnée par la valeur "fr" pour le lieu. La règle sélectionne l'entrée si et seulement si toutes les valeurs non vides correspondent (partiellement) à la naissance de la personne. Si vous voulez sélectionner sur un seul champ, laissez les autres champs vides.

\*; A un événement personnel : cette règle sélectionne les personnes dont un événement individuel correspond aux valeurs données pour Date, Lieu, Type et Description. La correspondance est faite même quand l'événement n'est que partiellement identique. Les correspondances sont insensibles à la casse des caractères. Par exemple, toute personne s'étant mariée en France sera sélectionnée par la valeur Mariage pour l'événement et "fr" pour le lieu. L'événement personnel est sélectionné dans une liste déroulante. La règle sélectionne l'entrée si et seulement si toutes les valeurs non vides correspondent (partiellement) à un événement de la personne. Si vous voulez sélectionner sur un seul champ, laissez les autres champs vides.

\*; A un événement familial : cette règle sélectionne les personnes dont un événement familial correspondant aux valeurs données pour Date, Lieu, Type et Description. La correspondance est faite même quand l'événement n'est que partiellement identique. Les correspondances sont insensibles à la casse des caractères. Par exemple, toute personne s'étant mariée en France sera sélectionnée par la valeur Mariage pour l'événement et "fr" pour le lieu. L'événement personnel est sélectionné dans une liste déroulante. La règle sélectionne l'entrée si et seulement si toutes les valeurs non vides correspondent (partiellement) à un événement de la personne. Si vous voulez sélectionner sur un seul champ, laissez les autres champs vides.

\*; Témoins : cette règle sélectionne les personnes qui sont présentes comme témoin. Si et seulement si le type d'événement (Individuel ou Familial) est indiqué, les événements de ce type seront recherchés.

\*; Individus avec des événements incomplets : cette règle sélectionne les individus sans date ou lieu dans l'un des événements.

\*; Familles avec des événements incomplets: cette règle sélectionne les familles sans date ou lieu dans l'un des événements.

## Filtres familiaux

Cette catégorie comprend les règles suivantes qui sélectionnent les personnes d'après leurs relations familiales :

\*; Individus avec des enfants : cette règle sélectionne les personnes avec des enfants.

\*; Individus ayant contractés plusieurs mariages : cette règle sélectionne des personnes avec plus d'un conjoint.

\*; Individus sans mariage : cette règle sélectionne des personnes sans conjoints.

\*; Individus adoptés : cette règle sélectionne les personnes adoptées.

\*; A les relations : cette règle sélectionne des personnes avec une relation particulière. Le nombre de relations et le nombre d'enfants peuvent être indiqués. La règle est efficace si, et seulement si, toutes les valeurs non vides (partiellement) correspondent. Pour employer juste une valeur, laissez les autres valeurs vides.

\*; Est le conjoint résultant du filtrage : cette règle sélectionne des personnes mariées à un individu associé à un filtre. Le nom du filtre doit être choisi parmi le menu.

\*; Est un enfant résultant du filtrage : cette règle sélectionne les personnes pour qui l'un ou l'autre parent est associé à un filtre. Le nom du filtre doit être choisi parmi le menu.

\*; Est un parent résultant du filtrage : cette règle sélectionne les personnes dont l'enfant est associé à un filtre. Le nom du filtre doit être choisi parmi le menu.

\*; Est un frère ou une soeur résultant du filtrage : cette règle sélectionne les frères et soeurs des individus associés à un filtre. Le nom du filtre doit être choisi parmi le menu.

## Filtres sur les ascendants

Cette catégorie comprend les règles suivantes qui sélectionnent les personnes d'après leurs relations d'ascendance avec d'autres personnes :

\*; Est l'ancêtre de : cette règle sélectionne les personnes ancêtres de la personne désignée. L'option Inclusif précise si la personne désignée est à considérer comme ancêtre d'elle-même, ce qui est utile pour construire des éditions. Vous pouvez entrer l'identifiant dans un champ texte, ou bien sélectionner une personne dans la liste en cliquant le bouton . Dans ce cas, l'identifiant apparaîtra dans le champ de saisie de texte après la sélection.

\*; Est l'ascendant d'un individu sur au moins N générations : cette règle sélectionne les personnes ancêtres de la personne désignée à au moins N générations d'écart. Par exemple, un écart de 2 sélectionnera les grands-parents, les arrière-grands-parents..., mais pas les parents de la personnes désignée.

\*; Est l'ascendant d'un individu sur moins de N générations : cette règle sélectionne les personnes ancêtres de la personne désignée à au plus N générations d'écart. Par exemple, un écart de 2 sélectionnera les parents et les grands-parents, mais pas les arrière-grands-parents... de la personnes désignée.

\*; A un ancêtre commun avec : cette règle sélectionne les personnes qui ont un ancêtre commun avec la personne désignée.

\*; A un ascendant commun avec les individus résultant du filtrage : cette règle sélectionne les personnes qui ont un ancêtre commun avec les personnes sélectionnées par un filtre. Le filtre est choisi par son nom dans un menu.

\*; Est l'ascendant d'un individu résultant du filtrage : cette règle sélectionne les ancêtres des personnes sélectionnées par un filtre. Le filtre est choisi par son nom dans un menu.

## Filtres sur les descendants

Cette catégorie comprend les règles suivantes qui sélectionnent les personnes d'après leurs relations de descendance avec d'autres personnes :

\*; Est descendant(e) de : cette règle sélectionne les personnes qui descendent de la personne désignée. L'option Inclusif précise si la personne désignée est à considérer comme descendant d'elle-même, ce qui est utile pour construire des rapports. Vous pouvez entrer l'identifiant dans un champ texte, ou bien sélectionner une personne dans la liste en cliquant le bouton . Dans ce cas, l'identifiant apparaîtra dans le champ de saisie de texte après la sélection.

\*; Est descendant d'un individu sur au moins N générations : cette règle sélectionne les personnes qui descendent de la personne désignée à au moins N générations d'écart. Par exemple, un écart de 2 sélectionnera les petits-enfants, les arrière-petits-enfants..., mais pas les enfants de la personnes désignée.

\*; Est descendant d'un individu sur moins de N générations : cette règle sélectionne les personnes qui descendent de la personne désignée à au plus N générations d'écart. Par exemple, un écart de 2 sélectionnera les enfants et les petits-enfants, mais pas les arrière-petits-enfants... de la personnes désignée.

\*; Est descendant d'un individu résultant du filtrage : cette règle sélectionne les personnes qui descendent d'une des personnes sélectionnées par un filtre. Le filtre est choisi par son nom dans un menu.

\*; Est un membre de la famille descendante de : cette règle sélectionne en plus des descendants directs de la personne désignée, ceux des conjoints des descendants directs.

## Filtres relationnels

Cette catégorie comprend les règles suivantes qui sélectionnent les personnes d'après leurs relations :

\*; Relation entre deux individus : cette règle sélectionne les ancêtres des deux personnes jusqu'à leur ancêtre commun s'il existe. Ceci donne la "liaison relationnelle" entre ces individus à travers leur(s) ancêtre(s) commun(s). Vous pouvez soit saisir l'ID de chaque personne dans le champ textuel approprié, soit sélectionner l'individu depuis une liste en appuyant sur le bouton . Pour ce dernier choix, l'ID apparaîtra dans le champ textuel après la sélection réalisée.

## Filtres divers

Cette catégorie comprend les règles suivantes qui n'appartiennent pas aux autres catégories :

\*; A l'attribut individuel : cette règle sélectionne les personnes qui ont l'attribut individuel avec une valeur donnée. L'attribut sur lequel porte la sélection est choisi dans un menu déroulant. La valeur désirée pour cet attribut est saisie dans une zone de texte.

\*; A l'attribut familial : cette règle sélectionne les personnes qui ont l'attribut familial avec une valeur donnée. L'attribut sur lequel porte la sélection est choisi dans un menu déroulant. La valeur désirée pour cet attribut est saisie dans une zone de texte.

\*; A un événement mormon : cette règle sélectionne les individus et familles ayant un événement mormon.

## Les étiquettes

Pour les personnes utilisant *Gmail* ou *Thunderbird*, les étiquettes sont familières. Au lieu de classer les messages dans des répertoires *Outlook* (Windows) ou *Evolution* (Linux), ils sont classés en assignant des étiquettes. Ainsi au lieu d'avoir une classification disjointe N:1 (un message ne peut être que dans 1 répertoire, un répertoire peut contenir plusieurs messages), dans *Gmail* et *Thunderbird* il y a une classifiaction N:M (un message peut avoir plusieurs étiquettes, et une étiquette peut être appliquée sur plusieurs messages électroniques).

Dans la même logique, quand vous avez un grand arbre, vous pouvez avoir besoin de générer des sous-ensembles de l'arbre, et ces derniers peuvent se superposer. Par exemple, avec les sous-ensembles de votre côté paternel et maternel, un sous-ensemble qui a émigré vers les États-Unis, ou des personnes connues dans votre arbre.

L'idée est d'assigner des étiquettes différentes pour chaque groupes : *PÈRE*, *MÈRE*, *USA* et *CONNU(E)* par exemple.

Les **Marqueurs** des versions antérieures sont comme les répertoires pour les messages électroniques. Un individu ne peut avoir qu'un seul marqueur. Les étiquettes sont plutôt des marqueurs à valeurs multiples.

Allez dans le . ![[_media/Etiquetmenuedit_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Actions disponibles à partir du menu Édition]] {{-}}

Ou cliquez sur le bouton ![[_media/16x16-gramps-tag.png]] dans la barre d'outils. ![[_media/Etiquetmenubouton_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Actions disponibles à partir du bouton Étiquettes]] {{-}}

### Dialogue nouvelle étiquette

![[_media/Etiquetnouvel_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nouvelle étiquette]]

Vous pouvez ajouter une étiquette à une ou plusieurs entrées des listes de chaque catégorie. Il suffit de sélectionner les entrées concernées avant d'appeler la boite . Dans le dialogue, saisir le nom d'étiquette souhaité et choisissez la couleur que vous voulez associer en cliquant sur l'échantillon de couleur en fin de ligne. {{-}}

### Organiser les étiquettes

![[_media/Etiquetorganis_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Organiser les étiquettes - exemple]] Le dialogue permet de changer leur ordre, de les supprimer, modifier. {{-}}

### Dialogue Sélection d'étiquettes

![[_media/Etiquetselect_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sélection d&#39;étiquette dans la fenêtre de saisie d&#39;un individu avec le bouton «Éditer la liste d&#39;étiquettes»]] Quand vous utilisez le bouton ![[_media/16x16-gramps-tag.png]] dans n'importe quelle fenêtre de saisie comme celle d'un le dialogue de sélection des étiquettes apparaît et permet l'ajout ou la suppression d'étiquettes existantes associés à cet enregistrement. Les étiquettes s'affiche par ordre alphabétique. {{-}}

### Utilisation des étiquettes

Voici quelques idées et opérations possibles avec les étiquettes.

#### Étiquettes et filtres

- Les étiquettes et filtres créent tous les deux des sous-ensembles dans l'arbre. Néanmoins il y a des différences dans l'utilisation.

![[_media/Etiquetfiltre_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Un filtre sur les étiquettes depuis la barre latérale Filtre]]

Spécifier votre branche paternelle en utilisant les filtres est relativement simple; il existe déjà des filtres basés sur cette logique pour le faire. D'un autre côté, spécifier les individus qui ont émigré vers les États-Unis est plus compliqué, tout comme pour les personnes connues il est impossible d'avoir une règle logique. Les étiquettes sont bien plus pratiques dans ce cas là.

Par ailleurs les filtres ont l'avantage d'être **dynamique**. Si vous avez un nouvel ancêtre de votre père dans votre base de données, il sera automatiquement ajouté au filtrage.

À l'inverse, les étiquettes sont **statiques**. Lorsque l'on ajoute une personne connue dans l'arbre, vous avez explicitement besoin de l'étiqueter *CONNU(E)*.

- Le premier objet qui vient à l'esprit est l'individu, et c'est également là où les étiquettes sont les plus utilisées. Néanmoins, on peut ajouter des étiquettes à d'autres objets :
  - Lieux: par exemple "Lieux à visiter",
  - Source: par exemple "Sources en allemand",
  - Notes: par exemple "Notes en cours", ou "Notes en allemand",
  - Media: par exemple "Image appartenant à l'oncle Alfred".

Les étiquettes sont utilisables pour **tous les objets principaux**. {{-}}

#### Colonne étiquettes

![[_media/PeopleListView-ExampleTagColoredRows-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Colonne Étiquettes et lignes colorées]]

Il est pratique d'avoir une colonne dans les vues des objets qui supportent les étiquettes. Le nom des étiquettes se présente comme une liste séparée par des virgules.

Pour ajouter cette colonne, passer par la (menu Affichage ou bouton de la barre d'outils) et sélectionnez la case à cocher dans l'onglet de la boite de dialogue. {{-}}

#### Rapport Étiquette

Le [Rapport Étiquette](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Rapports#Rapport_Étiquette) liste les [principaux objets](wiki:Gramps_Glossary#primary_object) (individus, familles, notes) qui ont l'étiquette sélectionnée. {{-}}

[M](wiki:Category:Fr:Documentation)
