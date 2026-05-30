---
title: Fr:Manuel wiki pour Gramps 6.0 - Catégories
categories:
- Fr:Documentation
managed: false
source: wiki-scrape
wiki_revid: 125441
wiki_fetched_at: '2026-05-30T18:34:10Z'
lang: fr
---

{{#vardefine:chapter\|4}} {{#vardefine:figure\|0}}

## Catégories du navigateur

L'information généalogique est très large et peut être extrêmement détaillée. L'afficher est un défi que Gramps relève en divisant et organisant l'information à travers une série de catégories. Chaque catégorie, possédant sa propre vue, affiche une partie de l'information totale, sélectionnée selon une catégorie particulière. Le navigateur est situé à la partie gauche de la fenêtre principale et permet la sélection des différentes catégories.

- [Tableau de bord](#Gramplets) : affiche les différents gramplets, petits widgets pouvant aider à la recherche généalogique.

<!-- -->

- [Individus](#Individus) : affiche les individus de l'arbre familial sans leurs connections. Cette catégorie contient une vue sous forme de liste et une vue hiérarchisée.

<!-- -->

- [Relations](#Relations) : affiche les relations entre la personne active et les autre individus sous forme de texte. Ceci inclut les parent, conjoints, et enfants.

<!-- -->

- [Familles](#Familles) : affiche les familles de l'arbre familial

<!-- -->

- [Graphiques](#Graphiques) : affiche un graphique pour la personne sélectionnée

<!-- -->

- [Événements](#Événements) : affiche les événements de l'arbre familial

<!-- -->

- [Lieux](#Lieux) : affiche les lieux de l'arbre familial

<!-- -->

- [Géographie](#Géographie) : affiche les données de votre arbre sur une carte

<!-- -->

- [Sources](#Sources) : affiche les sources de l'arbre familial

<!-- -->

- [Citations](#Citations) : affiche les citations de l'arbre familial

<!-- -->

- [Dépôts](#Dépôts) : affiche les dépôts de l'arbre familial

<!-- -->

- [Media](#Media) : affiche les objets media de l'arbre familial

<!-- -->

- [Notes](#Notes) : affiche les notes de l'arbre familial

Ces catégories peuvent contenir plusieurs représentations de vos données. Chaque présentation spécifique est appelée une Vue. Par exemple :

- Catégories :
  - Vue (1)
  - Vue (2)

Pour chaque catégorie, vous avez plusieurs façons de changer de vue :

1.  En cliquant sur l'icône correspondante dans la barre d'outils
2.  A partir du
3.  Par des [raccourcis clavier](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Raccourcis_clavier#Raccourcis). Voir le raccourci *Change la vue vers son numéro 1/2/... dans la catégorie*

La section suivante présente une brève description de chaque catégorie et des vues correspondantes.

## Tableau de bord

![[_media/Grampletsview-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplets]]

Cette catégorie affiche un certain nombre de [widgets](http://fr.wikipedia.org/wiki/Widget), appelés Gramplets, qui peuvent vous aider dans vos recherches. Deux gramplets sont affichés au démarrage (Bienvenue et Principaux noms de famille) dans une mise en page en deux colonnes. Quand un arbre familial est ouvert, par un clic-droit dans une zone vide de la vue, vous aurez accès à un menu contextuel qui affiche la liste des Gramplets que vous pouvez ajouter et utiliser.

- : ce gramplet calcule les âges des individus de votre arbre familial, en vie à cette date donnée.

- : affiche plusieurs graphiques sur les tranches d'âge

- : dans cette fenêtre vous pouvez ajouter votre liste "À faire", ou toute autre note. Plusieurs gramplets "À faire" peuvent vous organiser dans vos recherches.

- : est une fenêtre **Bienvenue dans Gramps**

- : Propositions de tâches à faire

- 

- : garde une trace de ce que vous avez fait et des enregistrements que vous avez regardés

- 

- : affiche les événements pour ces jours/mois et années.

- : affiche votre **top 10** des noms de famille.

- : affiche une fenêtre avec une **nuée** de les plus courants.

- : affiche une fenêtre avec un résumé de l' : nombre d'individus, hommes et femmes, nombre de familles, media, etc.

D'autres Gramplets de développeur indépendants peuvent être installés comme :

- Gramplet Nouvelles - les nouvelles de Gramps
- Gramplet Données saisies- modifie le nom de la personne active, ses date et lieu de naissance, ses date et lieu de décès, et ajoute des individus
- Gramplet Python- un shell Python
- Gramplet FAQ- questions fréquentes
- Gramplet Note- voir et modifier la note principale de la personne active

et plein d'autres. Voir [Extensions](wiki:Third-party_Addons) pour plus de détails.

Pour obtenir plus d'informations sur l'utilisation des Gramplets, voir [Gramplets](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/fr). {{-}}

## Individus

Dans la , les vues sous forme de liste simple ou de liste (par défaut) affichent la liste de tous les individus dans la base de données. A partir de cette vue, vous pouvez ajouter, modifier, enleveer ou fusionner des individus. Chaque vue (liste simple ou groupée) affiche plusieurs colonnes d'information sur chaque personne.

Par défaut, la vue affiche :

- Son nom
- Son Id Gramps
- Son genre
- Sa date de naissance
- Sa date de décès

Des colonnes supplémentaires peuvent être affichées :

- Son lieu de naissance
- Son lieu de décès
- Le nom de son conjoint
- Nombre de parents
- Nombre de marriages
- Nombre d'enfants
- Nombre de notes 'A faire'
- Privé
- Étiquettes
- Date dernière modification

[L'éditeur de colonne](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Éditeur_de_colonne) peut être utilisé pour afficher, cacher ou changer l'ordre des colonnes affichées. Cet éditeur est accessible par le menu ou en cliquant sur le bouton ![[_media/Gramps-config.png]] de la barre d'outils.

Voir aussi :

- [Utilisation de la catégorie Individus](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Navigation#Utilisation_de_la_catégorie_Individus)
- [Modifier les informations des individus](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Ajouter_des_individus,_dates,_familles_et_relations#L&#39;information_personnelle)

{{-}}

### Types de vues

Deux types de vues existent dans cette catégorie:

- La vue hiérarchisée des individus : Les individus sont groupés d'après leur nom de famille. A gauche de chaque nom de famille il y a une flèche ou un autre indicateur du type *+*. Cliquez sur l'indicateur pour déployer l'ensemble de la liste d'individus partageant le même nom de famille. Cliquez une nouvelle fois sur l'indicateur compactera la liste et n'affichera que le nom de famille.

![[_media/People_Treeview-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vue hiérarchisée des individus (défaut)]]

{{-}}

- La vue sous forme de liste d'individus : Liste de tous les individus de la base de données triés sur la première colonne qui, par défaut, est la colonne `Nom`.

![[_media/People_Listview-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Liste des individus]] {{-}}

### Onglet de la barre inférieure pour la catégorie Individus

Les deux vues (groupée et liste simple) partage les onglets suivant dans la [barre inférieurs](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Fenêtre_principale#Barres_inférieure_et_latérale) : {{-}}

#### Détails

Voir le Gramplet [Details](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Gramplets#Détails) {{-}}

#### Galerie

Voir le Gramplet [Gallery](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Gallery) {{-}}

#### Evènements

Voir le Gramplet [Events](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Events) {{-}}

#### Enfants

Voir le Gramplet [Children](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Children) {{-}}

#### Citations

Voir le Gramplet [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) {{-}}

#### Notes

Voir le Gramplet [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) {{-}}

#### Attributs

Voir le Gramplet [Attributs](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Gramplets#Attributs) {{-}}

#### Références

Voir le Gramplet [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) {{-}}

### Onglets de la barre latérale de la catégorie Individus

Les deux vues (groupée et liste simple) partage les onglets suivant de la [barre latérale](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Fenêtre_principale#Barres_inférieure_et_latérale) par défaut. {{-}}

#### Filtre

Voir le Gramplet [Filtre](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Gramplets#Filtre) {{-}}

## Relations

La catégorie Relations affiche une vue de toutes les liens de parenté autour de la personne active (la personne sélectionnée). En particulier, cette vue montre ses parents, ses frères et sœurs, ses conjoints et ses enfants.

La catégorie Relations est adaptée pour permettre une navigation rapide. Vous pouvez changer rapidement de personne active simplement en cliquant sur le nom de n'importe quelle personne listée. Chaque nom est un [lien hypertexte](http://fr.wikipedia.org/wiki/Hyperlien), similaire à une page internet.

Le nom de la personne active est affiché en **gras**. Les autres noms sont affichés en style **gras** et *italique* selon les relations existantes pour cette personne.

- Pour un individu noté comme parent ou conjoint de la personne active, le nom utilise un [style typographique différent](http://fr.wikipedia.org/wiki/Graisse_%28typographie%29) si cet individu a au moins un parent.
- Pour un individu noté comme enfant, frère ou sœur de la personne active, le nom utilise un [style typographique différent](http://fr.wikipedia.org/wiki/Graisse_%28typographie%29) si cet individu a au moins un enfant.

Les dates sont en style normal ou 'italique' si l'événement affiché est un événement de recours, i.e. un événement qui se substitue à un autre événement manquant. Cela peut être un baptême pour une naissance, l'inhumation pour le décés, etc.

### Vue de la catégorie Relations

Pour les vue de la catégorie Relations, par le menu ou la barre d'outils, vous pouvez sélectionner :

- ou l'icône  - ouvre la

- ou l'icône  - pour créer une nouvelle famille avec la personne active listée comme enfant.

- ou l'icône  - qui ouvre le [Sélecteur de famille](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Catégories#S.C3.A9lecteur_de_famille#Sélecteur_de_famille) pour pouvoir choisir dans la liste des familles existantes et ensuite ajouter la personne comme enfant de cette famille.

- ou l'icône

- ou l'icône  - pour ouvrir la fenêtre [Réorganiser les relations](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Cat%C3%A9gories#R.C3.A9organiser_les_relations)

![[_media/Family-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vue Relations]] ![[_media/Family2-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vue Relations]]

La vue Relations affiche ces différentes sections :

#### La personne active

- en haut de l'écran, sont affichés le nom, , les informations de et de ainsi que le calcul de l'âge de la personne active. Vous pouvez sélectionner et copier le texte des champs de naissance et décès.
- Si une photo de l'individu est disponible, elle est affichée sur le côté droit. Cette photo est la première image disponible dans la galerie de cette personne (si elle existe). Vous pouvez cliquer sur la photo pour l'ouvrir dans la visionneuse par défaut.
- A côté du nom de la personne il y a un symbole indiquant le genre, et un bouton . Cliquer sur le bouton vous permettra d'éditer toutes les informations de l'individu dans un dialogue d'.

#### Les parents

La section parents affiche les familles dont la personne est l'enfant. Puisqu'il est possible pour une personne d'avoir plusieurs couples de parents, il est possible d'avoir plusieurs sections parents.

Vous pouvez éditer des parents existants en sélectionnant le bouton à côté des parents. Si vous sélectionnez à côté du couple de parents, alors la personne active ne sera plus l'enfant des parents. Ce bouton ne supprime pas la relation entre les parents.

#### Sélecteur de famille

![[_media/Selecteurfamille-52-fr.png|Right|Sélecteur famille]] La fenêtre de vous permet de créer un lien avec une famille existante. Les colonnes suivantes sont affichées : ID (ordre de tri par défaut), Père, Mère, Dernière modification. Utilisez le bouton pour filtrer la liste en fonction d'une des options de la liste déroulante :

- **ID contient** (par défaut)
- *ID ne contient pas*
- *Père contient*
- *Père ne contient pas*
- *Mère contient*
- *Mère ne contient pas*
- *Dernière modification contient*
- *Dernière modification ne contient pas*

#### Frères et sœurs

Cette section monte les frères et sœurs de la personne active.

#### Famille

Cette section est similaire à la section parents qui affiche les familles où la personne active est un parent. Parce qu'il est possible d'avoir de multiples familles, il est possible d'avoir de multiples sections famille. Chaque section famille affiche le conjoint et les enfants.

Vous pouvez ajouter une famille en sélectionnant dans la barre d'outils. Ceci créera une nouvelle famille dont la personne active sera le père ou la mère.

Sélectionner le bouton à côté du conjoint vous permettra d'éditer la famille affichée. Cliquer sur le bouton enlèvera la personne de la famille affichée.

#### Réorganiser les relations

![[_media/Reorder-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Réorganiser les relations]] Quand il existe plus d'un couple de parents ou plus d'un conjoint pour la personne active. Sélectionnez une des méthodes suivantes :

- Le menu
- Le bouton avec icône de la barre d'outils
- Ou l'icône à côté le texte
- Ou l'icône à côté le texte

pour afficher la fenêtre qui va vous permettre de modifier l'ordre :

- des parents dans la partie haute, , en utilisant les flèches haut-bas.
- des familles dans la partie du bas, , en utilisant les flèches haut-bas.

#### Enfants

Les enfants de la personne active.

{{-}}

#### Configuration

![[_media/Configure_RelView-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Configuration de la vue Relations]]

Vous pouvez contrôler le nombre d'information à afficher en utilisant le menu ou en cliquant sur le bouton ). Ce dialogue vous permet :

- Onglet
  - afficher ou de cacher les détails (dates de naissance et de décès) (tous sauf la personne active)

  - afficher ou de cacher les frères et sœurs

<!-- -->

- Onglet
  - utiliser ou non des nuances de couleurs permettant de mettre en avant les informations

  - afficher ou de cacher les boutons d'éditions à côté des individus

  - afficher les liens vers les individus sous forme de liens hypertexte.

### Barre inférieure de la catégorie Relations

La vue Relations n'affiche pas de Gramplet par défaut dans la [barre inférieure](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Fen%C3%AAtre_principale#Barres_inf.C3.A9rieure_et_lat.C3.A9rale). Vous pouvez l'ajouter si besoin.

### Barre latérale de la catégorie Relations

La vue Relations n'affiche pas de Gramplet par défaut dans la [barre latérale](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Fen%C3%AAtre_principale#Barres_inf.C3.A9rieure_et_lat.C3.A9rale). Vous pouvez l'ajouter si besoin.

{{-}}

## Familles

![[_media/Family_list-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vue Familles]]

La vue Familles affiche une liste de toutes les familles de la base de données. Depuis cette vue, vous pourrez ajouter, éditer, supprimer ou fusionner les familles. Par défaut, Gramps affiche id, père, mère, relations et date de mariage.

Vous pouvez faire un click droit sur une famille et, par le menu contextuel, sélectionner "Activer la mère" ou "Activer le père".

Voir aussi :

- [Voir la catégorie famille](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Navigation#Utilisation_de_la_cat.C3.A9gorie_Familles)
- [Édition des informations sur les relations](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Ajouter_des_individus,_dates,_familles_et_relations#.C3.89dition_de_l.27information_sur_les_relations)

{{-}}

### La barre inférieure de la catégorie familles

Elle affiche par défaut les onglets suivants qui sont autant de [Gramplets](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Gramplets) et qui peuvent donc être gérés comme tel avec le bouton flèche vers le bas :

- Galerie
- Evènements
- Enfants
- Citations
- Notes
- Attributs
- Références

### La barre latérale de la catégorie famille

Elle affiche par défaut le Gramplet suivant :

- Filtre

## Graphiques

La catégorie Graphiques affiche différentes représentations des ascendants ou des descendants de la personne active. Par défaut, c'est la vue Vue Arbre généalogique qui s'affiche. Les Vues en Roue ou arbre au fil du temps peuvent être sélectionnée dans la barre d'outils ou par le menu .

### Vue Arbre

![[_media/ChartsViewPedigreeView1-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vue Arbre]]

Le vue Arbre affiche jusqu'à 9 générations sous forme d'un graphique. Suivant la taille de le fenêtre, vous pouvez être amené à utiliser les barres de défilement pour voir les différentes partie du graphique.

Chaque individu est délimité par un rectangle avec son nom, ses informations de naissance (défini par un astérisque \*) et de décès (défini par un signe +), un ruban noir dans le coin supérieur gauche indique une personne décédée (ou supposé comme tel par Gramps), ainsi qu'une image si elle existe. Deux lignes partent de ce rectangle. Celle du haut se dirige vers le père et celle du bas vers la mère. Les lignes pleines représentent les liens de parenté biologiques par la naissance, les lignes en pointillé les autres liens de parenté, tels que adoption, beau-parents, tutelle, etc.

À la gauche de la personne active il y a un bouton en flèche , actif seulement si l'individu actif a des enfants. Cliquer sur le bouton va déployer une liste de ses enfants. Sélectionner un enfant le rendra actif pour le graphique.

![[_media/Pedigree_child_cut-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu enfants]].

Dans le menu, la typographie du nom des enfants est différente suivant qu'ils représentent une branche morte de l'arbre ou qu'ils ont une descendance. Les enfants qui n'ont pas d'enfants eux-mêmes (branche morte) vont apparaître en caractères normaux, alors que ceux qui sont parents seront en gras.

Si l'individu actif n'a qu'un seul enfant, aucun menu ne sera affiché (puisqu'il n'y a qu'un seul choix) et l'enfant sera la personne active si l'on clique sur la flèche.

Deux flèches vers la droite sont affichées dans la partie droite de la fenêtre. Celle du haut prend comme personne active le père de la personne active. Celle du bas met comme nouvelle personne active la mère de la personne active. Comme précédemment, tout l'affichage change alors en conséquence.

![[_media/Pedigree_siblings_cut-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Contexte personnel]]

Un clic-droit sur n'importe lequel des individus dans la vue arbre généalogique appelera le « menu contextuel ».

Parmi les autres élèment utiles, le menu contextuel a des sous-menus listant les , , , de l'individu.

Les sous-menu « grisés » indiquent l'absence de données dans la catégorie. Comme pour le menu des enfants vu plus haut, le menu des enfants et des parents fait la distinction entre les branches mortes et les branches avec descendants.

#### Configurer la vue active

![[_media/ChartsViewPedigreeViewConfigure-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vue Arbre - mise en page]]

L'onglet de la fenêtre du menu propose des options :

-  (coché par défaut)

-  (coché par défaut)

-  (coché par défaut)

-  (non coché par défaut)

- - **Standard**(par défaut)
  - Compact
  - Étendu

- - Vertical (↑)
  - Vertical (↓)
  - **Horizontal (→)**(par défaut)
  - Horizontal (←)

- curseur gradué de 2 à 9. Réglé à `5`(par défaut)

![[_media/ChartsViewPedigreeView3-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vue Arbre 3]] ![[_media/ChartsViewPedigreeView4-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vue Arbre 4]]

{{-}}

### Vue Roue des ascendants

![[_media/ChartsViewFanChart-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vue Roue des ascendants]]

Cette vue affiche les ascendants mais dans une roue ou en éventail. Cliquer dans la roue va doubler la section liée à l'ascendant. Un deuxième clic ramènera la roue à son état originel. Un clic sur le bouton droit appelle le menu contextuel, comme dans la vue Arbre, permettant de naviguer vers d'autres individus.

Cette vue permet d'obtenir une ascendance élargie de manière plus compacte et de voir très rapidement quelles parties d'une ascendance nécessitent des recherches supplémentaires.

Vous pouvez faire pivoter la vue en cliquant et en faisant glisser l'extérieur du graphique en éventail. Vous pouvez déplacer la vue en cliquant et en faisant glisser à l'intérieur de la partie intérieure (blanche).

1.  La vue peut être un cercle, un demi-cercle ou un quart de cercle. Les plus anciens sont toujours à la partie inférieure ou latérale de la vue.
2.  Les enfants de l'individu du centre (en blanc) sont symbolisés par le petit cercle coloré au centre
3.  Faites glisser et déposez les personnes au centre pour changer la personne active
4.  Options de couleur

:# Couleur des boîtes basées sur l'âge des personnes

:# Les couleurs des boîtes dépendent de la période de vie de l'individu

:# Palettes de couleurs définies: blanc, classique, basées sur le genre, et définies par l'utilisateur

1.  Filtrage : utilisez le filtre de la barre latérale pour obtenir rapidement des détails sur les individus affichés. Par exemple: combien de personnes ont des événements de naissance, qui a l'attribut « yeux bleus », etc. Les résultats filtrés sont en gras, ceux qui ne correspondent pas au filtre sont affichés de manière transparente.
2.  Affiche jusqu'à 11 générations.
3.  Imprimez la vue depuis la barre d'outils. La roue comme vous la voyez (après rotation, changement de couleur, changement de génération) peut être imprimée via le bouton «imprimer» ou bien sauvegardée au format svg (pour modification avec Inkscape, ou visualisation p.e. avec Firefox), pdf ou ps.
4.  La police utilisée peut être sélectionnée, et se redimensionne automatiquement à la taille des cases. Sur une couleur sombre, la couleur de police est blanche, sinon, noire.

Voir aussi [Gramplet graphique roue](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Gramplets#Roue)

{{-}}

#### Configurer la vue active

![[_media/Configuration_roue_Focal-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Configuration du graphique roue avec les réglages par défaut]]

Par le menu

- *9* (par défaut)

- *Sans* (par défaut)

- - Couleur du genre
  - **Gradient basé sur la génération** (par défaut)
  - Gradient basé sur l'âge (0-100)
  - Couleur unique de filtrage
  - Couleur basée sur une période temporelle
  - Blanc
  - Schéma de couleur classique pour le rapport
  - Schéma de couleur classique pour la vue

- *\#ef2929* (par défaut)

- *\#3d37e9* (par défaut)

- - **cercle complet** (par défaut)
  - Demi-cercle
  - Quadrant

- 

- 

- 

- 

{{-}}

### Roue des descendants

![[_media/ChartsCategory-DescendantFanChart-fullcircle-9gen-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vue cercle complet - arbre des descendants]]

C'est un graphique en roue montrant les descendants directs de l'individu actif.

{{-}}

#### Configurer la vue active

![[_media/Configuration_roue_descend_Focal-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Configuration graphique roue des descendants]]

Par le menu Divers paramètres disponibles comme à la section précédente.

{{-}}

### Roue 2 chemins

![[_media/ChartsCategory-2-WayFan-fullcircle-ances4gen-descen4gen-example-defaults-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vue 2 chemins - 4 génération d'ascendants (haut) / 4 générations descendants (bas)]]

Il s'agit d'un graphique en roue affichant à la fois les ascendants dans une moitié, d'un côté de la roue et les descendants dans l'autre moitié.

{{-}}

#### Configurer la vue active

Par le menu Divers paramètres disponibles comme dans les sections précédentes. {{-}}

### Barre inférieure de la catégorie Graphique

La vue Graphique n'affiche pas de Gramplet par défaut dans la [barre inférieure](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Fen%C3%AAtre_principale#Barres_inf.C3.A9rieure_et_lat.C3.A9rale). Vous pouvez l'ajouter si besoin.

### La barre latérale de la catégorie Graphique

Elle affiche par défaut le Gramplet suivant :

- Filtre

Seules les vues et ont un filtre affiché par défaut

### Voir aussi :

- Plusieurs greffons permettent de disposer de graphiques supplémentaires. Voir pour les activer. Notamment [Fr:Vue_Graphique](wiki:Fr:Vue_Graphique) qui permet d'avoir un affichage graphique de l'arbre, interactif et moderne. Voir aussi [Fr:Interactive_Family_Tree](wiki:Fr:Interactive_Family_Tree) permettant un autre affichage interactif de votre arbre dans votre navigateur Internet.

## Événements

Les événements peuvent être partagés entre plusieurs individus et familles. La vue des événéments liste tous les événéments enregistrés dans l'arbre familial.

Les colonnes disponibles dans la vue sont : , , , , , et de l'événement.

![[_media/Events-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vue Événements]]

Par défaut la vue affiche les colonnes , , , et de l'événement. Le dialogue de l' peut être utilisé pour ajouter, enlever et réarranger les colonnes affichées. Cette fonction est accessible depuis le bouton dans la barre d'outils.

La liste des événements peut être triée de plusieurs façons, en cliquant sur l'en-tête de la colonne. Cliquer une fois va trier dans le sens croissant, re-cliquer va trier dans le sens décroissant.

{{-}}

### La barre inférieure de la catégorie Évènements

Elle propose les onglets suivants :

- Galerie
- Citations
- Notes
- Attributs
- Références

### La barre latérale propose

Elle propose :

- Filtre

## Lieux

![[_media/Place_ListView-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vue liste des lieux]]

Les vues des lieux listent les emplacements géographiques où ont lieu les événements. Cela peut être les lieux de naissance, décès, mariage des individus ainsi que leur adresse, travail ou toute autre référence géographique. La vue des lieux affiche les , , , , , , , et la date a laquelle il a été . Toutes ces colonnes peuvent être triées en cliquant sur leur en-tête.

Voir aussi [Saisie des lieux dans Gramps](wiki:Lieux_dans_Gramps) {{-}}

### Vue hiérarchisée ou liste

![[_media/PlacesCategory_PlaceTreeView-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vue hiérarchisée des lieux]]

Les deux vues de cette catégorie montrent les lieux groupés ou non. Le choix se fait dans le menu ou par les boutons de la barre d'outils. La vue en arbre tente de grouper les lieux selon une hiérarchie logique : pays, région ou province, etc

Un click droit permet de déployer un nœud ou tous les nœuds.

Cette vue est apparue dans la version 6.0.0. Dans les futures versions l'objectif est de rendre le groupage encore plus intelligent.

L'autre vue ne fait que afficher tous les lieux dans une longue liste.

{{-}}

### Configurer la vue active

Vous pouvez contrôler la disposition de la liste des lieux (quelles colonnes seront affichées et l'ordre d'affichage) en cliquant sur le bouton ![[_media/Gramps-config.png]]  ou par le menu ou par le [raccourci clavier](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Raccourcis_clavier#Raccourcis) "Configurer la vue active".

{{-}} ![[_media/Configuration_Lieux_Focal-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Configuration des colonnes]]La fenêtre de configuration des lieux est utilisée pour ajouter, enlever et réorganiser les colonnes affichées. Les changements seront effectifs seulement quand le bouton est cliqué.

Une fois la vue en colonnes affichée, cliquer sur une en-tête de colonne classe les enregistrements dans l'ordre croissant pour cette colonne ; cliquer à nouveau classe en ordre décroissant.

Ces options de configuration et les filtres en cours s'appliqueront aussi aux données exportées par le menu

{{-}}

### Service cartographique

![[_media/Map_service_Focal.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Lieux - Bouton &quot;Tentative pour localiser les évènements sélectionnés avec un service cartographique (OpenstreetMap, Google Maps, ...&quot;]] Si un lieu est activé, vous pouvez sélectionner dans la barre d'outils, le bouton . A droite du bouton, la flèche ouvre une liste permettant de choisir le service entre OpenstreetMap, Google Maps, Google earth). Le service s'ouvre dans votre navigateur Internet et va utiliser le nom ou la longitude et la latitude du lieu pour afficher l'emplacement via le site internet choisi. Pour Google Earth, la fonction peut vous proposer de sauver les coordonnés pour les ouvrir secondairement avec Google Earth.

Voir aussi :

- [Map Services - Google Earth](wiki:Addon:MapService-GoogleEarth) - greffon pour utiliser Google Earth.

{{-}}

### La barre inférieure de la catégorie Lieux

Elle propose les onglets suivants :

- Détails
- Parti de
- Inclus
- Galerie
- Citations
- Notes
- Références

### La barre latérale propose

Elle propose :

- Filtre

## Géographie

Cette catégorie est une représentation de vos données d'évènements sur une carte. Elle contient plusieurs vues Géographie qui permettent de voir tous les individus et leurs événements localisés sur une carte via un fournisseur de carte sur Internet (OpenStreetMap, Google maps ... ).

![[_media/Geographie_tslieux_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} vue Géographie]]

La vue Géographie peut afficher :

- Tous les lieux liés à l'individu actif
- Tous les lieux liés à la famille active
- Tous les lieux liés à une sélection d'événements par un filtre
- Tous les lieux liés aux événements
- Tous les lieux connus dans votre arbre
- Montre si deux individus ont pu se rencontrer
- Montre si deux familles ont pu se rencontrer
- Montre tous les déplacements ou résidences pour un individu et ses descendants.

Ces options sont accessibles via les boutons de la barre d'outils. Pour filtrer les lieux ou événements, activez la barre latérale de filtrage ()

Pour que cette vue fonctionne correctement :

- les évènements doivent être associés à des lieux.
- Ces lieux doivent posséder des coordonnées : latitude et longitude.
- Si un lieu n'a pas de coordonnées associées, vous ne le visualiserez jamais sur la carte.
- Si internet est actif, pour tous les déplacements sur la carte et à toutes les niveaux de zoom, toutes les tuiles de la carte sont sauvées.
  - Si Internet n'est plus disponible, toutes les tuiles déjà sauvées dans une session précédente seront ré-utilisées.
  - La carte peut donc être utilisée sans Internet et tous les sites visités seront toujours disponibles aux différent niveaux de zoom déjà utilisés.
  - La seule chose à faire, pour chaque lieu ou zone que vous souhaitez utiliser sans Internet, les sélectionner, changer le zoom de la carte. Vous pourrez alors les utiliser à nouveau sans connexion.

#### Les différentes vues

<table>
<thead>
<tr>
<th colspan="3" style="text-align: left;"><h5 id="tous_les_lieux_connus_pour_un_individu">Tous les lieux connus pour un individu</h5></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;" data-valign="top">![[_media/gramps-person-11.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} L'individu]]</td>
<td style="text-align: left;" data-valign="top"><p>Cette vue montre toutes les lieux visités par un individu durant sa vie.</p>
<p>Cette vue n'est pas connectée aux filtres. Elle ne dépend donc que de l'individu actif et de l'historique.</p>
<p>Si vous souhaitez utiliser la fonctionalité "Animation", cliquez sur le bouton droit de la souris. Vous obtiendrez un menu. Dans ce menu, vous pouvez sélectionner "Animation" pour visualiser les différents déplacements de l'individu actif.</p>
<p>Si l'individu actif a plusieurs évènements, vous pourrez visualiser les déplacements entre ces différents lieux. Le déplacement est relatif aux dates ou à la distance et peux être adapté dans les préférences de la carte. Si la distance entre deux lieux est supérieure à la valeur en dixièmes de degré, le déplacement sera calculé en fonction de la distance à la place des dates. Dans ce cas, le nombre de pas entre les deux lieux peuvent être modifiés. Vous pouvez modifier la vitesse d'animation entre deux pas. Les déplacement démarrent à la date du premier évènement pour se terminer à la date du dernier évènement.</p>
<p>Dans le menu de configuration, vous pouvez modifier :</p>
<ol>
<li>La vitesse d'animation en millisecondes.</li>
<li>Combien de pas seront nécessaire entre deux marqueurs pour les grandes distances.</li>
<li>La valeur minimum (latitude/longitude) pour sélectionner une grande distance. Cette valeur est exprimée en dixième de degré.</li>
</ol></td>
<td style="text-align: left;" data-valign="top">![[_media/Gramps_configuration_2-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} L'animation]]</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;"><h6 id="tous_les_lieux_connus_pour_un_individu_avec_informations_géographiques_fichiers_kml">Tous les lieux connus pour un individu avec informations géographiques (fichiers kml)</h6></td>
</tr>
<tr>
<td style="text-align: left;" data-valign="top">![[_media/gramps-person-kml.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Une personne avec 3 fichiers kml]]</td>
<td style="text-align: left;" data-valign="top"><p>Si vous avez ajouté des fichiers de type kml dans l'onglet galerie d'un événement, cette vue vous montrera un chemin ou une surface pour chaque fichier kml.</p>
<p>Dans l'exemple suivant, vous voyez 3 fichiers kml :</p>
<ol>
<li>La ferme du lieu de naissance de cette personne.</li>
<li>Le chemin pour aller à l'école (évènement scolaire).</li>
<li>Les limites de la paroisse ou commune (évènement baptême).</li>
</ol></td>
<td style="text-align: left;" data-valign="top"></td>
</tr>
<tr>
<td colspan="3" style="text-align: left;"><h5 id="tous_les_lieux_connus_pour_une_famille">Tous les lieux connus pour une famille</h5></td>
</tr>
<tr>
<td style="text-align: left;" data-valign="top">![[_media/gramps-family-10.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} La famille]]</td>
<td style="text-align: left;" data-valign="top"><p>Cette vue permet de visualiser toutes les lieux visités par tous les membres d'une famille pendant leur vie.</p>
<p>Cette vue n'est pas connectée aux filtres. Elle ne dépend donc que de la famille active et de l'historique.</p>
<p>Il n'y a pas d'options complémentaires dans le menu de configuration.</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="3" style="text-align: left;"><h5 id="se_sont_ils_rencontrés">Se sont-ils rencontrés ?</h5></td>
</tr>
<tr>
<td style="text-align: left;" data-valign="top">![[_media/gramps-person-meeting-9.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Se sont-ils rencontrés?]]</td>
<td style="text-align: left;" data-valign="top"><p>Cette vue est utilisée pour montrer si deux individus ont pu se rencontrer durant leur vie.</p>
<p>Vous devez sélectionner un individu de référence :</p>
<ol>
<li>À partir du menu popup (bouton droit de la souris) : Choisir l'individu de référence</li>
<li>À partir de la barre d'outils</li>
</ol>
<p>Quand l'individu de référence est choisie, vous verrez tous les lieux qui lui sont associés. Pour chaque lieu connu avec des coordonnées, un « cercle » ou un « ovale » sera affiché en fonction de la longitude.</p>
<p>Le rayon du cercle peut être réglé dans la configuration de la géographie. Cette valeur est exprimée en dixième de degré.</p></td>
<td style="text-align: left;" data-valign="top">![[_media/Gramps_configuration_3-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} La sélection]]</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;"><h5 id="ces_deux_familles_se_sont_elles_rencontrées">Ces deux familles se sont-elles rencontrées ?</h5></td>
</tr>
<tr>
<td style="text-align: left;" data-valign="top">![[_media/gramps-family-meeting-8.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ces deux familles se sont-elles rencontrées?]]</td>
<td style="text-align: left;" data-valign="top"><p>Cette vue est utilisée pour montrer si deux familles ont pu se rencontrer durant leur vie.</p>
<p>Vous devez sélectionner une famille de référence :</p>
<ol>
<li>À partir du menu popup (bouton droit de la souris) : Choisir la famille de référence</li>
<li>À partir de la barre d'outils</li>
</ol>
<p>Quand la famille de référence est choisie, vous verrez tous les déplacements associés à ses membres . Pour chaque lieu connu avec coordonnées, vous verrez un « cercle » ou un « ovale » en fonction de la longitude.</p>
<p>Le rayon du cercle peut être réglé dans la configuration de la géographie. Cette valeur est exprimée en dixième de degré.</p></td>
<td style="text-align: left;" data-valign="top">![[_media/Gramps_configuration_3-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} La sélection]]</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;"><h5 id="toutes_les_résidences_ou_déplacements_dun_individu_et_ses_descendants">Toutes les résidences ou déplacements d'un individu et ses descendants</h5></td>
</tr>
<tr>
<td style="text-align: left;" data-valign="top">![[_media/gramps-geomoves-5.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Toutes les résidences ou déplacements d'un individu et ses descendants]]</td>
<td style="text-align: left;" data-valign="top"><p>Cette vue est utilisée pour montrer les déplacements ou résidences d'un individu et de tous ses descendants.</p>
<p>Une visualisation est réalisée par génération. Il est possible de modifier le temps entre deux visualisations de génération dans la configuration de la géographie.</p>
<p>Cette vue n'est pas connectée aux filtres. Elle ne dépend donc que de l'individu actif et de l'historique.</p>
<p>Dans le menu de configuration, vous pouvez :</p>
<ol>
<li>Changer le nombre de génération à montrer</li>
<li>Changer le temps en millisecondes entre deux affichages de générations.</li>
</ol></td>
<td style="text-align: left;" data-valign="top">![[_media/Gramps_configuration_4-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Paramètres de déplacements]]</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;"><h5 id="tous_les_lieux_liées_aux_évènements">Tous les lieux liées aux évènements</h5></td>
</tr>
<tr>
<td style="text-align: left;" data-valign="top">![[_media/gramps-events-7.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Évènements]]</td>
<td style="text-align: left;" data-valign="top"><p>Cette vue est utilisée pour montrer toutes les lieux liés aux évènements. L'affichage peut être long lorsqu'il y a beaucoup d'évènements.</p>
<p>Il n'y a pas d'options complémentaires dans le menu de configuration.</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="3" style="text-align: left;"><h5 id="tous_les_lieux_avec_coordonnées">Tous les lieux avec coordonnées</h5></td>
</tr>
<tr>
<td style="text-align: left;" data-valign="top">![[_media/GeographyCategory-GeoPlaces-view-AllKnownPlaces-openstreemap-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Lieux]]</td>
<td style="text-align: left;" data-valign="top"><p>Cette vue montre toutes les lieux connus de la base de données. Ces lieux doivent posséder des coordonnées.</p>
<p>Il n'y a pas d'options complémentaires dans le menu de configuration.</p>
<p>Par contre, il peut être nécessaire par un click droit sur la carte de sélectionner « Afficher tous les lieux » pour affectivement les voir.</p></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

### Utilisation

#### La configuration

Via le bouton de la barre d'outils (ou via le menu )

La fenêtre de configuration possède deux onglets :

- Onglet La carte pour toutes les vues

![[_media/Gramps_configuration_1-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} La carte]]

1.  Dans quel répertoire sauvegarder les tuiles de la carte (défaut est *\$HOME/.gramps/maps*). ATTENTION, cela peux prendre plusieurs gigaoctets sur le disque dur.
2.  Le niveau de zoom par défaut lorsqu'on centre la carte ou lorsqu'on sélectionne un marqueur. À chaque fois que la vue graphique redessinera la carte, ce niveau de zoom sera utilisé.
3.  Utiliser le clavier numérique pour les raccourcis. Soit on choisit le + et le - sur le clavier numérique (défaut), soit sur le clavier alpha.

- Onglet spécifique pour la vue en cours

Voir la description de la vue.

#### Comment zoomer et déplacer la carte ?

##### Zoomer et dézoomer la carte

Pour cela, on utilisera :

1.  Les boutons +/- en haut et à gauche de la carte
2.  La molette de la souris.
3.  Les touches + et - du clavier numérique (défaut).

On peut remplacer le clavier numérique par le clavier alphanumérique dans la configuration de la géographie.

##### Déplacer la carte

Pour déplacer la carte, il suffit de :

1.  Cliquer et de déplacer la souris.
2.  Utiliser les flèches.

#### L'action de la souris sur la carte

Le bouton droit ci-dessous correspond à une personne droitière. Ce sera le bouton de gauche pour une personne gauchère.

##### bouton 1 (gauche)

Vous avez deux usages pour le bouton 1 :

1.  La sélection d'un marqueur.
2.  Valider une sélection de région.

##### bouton 2 (milieu)

Le seul usage de ce bouton est de sélectionner une zone sur la carte.

1.  Lorsque enfoncé : démarrer la sélection de la zone ou région.
2.  Lorsque relaché, fin de la sélection.

Vous devez alors cliquer sur le bouton 1 pour terminer la sélection.

##### bouton 3 (droit)

Le seul usage de ce bouton :

1.  Montrer le menu popup.

##### La souris survole un marqueur

Lorsque la souris survole un marqueur, le nom du lieu ou des lieux est affiché dans la barre d'état.

#### Le menu popup

De ce menu, vous avez les fonctions suivantes pour les vues :

1.  Cacher ou montrer la cible (le viseur).
2.  Verrouiller ou déverrouiller le zoom.
3.  Changer la carte par défaut (fournisseur).
4.  Ajouter un lieu ou lier un lieu existant dans la base de donnée à la position de la souris.
5.  Ajouter un lieu à partir d'un fichier kml.
6.  Centrer la carte à la position de la souris.
7.  Effacer toutes les tuiles déjà mémorisées pour ce fournisseur d'accès.

#### Cliquer sur un marqueur

Nous avons deux cas :

1.  évènements : pour chaque évènement, nous pouvons éditer cet évènement ou centrer la carte sur le lieu associé.
2.  lieux : pour chaque lieu, nous pouvons éditer ce lieu ou centrer la carte sur ce lieu.

Quand on centre la carte, le zoom utilisé est celui défini dans les préférences de la vue géographie.

Nous pouvons avoir plusieurs marqueurs dans la zone cliquée en fonction du zoom. Dans ce cas, pour un emplacement sélectionné, tous les évènements ou lieux relatifs à ce marqueur seront affichés. On peut dans ce cas avoir un mixage des deux cas décrit ci-dessus.

#### Ajouter ou Lier à un lieu

Pour cela, cliquer sur le bouton de la souris, vous aurez le menu popup. Dans ce menu, vous pouvez sélectionner "Ajouter un lieu" ou "Lier à un lieu"

Quand vous ajoutez ou essayez de lier un lieu à la position de la souris, vous obtenez une fenêtre de sélection de région. Vous verrez sur la carte un cercle ou ovale dans lequel vous pourrez choisir les noms de lieu des marqueurs. Vous pourrez ajuster le rayon de ce cercle avec le curseur situé dans cette fenêtre de sélection. En fonction du diamètre de ce cercle, une liste est crée. Si le lieu choisi contient des champs déjà entrés, ces valeurs seront affichées dans une rangée de la liste de couleur verte. Si vous acceptez ces valeurs double cliquez sur cette rangée. Si vous ne souhaitez pas réutiliser ces valeurs, choisissez une autre rangée qui contient ce qui vous semble plus réaliste.

Une autre méthode pour ajouter une latitude et une longitude :

- Téléchargez le [Arrangement des lieux](wiki:Place_completion_tool) via le menu . Si vous téléchargez les données associées à votre pays, cet outil pourra ajouter la latitude-longitude à tous vos lieux.

#### Ajouter un lieu à partir d'un fichier kml

Pour cela, cliquer sur le bouton de la souris, vous aurez le menu popup. Dans ce menu, vous pouvez sélectionner "Ajouter un lieu depuis un fichier kml"

Vous obtenez une fenêtre de sélection de fichier. Sélectionner le fichier que vous souhaitez ajouter. Si vous avez plusieurs lieux dans le même fichier kml, une fenêtre d'édition de lieu sera ouverte pour chaque lieu. Faites attention.

#### Comment changer de fournisseur de carte ?

Nous avons plusieurs fournisseurs de carte disponible. Cliquez sur le bouton droit de la souris, vous obtenez un menu popup. En bas de ce menu, choisissez "Remplacer <fournisseur actuel> par =\>"

Les fournisseurs suivant sont disponible :

1.  OpenStreetMap (défaut) : l'avantage de [OpenStreetMap](http://www.openstreetmap.org/) est que c'est un projet libre. Vous pouvez donc mettre à jour la carte avec les informations manquantes sur leur site web.
2.  Maps For Free
3.  OpenCycleMap
4.  Public Transport
5.  Google street
6.  Google sat
7.  Google hybrid
8.  Virtualearth street
9.  Virtualearth sat
10. Virtualearth hybrid

#### Pouvons-nous changer la couleur des marqueurs ?

Oui, mais seulement dans la vue « Tous les lieux connus » ! Pour changer les couleurs, ouvrir la fenêtre de configuration comme d'habitude.

Pour les autres, les couleurs sont fixées en dur dans Gramps. La couleur verte est associée aux fournisseurs suivants : openstreetmap, Maps for free, Opencyclemap and Public transport. Tous les autres fournisseurs sont de couleur rouge.

#### Comment ajouter/enlever la cible ?

Elle est aussi appelée mire ou viseur. Il est souvent pratique de savoir ou la carte est centrée. Cette fonctionalité est disponible à partir du bouton 3 de la souris. Dans le menu popup obtenu, choisissez "Retirer/Ajouter la cible" Cela peut être utile pour ajouter ou lier un lieu aux bonnes coordonnées géographiques.

#### Comment verrouiller/Déverrouiller la carte ?

Lorsqu'on change de carte, de vue, le zoom est recalculé. Il peut être utile dans certains cas de garder le même zoom et la même position. Pour cela, cliquez sur le bouton 3 de la souris Dans le menu popup, sélectionnez « Déverrouillez/verrouillez le zoom et la position »

### Prérequis pour obtenir la vue Géographie

Pour gramps 4.x, vous devez installer osmgpsmap version 1.0 et au dessus et le paquet gir associé.

`Par exemple, sur *Ubuntu, vous devez installer : gir1.2-osmgpsmap-1.0 et libosmgpsmap-1.0-0`

### Problèmes possible

1.  Pas de vue : Avez-vous installé osmgpsmap ? (*gramps -v* peut vous aider)
2.  Pas de tuiles : Avez-vous une connexion internet active ?
3.  Pas de tuiles pour un fournisseur : Si les autres fournisseurs s'affichent correctement, soumettez un rapport de bogue.
4.  Tuiles manquantes : Vous n'avez pas Internet et c'est la première fois que vous voulez afficher ce lieu.
5.  Tuiles manquantes : Ce peut être la même chose que pas de tuiles pour un fournisseur s'ils modifient les règles d'accès aux tuiles (par exemple : user-agent)
6.  Autres cas : soumettez un rapport de bogue.

## Sources

La catégorie Sources liste les sources stockées dans la base de données.

Deux types de vues existent dans cette catégorie :

- La vue par défaut (hiérarchisée avec citations) : à gauche de chaque Source il y a une flèche ou un autre indicateur du type +. Cliquez sur l'indicateur pour déployer l'ensemble des Citations partageant la même Source. Cliquez une nouvelle fois sur l'indicateur compactera la liste et n'affichera que la Source.

<!-- -->

- La vue alternative : les sources sont présentées sous forme d'une liste.

![[_media/Sources_citationtreeview-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vue hiérarchisée avec citations]] ![[_media/Sources-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} vue Sources]] {{-}}

Ceci peut inclure différents documents (naissance, décès, actes de mariage, etc.), livres, films, journaux - tout ce qui peut vous aider dans vos recherches. Gramps vous offre une option pour définir une source pour chaque événement (naissances, décès, mariages, etc.). La vue des sources utilise un , , et un pour cette source, ainsi que toute information de pouvant y être associée.

La liste des sources peut être triée en cliquant sur l'en-tête de la colonne.

Cliquer une fois va trier dans le sens croissant, re-cliquer va trier dans le sens décroissant. Le dialogue peut être utilisé pour enlever ou changer l'affichage des colonnes.

Voir aussi [Modifier les informations sur les Sources](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Fonctionnement_des_%C3%A9v%C3%A9nements,_sources,_lieux,_d%C3%A9p%C3%B4ts_et_notes#.C3.89dition_de_l.27information_sur_les_sources)

### La barre inférieure de la catégorie Source

Elle propose les onglets suivants :

- Galerie
- Notes
- Références

### La barre latérale de la catégorie Source

Elle propose :

- Filtre

{{-}}

## Citations

![[_media/Citations_citationlistview-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vue Citations]]

La catégorie Citations liste les citations des informations stockées dans la base de données.

Les citations spécifient quelles parties d'une Source sont applicables pour un événement donné. Par exemple, une Source peut être un livre, et la Citation peut être une page de ce livre. Gramps offre la possibilité d'associer une Citation différente pour chaque Événement (naissances, décès, mariages, etc.). La vue Citations liste le , l' , et la de la citation, ainsi que le .

La liste de Citations peut être triée en cliquant sur l'en-tête de la colonne.

Cliquer une fois va trier dans le sens croissant, re-cliquer va trier dans le sens décroissant. Le dialogue Éditeur de colonnes peut être utilisé pour enlever ou changer l'affichage des colonnes.

### La barre inférieure de la catégorie Citations

Elle propose les onglets suivants :

- Galerie
- Notes
- Références

### La barre latérale de la catégorie Citations

Elle propose :

- Filtre

{{-}}

## Dépôts

![[_media/Repository-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vue Dépôts]]

Un dépôt peut être défini comme une collection de sources.

Chaque source dans la base de données peut référencer un dépôt (comme une bibliothèque) dans lequel elle est présente. Le fonctionnement de la vue dépôts est similaire à celui des autres vues.

### La barre inférieure de la catégorie Dépôts

Elle propose les onglets suivants :

- Détails
- Notes
- Références

### La barre latérale de la catégorie Dépôts

Elle propose :

- Filtre

{{-}}

## Media

![[_media/Media-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vue Media]]

La vue des media liste les objets media utilisés dans la base de données.

Les objets media sont n'importe quel fichier relié aux données généalogiques.

La plupart du temps, ce sont des images, des fichiers sons, des animations, etc.

Les en-têtes de colonnes sont , , , et de l'objet media.

La boite de dialogue , menu , peut être utilisé pour réarranger l'affichage des colonnes, lesquelles obéissent aux règles de tri.

### La barre inférieure de la catégorie Media

Elle propose les onglets suivants :

- Aperçu : dans cet onglet, vous pouvez double-cliquer sur le media/la photo pour l'ouvrir dans la visionneuse par défaut.
- Citations
- Notes
- Attributs
- Métadonnées Image
- Références

### La barre latérale de la catégorie Media

Elle propose :

- Filtre

{{-}}

## Notes

![[_media/Notesview-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vue Notes]]

Une note est un texte brut ou formaté qui est stockée comme les autres objets.

Le fonctionnement des notes est similaire aux autres vues. La vue liste toutes les stockées dans un .

Sous vous pouvez changer l'affichage des colonnes. Les possibilités sont , , , , et .

Le de note choisi à la création (ou en modification) peut être : *Note sur l'événement*, *À faire*, *Citation*, *Code HTML*, *Général*, *Inconnu*, *Lien*, *Rapport*, *Recherche*, *Texte source*, *Transcription*.

Cliquer deux fois sur la note dans la liste va ouvrir une fenêtre dans laquelle vous pourrez éditer cette dernière. Vous pouvez changer les polices de caractères, leurs couleurs, ainsi que la couleur de fond. Un vérificateur d'orthographe est disponible en *anglais* et dans votre langue de système (si GTKSpell est installé).

Voir aussi [Modifier les informations d'une note](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Fonctionnement_des_%C3%A9v%C3%A9nements,_sources,_lieux,_d%C3%A9p%C3%B4ts_et_notes#.C3.89dition_de_l.27information_sur_les_notes)

### La barre inférieure de la catégorie Notes

Elle propose les onglets suivants :

- Références

### La barre latérale de la catégorie Notes

Elle propose :

- Filtre

{{-}}

[Category:Fr:Documentation](wiki:Category:Fr:Documentation)
