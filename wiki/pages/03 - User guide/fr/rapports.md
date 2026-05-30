---
title: Fr:Manuel wiki pour Gramps 6.0 - Rapports
categories:
- Fr:Documentation
managed: false
source: wiki-scrape
wiki_revid: 124876
wiki_fetched_at: '2026-05-30T18:42:45Z'
lang: fr
---

{{#vardefine:chapter\|11}} {{#vardefine:figure\|0}} Ces sections décrivent les différents rapports disponibles dans Gramps.

## Introduction

Voir [Produire des rapports‎](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_1/fr) pour quelques remarques générales.

## Rapports

![[_media/Outil_rapport_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Icône barre d&#39;outils «Ouvrir le dialogue des rapports»]] Les rapports sont accessibles par le menu **Rapports-\>Type de rapport-\>rapport particulier**.

Alternativement, vous pouvez passer en revue le choix complet des rapports disponibles dans un dialogue que l'on obtient en cliquant sur l'icône de la barre d'outils. {{-}}

### Boite de dialogue Sélection d'un rapport

![[_media/Dialogue_selectionrapport_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogue Sélection d&#39;un rapport]] La boite de dialogue vous permet de naviguer parmi tous les rapports disponibles avec une brève description. Ouvrez la liste en cliquant sur la flèche devant les catégories. {{-}}

## Valeurs de substitution

Voir les [valeurs de substitution](wiki:Gramps_6.0_Wiki_Manual_-_Valeurs_de_substitution).

## Options communes

- id: l'individu central pour le filtre (ex: *Smith, Edwin Michael*)
- filtre: Détermine les individus à inclure dans le rapport

1.  Toute la base de données
2.  Descendants de Smith, Edwin Michael
3.  Familles descendantes de Smith, Edwin Michael
4.  Ascendants de Smith, Edwin Michael
5.  Individus ayant un ancêtre commun avec Smith, Edwin Michael
6.  Et les filtres personnels que vous pourrez élaborer par l' du menu . Ils vous permettent définir précisément les individus devant apparaître dans le rapport. Voir [Les Filtres](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Les_filtres).

## Livres

Il n'y a actuellement qu'un seul rapport dans cette catégorie : le Gestionnaire de livre.

Le gestionnaire de livre produit un document unique (un livre) contenant un ensemble de rapports graphiques et textuels. En conséquence, ceci autorise un ensemble d'association de documents généré par Gramps.

Quand est sélectionné, le dialogue de est affiché. {{-}}

### Dialogue Gestion des Livres

![[_media/Bookreport-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport Livre]] La boite de dialogue comprend trois parties : , et

#### Nom du livre

La zone de saisie affiche le nom du livre actuel. Vous pouvez le modifier et enregistrer ce livre (et l'ensemble des paramètres de ses composants) pour une utilisation ultérieure. Si vous chargez un livre déjà enregistré (voir plus bas), vous verrez ce nom de livre que vous pourrez changer si vous voulez le configurer différemment.

##### La barre d'outils du nom du livre

Les boutons alignés à droite de la zone agissent sur l'ensemble du livre :

- Le bouton supprime tous les de la section .
- Le bouton enregistre le livre sous le nom donné dans le champ pour être utilisé plus tard. Si le nom du livre existe déjà, il vous sera demandé si vous voulez pour le remplacer ; vous pouvez aussi annuler et donner un autre nom. .

{{-}} ![[_media/Dialogue_livresdispo_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Livres disponibles]]

- Le bouton ouvre une fenêtre qui affiche tous les livres déjà enregistrés. Dans cette fenêtre, double-cliquez sur le nom d'un livre ou sélectionnez-le puis cliquer le bouton pour le charger.

{{-}} ![[_media/Dialogue_gestionlivres_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gestions des Livres]]

- Le bouton ouvre une fenêtre légèrement différente qui affiche la liste des livres disponibles que vous pouvez supprimer par le bouton après les avoir sélectionnés.

{{-}}

#### Articles disponibles

La partie moyenne de la boite de dialogue liste les pour être inclus dans le livre.

##### Sélection des articles disponibles

Presque tous les articles disponibles pour l'inclusion dans le livre sont des rapports textuels ou graphiques, et sont donc disponibles sous forme de rapports autonomes (voir le sommaire de cette page). L'exception reste les articles qui sont seulement disponibles comme articles de livre et qui vont être traités dans cette section. Pour chacun, sera explicitée la fenêtre de configuration.

Pour les ajouter dans le livre actuel, double-cliquez sur un article ou sélectionnez-le et cliquez sur le bouton + de la barre d'outils latérale de la section inférieure de la fenêtre.

Pour accéder au dialogue de configuration, il faut d'abord les ajouter au puis les sélectionner dans cette liste avec de cliquer sur le bouton , ou double-cliquer sur leur nom dans la liste du livre. {{-}}

###### Index alphabétique

![[_media/Article_indexalpha_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Index alphabétique - Configuration]] Cet item crée une(des) page(s) avec un index alphabétique des individus notés dans des certains rapports textuels.

Dans l'onglet *Options du rapport* vous pouvez choisir la langue de traduction dans une liste déroulante. {{-}}

###### Texte personnalisé

![[_media/Article_texteperso_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Texte personnalisé - Configuration]] Cet item crée une page avec trois paragraphes, chacun contenant un texte personnalisé :

- Texte initial :
- Texte du milieu :
- Texte final :

Les champs sont extensibles si bien que vous pouvez mettre tout le texte que vous voulez.

La partie inférieure de la fenêtre affiche les **Options du document** : choisissez le style par défaut ou cliquer sur le bouton . Il va ouvrir une fenêtre où vous pouvez ajouter ou supprimer des styles. Pour plus de détails, voir [Éditeur de style](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Éditeur_de_style). Cet item était supposé être utilisé pour les épigraphes, dédicaces, informations, notes et autres. {{-}}

###### Table des matières

![[_media/Article_tablematieres_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Table des matières - Configuration]] La table des matières est générée pour un livre comme une liste des parties de ce livre ou d'un document, organisée dans l'ordre dans lequel ils apparaissent.

Dans l'onglet des *Options du rapport* vous pouvez choisir la langue de dans la liste déroulante.

{{-}}

###### Page de garde

![[_media/Article_pagegarde_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Page de garde - Configuration]] Cet item crée une page de garde dont vous pouvez modifier les options.

L'onglet des est composé de trois champs de saisie de texte où vous pouvez modifier le **Titre**, le **Sous-titre** et le **Pied de page** (à titre d'exemple, des textes sont proposés).

Une peut être placée entre le sous-titre et le pied de page en cliquant le bouton qui ouvre un dialogue permettant de sélectionner une image existant parmi les media.

Vous pouvez aussi changer la plutôt que la taille par défaut.

La partie inférieure de la fenêtre affiche les **Options du document** où vous pouvez choisir le **Style** par défaut ou cliquer sur le bouton . Il va ouvrir une fenêtre où vous pouvez ajouter ou supprimer des styles. Pour plus de détails, voir [Éditeur de style](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Éditeur_de_style).

Les capacités de configuration de ce composant lui permettent d'être utilisé comme titre pour le livre, ses chapitres ou même un simple composant. {{-}}

#### Livre actuel

C'est la partie inférieure de la fenêtre. La barre d'outils avec les boutons alignés verticalement à droite de la section agit sur le composant sélectionné avec les fonctions suivantes :

- Le bouton ajoute le composant sélectionné dans la section à la section en dessous. Un double-clic sur un article de la liste du haut a le même résultat.
- Le bouton retire le composant sélectionné dans la liste de la section .
- Les boutons et déplacent le composant sélectionné dans le , en l'avançant ou le reculant d'un composant.
- Le bouton sert à définir les options de l'article sélectionné dans le -- à condition de l'avoir sélectionné d'abord. Un double-clic sur un article de cette liste ouvre aussi le dialogue de configuration. Cette boite de dialogue est spécifique à l'article à configurer. Si vous ne le configurez pas, des options par défaut nécessaires seront appliquées. L'option commune à presque tous les articles est la personne centrale : l'individu sur lequel l'article est centré. Grâce à cette option, vous pouvez créer un livre avec des articles centrés sur des personnes différentes (ex : les ancêtres de votre mère et ceux de votre père comme des chapitres différents. Par défaut, la personne centrale est définie comme la .

{{-}}

### Dialogue Générer le livre

![[_media/Rapport_genererlivre_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogue - Générer le livre]] Si toutes les sélections sont faites, cliquez sur le bouton pour créer votre livre personnalisé. La fenêtre s'ouvrira. Il y a deux sections :

- Les permettant de changer la taille, l'orientation et les marges de la page. Un choix cliquable permet de choisir les valeurs métriques.
- Les pour modifier :
  - Le format de sortie : un menu déroulant vous permettant de choisir entre : **OpenDocument Texte**, **PDF**, **PostScript** ou **Imprimer…**.
  - Une case à cocher existe pour ouvrir le document dans votre visualiseur par défaut comme LibreOffice Writer.
  - Le nom du fichier : la valeur par défaut est */votre répertoire/<Nom de votre arbre>\_book.pdf* que vous pouvez modifier. L'extension change en fonction du format de sortie choisi.

Cliquez sur le bouton pour enregistrer le livre.

#### Voir aussi

- [Add a table contents or an index to a Book of Reports](wiki:Add_Table_of_Contents_or_Index_to_reports)

{{-}}

## <span id="Graphical Reports"></span>Rapports graphiques

Les rapports graphiques représentent l'information sous la forme de diagrammes et de graphiques. La plupart des options sont communes à toutes ces rapports et elles seront décrites une seule fois au début de cette section. Les quelques options spécifiques à un rapport donné seront décrites avec le chapitre du rapport. Voir également les [Valeurs de substitution](wiki:Gramps_6.0_Wiki_Manual_-_Valeurs_de_substitution).

### Options communes

#### Options du papier

![[_media/Rapport_optionspapier_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Onglet Options du papier]] Avec l'onglet vous pouvez changer :

- Le
  - Letter par défaut

  - 

  - 

  - 

- Les (droite, gauche, haut et bas)

-  : pour choisir des valeurs métriques ou non (cm ou in.)

Voir aussi le dialogue qui peut survenir si votre taille de page personnalisée est trop grande. {{-}}

#### Les options du document

Les options ci-dessous peuvent varier légèrement en fonction du format de sortie sélectionné. ![[_media/Rapport_optionsdocument_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport - Options du document]]

- choisissez le format de sortie :

  - *OpenDocument Texte* (si vous voulez modifier le document avec LibreOffice/OpenOffice)
  - *Document PDF*
  - *PostScript*
  - *Imprimer…*
  - *Document SVG* (Scalable Vector Graphics)  : pour un affichage dans un navigateur ou une modification avec un éditeur graphique adapté.

-  : permet de choisir d'ouvrir le fichier avec le visualiseur par défaut de votre système.

- nom du fichier avec comme valeur par défaut */home/<nom utilisateur>/<Nom arbre familial><Nom du rapport>.<extension du format de sortie>* (chemin variant légèrement avec votre système d'exploitation, ici sous Linux)

- (*défaut* par défaut). Avec le bouton vous pouvez ajouter des styles de document.

- (*arrière-plan transparent* par défaut)

{{-}}

#### Sélectionner l'individu pour le rapport

Le dialogue permet de sélectionner un individu existant déjà dans le rapport et, une fois sélectionné, de le définir comme personne centrale dans les . ![[_media/Rapport_sélectionindividu_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport - Sélection individu]] Par défaut, c'est la persosnne active.

Vous pouvez cocher la case pour afficher l'ensemble des individus de l'arbre familial (non coché par défaut). {{-}}

#### Options de mise à l'échelle et dimensionnement

![[_media/Rapport_adapterarbre_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Onglet Options / adapter l&#39;arbre]] L'arbre est construit, dans un premier temps, sur un canevas qui peut s'adapter à un arbre de n'importe quelle taille. A partir de ce canevas, les options suivantes peuvent changer la façon de l'afficher finalement sur une page.

Cette option agrandit/réduit la taille du rapport sur le canevas pour s'adapter à la taille de la page (définie dans les options du papier) sur lequel vous voulez imprimer. Les options sont :

- **Ne pas redimensionner l'arbre** (par défaut)
- **Adapter l'arbre seulement en largeur**
- **Adapter l'arbre à la taille de la page** (largeur et hauteur)

Si la case n'est pas cochée, les options *Adapter l'arbre* entraîne les conséquences suivantes :

- **Ne pas redimensionner l'arbre** résulte en un rapport qui s'étend sur plusieurs pages horizontalement et/ou verticalement.
- **Adapter l'arbre seulement en largeur** résulte en un rapport qui s'étend sur de multiples pages verticalement. Aucune page l'une à côté de l'autre, seulement l'une au dessus de l'autre.
- **Adapter l'arbre à la taille de la page** résulte en un rapport qui tient sur une page. Le rapport sera imprimé sur une page de la taille définie dans les options papier.

Cette option indique comment redimensionner la page sur laquelle on va imprimer. Si **non cochée**, la taille de la page est définie dans les options du papier. Si cochée, les options *Adapter l'arbre* entraîne les conséquences suivantes : Outrepasser/ignorer les réglages des options du papier va imprimer sur une page avec les mêmes dimensions que le canevas utilisé par l'arbre. Ainsi, en reprenant les trois options ci-dessus pour *Adapter l'arbre*, voici les conséquences suivant votre choix :

- Avec **Ne pas redimensionner l'arbre**, cette option va complètement ignorer ce qui est défini dans les options du papier et imprimer sur une page suffisamment grande pour afficher l'arbre en entier.
- Avec **Adapter l'arbre seulement en largeur**, cette option va ignorer seulement la hauteur de papier définie dans les options du papier. L'arbre sera redimensionné pour s'adapter à la largeur du papier définie. Seule la hauteur de la page est redéfinie par la hauteur de l'arbre à imprimer.
- Avec **Adapter l'arbre à la taille de la page** l'arbre sera redimensionné à la taille de la page. Mais comme décrit plus haut, un espace vide apparaitra dans la largeur ou la hauteur. L'option va diminuer cet espace perdu pour le supprimer.

{{-}}

#### Facteur de modification de l'espace Y de la boite

![[_media/Rapport_optionsavance_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport arbre des descendants - Onglet avancé]] Augmente ou diminue l'espace Y entre les boites.

#### Facteur d'adaptation pour l'ombre de l'aire

Augmente ou diminue l'ombre de la boite. {{-}}

#### Savoir sur quel support vous allez imprimer

Mettre à l'échelle un arbre est une fonction avancée. Dans -\> , ajuster la taille du texte que vous allez imprimer. Diminuer la taille n'est pas souhaitable car le texte devient difficile à lire. L'augmenter est mieux mais peut entraîner des complications. C'est pourquoi voici quelques points importants pour obtenir de belles impression de documents.

Avant tout chose, sur quelle taille de papier allez-vous pouvoir imprimer ? Demandez autour de vous quels sont les opportunités disponibles. Des services professionnels peuvent proposer des tailles inhabituelles.

Il est aussi intéressant de faire d'abord une impression du rapport avec comme option pour *Ne pas redimensionner l'arbre* et en cochant l'option pour savoir quelles sont les dimensions du rapport (largeur et hauteur). Ceci vous aidera à comprendre comment mettre ce rapport sur les feuilles dont vous disposez. Et voici quelques autres idées simples à prendre en compte :

- Un rapport qui est très haut et pas trop large sera plus facile à imprimer avec seulement l'option *Adapter l'arbre seulement en largeur*.
- Avec la largeur normal des rapports, qu'est ce qui donne le meilleur résultat ? Paysage ou portrait ?
- Comme la largeur de toutes les boites est ajustée à la boite la plus grande, pouvez-vous utiliser l'option Rapports des descendants -\> remplacer pour abbréger ou enlever des items longs qui ne sont pas utiles ?
- La taille du titre. S'il y a de la place, vous pouvez agrandir le titre. S'il est trop grand, il va modifier la largeur du rapport.

{{-}}

Les rapports graphiques suivants sont actuellement disponibles dans Gramps :

### <u>Arbre des ascendants</u>

![[_media/Graphical_reports-Ancestor_tree-Sample_pdf_output-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Arbre des ascendants - aperçu d&#39;un exemple de sortie]] Ce rapport produit un diagramme des ancêtres de la personne active.

Choisissez le menu

Voir aussi les options communes ci-dessus. {{-}}

#### Options de l'arbre

![[_media/Ancestor_tree_tab-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Options de l'arbre]]

L' est choisi ici. La personne active est l'individu par défaut.

- 

Avec le champ vous pouvez changer le nombre de génération à prendre en compte.

L' vous permet de sélectionner le nombre de générations à afficher avec des cases vides si l'arbre n'est pas complet.

Il y a également une option pour . {{-}}

#### Options du rapport

![[_media/Rapport_arbreascendantsoptions_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} L&#39;onglet Options du rapport]] Cet onglet vous permet d'inclure d'autres items dans le rapport.

Le permet de choisir le titre du rapport.

- *Ne pas inclure le titre*
- *Inclure le titre du rapport*

Et cet onglet inclut également une case à cocher **□** pour , , et .

Pour l'option , voir les options communes décrites plus haut. {{-}}

#### Options du rapport (2)

![[_media/Rapport_arbreascendantsoptions2_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} L'onglet Options du rapport (2)]]

-  : Sélectionner le format pour afficher les noms entre **Nom, Prénom Suffixe** (par défaut)/ Prénom Nom Suffixe / Prénom / Nom, Prénom Patronyme Suffixe Préfixe / Nom, Prénom usuel

-  : Sélectionner pour inclure dans le rapport, ou non, les individus vivants. Choisir entre **Inclus, avec toutes les données** (par défaut) / Noms complets, mais données non visibles / Prénoms remplacés, données non visibles / Noms complets remplacés, données non visibles / Ne pas inclure

- `0`(par défaut) - Sélectionner le nombre d'années depuis le décès à prendre en compte pour le rapport. Ceci permet d'inclure ou exclure dans le rapport les individus décédés récemment.

  -  (case à cocher, cochée par défaut)

- La traduction à utiliser pour ce rapport.

- Le format pour les dates. Choisir **Défaut système (J/M/A) (14/02/2018)** / YYYY-MM-DD(ISO)(2018-02-14) / Jour Mois Année (14 février 2018) / Jour MOI Année (14 fevr 2018) / Jour. Mois Année (14. fevrier 2018) / Jour. MOI Année (14. fevr 2018) / Mois Jour, Année (février 14, 2018) / MOI, Jour Année (févr 14, 2018)

{{-}}

#### Affichage

![[_media/Rapport_arbreascendantaffichage_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} L'onglet affichage]]

Cet onglet vous permet de déterminer le à utiliser pour le rapport. Tous les pères, grand-pères, etc. utiliseront ce format.

Le à utiliser pour toutes les mères, grand-mères, etc. utiliseront ce format.

Les {} autour de la ligne d'information du décès établit que toute la ligne sera affichée SEULEMENT s’il y a une information sur le décès. Voir [Valeurs de substitution](wiki:Gramps_6.0_Wiki_Manual_-_Valeurs_de_substitution) pour plus de détails notamment sur l'ajout des lieux et attributs et les formats de nom, dates et lieux.

vous permet de spécifier si l'individu central utilise le format d'affichage du père ou de la mère défini dans l'onglet 'Options de l'arbre'.

spécifie si on affiche une boîte supplémentaire entre le père et la mère qui contiendra l'information sur le mariage. Le (voir [Valeurs de substitution](wiki:Gramps_6.0_Wiki_Manual_-_Valeurs_de_substitution)) spécifie ce qui sera affiché dans la boîte.

{{-}}

#### Avancé

![[_media/Rapport_arbreascendantsavance_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} L'onglet avancé]]

- ceci vous permet de saisir deux chaînes de caractères séparées par '/' qui indique que vous voulez remplacer la première chaine par la deuxième. Par exemple :

      République française/RF

  remplace République française par RF.

-  : cocher cette case ajoute un note (non cochée par défaut). Le champ spécifie le contenu de la note.

-  :spécifie où placer la note sur la page (supérieur gauche par défaut).

- augmente ou diminue l'espace entre les boites (par défaut 1 pouce).

- Augmente ou diminue l'ombre de la boite (par défaut 1 pouce).

{{-}}

### <u>Calendrier</u>

![[_media/Rapport_calendrier_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Le rapport Calendrier]] Ce rapport produit un calendrier avec les anniversaires et les dates de mariage avec une page par mois.

Choisir

Vous pouvez imprimer les mêmes informations en format texte en utilisant le rapport *Jours de naissance et anniversaires…*

Voir [Outils calendrier des vacances](wiki:Calendar_tools_holidays) (en anglais) pour une explication quant au choix des vacances qui apparaissent dans la sortie du calendrier. Vois aussi les *Options communes* en-tête de ce chapitre.

{{-}}

#### Options du rapport

![[_media/Rapport_calendrieroptions_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Options du rapport calendrier]]

- sélectionnez un filtre pour définir les individus qui apparaîtront dans le calendrier.

  - **Toute le base de donnée** (par défaut)
  - Descendants de la personne active
  - Familles descendantes de la personne active
  - Ascendants de la personne active
  - Individus ayant un ancêtre commun avec la personne active
  - tout filtre personnalisé précédemment créé

- l'individu central pour le rapport, habituellement la personne active sauf si vous utilisez le bouton qui ouvre le dialogue de sélection d'un individu.

- (**Mon calendrier** par défaut), première ligne de texte sous le calendrier.

- (**Généré par Gramps** par défaut), deuxième ligne de texte sous le calendrier.

- ([`http://gramps-project.org/`](http://gramps-project.org/) par défaut), troisième ligne de texte sous le calendrier.

{{-}}

#### Options du rapport (2)

![[_media/Rapport_calendrieroptions2_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Options (2) du rapport calendrier]]

-  : Sélectionner le format pour afficher les noms entre **Nom, Prénom Suffixe** (par défaut)/ Prénom Nom Suffixe / Prénom / Nom, Prénom Patronyme Suffixe Préfixe / Nom, Prénom usuel

-  (case à cocher, cochée par défaut)

-  (case à cocher, cochée par défaut)

- La traduction à utiliser pour ce rapport.

{{-}}

#### Contenu

![[_media/Rapport_calendriercontenu_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport calendrier - configuration du contenu]]

- saisir l'année. Par défaut, l'année en cours.

- sélectionnez le pays pour voir les jours fériés corrrespondant.

- (par défaut, lundi). Sélectionner le premier jour de la semaine pour le rapport.

- - **L'épouse garde son nom de jeune fille** (par défaut)
  - L'épouse utilise le nom de son mari (à partir de la première famille listée)
  - L'épouse utilise le nom de son mari (à partir de la dernière famille listée)

-  : inclure ou non les dates de naissance dans le calendrier (coché par défaut)

-  : inclure ou non les anniversaires de mariage dans le calendrier (coché par défaut)

{{-}}

### <u>Arbre des descendants</u>

![[_media/Rapport_descendants_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Arbre des descendants]]

Ce rapport génère un graphique des descendants de la personne active. Alternativement, il peut afficher les descendants des parents de la personne active.

Choisissez le menu

Voir aussi les options communes en-tête de chapitre. {{-}}

#### Options de l'arbre

![[_media/Rapport_descendantsoptionsarbre_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Arbre des descendants - Options de l&#39;arbre]] sélectionne l'individu de départ pour le rapport. Par défaut, c'est la personne active.

(**10** par défaut). Le nombre de générations à afficher sur le diagramme (l'individu de départ inclus). Si l'option est cochée, le diagramme affichera une génération supplémentaire.

spécifie la profondeur d'affichage des conjoints. Est-ce-que le conjoint du conjoint est affiché ainsi que ses enfants ?

va dessiner un diagramme des descendants à partir des parents de la personne de départ, s'ils existent dans la base de données. Ceci modifiera aussi le titre du rapport s'il est activé dans les options : le titre indiquera alors qu'il s'agit de la descendance du père et de la mère.

Voir l'exemple au pied de ce chapitre.

L'option va essayer de compresser l'arbre le plus possible tout en le gardant lisible mais il n'agit pas sur la première génération des parents si l'option est cochée.

Exemple pour illustrer la répercussion du choix du

- Louis est un descendant direct
  - Louis a été marié à Elsa et a eu deux enfants
  - Louis a aussi été marié à Gwenaëlle et a eu un enfant
    - Gwenaëlle avait aussi été marié avec Karl
      - Gwenaëlle et Karl avait eu un enfant

En suivant cet exemple, suivant le niveau de conjoints sélectionné, voici ce qui sera affiché :

- 0 indique que seuls les descendants directs seront affichés. Rien ne sera indiqué sur les conjoints et les mariages. Seul Louis apparaîtra avec ses trois enfants.
- 1 indique que seuls les conjoints concernés par les descendants directs seront affichés. Ici, Louis sera affiché avec 2 boites d'information sur les mariages. Sous le premier seront affichés deux enfants et sous le second un enfant.
- 2 indique que les conjoints des conjoints sont affichés. Comme le 1 précédent, mais on verra le deuxième mariage de Gwenaëlle ainsi que les enfants s'il y en a.
- 3 Tout le monde apparaît.

Avec un choix supérieur à 1, l'arbre sera difficile à lire sans cocher l'option .

{{-}}

#### Options du rapport

![[_media/Rapport_arbredescendantsoptions_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Options du rapport]] permet de choisir l'affichage d'un titre pour le rapport. Les options disponibles sont :

- *Ne pas inclure de titre*
- *Arbre des descendant pour <la personne de départ> / <les parents de la personne de départ>* suivant les choix de l'onglet 'Options de l'arbre'. Au maximum, deux personnes sont listées dans le titre. Si le *Niveau de conjoints* est égal à deux ou plus, les descendants des «conjoints des conjoints» seront inclus dans le diagramme mais ne sont pas listés dans le titre.

Les options sont décrites précisément dans les options communes en tête de chapitre.

{{-}}

#### Options du rapport (2)

![[_media/Rapport_arbredescendantsoptions2_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Options du rapport (2)]]

-  : Sélectionner le format pour afficher les noms entre **Nom, Prénom Suffixe** (par défaut)/ Prénom Nom Suffixe / Prénom / Nom, Prénom Patronyme Suffixe Préfixe / Nom, Prénom usuel

  -  (case à cocher, cochée par défaut)

-  : Sélectionner pour inclure dans le rapport, ou non, les individus vivants. Choisir entre **Inclus, avec toutes les données** (par défaut) / Noms complets, mais données non visibles / Prénoms remplacés, données non visibles / Noms complets remplacés, données non visibles / Ne pas inclure

- `0`(par défaut) - Sélectionner le nombre d'années depuis le décès à prendre en compte pour le rapport. Ceci permet d'inclure ou exclure dans le rapport les individus décédés récemment.

- La traduction à utiliser pour ce rapport.

- Le format pour les dates. Choisir **Défaut système (J/M/A) (14/02/2018)** / YYYY-MM-DD(ISO)(2018-02-14) / Jour Mois Année (14 février 2018) / Jour MOI Année (14 fevr 2018) / Jour. Mois Année (14. fevrier 2018) / Jour. MOI Année (14. fevr 2018) / Mois Jour, Année (février 14, 2018) / MOI, Jour Année (févr 14, 2018)

{{-}}

#### Affichage

![[_media/Rapport_arbredescendantsaffichage_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Onglet Affichage]] définit l'affichage de tous les descendants dans l'arbre. Par défaut:

    $n
    n. $b
    {d. $d}

qui affiche le nom, la date de naissance et de décès sur des lignes successives dans le format défini dans l'onglet Affichage des préférences de Gramps. Les {} autour de la ligne d'information du décès établit que toute la ligne sera affichée seulement s’il y a une information sur la date de décès de cet individu. Voir [Valeurs de substitution](wiki:Gramps_6.0_Wiki_Manual_-_Valeurs_de_substitution) pour plus de détails notamment sur l'ajout des lieux et attributs et les formats de nom, dates et lieux.

spécifie ce qui est affiché pour chaque conjoint. Par défaut, le modèle est identique au descendant. Si vous ne souhaitez pas avoir une aire séparée pour le mariage, la section conjoint permet également d'afficher l'information du mariage par exemple en ajoutant la ligne

    m. $m 

qui affichera la date du mariage.

affichera dans l'arbre une boite séparée pour chaque mariage. Son contenu est défini avec le champ avec par défaut

    m. $m 

qui affiche la date du mariage. Si vous ne cocher pas cette case, le mariage ne sera pas affiché à moins que vous ajoutiez aux informations du conjoint comme décrit plus haut.

{{-}}

#### Avancé

![[_media/Rapport_arbredescendantsavance_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Onglet avancé]]

- ceci vous permet de saisir deux chaînes de caractères séparées par '/' qui indique que vous voulez remplacer la première chaine par la deuxième. Par exemple :

<!-- -->

    République française/RF
    Llanfair­pwllgwyn­gyllgo­gerychwyrn­drobwll­llanty­silio­gogogoch/Llanfairpwll

Chaque largeur de colonne est définie par la plus large boite dans le rapport. Ainsi, si une boite se trouve bien plus large que les autres, un grand espace va être perdu. L'option de remplacement permet d'enlever ou abréger des parties du texte qui ne sont pas utiles, ou qui peuvent être raccourcis de telle façon que la perte d'espace soit minimale.

-  : cocher cette case ajoute un note (non cochée par défaut). Le champ spécifie le contenu de la note. Par exemple, ajouter la variable «\$T» dans la note affichera le jour de création du rapport. Le formatage de date standard est appliqué (Voir [Valeurs de substitution](wiki:Gramps_6.0_Wiki_Manual_-_Valeurs_de_substitution)).

-  :spécifie dans quel coin du rapport placer la note (inférieur gauche par défaut).

- augmente ou diminue l'espace entre les boites (par défaut 1 pouce).

- Augmente ou diminue l'ombre de la boite (par défaut 1 pouce).

{{-}}

#### Exemple

![[_media/Rapport_descendantssansparents_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Exemple 1 : Arbre des descendants de Adkins Minnie ; son mari a eu une 2e épouse]] ![[_media/Rapport_descendantsavecparents_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Arbre des descendants à partir des parents de Page Florence]] Dans l'exemple 1, s'affichent les descendants de Adkins Minnie ; la case «Démarrer avec les parents» n'a pas été cochée. La deuxième épouse de son mari apparaît. Dans l'exemple 2, nous partons de Page Florence qui est la fille d'Adkins Minnie mais la case «Démarrer avec les parents» a été cochée.

Les différences pour le diagramme comprenant les parents concernent :

- la présentation des parents de la première génération  : comme les parents de la personne active doivent être adjacents, les conjoints peuvent être présentés dans le désordre.
- selon le paramètre de la profondeur de conjoints, les deux parents sont au même niveau au dépend des autres conjoints, bien que le conjoint soit soumis aux options définies dans le format d'affichage le concernant.

{{-}}

### <u>Arbre familial des descendants</u>

#### Options de l'arbre

![[_media/Rapport_arbrefamildescendantsoptarbre_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Les options de l'arbre]]

L'option sélectionnera la famille centrale (père et mère) pour ce rapport. La famille par défaut est la famille active.

 : si cette case est cochée, l'arbre va commencer avec les parents des deux conjoints (s'ils existent dans la base de données) et tous les descendants de couples de parents selon la profondeur de conjoints sélectionnée. Le nombre de générations affichées est alors supérieur de un au nombre défini dans le champ .

Comme les parents doivent être au centre du diagramme, ils ne sont pas classés dans l'ordre avec leurs frères et sœurs mais comme le premier et le dernier enfant de leur parent respectif. De plus, si les parents de départ ont eu d'autres conjoints, ils seront affichés deux fois. Ceci vaut aussi pour les parents des père et mère de départ.

Si cette option n'est pas cochée, la présentation est proche de l'arbre des descendants sauf pour la première génération et les options de titre. {{-}}

#### Options du rapport

Le propose des options supplémentaires :

1.  *Ne pas inclure de titre*
2.  *Arbre des descendants pour \[individus(s) sélectionné(s)\]*
3.  *Graphique familiale de \[noms de la famille choisie\]*
4.  *Arbre des cousins pour \[noms des enfants\]* (disponible seulement si est cochée)

#### Le résultat final

![[_media/Family_Descendant_chart-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} L'arbre familial des descendants]]

Le résultat final est visible à la droite de cette page. {{-}}

### Roue des ascendants

![[_media/Rapport_roueascendants_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Roue des ascendants]] Ce rapport produit un diagramme ressemblant à un éventail, avec la personne active au centre, ses parents dans le demi-cercle suivant, ses grand-parents dans le prochain demi-cercle, et ainsi de suite, pour un total de cinq générations.

Choisir ce rapport par

Voir les options communes en tête de chapitre. {{-}}

#### Les options du rapport

![[_media/Rapport_roueascendantsoptions_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Options du rapport]]

-  : l'individu central pour le rapport. Utilisez le bouton pour changer d'individu central.

- (**5** par défaut) Le nombre de générations à prendre en compte pour le rapport.

- : la forme du graphique

  - cercle
  - demi-cercle
  - quart de cercle

- : choisir blanc ou **selon la génération** (par défaut).

- : choisir droit ou courbé.

-  : affiche l'arrière-plan bien qu'il n'y ait pas d'information (coché par défaut)

-  : Vous pouvez personnaliser la police et la couleur pour chaque génération avec l'éditeur de style (coché par défaut)

{{-}}

#### Les options du rapport (2)

![[_media/Rapport_roueascendantsoptions2_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Options du rapport]]

-  (coché par défaut)

-  : Sélectionner pour inclure dans le rapport, ou non, les individus vivants. Choisir entre **Inclus, avec toutes les données** (par défaut) / Noms complets, mais données non visibles / Prénoms remplacés, données non visibles / Noms complets remplacés, données non visibles / Ne pas inclure

- `0`(par défaut) - Sélectionner le nombre d'années depuis le décès à prendre en compte pour le rapport. Ceci permet d'inclure ou exclure dans le rapport les individus décédés récemment.

- La traduction à utiliser pour ce rapport.

{{-}}

### <u>Diagrammes statistiques</u>

Ce rapport affiche des statistiques sur votre arbre familial.

<div>

- ![[_media/Rapport_statmoisnais_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graphique 1 (Mois de naissance)]]

- ![[_media/Rapport_statgenre_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graphique 2 (Genre)]]

- ![[_media/Rapport_statnbreenfants_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graphique 3 (Nombre d'enfants) -]]

</div>

Choisissez le menu

Les options spécifiques incluent le filtre, les méthodes de tri, des limites pour la naissance ou le genre pour l'inclusion dans des statistiques. Vous pouvez aussi spécifier le nombre minimum d'items pour un diagramme en barre qui sera transformé en diagramme circulaire si ce nombre n'est pas atteint. Les onglets , et permet de sélectionner les graphiques supplémentaires à afficher dans le rapport.

Voir aussi les options communes en tête de chapitre. {{-}}

#### Options du rapport

![[_media/Rapport_statoptions_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Options du rapport]]

- sélectionnez un filtre pour définir les individus qui apparaîtront dans le calendrier.

  - **Toute le base de donnée** (par défaut)
  - Descendants de la personne active
  - Familles descendantes de la personne active
  - Ascendants de la personne active
  - Individus ayant un ancêtre commun avec la personne active
  - tout filtre personnalisé précédemment créé

- l'individu central pour le rapport, habituellement la personne active. Le bouton ouvre le dialogue de sélection d'un individu pour choisir un autre individu central.

- définit la méthode utilisée pour trier les données statistiques.

  - **Nombre d'articles** (par défaut)
  - Nom de l'article

- 

- (**1700** par défaut) année de naissance à partir de laquelle on ajoute les individus : mettez une année pour l'utiliser

- (**année en cours** par défaut) année de naissance avant laquelle on ajoute les individus : mettez une année pour l'utiliser

- .

- sélectionnez quels genres sont inclus dans les statistiques.

  - **Hommes et femmes** (par défaut)
  - Hommes
  - Femmes

- (**8** par défaut). La limite en dessous de laquelle un diagramme circulaire sera utilisé au lieu d'un diagramme en bâtons.

-   : inclure ou non les comptes des individus sans information.

{{-}}

#### Options du rapport (2)

![[_media/Rapport_statoptions2_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Options du rapport (2)]]

-  : Sélectionner le format pour afficher les noms entre **Nom, Prénom Suffixe** (par défaut)/ Prénom Nom Suffixe / Prénom / Nom, Prénom Patronyme Suffixe Préfixe / Nom, Prénom usuel

  -  (case à cocher, cochée par défaut)

-  : Sélectionner pour inclure dans le rapport, ou non, les individus vivants. Choisir entre **Inclus, avec toutes les données** (par défaut) / Noms complets, mais données non visibles / Prénoms remplacés, données non visibles / Noms complets remplacés, données non visibles / Ne pas inclure

- `0`(par défaut) - Sélectionner le nombre d'années depuis le décès à prendre en compte pour le rapport. Ceci permet d'inclure ou exclure dans le rapport les individus décédés récemment.

- La traduction à utiliser pour ce rapport.

{{-}}

#### Graphiques 1

![[_media/Rapport_statgraph1_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Options Graphiques 1]] Les diagrammes proposés sont :

- 

- 

- 

- 

- 

- 

{{-}}

#### Graphiques 2

![[_media/Rapport_statgraph2_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Options Graphiques 2]] Les diagrammes proposés sont :

- 

- 

- 

- 

- 

- 

{{-}}

#### Graphiques 3

![[_media/Rapport_statgraph3_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Options Graphiques 2]] Les diagrammes proposés sont :

- 

- 

- 

- 

- 

- 

{{-}}

### <u>Graphique temporel</u>

![[_media/Rapport_timeline_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graphique temporel - aperçu]]

Ce rapport affiche l'ensemble de personnes avec leur existence présentée sur une échelle chronologique commune.

Choisissez le menu {{-}}

#### Options du rapport

![[_media/Rapport_temporeloptions_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graphique temporel - Options]]

- sélectionnez un filtre pour définir les individus qui apparaîtront dans le calendrier.

  - **Toute le base de donnée** (par défaut)
  - Descendants de la personne active
  - Familles descendantes de la personne active
  - Ascendants de la personne active
  - Individus ayant un ancêtre commun avec la personne active
  - tout filtre personnalisé précédemment créé

- l'individu central pour le rapport, habituellement la personne active. Le bouton ouvre le dialogue de sélection d'un individu pour choisir un autre individu central.

- - **Naissance** (par défaut)
  - Nom

{{-}}

#### Options du rapport (2)

![[_media/Rapport_temporeloptions2_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graphique temporel - Options (2)]]

-  : Sélectionner le format pour afficher les noms entre **Nom, Prénom Suffixe** (par défaut)/ Prénom Nom Suffixe / Prénom / Nom, Prénom Patronyme Suffixe Préfixe / Nom, Prénom usuel

  -  (case à cocher, cochée par défaut)

-  : Sélectionner pour inclure dans le rapport, ou non, les individus vivants. Choisir entre **Inclus, avec toutes les données** (par défaut) / Noms complets, mais données non visibles / Prénoms remplacés, données non visibles / Noms complets remplacés, données non visibles / Ne pas inclure

- `0`(par défaut) - Sélectionner le nombre d'années depuis le décès à prendre en compte pour le rapport. Ceci permet d'inclure ou exclure dans le rapport les individus décédés récemment.

- La traduction à utiliser pour ce rapport.

{{-}}

## <span id="Graphs"></span>Diagrammes

Ces rapports sont dépendants de [GraphViz](http://www.graphviz.org/) qui doit être installé sur votre ordinateur.

Les trois diagrammes disponibles partagent des options communes.

Ils partagent aussi des options communes avec d’autres rapports : et . {{-}}

### Options communes

#### Mise en page GraphViz

![[_media/Rapport_miseenpagegraphviz_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Onglet Mise en page]]

- : choisissez la famille de police. Si certains caractères internationaux n’apparaissent pas, utilisez la police **FreeSans**. FreeSans est disponible depuis [NonGNU.org](http://www.nongnu.org/freefont/).

  - Défaut
  - PostScript/ Helvetica
  - True Type/ FreeSans

- : la taille de la police en points (**14** par défaut).

-   
  comment le graphique sera généré - de haut en bas ou de gauche à droite.

  - **Vertical (de haut en bas)** (par défaut)
  - Vertical (de bas en haut)
  - Horizontal (de gauche à droite)
  - Horizontal (de droite à gauche)

- : (**1** par défaut) GraphViz peut générer de très grands graphiques en étalant le graphique sur une matrice de pages. Ce paramètre indique le nombre de pages sur une entendue horizontale. **Seulement valide pour .gv et pdf via Ghostscript**.

- : (**1** par défaut) GraphViz peut générer de très grands graphiques en étalant le graphique sur une matrice de pages. Ce paramètre indique le nombre de pages sur une entendue verticale. **Seulement valide pour .gv et pdf via Ghostscript**.

- : (inférieur gauche par défaut) le sens du graphique à la sortie. Cette option n’est disponible que si le nombre de pages horizontales ou verticales est supérieur à 1.

-  : comment les lignes entre les objets sont dessinées. Choisir entre :

  - Droit
  - Courbe (par défaut)
  - Orthogonal

#### Options GraphViz

![[_media/Rapport_optionsgraphviz_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Onglet Options GraphViz]]

- : Affecte grandement la façon dont le graphique est disposé dans la page, spécifiquement l’espace entre les nœux et l’échelle du graphe (voir conseil **1**).

  - Compresser à la taille minimale
  - Remplir la zone donnée
  - Étendre uniformément

<hr>

Conseil 1 : Si le diagramme est plus petit que la zone d’impression :

- **Compresser à la taille minimale** ne modifiera pas l’espacement des nœuds
- **Remplir la zone donnée** augmentera l’espacement des nœuds pour s’ajuster à la taille de la feuille en largeur et en hauteur
- **Étendre uniformément** augmentera l’espacement des nœuds uniformément pour préserver le ratio d’aspect

Si le diagramme est plus grand que la zone d’impression :

- **Compresser à la taille minimale** va réduire le diagramme pour parvenir à un aspect resserré au dépend de la symétrie.
- **Remplir la zone donnée** va réduire le diagramme pour pour s’adapter à la zone d’impression après avoir d’abord augmenté l’espacement des nœuds.
- **Étendre uniformément** va réduire le diagramme uniformément pour s’adapter à la zone d’impression.

<hr>

- : (**72** par défaut) dots-per-inch (points par pouce). Quand vous créer des fichiers PostScript ou PDF, utiliser 72. Typiquement entre 75 et 120 pour générer un fichier .png ou .gif, voire 300 ou 600 si les fichiers doivent être imprimés.

- : l’espace à laisser, en pouces, entre les lignes.

- : l’espace à laisser, en pouces, entre les colonnes.

-  (coché par défault) Les sous-graphiques peuvent aider GraphViz à positionner les conjoints ensemble, mais avec des diagrammes non négligeables, cela entraîne des lignes plus longues et des diagrammes plus grands.

{{-}}

#### Note

![[_media/Rapport_confignote_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Onglet Note Graphviz]]

- (vide par défaut) Ce texte sera ajouté au diagramme.

- Si la note apparaît en haut ou en bas de la page.

  - **Haut** (par défault)
  - *Bas*

- (`10` par défaut) La taille du texte de la note, en points.

{{-}}

### <u>Graphique de lignées familiales</u>

![[_media/Rapport_ligneesfamiliales_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Exemple de graphique lignées familiales]]

Génère un diagramme de lignées familiales en utilisant le générateur [GraphViz](wiki:Output_formats#Graphviz).

Une utilisation typique de ce rapport est l’impression de graphiques simples sur des **traceurs graphiques grand format**.

Pour créer un , sélectionner le menu et ensuite dans l’onglet , sélectionnez au moins une personne avec le dialogue . Il vous est alors proposé une seconde personne que vous pouvez accepter ou non. Le bouton permet de créer le rapport. {{-}}

#### Options du rapport

![[_media/Rapport_ligneesfamiloptions_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graphique lignées familiales - Options du rapport]]

-  Les parents et leurs ancêtres seront pris en compte à la détermination des «lignées familiales» (coché par défaut)

-  (coché par défaut)

-  Les individus et les familles non directement reliés aux individus recherchés seront omis à la détermination des «lignées familiales». (coché par défaut)

-  : Choisissez la direction des flèches

  - **Descendants \<- Ascendants**(par défault) - flèches orientées en direction des Descendants.
  - *Descendants -\> Ascendants* - flèches orientées en direction des Ascendants.
  - *Descendants \<-\> Ascendants* - flèches orientées vers les deux.
  - *Descendants - Ascendants* - Aucune (pas d’affichage de flèches)

- \- Les individus de sexe masculin seront affichés en bleu et ceux de sexe féminin en rouge, sauf indication contraire dans l’onglet Individus. Si le genre d’un individu est inconnu, il sera affiché en gris.

  - *Bordure en noir et blanc (intérieur vide)* - Contour en noir et blanc
  - *Bordure en couleur (intérieur vide)*
  - **Remplissage avec des couleurs** (par défaut)

-  pour différencier les femmes et les hommes (non coché par défaut)

- s’il faut inclure l’identifiant Gramps.

  - **Ne pas inclure** par défaut
  - Partager une ligne existante
  - Ajouter sur la même ligne

{{-}}

#### Options du rapport (2)

![[_media/Rapport_ligneesfamiloptions2_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graphique lignées familiales - Options du rapport (2)]]

- \- Sélectionne le format des noms à afficher. Ce choix est théoriquement fait dans le réglage par défaut du de l’onglet Affichage dans [Edition &gt; Préférences…](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Affichage) Ou pour passer outre ce réglage pour ce rapport, choisissez :

  - **Défaut** - (dans un nouvel arbre familial, c’est normalement *Nom*, *Prénom* *Suffixe*)
  - Nom, Prénom Suffixe
  - Prénom, Nom Suffixe
  - Prénom
  - Nom, Prénom Patronyme Suffixe Préfixe
  - NOM, Prénom (usuel)

-  (coché par défaut) - S’il faut inclure les données privées.

- \- Comment gérer les (informations à propos des) individus vivants

  - **Inclus, avec toutes les données** (par défaut)
  - Noms complets, mais données non visibles
  - Prénoms remplacés, données non visibles
  - Noms complets remplacés, données non visibles
  - Ne pas inclure

- `0`(par défaut) - S’il faut restreindre les données concernant les individus décédés récemment.

- La traduction à utiliser pour ce rapport. Le sélecteur de langue affiche toutes les langues prises en charge par Gramps. Par défaut, la langue que vous utilisez avec Gramps.

- Le format et la langue pour les dates avec des exemples

  - Défaut système - Choisissez cette option pour utiliser le format de date défini dans de l’onglet Affichage dans [Edition &gt; Préférences…](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Affichage)
  - **YYYY-MM-DD(ISO)(2018-02-14)** (par défaut pour le rapport)
  - Jour Mois Année (14 février 2018)
  - Jour MOI Année (14 fevr 2018)
  - Jour. Mois Année (14. fevrier 2018)
  - Jour. MOI Année (14. fevr 2018)
  - Mois Jour, Année (février 14, 2018)
  - MOI, Jour Année (févr 14, 2018)

{{-}}

#### Individus recherchés

![[_media/Rapport_lignéesfamilindividurech_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graphique lignées familiales - Individus recherchés]] Le graphique fonctionne en débutant avec une liste d'"Individus recherchés". Cette liste préliminaire d’individus est alors utilisée pour trouver les ascendants et descendants.

-  : cliquez sur le bouton et pour ajouter/supprimer des individus à rechercher. En cas de doute, essayez d’ajouter vos grand-parents comme point de départ.

-  (case non cochée par défaut)

  - `50` par défaut. Le nombre maximum d’ascendants à inclure. Le maximum est pour le nombre total d’individus et non pour les générations à afficher dans le graphique.

-  (case non cochée par défaut)

  - `50` par défaut. Le nombre maximum de descendants à inclure. Le maximum est pour le nombre total d’individus et non pour les générations à afficher dans le graphique.

{{-}}

#### Inclure

![[_media/Rapport_ligneesfamilinclure_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Lignées familiales - Configuration Inclure]]

-  : date de naissance, date de décès, et dates de mariage seront incluses dans le graphique si cette option est cochée (cochée par défaut).

-  : du précédent, n’affiche que les années. (non cochée par défaut)

-  : lieu de naissance, lieu de décès, et lieux de mariage seront inclus dans le graphique si cette option est cochée (cochée par défaut).

-  : l’aire de texte prévue pour le mariage inclura le nombre d’enfants si cette option est cochée (non cochée par défaut).

-  (cochée par défaut)

- - **Au-dessus du nom** (par défaut)
  - À coté du nom

- - **Normal** (par défaut)
  - Grand

{{-}}

#### Couleurs de la famille

![[_media/Rapport_ligneesfamilcouleurfamil_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Lignées familiales - Couleurs de la famille]]

-  : Sélectionnez la couleur à utiliser pour les individus porteur du même nom de famille. Deux colonnes sont disponibles : **Nom** et **couleur**. Cliquez sur le bouton pour ajouter un nom à partir du dialogue de puis cliquer le bouton . Faites un double-clic sur une ligne pour éditer la couleur du nom et choisissez une couleur dans le dialogue parmi celles affichées puis cliquez le bouton .

{{-}}

#### Individus

![[_media/Rapport_ligneesfamilindividus_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Lignées familiales - Configuration Individus]] Pour chacune des catégories suivantes, vous pouvez sélectionner une couleur en faisant un double-clic sur le ruban de couleur. Dans le dialogue qui s'ouvre choisissez la couleur puis cliquer sur le bouton .

-  : la couleur à utiliser pour les individus de sexe masculin

-  : la couleur à utiliser pour les individus de sexe féminin

- : la couleur à utiliser pour les individus dont le genre n'est pas connu (et pour les individus dont le nom de famille ne correspond à aucun nom défini dans l'onglet "Couleur de la famille").

- : la couleur à utiliser pour les familles (mariages).

{{-}}

### <u>Sablier</u>

![[_media/Hourglass_report.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sablier sur Smith John Hjalmar]]

Génère un graphique en sablier en utilisant le générateur GraphViz. Aller à {{-}}

#### Options du rapport

![[_media/Rapport_sablieroptions_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sablier - Options du rapport]]

- l'individu central pour le rapport, par défaut la personne active.

  - Le bouton . - Modifie l'individu central.

- par défaut `10`

- par défaut `10`

-   
  Choisir vers quelle direction vont les flèches :

  - *Centre -\> Autres* (par défaut) - les flèches vont de l'individu central vers les autres.
  - *Centre \<- Autres* - les flèches vont vers l'individu central à partir des autres.
  - *Centre \<-\> Autres* - les flèches vont dans les deux directions.
  - *Centre - Autres* - Aucune (pas de flèche affichée)

- \- Les individus de sexe masculin seront affichés en bleu et ceux de sexe féminin en rouge, sauf indication contraire dans l’onglet Individus. Si le genre d’un individu est inconnu, il sera affiché en gris.

  - *Bordure en noir et blanc (intérieur vide)* - Contour en noir et blanc
  - *Bordure en couleur (intérieur vide)*
  - **Remplissage avec des couleurs** (par défaut)

-  pour différencier les femmes et les hommes (non coché par défaut)

- s’il faut inclure l’identifiant Gramps.

  - **Ne pas inclure** par défaut
  - Partager une ligne existante
  - Ajouter sur la même ligne

{{-}}

#### Options du rapport (2)

![[_media/Rapport_sablieroptions2_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sablier - Options du rapport (2)]]

- \- Sélectionne le format des noms à afficher. Ce choix est théoriquement fait dans le réglage par défaut du de l’onglet Affichage dans [Edition &gt; Préférences…](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Affichage) Ou pour passer outre ce réglage pour ce rapport, choisissez :

  - **Défaut** - (dans un nouvel arbre familial, c’est normalement *Nom*, *Prénom* *Suffixe*)
  - Nom, Prénom Suffixe
  - Prénom, Nom Suffixe
  - Prénom
  - Nom, Prénom Patronyme Suffixe Préfixe
  - NOM, Prénom (usuel)

-  (coché par défaut) - S’il faut inclure les données privées.

- \- Comment gérer les (informations à propos des) individus vivants

  - **Inclus, avec toutes les données** (par défaut)
  - Noms complets, mais données non visibles
  - Prénoms remplacés, données non visibles
  - Noms complets remplacés, données non visibles
  - Ne pas inclure

- `0`(par défaut) - S’il faut restreindre les données concernant les individus décédés récemment.

- La traduction à utiliser pour ce rapport. Le sélecteur de langue affiche toutes les langues prises en charge par Gramps. Par défaut, la langue que vous utilisez avec Gramps.

- Le format et la langue pour les date avec des exemples

  - Défaut système - Choisissez cette option pour utiliser le format de date défini dans de l’onglet Affichage dans [Edition &gt; Préférences…](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Affichage)
  - YYYY-MM-DD(ISO)(2021-02-14)
  - Jour Mois Année (14 février 2021)
  - Jour MOI Année (14 fevr 2021)
  - Jour. Mois Année (14. fevrier 2021)
  - Jour. MOI Année (14. fevr 2018)
  - Mois Jour, Année (février 14, 2021)
  - MOI, Jour Année (févr 14, 2021)

{{-}}

#### Style du graphique

![[_media/Rapport_sablierstylegraph_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sablier - Style du graphique]]

Pour chacune des catégories suivantes, vous pouvez sélectionner une couleur en faisant un double-clic sur le ruban de couleur. Dans le dialogue qui s'ouvre choisissez la couleur puis cliquer sur le bouton .

- : la couleur à utiliser pour les individus de sexe masculin

- : la couleur à utiliser pour les individus de sexe féminin

- : la couleur à utiliser pour les individus dont le genre n'est pas connu (et pour les individus dont le nom de famille ne correspond à aucun nom défini dans l'onglet "Couleur de la famille").

- : la couleur à utiliser pour les familles (mariages).

{{-}}

### <u>Graphique relationnel</u>

![[_media/Relgrafexample.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Exemple d&#39;une personne avec plusieurs conjoints]] Ce rapport est très intéressant car il permet de créer un graphique complexe et détaillé au format [GraphViz](http://www.graphviz.org/) notamment grâce aux filtres personnalisés. Il sera ainsi possible de réaliser, par exemple, un graphique reprenant l'ensemble de la parenté pour une branche de l'arbre familial. La qualité du résultat est néanmoins dépendante du nombre d'individus et du format de sortie. Il est accessible par le menu . Une fenêtre permet alors de régler tous les paramètres.

Voir aussi [Options communes](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Rapports#Options_communes_2) {{-}}

#### Options du rapport

![[_media/Rapport_graphrelationneloptions_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graphique relationnel - Options]]

- Choisir le filtre à appliquer au rapport parmi :

  - *Toute la base de données* (par défaut) (**non recommandé !** si le nombre d'individus enregistré dans la base de données est volumineux)
  - Descendants de la personne active
  - Familles descendantes de la personne active
  - Ascendants de la personne active
  - Individus ayant un ascendant commun avec la personne active
  - *Tous les [filtres personnalisés](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Les_filtres#Éditeur_de_filtre_personnalisé) que vous aurez créés seront listés au-dessous*

- L’individu central pour le filtre. Par défaut, la personne active. Si vous utilisez un filtre personnalisé, aucun individu ne peut être sélectionné.

  - Le bouton modifie la personne centrale du filtre.

- : Choisissez la direction des flèches

  - **Descendants \<- Ascendants**(par défault) - flèches orientées en direction des Descendants.
  - *Descendants -\> Ascendants* - flèches orientées en direction des Ascendants.
  - *Descendants \<-\> Ascendants* - flèches orientées vers les deux.
  - *Descendants - Ascendants* - Aucune (pas d’affichage de flèches)

- \- Les individus de sexe masculin seront affichés en bleu et ceux de sexe féminin en rouge, sauf indication contraire dans l’onglet Individus. Si le genre d’un individu est inconnu, il sera affiché en gris.

  - *Bordure en noir et blanc (intérieur vide)* - Contour en noir et blanc
  - *Bordure en couleur (intérieur vide)*
  - **Remplissage avec des couleurs** (par défaut)

-  pour différencier les femmes et les hommes (non coché par défaut)

-  pour différencier les individus de genre inconnu (non coché par défaut)

- s’il faut inclure l’identifiant Gramps.

  - **Ne pas inclure** par défaut
  - Partager une ligne existante
  - Ajouter sur la même ligne

{{-}}

#### Options du rapport (2)

![[_media/Rapport_graphrelationneloptions2_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graphique relationnel - Options du rapport (2)]]

- \- Sélectionne le format des noms à afficher. Ce choix est théoriquement fait dans le réglage par défaut du de l’onglet Affichage dans [Edition &gt; Préférences…](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Affichage) Ou pour passer outre ce réglage pour ce rapport, choisissez :

  - **Défaut** - (dans un nouvel arbre familial, c’est normalement *Nom*, *Prénom* *Suffixe*)
  - Nom, Prénom Suffixe
  - Prénom, Nom Suffixe
  - Prénom
  - Nom, Prénom Patronyme Suffixe Préfixe
  - NOM, Prénom (usuel)

-  (coché par défaut) - S’il faut inclure les données privées.

- \- Comment gérer les (informations à propos des) individus vivants

  - **Inclus, avec toutes les données** (par défaut)
  - Noms complets, mais données non visibles
  - Prénoms remplacés, données non visibles
  - Noms complets remplacés, données non visibles
  - Ne pas inclure

- `0`(par défaut) - S’il faut restreindre les données concernant les individus décédés récemment.

- La traduction à utiliser pour ce rapport. Le sélecteur de langue affiche toutes les langues prises en charge par Gramps. Par défaut, la langue que vous utilisez avec Gramps.

- Le format et la langue pour les date avec des exemples

  - Défaut système - Choisissez cette option pour utiliser le format de date défini dans de l’onglet Affichage dans [Edition &gt; Préférences…](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Affichage)
  - YYYY-MM-DD(ISO)(2018-03-14)
  - Jour Mois Année (14 février 2018)
  - Jour MOI Année (14 fevr 2018)
  - Jour. Mois Année (14. fevrier 2018)
  - Jour. MOI Année (14. fevr 2018)
  - Mois Jour, Année (février 14, 2018)
  - MOI, Jour Année (févr 14, 2018)

{{-}}

#### Inclure

![[_media/Rapport_graphrelationnelinclure_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graphique relationnel - Configuration Inclure]]

- S'il faut inclure les dates et/ou les lieux

  - **Ne pas inclure de date et de lieu** (par défaut)
  - Inclure les dates (de naissance, mariage, décès), mais pas les lieux
  - Inclure les dates (de naissance, mariage, décès), ainsi que les lieux
  - Inclure les dates (de naissance, mariage, décès), ainsi que les lieux si pas de date
  - Inclure les années (de naissance, mariage, décès), mais pas les lieux
  - Inclure les années (de naissance, mariage, décès), ainsi que les lieux
  - Inclure les lieux (de naissance, mariage, décès), mais pas les dates
  - Inclure les dates (de naissance, mariage, décès), ainsi que les lieux sur la même ligne

-  (cochée par défaut)

-  (non cochée par défaut).

-  (non cochée par défaut).

-  (non cochée par défaut)

- - **Au-dessus du nom** (par défaut)
  - À coté du nom

- - **Ne pas inclure la profession** (par défaut)
  - Inclure la description de la dernière profession
  - Inclure la date, description et le lieu pour toutes les professions

{{-}}

#### Style du graphique

![[_media/Rapport_graphrelationnelstyle_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graphique relationnel - Style du graphique]] Pour chacune des catégories suivantes, vous pouvez sélectionner une couleur en faisant un double-clic sur le ruban de couleur. Dans le dialogue qui s'ouvre choisissez la couleur puis cliquer sur le bouton .

- : la couleur à utiliser pour les individus de sexe masculin

- : la couleur à utiliser pour les individus de sexe féminin

- : la couleur à utiliser pour les individus dont le genre n'est pas connu (et pour les individus dont le nom de famille ne correspond à aucun nom défini dans l'onglet "Couleur de la famille").

- : la couleur à utiliser pour les familles (mariages).

(coché par défaut) (coché par défaut) {{-}}

Vous pouvez trouver plus de détails dans le tutorial [Comment produire un graphique relationnel](http://www.gramps-project.org/wiki/index.php?title=Howto:_Make_a_relationship_chart/fr).

#### Exemple

![[_media/Graph_relationnel_exemple_51_fr.jpg|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Exemple d'une personne avec plusieurs conjoints]]

Maintenant réalisons un exemple concret. On veut un rapport relationnel avec les familles descendantes d'une certaine personne.

1.  Premièrement, vérifiez que cette personne est la *personne active*. Vous pourrez toujours la changer plus tard si besoin, mais c'est plus simple.
2.  Allez dans le menu
3.  Taille du papier : A4, mètrique, paysage ; nous savons qu'il n'y aura pas beaucoup de personnes dans le graphique, donc ce sera suffisant (*dans le cas contraire vous pouvez utiliser la taille maximum*).
4.  Options du rapport. Filtre : Familles descendantes de…, remplissage avec des couleurs, utiliser des coins arrondis.
5.  Style du graphique : Afficher les noeuds familiaux.
6.  Mise en page GraphViz : Taille de la police de caractère : 15 pts - FreeSans ; Direction : de haut en bas.
7.  Options GraphViz : remplir la zone donnée, dpi 133.
8.  Note : nous ajoutons un titre en-tête et sa taille : 18 pts.
9.  Format de sortie : nous voulons un fichier JPEG.

Voici le résultat...

- **Vous pouvez trouver plus de détails dans le tutorial [Comment produire un graphique relationnel](wiki:Comment_produire_un_graphique_relationnel)**.

{{-}}

## <span id="Text Reports"></span>Rapports texte

Les rapports de texte présentent l'information comme du texte formaté. La plupart des options sont communes à tous ces rapports et vont être décrites ici sous Options communes.

### Options communes

Les options communes à toutes les éditions en mode texte sont le nom du fichier de sortie, le format du fichier de sortie, le choix du style, la taille et l'orientation de la page. Les édition HTML n'ont pas d'option liées au format de page. Elles ont à la place le choix d'un modèle HTML parmi ceux fournis avec Gramps ou bien que vous avez défini. En option, l'édition peut être ouverte immédiatement avec son application par défaut (choisie dans le menu principal de votre distribution).

Les quelques options spécifiques à un rapport seront décrites avec l'entrée en question ainsi que dans les [références de la ligne de commande](wiki:Plugins_Command_Line).

Pour chaque rapport, la boite de dialogue de configuration comprend une partie supérieure avec des onglets en nombre variable suivant le rapport (comme options du papier) et une partie inférieure **Options du document**.

#### Options du papier

![[_media/Rapporttxt_parametres_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Options du papier et du document]] Avec l'onglet vous pouvez changer :

- Le
  - Letter par défaut

  - 

  - 

  - 

- Les (droite, gauche, haut et bas)

-  : pour choisir des valeurs métriques ou non (cm ou in.)

#### Options du document

Les options ci-dessous peuvent varier légèrement en fonction du format de sortie sélectionné.

- choisissez le format de sortie :

  - Texte brut
  - Imprimer…
  - HTML
  - OpenDocument Texte
  - Document PDF
  - PostScript
  - Document RTF

-  : permet de choisir d'ouvrir le fichier avec le visualiseur par défaut de votre système.

- nom du fichier avec comme valeur par défaut */home/<nom utilisateur>/<Nom arbre familial><Nom du rapport>.<extension du format de sortie>* (chemin variant légèrement avec votre système d'exploitation, ici sous Linux)

- (*défaut* par défaut). Avec le bouton vous pouvez ajouter des styles de document.

- (*72* par défaut) pour les documents en texte brut

{{-}}

### <u>Liste Ahnentafel (Sosa-Stradonitz)</u>

![[_media/Rapporttxt_sosa_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport liste Ahnentafel]] Ce rapport liste la personne active et ses ancêtres avec leurs données de naissance et décès.

Allez au menu

Chaque personne reçoit un numéro suivant un schéma appelé Ahnentafel, [Sosa-Stradonitz](http://fr.wikipedia.org/wiki/Numérotation_de_Sosa-Stradonitz) ou encore Eyzinger selon les sources.

Le principe est de donner le numéro 1 à la personne active. Son père reçoit le numéro 2, sa mère le numéro 3.

Et ainsi de suite pour les générations suivantes: les parents du père sont notés 4 et 5, les parents de la mère 6 et 7. Donc, pour chaque personne ayant un nombre N dans cet arbre, les nombres du père et de la mère sont respectivement 2N et 2N+1.

`   individu = n`  
`   père = 2n`  
`   mère = 2n+1`

Chaque entrée est un nouveau paragraphe indépendant, et contient les informations suivantes :

- Le numéro de l'individu.
- Le nom de l'individu.
- Les informations de naissance, si disponible.
- Les informations de décès, si disponible.
- Les informations d'inhumation, si disponible.

Voir aussi les options communes en tête de cette section. {{-}}

#### Options du rapport

![[_media/Rapporttxt_sosaoptions_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Options du rapport]]

- l'individu central pour le rapport. Par défaut, c'est la personne active.

- (**10** par défaut). Le nombre de générations à inclure dans le rapport

- - **Ne pas inclure** (par défaut)
  - Inclure

S'il faut passer à une nouvelle page entre chaque génération ou non (non coché par défaut) Indique si un saut de ligne doit suivre le nom (non coché par défaut) {{-}}

#### Options du rapport (2)

![[_media/Rapporttxt_sosaoptions2_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Graphique lignées familiales - Options du rapport (2)]]

- \- Sélectionne le format des noms à afficher. Ce choix est théoriquement fait dans le réglage par défaut du de l’onglet Affichage dans [Edition &gt; Préférences…](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Affichage) Ou pour passer outre ce réglage pour ce rapport, choisissez :

  - **Défaut** - (dans un nouvel arbre familial, c’est normalement *Nom*, *Prénom* *Suffixe*)
  - Nom, Prénom Suffixe
  - Prénom, Nom Suffixe
  - Prénom
  - Nom, Prénom Patronyme Suffixe Préfixe
  - NOM, Prénom (usuel)

-  (coché par défaut) - S’il faut inclure les données privées.

- \- Comment gérer les (informations à propos des) individus vivants

  - **Inclus, avec toutes les données** (par défaut)
  - Noms complets, mais données non visibles
  - Prénoms remplacés, données non visibles
  - Noms complets remplacés, données non visibles
  - Ne pas inclure

- `0`(par défaut) - S’il faut restreindre les données concernant les individus décédés récemment.

- La traduction à utiliser pour ce rapport. Le sélecteur de langue affiche toutes les langues prises en charge par Gramps. Par défaut, la langue que vous utilisez avec Gramps.

- Le format et la langue pour les dates avec des exemples

  - **Défaut système (j/M/A) (14/02/2018)** (par défaut) - Cette option utilise le format de date défini dans de l’onglet Affichage dans [Edition &gt; Préférences…](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Affichage)
  - YYYY-MM-DD(ISO)(2018-02-14)
  - Jour Mois Année (14 février 2018)
  - Jour MOI Année (14 fevr 2018)
  - Jour. Mois Année (14. fevrier 2018)
  - Jour. MOI Année (14. fevr 2018)
  - Mois Jour, Année (février 14, 2018)
  - MOI, Jour Année (févr 14, 2018)

{{-}}

### <u>Jours de naissance et anniversaires</u>

![[_media/Rapporttxt_annivers_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport anniversaires]] Ce rapport liste les anniversaires et les anniversaires de mariage. Il donne les mêmes informations que le rapport graphique Calendrier mais dans un format texte.

Allez au menu

{{-}}

#### Options du rapport

![[_media/Rapporttxt_anniversoptions_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Options du rapport]]

- sélectionnez un filtre pour définir les individus qui apparaîtront dans le rapport.

  - **Toute le base de donnée** (par défaut)
  - Descendants de la personne active
  - Familles descendantes de la personne active
  - Ascendants de la personne active
  - Individus ayant un ancêtre commun avec la personne active
  - tout filtre personnalisé précédemment créé est listé sous les précédents

- l'individu central pour le rapport, habituellement la personne active sauf si vous utilisez le bouton qui ouvre le dialogue de sélection d'un individu.

- Titre du rapport. **Jours de naissance et anniversaires** (par défaut)

- (**Mon rapport d'anniversaire** par défaut), première ligne de texte sous le rapport.

- (**Généré avec Gramps** par défaut), deuxième ligne de texte sous le rapport.

- ([`http://gramps-project.org/`](http://gramps-project.org/) par défaut), troisième ligne de texte sous le rapport.

{{-}}

#### Options du rapport (2)

![[_media/Rapporttxt_anniversoptions2_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Options (2) du rapport]]

-  : Sélectionner le format pour afficher les noms entre **Nom, Prénom Suffixe** (par défaut)/ Prénom Nom Suffixe / Prénom / Nom, Prénom Patronyme Suffixe Préfixe / Nom, Prénom usuel

-  (case à cocher, cochée par défaut)

-  (case à cocher, cochée par défaut)

- La traduction à utiliser pour ce rapport.

{{-}}

#### Contenu

![[_media/Rapporttxt_anniverscontenu_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Onglet Contenu du rapport]]

- saisir l'année. Par défaut, l'année en cours.

- sélectionnez le pays pour voir les jours fériés corrrespondant.

- - **L'épouse garde son nom de jeune fille** (par défaut)
  - L'épouse utilise le nom de son mari (à partir de la première famille listée)
  - L'épouse utilise le nom de son mari (à partir de la dernière famille listée)

-  : inclure ou non les dates de naissance dans le rapport (coché par défaut)

-  : inclure ou non les anniversaires de mariage dans le rapport (coché par défaut)

-  : inclure ou non les anniversaires de décès dans le rapport (coché par défaut)

-  : inclure ou non la relation avec la souche dans le rapport (création du rapport plus lent) (non coché par défaut)

{{-}}

### <u>Nombre d'ascendants</u>

![[_media/Rapporttxt_nbreascendants_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nombre d&#39;ascendants]] Ce rapport présente le nombre d'ancêtres de la personne active.

Aller au menu .

Le rapport affichera les détails suivants :

  
La génération 1 contient 1 individu : 100 % : la personne choisie au départ

<!-- -->

  
La génération 2 contient 2 individus : 100 % : les deux parents sont connus

<!-- -->

  
…

<!-- -->

  
La génération 8 contient 35 individus : 27,34 % **ce qui signifie que sur les (2\*\*7) 128 ancêtres possibles à la génération 8, 27 % sont connus.**

Enfin, le **total** des ascendants de la génération 2 à la dernière listée est également donné en nombre et pourcentage.

Voir aussi les *options communes* en haut de cette section.

#### Options du rapport

![[_media/Rapporttxt_nbreascendantsoptions_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nombre d'ascendants - Options]]

- l'individu central pour le rapport, habituellement la personne active sauf si vous utilisez le bouton qui ouvre le dialogue de sélection d'un individu.

-  : Sélectionner le format pour afficher les noms entre :

  - **Nom, Prénom Suffixe** (par défaut)
  - Prénom Nom Suffixe
  - Prénom
  - Nom, Prénom Patronyme Suffixe Préfixe
  - Nom, Prénom usuel

-  (case à cocher, cochée par défaut)

- La traduction à utiliser pour ce rapport.

{{-}}

{{-}}

### <u>Fiche individuelle complète</u>

![[_media/Rapporttxt_ficheindividuel_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fiche individuelle complète - Extrait d'un exemple]]

Ce rapport fournit différents résumés pour un compte rendu succinct individuel.

Allez au menu

Vous aussi les *Options communes* au début de cette section. {{-}}

#### Options du rapport

![[_media/Rapporttxt_listeindividueloptions_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fiche individuelle complète - Options]] L'avantage de ce rapport est l'option spécifique de filtre. Selon le choix de filtre (personne active seulement, ses descendants, ses ancêtres, ou base de données entière), le rapport peut contenir d'un à plusieurs résumés différents. Une autre option pour ce rapport est l'inclusion d'informations sur les sources liée aux événements.

- Choisir entre :

  - **La personne active**(par défaut)
  - Toute le base de donnée
  - Descendants de la personne active
  - Familles descendantes de la personne active
  - Ascendants de la personne active
  - Individus ayant un ancêtre commun avec la personne active
  - tout filtre personnalisé précédemment créé est listé sous les précédents

- l'individu central pour le rapport, habituellement la personne active sauf si vous utilisez le bouton qui ouvre le dialogue de sélection d'un individu.

(coché par défaut) (non coché par défaut) {{-}}

#### Options du rapport (2)

![[_media/Rapporttxt_ficheindividueloptions2_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fiche individuelle complète - Options (2)]]

- \- Sélectionne le format des noms à afficher. Ce choix est théoriquement fait dans le réglage par défaut du de l’onglet Affichage dans [Edition &gt; Préférences…](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Affichage) Ou pour passer outre ce réglage pour ce rapport, choisissez :

  - **Défaut** - (dans un nouvel arbre familial, c’est normalement *Nom*, *Prénom* *Suffixe*)
  - Nom, Prénom Suffixe
  - Prénom, Nom Suffixe
  - Prénom
  - Nom, Prénom Patronyme Suffixe Préfixe
  - NOM, Prénom (usuel)

- - **Défaut**
  - Complet

-  (coché par défaut) - S’il faut inclure les données privées.

- \- Comment gérer les (informations à propos des) individus vivants

  - **Inclus, avec toutes les données** (par défaut)
  - Noms complets, mais données non visibles
  - Prénoms remplacés, données non visibles
  - Noms complets remplacés, données non visibles
  - Ne pas inclure

- `0`(par défaut) - S’il faut restreindre les données concernant les individus décédés récemment.

- La traduction à utiliser pour ce rapport. Le sélecteur de langue affiche toutes les langues prises en charge par Gramps. Par défaut, la langue que vous utilisez avec Gramps.

- Le format et la langue pour les dates avec des exemples

  - **Défaut système (j/M/A) (14/02/2018)** (par défaut) - Cette option utilise le format de date défini dans de l’onglet Affichage dans [Edition &gt; Préférences…](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Affichage)
  - YYYY-MM-DD(ISO)(2018-02-14)
  - Jour Mois Année (14 février 2018)
  - Jour MOI Année (14 fevr 2018)
  - Jour. Mois Année (14. fevrier 2018)
  - Jour. MOI Année (14. fevr 2018)
  - Mois Jour, Année (février 14, 2018)
  - MOI, Jour Année (févr 14, 2018)

{{-}}

#### Inclure

![[_media/Rapporttxt_ficheindividuelinclure_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fiche individuelle complète - Options Inclure]]

-  (coché par défaut)

-  (coché par défaut)

-  (non coché par défaut)

-  (coché par défaut)

{{-}}

#### Inclure (2)

![[_media/Rapporttxt_ficheindividuelinclure2_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fiche individuelle complète - Options Inclure (2)]]

- - **Ne pas inclure** (par défaut)
  - Inclure

-  (coché par défaut)

-  (coché par défaut)

-  (coché par défaut)

-  (non coché par défaut) S'il faut inclure les relations avec la personne souche (Note : ralentit la création du rapport)

{{-}}

#### Sections

![[_media/Rapporttxt_ficheindividuelsections_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fiche individuelle complète - Options Sections]]

- -  (coché par défaut)

  -  (coché par défaut)

  -  (coché par défaut)

  -  (coché par défaut)

  -  (coché par défaut)

  -  (coché par défaut)

  -  (coché par défaut)

  -  (coché par défaut)

  -  (coché par défaut)

{{-}}

### <u>Liste simplifiée des descendants</u>

![[_media/Rapporttxt_listsimpldescend_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Liste simplifiée des descendants - Extrait d'un exemple]]

Ce rapport présente les descendants de la personne active avec une courte description avec un style indenté.

Allez au menu

{{-}} Vous aussi les *Options communes* au début de cette section.

#### Options du rapport

![[_media/Rapporttxt_listsimpldescendoptions_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Options du rapport]]

-  : l'individu central pour le rapport. Utilisez le bouton pour changer d'individu central.

- Le [système de numérotation](wiki:Genealogical_Numbering_Systems) à utiliser.

  - **[Numérotation simple](wiki:Genealogical_Numbering_Systems#simple_numbering)** (par défaut)
  - Numérotation [d'Aboville](wiki:Genealogical_Numbering_Systems#d&#39;Aboville)
  - Numérotation [Henry](wiki:Genealogical_Numbering_Systems#Henry)
  - Numérotation [Henry modifiée](wiki:Genealogical_Numbering_Systems#modified_henry)
  - Numérotation [de Villiers](wiki:Genealogical_Numbering_Systems#de_villiers)/[Pama](wiki:Genealogical_Numbering_Systems#pama)
  - Numérotation [Meurgey de Tupigny](wiki:Genealogical_Numbering_Systems#meurgey_de_tupigny)

- (**10** par défaut) Le nombre de générations à prendre en compte pour le rapport.

- s’il faut inclure l’identifiant Gramps.

  - **Ne pas inclure** par défaut
  - Inclure

-  : (non coché par défaut) S'il faut ou non afficher les informations du mariage dans le rapport

-  : (non coché par défaut) S'il faut ou non afficher les informations du divorce dans le rapport

-  : (coché par défaut) s'il faut afficher ou non les informations sur les branches dupliquées

{{-}}

#### Options du rapport (2)

![[_media/Rapporttxt_listsimpldescendoptions2_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Options du rapport (2)]]

- \- Sélectionne le format des noms à afficher. Ce choix est théoriquement fait dans le réglage par défaut du de l’onglet Affichage dans [Edition &gt; Préférences…](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Affichage) Ou pour passer outre ce réglage pour ce rapport, choisissez :

  - **Défaut** - (dans un nouvel arbre familial, c’est normalement *Nom*, *Prénom* *Suffixe*)
  - Nom, Prénom Suffixe
  - Prénom, Nom Suffixe
  - Prénom
  - Nom, Prénom Patronyme Suffixe Préfixe
  - NOM, Prénom (usuel)

- - **Défaut**
  - Complet

-  (coché par défaut) - S’il faut inclure les données privées.

- \- Comment gérer les (informations à propos des) individus vivants

  - **Inclus, avec toutes les données** (par défaut)
  - Noms complets, mais données non visibles
  - Prénoms remplacés, données non visibles
  - Noms complets remplacés, données non visibles
  - Ne pas inclure

- `0`(par défaut) - S’il faut restreindre les données concernant les individus décédés récemment.

- La traduction à utiliser pour ce rapport. Le sélecteur de langue affiche toutes les langues prises en charge par Gramps. Par défaut, la langue que vous utilisez avec Gramps.

- Le format et la langue pour les dates avec des exemples

  - **Défaut système (j/M/A) (14/02/2018)** (par défaut) - Cette option utilise le format de date défini dans de l’onglet Affichage dans [Edition &gt; Préférences…](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Affichage)
  - YYYY-MM-DD(ISO)(2018-02-14)
  - Jour Mois Année (14 février 2018)
  - Jour MOI Année (14 fevr 2018)
  - Jour. Mois Année (14. fevrier 2018)
  - Jour. MOI Année (14. fevr 2018)
  - Mois Jour, Année (février 14, 2018)
  - MOI, Jour Année (févr 14, 2018)

{{-}}

### <u>Liste détaillée des ascendants</u>

![[_media/Rapporttxt_listdetailascend_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Liste détaillée des ascendants - Extrait exemple]] Ce rapport présente en détails les ancêtres de la personne active. Les données de naissance et décès ainsi que les mariages sont listées ainsi que la numérotation Ahnentafel/Sosa-Stradonitz. Il partage beaucoup de propriétés avec le rapport 'Liste détaillée des descendants'.

Allez au menu

{{-}} Vous aussi les *Options communes* au début de cette section.

#### Options du rapport

![[_media/Rapporttxt_listdetailascendoptions_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Options]] Ce rapport est structuré par la numérotation Sosa-Stradonitz.

-  : l'individu central pour le rapport. Utilisez le bouton pour changer d'individu central.

- (**1** par défaut) Le numéro Sosa-Stradonitz de l'individu central.

- (**10** par défaut) Le nombre de générations à prendre en compte pour le rapport.

- s’il faut inclure l’identifiant Gramps.

  - **Ne pas inclure** par défaut
  - Inclure

(non coché par défaut) (non coché par défaut) {{-}}

#### Options du rapport (2)

![[_media/Rapporttxt_listdetailascendoptions2_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Options (2)]]

- \- Sélectionne le format des noms à afficher. Ce choix est théoriquement fait dans le réglage par défaut du de l’onglet Affichage dans [Edition &gt; Préférences…](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Affichage) Ou pour passer outre ce réglage pour ce rapport, choisissez :

  - **Défaut** - (dans un nouvel arbre familial, c’est normalement *Nom*, *Prénom* *Suffixe*)
  - Nom, Prénom Suffixe
  - Prénom, Nom Suffixe
  - Prénom
  - Nom, Prénom Patronyme Suffixe Préfixe
  - NOM, Prénom (usuel)

- - **Défaut**
  - Complet

-  (coché par défaut) - S’il faut inclure les données privées.

- \- Comment gérer les (informations à propos des) individus vivants

  - **Inclus, avec toutes les données** (par défaut)
  - Noms complets, mais données non visibles
  - Prénoms remplacés, données non visibles
  - Noms complets remplacés, données non visibles
  - Ne pas inclure

- `0`(par défaut) - S’il faut restreindre les données concernant les individus décédés récemment.

- La traduction à utiliser pour ce rapport. Le sélecteur de langue affiche toutes les langues prises en charge par Gramps. Par défaut, la langue que vous utilisez avec Gramps.

- Le format et la langue pour les dates avec des exemples

  - **Défaut système (j/M/A) (14/02/2018)** (par défaut) - Cette option utilise le format de date défini dans de l’onglet Affichage dans [Edition &gt; Préférences…](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Affichage)
  - YYYY-MM-DD(ISO)(2018-02-14)
  - Jour Mois Année (14 février 2018)
  - Jour MOI Année (14 fevr 2018)
  - Jour. Mois Année (14. fevrier 2018)
  - Jour. MOI Année (14. fevr 2018)
  - Mois Jour, Année (février 14, 2018)
  - MOI, Jour Année (févr 14, 2018)

{{-}}

#### Contenu

![[_media/Rapporttxt_listdetailascendcontenu_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Option Contenu]]

-  (coché par défaut) Utiliser des phrases complètes ou une formulation succincte.

-  (coché par défaut)

-  (coché par défaut)

-  (coché par défaut)

-  (non coché par défaut)

{{-}}

#### Inclure

![[_media/Rapporttxt_listdetailascendinclure_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Option Inclure]]

-  (coché par défaut)

-  (non coché par défaut)

-  (non coché par défaut)

-  (non coché par défaut) S'il faut inclure les autres évènements auxquels les individus ont participé.

-  (coché par défaut)

-  (non coché par défaut)

{{-}}

#### Inclure (2)

![[_media/Rapporttxt_listdetailascendinclure2_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Option Inclure (2)]]

-  (coché par défaut)

-  (non coché par défaut)

-  (non coché par défaut)

-  (non coché par défaut)

-  (non coché par défaut)

-  (non coché par défaut)

{{-}}

#### Informations absentes

![[_media/Rapporttxt_listdetailascendinfoabsc_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Option Informations absentes]]

-  (non coché par défaut) S'il faut remplacer les lieux manquants par des espaces vides.

-  (non coché par défaut) S'il faut remplacer les dates manquantes par des espaces vides.

{{-}}

### <u>Liste détaillée des descendants</u>

![[_media/Rapporttxt_listdetaildescend_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Liste détaillée des descendants - Exemple - extrait]]

Ce rapport présente en détails les descendants de la personne active par génération, suivant la tradition des rapports textuels des descendants par génération. Il a pour but de présenter toutes les caractéristiques importantes attendues dans cette mise en forme classique des descendants et bénéficie des influences de différentes sources. L'équipe Gramps a dans ses objectifs le souhait que ce rapport puisse être adopté par les institutions professionnelles de la généalogie dans le monde entier. En conséquence, il est hautement personnalisable.

Le rapport comprend un ensemble de données biographiques, les mariages et (en option) les notes et les informations sur les conjoints. Parmi les différentes options, il y a le nombre de générations à prendre en compte, le calcul des âges, le style de texte entre des phrases complètes ou abrégées et s'il faut inclure les images. Le rapport utilise [la numérotation Henry](http://en.wikipedia.org/wiki/Genealogical_numbering_systems#Henry_System) qui diffère de [la numérotation d'Aboville](http://fr.wikipedia.org/wiki/Num%C3%A9rotation_d%27Abboville) par l'utilisation de lettres pour les nombres supérieurs à 9, ainsi que l'absence de point de séparation entre les numéros. (Les numérotations [d'Aboville](http://fr.wikipedia.org/wiki/Num%C3%A9rotation_d%27Abboville) et d'[Enregistrement](http://en.wikipedia.org/wiki/Genealogical_numbering_systems#Register_System) sont disponibles en option.)

Allez au menu

{{-}} Vous aussi les *Options communes* au début de cette section.

#### Options du rapport

![[_media/Rapporttxt_listdetaildescendoptions_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Options]]

-  : l'individu central pour le rapport. Utilisez le bouton pour changer d'individu central.

- - **Numérotation Henry** (par défaut)
  - Numérotation Henry modifiée
  - Numérotation d'Aboville
  - Numérotation Enregistrement

- Comment les individus sont organisés dans le rapport.

  - **affiche les individus par génération** (par défaut)
  - affiche les individus par branche

- (**10** par défaut) Le nombre de générations à prendre en compte pour le rapport.

- s’il faut inclure l’identifiant Gramps.

  - **Ne pas inclure** par défaut
  - Inclure

(non coché par défaut) (non coché par défaut) {{-}}

#### Options du rapport (2)

![[_media/Rapporttxt_listdetaildescendoptions2_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Options (2)]]

- \- Sélectionne le format des noms à afficher. Ce choix est théoriquement fait dans le réglage par défaut du de l’onglet Affichage dans [Edition &gt; Préférences…](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Affichage) Ou pour passer outre ce réglage pour ce rapport, choisissez :

  - **Défaut** - (dans un nouvel arbre familial, c’est normalement *Nom*, *Prénom* *Suffixe*)
  - Nom, Prénom Suffixe
  - Prénom, Nom Suffixe
  - Prénom
  - Nom, Prénom Patronyme Suffixe Préfixe
  - NOM, Prénom (usuel)

- - **Défaut**
  - Complet

-  (coché par défaut) - S’il faut inclure les données privées.

- \- Comment gérer les (informations à propos des) individus vivants

  - **Inclus, avec toutes les données** (par défaut)
  - Noms complets, mais données non visibles
  - Prénoms remplacés, données non visibles
  - Noms complets remplacés, données non visibles
  - Ne pas inclure

- `0`(par défaut) - S’il faut restreindre les données concernant les individus décédés récemment.

- La traduction à utiliser pour ce rapport. Le sélecteur de langue affiche toutes les langues prises en charge par Gramps. Par défaut, la langue que vous utilisez avec Gramps.

- Le format et la langue pour les dates avec des exemples

  - **Défaut système (j/M/A) (14/02/2018)** (par défaut) - Cette option utilise le format de date défini dans de l’onglet Affichage dans [Edition &gt; Préférences…](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Affichage)
  - YYYY-MM-DD(ISO)(2018-02-14)
  - Jour Mois Année (14 février 2018)
  - Jour MOI Année (14 fevr 2018)
  - Jour. Mois Année (14. fevrier 2018)
  - Jour. MOI Année (14. fevr 2018)
  - Mois Jour, Année (février 14, 2018)
  - MOI, Jour Année (févr 14, 2018)

{{-}}

#### Contenu

![[_media/Rapporttxt_listdetaildescendcontenu_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Option Contenu]]

-  (coché par défaut) Utiliser des phrases complètes ou une formulation succincte.

-  (coché par défaut)

-  (coché par défaut)

-  (non coché par défaut)

{{-}}

#### Inclure

![[_media/Rapporttxt_listdetaildescendinclure_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Option Inclure]]

-  (coché par défaut)

-  (non coché par défaut)

-  (non coché par défaut)

-  (non coché par défaut)

-  (non coché par défaut)

-  (coché par défaut)

-  (non coché par défaut)

{{-}}

#### Inclure (2)

![[_media/Rapporttxt_listdetaildescendinclure2_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Option Inclure (2)]]

-  (coché par défaut)

-  (non coché par défaut)

-  (non coché par défaut)

-  (non coché par défaut)

-  (non coché par défaut)

-  (non coché par défaut)

-  (coché par défaut)

-  (non coché par défaut)

{{-}}

#### Informations absentes

![[_media/Rapporttxt_listdetaildescendinfoabs_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Option Informations absentes]]

-  (non coché par défaut) S'il faut remplacer les lieux manquants par des espaces vides.

-  (non coché par défaut) S'il faut remplacer les dates manquantes par des espaces vides.

{{-}}

{{-}}

### <u>Rapport de fin de lignée</u>

![[_media/Rapporttxt_finlignee_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport fin de lignée]]

Ce rapport fournit une liste des derniers ascendants connus pour un individu avec sa lignée généalogique, trié par générations.

Allez au menu {{-}} Vous aussi les *Options communes* au début de cette section.

#### Options du rapport

![[_media/Rapporttxt_finligneeoptions_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport fin de lignée - Options]]

-  : l'individu central pour le rapport. Utilisez le bouton pour changer d'individu central.

- \- Sélectionne le format des noms à afficher. Ce choix est théoriquement fait dans le réglage par défaut du de l’onglet Affichage dans [Edition &gt; Préférences…](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Affichage) Ou pour passer outre ce réglage pour ce rapport, choisissez :

  - **Défaut** - (dans un nouvel arbre familial, c’est normalement *Nom*, *Prénom* *Suffixe*)
  - Nom, Prénom Suffixe
  - Prénom, Nom Suffixe
  - Prénom
  - Nom, Prénom Patronyme Suffixe Préfixe
  - NOM, Prénom (usuel)

-  (coché par défaut) - S’il faut inclure les données privées.

- \- Comment gérer les (informations à propos des) individus vivants

  - **Inclus, avec toutes les données** (par défaut)
  - Noms complets, mais données non visibles
  - Prénoms remplacés, données non visibles
  - Noms complets remplacés, données non visibles
  - Ne pas inclure

- `0`(par défaut) - S’il faut restreindre les données concernant les individus décédés récemment.

- La traduction à utiliser pour ce rapport. Le sélecteur de langue affiche toutes les langues prises en charge par Gramps. Par défaut, la langue que vous utilisez avec Gramps.

- Le format et la langue pour les dates avec des exemples

  - **Défaut système (j/M/A) (14/02/2018)** (par défaut) - Cette option utilise le format de date défini dans de l’onglet Affichage dans [Edition &gt; Préférences…](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Affichage)
  - YYYY-MM-DD(ISO)(2018-02-14)
  - Jour Mois Année (14 février 2018)
  - Jour MOI Année (14 fevr 2018)
  - Jour. Mois Année (14. fevrier 2018)
  - Jour. MOI Année (14. fevr 2018)
  - Mois Jour, Année (février 14, 2018)
  - MOI, Jour Année (févr 14, 2018)

{{-}}

### <u>Rapport de lieu</u>

![[_media/Rapporttxt_lieu_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport de lieu]]

Ce rapport fournit une liste des individus et événements référencés dans un ou plusieurs lieux sélectionnés par l'utilisateur.

Allez au menu {{-}} Vous aussi les *Options communes* au début de cette section.

#### Les options du rapport

![[_media/Rapporttxt_lieuoptions_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport de lieu - Options avec dans cette exemple la sélection de la ville de Dover]]

- Sélectionner les lieux avec un filtre personnalisé créé antérieurement.

- - Bouton  - Ouvre le dialogue pour vous permettre de sélectionner un lieu à ajouter.
  - Bouton  - Sélectionner un lieu dans la liste puis cliquer sur ce bouton pour le supprimer.

- \- Si le rapport doit être centré sur un évènement ou un individu.

  - **Évènement** (par défault)
  - Individu

{{-}}

#### Les options du rapport (2)

![[_media/Rapporttxt_lieuoptions2_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport de lieu - Options (2)]]

- \- Sélectionne le format des noms à afficher. Ce choix est théoriquement fait dans le réglage par défaut du de l’onglet Affichage dans [Edition &gt; Préférences…](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Affichage) Ou pour passer outre ce réglage pour ce rapport, choisissez :

  - **Défaut** - (dans un nouvel arbre familial, c’est normalement *Nom*, *Prénom* *Suffixe*)
  - Nom, Prénom Suffixe
  - Prénom, Nom Suffixe
  - Prénom
  - Nom, Prénom Patronyme Suffixe Préfixe
  - NOM, Prénom (usuel)

- - **Défaut**
  - Complet

-  (coché par défaut) - S’il faut inclure les données privées.

- \- Comment gérer les (informations à propos des) individus vivants

  - **Inclus, avec toutes les données** (par défaut)
  - Noms complets, mais données non visibles
  - Prénoms remplacés, données non visibles
  - Noms complets remplacés, données non visibles
  - Ne pas inclure

- `0`(par défaut) - S’il faut restreindre les données concernant les individus décédés récemment.

- La traduction à utiliser pour ce rapport. Le sélecteur de langue affiche toutes les langues prises en charge par Gramps. Par défaut, la langue que vous utilisez avec Gramps.

- Le format et la langue pour les dates avec des exemples

  - **Défaut système (j/M/A) (14/02/2018)** (par défaut) - Cette option utilise le format de date défini dans de l’onglet Affichage dans [Edition &gt; Préférences…](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Affichage)
  - YYYY-MM-DD(ISO)(2018-02-14)
  - Jour Mois Année (14 février 2018)
  - Jour MOI Année (14 fevr 2018)
  - Jour. Mois Année (14. fevrier 2018)
  - Jour. MOI Année (14. fevr 2018)
  - Mois Jour, Année (février 14, 2018)
  - MOI, Jour Année (févr 14, 2018)

{{-}}

### <u>Fiche familiale</u>

![[_media/Rapporttxt_fichefamil_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport Fiche familiale]] Ce rapport présente un groupe familial, c'est à dire un couple de parents et leurs enfants.

Allez au menu {{-}} Vous aussi les *Options communes* au début de cette section.

#### Options du rapport

![[_media/Rapporttxt_fichefamiloptions_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport Fiche familiale - Options]]

- Choisir entre :

  - **La famille active** (par défaut) La famille de la personne active.
  - Toutes les familles
  - Familles descendantes - de la famille active
  - Familles des ascendants - de la famille active

- le famille centrale pour ce filtre, par défaut la famille de l'individu actif. Le bouton ouvre le dialogue de sélection des familles.

(non coché par défaut) Créer des rapports pour tous les descendants de cette famille. {{-}}

#### Options du rapport (2)

![[_media/Rapporttxt_fichefamiloptions2_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport Fiche familiale - Options (2)]]

- \- Sélectionne le format des noms à afficher. Ce choix est théoriquement fait dans le réglage par défaut du de l’onglet Affichage dans [Edition &gt; Préférences…](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Affichage) Ou pour passer outre ce réglage pour ce rapport, choisissez :

  - **Défaut** - (dans un nouvel arbre familial, c’est normalement *Nom*, *Prénom* *Suffixe*)
  - Nom, Prénom Suffixe
  - Prénom, Nom Suffixe
  - Prénom
  - Nom, Prénom Patronyme Suffixe Préfixe
  - NOM, Prénom (usuel)

- - **Défaut**
  - Complet

-  (coché par défaut) - S’il faut inclure les données privées.

- \- Comment gérer les (informations à propos des) individus vivants

  - **Inclus, avec toutes les données** (par défaut)
  - Noms complets, mais données non visibles
  - Prénoms remplacés, données non visibles
  - Noms complets remplacés, données non visibles
  - Ne pas inclure

- `0`(par défaut) - S’il faut restreindre les données concernant les individus décédés récemment.

- La traduction à utiliser pour ce rapport. Le sélecteur de langue affiche toutes les langues prises en charge par Gramps. Par défaut, la langue que vous utilisez avec Gramps.

- Le format et la langue pour les dates avec des exemples

  - **Défaut système (j/M/A) (14/02/2018)** (par défaut) - Cette option utilise le format de date défini dans de l’onglet Affichage dans [Edition &gt; Préférences…](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Affichage)
  - YYYY-MM-DD(ISO)(2018-02-14)
  - Jour Mois Année (14 février 2018)
  - Jour MOI Année (14 fevr 2018)
  - Jour. Mois Année (14. fevrier 2018)
  - Jour. MOI Année (14. fevr 2018)
  - Mois Jour, Année (février 14, 2018)
  - MOI, Jour Année (févr 14, 2018)

{{-}}

#### Inclure

![[_media/Rapporttxt_fichefamilinclure_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport Fiche familiale - Inclure]]

-  (coché par défaut)

-  (coché par défaut)

-  (non coché par défaut)

-  (non coché par défaut)

-  (non coché par défaut)

-  (non coché par défaut)

{{-}}

#### Inclure (2)

![[_media/Rapporttxt_fichefamilinclure2_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport Fiche familiale - Inclure (2)]]

- - **Ne pas inclure** (par défaut)
  - Inclure

-  (non coché par défaut)

-  (non coché par défaut)

-  (coché par défaut)

-  (non coché par défaut) S'il faut ajouter un numéro pour chaque génération descendante.

-  (coché par défaut) S'il faut inclure un champ pour chaque information manquante.

### <u>Rapport de parenté</u>

![[_media/Rapporttxt_parente_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport de parenté]] Ce rapport fournit la parenté de l'individu sélectionné selon le niveau de recherche (ascendants, descendants) choisi par l'utilisateur.

Allez au menu {{-}}

Vous aussi les *Options communes* au début de cette section.

#### Options du rapport

![[_media/Rapporttxt_parenteoptions_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport de parenté - Options]]

- l'individu central pour le rapport, par défaut la personne active.

  - Le bouton . - Modifie l'individu central.

- par défaut `2`

- par défaut `2`

-  (coché par défaut)

-  (coché par défaut)

-  (coché par défaut)

{{-}}

#### Options du rapport (2)

![[_media/Rapporttxt_parenteoptions2_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport de parenté - Options (2)]]

- \- Sélectionne le format des noms à afficher. Ce choix est théoriquement fait dans le réglage par défaut du de l’onglet Affichage dans [Edition &gt; Préférences…](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Affichage) Ou pour passer outre ce réglage pour ce rapport, choisissez :

  - **Nom, Prénom Suffixe** (par défaut)
  - Prénom, Nom Suffixe
  - Prénom
  - Nom, Prénom Patronyme Suffixe Préfixe
  - NOM, Prénom (usuel)

-  (coché par défaut) - S’il faut inclure les données privées.

- \- Comment gérer les (informations à propos des) individus vivants

  - **Inclus, avec toutes les données** (par défaut)
  - Noms complets, mais données non visibles
  - Prénoms remplacés, données non visibles
  - Noms complets remplacés, données non visibles
  - Ne pas inclure

- `0`(par défaut) - S’il faut restreindre les données concernant les individus décédés récemment.

- La traduction à utiliser pour ce rapport. Le sélecteur de langue affiche toutes les langues prises en charge par Gramps. Par défaut, la langue que vous utilisez avec Gramps.

- Le format et la langue pour les date avec des exemples

  - Défaut système - Choisissez cette option pour utiliser le format de date défini dans de l’onglet Affichage dans [Edition &gt; Préférences…](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Affichage)
  - YYYY-MM-DD(ISO)(2021-02-14)
  - Jour Mois Année (14 février 2021)
  - Jour MOI Année (14 fevr 2021)
  - Jour. Mois Année (14. fevrier 2021)
  - Jour. MOI Année (14. fevr 2018)
  - Mois Jour, Année (février 14, 2021)
  - MOI, Jour Année (févr 14, 2021)

{{-}}

### <u>Rapport de liens de note</u>

![[_media/Rapporttxt_liensnote_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport de liens de note]] Ce rapport affiche et vérifie la cohérence des *liens internes* créés avec l'éditeur de liens dans les notes Gramps et liste sans les vérifier les adresses Internet externes créées avec l'éditeur d'adresses Internet.

Allez au menu {{-}}

Vous aussi les *Options communes* au début de cette section et [Editeur de notes](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Fonctionnement_des_événements,_sources,_lieux,_dépôts_et_notes#L.27.C3.A9diteur_de_note). Il n'y a pas d'options spécifiques à ce rapport.

### <u>Rapport Étiquette</u>

![[_media/Rapporttxt_etiquette_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport Étiquette avec l&#39;option étiquette complète]] Ce rapport liste les objets principaux (individus, familles, notes) correspondant à l'étiquette sélectionnée.

Allez au menu {{-}}

Vous aussi les *Options communes* au début de cette section.

#### Options du rapport

![[_media/Rapporttxt_etiquetteoptions_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport Étiquette - Options]]

- Sélectionner l'étiquette à utiliser pour le rapport.

- \- Sélectionne le format des noms à afficher. Ce choix est théoriquement fait dans le réglage par défaut du de l’onglet Affichage dans [Edition &gt; Préférences…](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Affichage) Ou pour passer outre ce réglage pour ce rapport, choisissez :

  - **Défaut** - (dans un nouvel arbre familial, c’est normalement *Nom*, *Prénom* *Suffixe*)
  - Nom, Prénom Suffixe
  - Prénom, Nom Suffixe
  - Prénom
  - Nom, Prénom Patronyme Suffixe Préfixe
  - NOM, Prénom (usuel)

- - **Défaut**
  - Complet

-  (coché par défaut) - S’il faut inclure les données privées.

- \- Comment gérer les (informations à propos des) individus vivants

  - **Inclus, avec toutes les données** (par défaut)
  - Noms complets, mais données non visibles
  - Prénoms remplacés, données non visibles
  - Noms complets remplacés, données non visibles
  - Ne pas inclure

- `0`(par défaut) - S’il faut restreindre les données concernant les individus décédés récemment.

- La traduction à utiliser pour ce rapport. Le sélecteur de langue affiche toutes les langues prises en charge par Gramps. Par défaut, la langue que vous utilisez avec Gramps.

- Le format et la langue pour les dates avec des exemples

  - **Défaut système (j/M/A) (14/02/2018)** (par défaut) - Cette option utilise le format de date défini dans de l’onglet Affichage dans [Edition &gt; Préférences…](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Affichage)
  - YYYY-MM-DD(ISO)(2018-02-14)
  - Jour Mois Année (14 février 2018)
  - Jour MOI Année (14 fevr 2018)
  - Jour. Mois Année (14. fevrier 2018)
  - Jour. MOI Année (14. fevr 2018)
  - Mois Jour, Année (février 14, 2018)
  - MOI, Jour Année (févr 14, 2018)

{{-}}

### <u>Rapport d'enregistrements</u>

![[_media/Rapporttxt_enregistrement_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport Enregistrements]] Le rapport d'enregistrements affiche un certain nombre d'enregistrements intéressants de votre base de données (la plupart lié à l'âge), comme l'individu vivant le plus âgé, la plus jeune mère, etc.

Allez au menu {{-}}

Vous aussi les *Options communes* au début de cette section.

#### Options du rapport

![[_media/Rapporttxt_enregistrementoptions_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport Enregistrements - Options]]

- sélectionnez un filtre pour définir les individus qui apparaîtront dans le rapport.

  - **Toute le base de donnée** (par défaut)
  - Descendants de la personne active
  - Familles descendantes de la personne active
  - Ascendants de la personne active
  - Individus ayant un ancêtre commun avec la personne active
  - tout filtre personnalisé précédemment créé est listé sous les précédents

- l'individu central pour le rapport, habituellement la personne active sauf si vous utilisez le bouton qui ouvre le dialogue de sélection d'un individu.

- (**3** par défaut)

- - **Ne pas utiliser le prénom usuel** (par défaut)
  - Remplacer les prénoms par le prénom usuel (Voir avertissement ci-dessous)
  - Souligner ou ajouter le prénom usuel dans les prénoms

- vide par défaut.

{{-}}

#### Options du rapport (2)

![[_media/Rapporttxt_enregistrementoptions2_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport Enregistrements - Options (2)]]

- \- Sélectionne le format des noms à afficher. Ce choix est théoriquement fait dans le réglage par défaut du de l’onglet Affichage dans [Edition &gt; Préférences…](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Affichage) Ou pour passer outre ce réglage pour ce rapport, choisissez :

  - **Nom, Prénom Suffixe** (par défaut)
  - Prénom, Nom Suffixe
  - Prénom
  - Nom, Prénom Patronyme Suffixe Préfixe
  - NOM, Prénom (usuel)

-  (coché par défaut) - S’il faut inclure les données privées.

- \- Comment gérer les (informations à propos des) individus vivants

  - **Inclus, avec toutes les données** (par défaut)
  - Noms complets, mais données non visibles
  - Prénoms remplacés, données non visibles
  - Noms complets remplacés, données non visibles
  - Ne pas inclure

- `0`(par défaut) - S’il faut restreindre les données concernant les individus décédés récemment.

- La traduction à utiliser pour ce rapport. Le sélecteur de langue affiche toutes les langues prises en charge par Gramps. Par défaut, la langue que vous utilisez avec Gramps.

{{-}}

#### Individu 1

![[_media/Rapporttxt_enregistrementindividu1_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport Enregistrements - Option Individu 1]]

-  (coché par défaut)

-  (coché par défaut)

-  (non coché par défaut)

-  (coché par défaut)

-  (coché par défaut)

-  (coché par défaut)

-  (non coché par défaut)

-  (non coché par défaut)

{{-}}

#### Individu 2

![[_media/Rapporttxt_enregistrementindividu2_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport Enregistrements - Option Individu 2]]

-  (coché par défaut)

-  (coché par défaut)

-  (coché par défaut)

-  (coché par défaut)

-  (non coché par défaut)

-  (non coché par défaut)

-  (non coché par défaut)

-  (non coché par défaut)

{{-}}

#### Famille

![[_media/Rapporttxt_enregistrementfamille_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport Enregistrements - Option Famille 1]]

-  (coché par défaut)

-  (coché par défaut)

-  (coché par défaut)

-  (non coché par défaut)

-  (coché par défaut)

-  (coché par défaut)

-  (coché par défaut)

{{-}}

### <u>Résumé de la base de données</u>

![[_media/Rapporttxt_resume_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport Enregistrements]] Ce rapport présente des statistiques générales comprenant le nombre d'individus par genre, les données incomplètes et des chiffres sur les familles et les objets multimédia.

Allez au menu

Le rapport fera état des informations suivantes de l'arbre familial ouvert avec l'affichage du nombre dans chaque catégorie.

- **Individus**
  - Nombre d'individus :
  - Hommes :
  - Femmes :
  - Individus de genre inconnu :
  - Noms incomplets :
  - Individus sans date de naissance :
  - Individus déconnectés :
  - Noms présents :
  - Individus avec media :

<!-- -->

- **Informations sur la famille**
  - Nombre de familles :

<!-- -->

- **Objets media**
  - Nombre de media présents :
  - Taille totale des objets media : en MB

<!-- -->

- Objets media manquants : affichera un chemin complet et le nom des fichiers pour chaque objet media manquant.

L'information donnée dans ce rapport est la même que dans le [Gramplet Statistiques](http://www.gramps-project.org/wiki/index.php?title=Gramps_6.0_Wiki_Manual_-_Gramplets/fr#Gramplet_Statistiques) {{-}} Vous aussi les *Options communes* au début de cette section.

#### Options du rapport

![[_media/Rapporttxt_resumeoptions_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport Enregistrements - Options]]

-  (coché par défaut) - S’il faut inclure les données privées.

- \- Comment gérer les (informations à propos des) individus vivants

  - **Inclus, avec toutes les données** (par défaut)
  - Noms complets, mais données non visibles
  - Prénoms remplacés, données non visibles
  - Noms complets remplacés, données non visibles
  - Ne pas inclure

- `0`(par défaut) - S’il faut restreindre les données concernant les individus décédés récemment.

- La traduction à utiliser pour ce rapport. Le sélecteur de langue affiche toutes les langues prises en charge par Gramps. Par défaut, la langue que vous utilisez avec Gramps.

{{-}}

## <span id="Web Pages"></span>Pages internet

### <u>Saga sur internet</u>

![[_media/Pagesweb_sagamayence_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Liste individuelle dans le style Mayence]] Un des rapports disponibles dans cette catégorie est la saga sur internet. Il produit un site web (qui est, une suite de pages web reliées par des liens), pour un ensemble d'individus sélectionnés.

#### Introduction

Le nouveau rapport génère des pages qui suivent le W3C, XHTML 1.0 et CSS 1. Ceci inclut la séparation du contenu et de la présentation. Pour des raisons pratiques, le style et apparence des nouvelles pages Internet peuvent être complètement pilotés depuis une feuille de style CSS sans altérer les pages individuelles. Plus d'informations sont maintenant affichées pour chaque individu, sources, lieux et objets media.

Des pages d'introduction peuvent être ajoutées pour fournir des informations supplémentaires, comme une histoire familiale.

Les enregistrements de généalogie peuvent générer beaucoup de fichiers que les serveurs Web mettront du temps à gérer s'ils sont dans un même répertoire. Le rapport Saga sur Internet s'efforce de garder un nombre de fichiers par répertoire à un niveau gérable. Pour cela, une organisation hiérarchique de répertoires est créée. Les noms des fichiers générés ne sont pas intuitifs mais sont uniques pour chaque individu. Des lancements successifs du rapport vont créer des fichiers qui gardent les mêmes noms, rendant plus facile la mise à jour de fichiers spécifiques.

#### Utilisation du rapport

![[_media/Pagesweb_saganebraska_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Détail de la page individu dans le style Nebraska]] Le rapport saga sur internet offre des options à l'utilisateur, lui permettant de nombreuses combinaisons et personnalisations.

Utilisez ce rapport depuis le menu .

#### Options du rapport

![[_media/Pagesweb_sagaoptions_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pages Web Saga - Options]]

-  : (non coché par défaut). Du fait d'un grand nombre de fichiers et répertoires générés, le transfert de ces derniers vers un serveur externe peut être délicat. C'est pourquoi, vous pouvez directement créer une archive au format gzip et tar (dit aussi 'tarball') pour un transfert plus facile sur le serveur où il sera décompressé.

****

-  : Le répertoire de destination pour les fichiers internet. La valeur par défaut étant le répertoire .

-  : Dans le champ texte vous pouvez changer la valeur **Mon arbre généalogique** par défaut, **ce qui est fortement recommandé**.

-  : (Tout individu correspondant au filtre et qui n'est pas exclus par les règles de données privées sera inclus dans la sortie). Les choix possibles :

  - **Toute la base de données** (par défaut)
  - Descendants de <la personne active>
  - Familles descendantes de <la personne active>
  - Ascendants de <la personne active>
  - Individus ayant un ascendant commun avec <la personne active>
  - Tout filtre personnel que vous avez créé

-  : L'individu central pour le rapport (disponible seulement si vous ne choisissez pas toute la base de données - La personne active par défaut). Utilisez le bouton pour sélectionner un autre individu.

  -  (non coché par défaut) - Pour chaque page d'individu.

- \- Comment gérer les (informations à propos des) individus vivants. Vous pouvez contrôler les informations sensibles concernant une personne encore en vie. Néanmoins, comme Gramps est un outil de recherche, il y a probablement des individus dont la date de décès n'est pas connue dans votre arbre généalogique. Pour savoir si un individu est *potentiellement encore vivant*, Gramps utilise un algorithme qui compare les dates de naissance, décès, baptême, dates de naissance et décès des ancêtres. L'algorithme considère qu'un individu est *peut-être encore en vie* à moins que le croisement des différentes données fasse que la *possibilité qu'il soit encore en vie* est improbable.

  - Inclus, avec toutes les données : Inclure toutes les informations de tous les individus, même si ils sont *peut-être encore en vie*.
  - Noms complets, mais données non visibles
  - Prénoms remplacés, données non visibles
  - Noms complets remplacés, données non visibles
  - Ne pas inclure : exclus toutes les informations des individus *peut-être encore en vie*.

- S’il faut restreindre les données concernant les individus décédés récemment. Cette option est inactive si l'option «Individus vivants» est réglée sur 'Inclus avec toutes les données'.

-  (non coché par défaut) - S’il faut inclure les données privées. Si votre intention est de fournir une version intégrale de vos données, cocher cette case va inclure toutes les données marquées comme privées avec le reste de la base de données.

#### Options html

![[_media/Pagesweb_sagaoptionshtml_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pages Web Saga - Options html]]

-  : L'extension à utiliser pour les fichiers internet. Choisissez entre la valeur par défaut , et .htm, .shtml, .php, .php3, .cgi.

-  : Le droit d'auteur à utiliser pour les pages internet. Le droit d'auteur international vous déclare propriétaire de vos données. Les autres personnes doivent avoir votre permissions pour les utiliser. En généalogie, le partage est un idéal commun. Vous pouvez vouloir définir d'autres droits aux utilisateurs de vos données. Par défaut, Gramps définit le **Droit d'auteur standard**, mais vous pouvez placer votre site sous différentes licences Creative Commons voire l'absence de notice sur le droit d'auteur. Ces licences donnent des permissions aux utilisateurs sans qu'ils vous contacte à chaque fois pour vous les demander. Voir le site internet de [Creative Commons](https://creativecommons.org/) pour plus d'informations.

![[_media/NWeb-Man-BasicSet.jpg|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Style basique - 5 choix de couleur]]

- 

  
La feuilles de style à utiliser pour les pages internet. Gramps fournit différentes feuilles de style pour vos pages. Chacune offrant une apparence unique pour vos pages. Pour l'instant, vous pouvez choisir entre le style **Basique** (**Bleu**, **Cyprès**, **Frêne**, **Lilas**, **Pêcher** ou **Épicéa**) ; le style **Malvoyants** ; le style **Mayence** ou **Nebraska**. Ou vous pouvez utiliser l'option **Aucune feuille de style**. Quelque soit le style choisi, la feuille de style utilisée sera *css/narrative-screen.css* dans le dossier du site nouvellement créé. Vous pouvez l'éditer si vous souhaitez personnaliser votre site. Néanmoins, si vous créer de nouveau le site avec le même chemin, votre feuille de style sera écrasée, à moins que vous utilisiez l'option **Aucune feuille de style**. Vous pouvez aussi utiliser votre propre feuille de style en la copiant dans le répertoire *\$HOME/.gramps/css/* : elle sera alors disponible dans la liste de choix à la création d'un nouveau rapport.

*les figures 1, 2 et 5 sont des exemples de style inclus avec Gramps 6.0*

-  : Choisissez la mise en page pour les menus de navigation.

  - **Horizontal -- Défaut**
  - Vertical -- côté gauche
  - Fondu -- que pour les navigateurs Webkit
  - Abaissé -- que pour les navigateurs Webkit

-  : Déterminer la mise en page par défaut pour la section Références de la citation dans la page source.

  - **Style normal de bordure** (Défaut)
  - Abaissé -- que pour les navigateurs Webkit

-  : Inclure ou non un arbre des ascendants pour chaque page de l'individu. Si vous cochez cette case, un arbre des ascendants sera ajouté. Le nombre de générations est défini avec l'option suivante.

-  : s'il faut ajouter ces boutons dans la barre de navigation

-  : s'il faut utiliser http ou https

{{-}}

#### Affichage

![[_media/Pagesweb_sagaaffichage_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pages Web Saga - Option Affichage]]

- 

  
Sélection du format d'affichage pour les noms. Choisissez:

- Nom, prénom Suffixe (**par défaut**)
- Prénom Nom Suffixe
- Prénom
- Nom, Prénom Patronyme Suffixe Préfixe
- Nom, prénom usuel

- La traduction à utiliser pour ce rapport.

- Le format et la langue pour les dates avec des exemples

- s’il faut inclure l’identifiant Gramps.

  - **Ne pas inclure** par défaut
  - Inclure

(non coché par défaut) Si non coché, ils restent dans l'ordre actuel. (non coché par défaut) Latitude et longitude. (non coché par défaut) Ils sont triés par date si non coché.

-  : Option active seulement si l'option «Inclure un arbre des ascendants» de l'onglet précédent a été cochée. Indique le nombre de générations à inclure dans cet arbre. La valeur par défaut est . Vous pouvez choisir depuis la liste déroulante : 2, 3, 4, ou 5 générations.

Si non, elles apparaissent tout de suite après les attributs. {{-}}

#### Création de page

![[_media/Pagesweb_sagacreatpage_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pages Web Saga - Option Création de page]] Cet onglet permet d'ajouter trois pages additionnelles mais aussi des notes qui s'afficheront sur toutes les pages créées par le générateur de page web.

Vous pouvez assigner un medium ou une note pour chacune des pages. Cette note ou ce medium doivent avoir été créés préalablement à la création du rapport. Par défaut, rien n'est assigné. Utilisez le bouton à la droite d'une ligne pour ajouter une référence.

- Les **page d'accueil** et d**'introduction** : Permet d'ajouter une note et une image.
- La **page contact** : Permet aussi d'ajouter une note et une image, mais attention, lorsque vous utilisez cette page sur un site public à ne pas afficher des informations privées que vous ne souhaitez pas publier. De même, n'affichez pas votre adresse mel standard mais une adresse réservée ou dans un format sécurisé.
- **En-tête HTML** et **pied de page HTML** : Permet d'ajouter une note pour personnaliser l'en-tête et le pied de page de chaque pages générées. L'entête apparaîtra directement en dessous du titre du site, et le pied de page au dessus de la déclaration des droits d'auteur.

{{-}}

#### Pages supplémentaires

![[_media/Pagesweb_sagapagesup_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pages Web Saga - Option Pages supplémentaires]]

- Le nom de la page supplémentaire tel qu'il s'affiche dans la barre de titre.

- Le chemin vers la page sans extension.

  - Bouton permet de naviguer jusqu'à votre page.

{{-}}

#### Génération des images

![[_media/Pagesweb_sagagenerimg_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pages Web Saga - Option Génération des images]]

-  : Inclure ou non une galerie des objets media.

-  : Inclure ou non les objets media non utilisés.

-  : Permet de créer uniquement un aperçu des images plutôt qu'en taille réel dans la page Média. Ceci vous permettra d'obtenir une archive plus petite à envoyer sur votre site internet hébergé.

- (Défaut: 800) : Permet de définir la largeur maximum de l'image affichée dans la page Média. Définissez 0 pour ignorer la limitation.

- (Défaut: 600) : Permet de définir la hauteur maximum de l'image affichée dans la page Média. Définissez 0 pour ignorer la limitation.

{{-}} ![[_media/Pageweb_sagaimage_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pages Web Saga - Région dans une image]] A noter que les [zones de référence](wiki:How_to_create_image_reference_regions) enregistrées dans les photos sont aussi affichées dans les pages Web Saga créées avec Gramps. Il n'y a pas d'option particulière à sélectionner ; il suffit qu'une zone de référence ait été définie pour une ou plusieurs images. Les pages Web Saga n'affiche ces zones de référence que pour les individus et les lieux. {{-}}

#### Télécharger

![[_media/Pagesweb_sagatelecharg_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pages Web Saga - Option Télécharger]]

-  : Permet d'inclure une option de téléchargement de la base de données.

-  : Fichier prévu pour être téléchargé.

  - Avec le bouton permettant de naviguer jusqu'au fichier voulu

-  : Donner une description pour ce fichier. Par défaut: **Arbre de la famille Martin**

-  : Second fichier prévu pour être téléchargé.

  - Avec le bouton permettant de naviguer jusqu'au fichier voulu

-  : Donner une description pour ce fichier. Par défaut: **Arbre de la famille Bernard**

{{-}}

#### Options avancées

![[_media/Pagesweb_sagaoptavanc_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pages Web Saga - Options avancées]] Ces paramètres indiquent le niveau d'informations à afficher dans les pages de liste de noms de famille ou d'individus.

-  : L'encodage à utiliser pour les fichiers internet.

  - **Unicode UTF-8 (recommandé)** (Par défaut)
  - ISO-8859-1
  - ISO-8859-2
  - ISO-8859-3
  - ISO-8859-4
  - ISO-8859-5
  - ISO-8859-6
  - ISO-8859-7
  - ISO-8859-8
  - ISO-8859-9
  - ISO-8859-10
  - ISO-8859-11
  - ISO-8859-12
  - ISO-8859-13
  - ISO-8859-14
  - ISO-8859-15
  - koi8_r

- 

- 

- 

- 

- 

- 

{{-}}

#### Inclure

![[_media/Pagesweb_sagainclure_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pages Web Saga - Option Inclure]]

- 

- 

- 

- 

- 

-  : Cette option créé un fichier GENDEX à la racine du site internet. Vous pouvez trouver des sites qui supportent ce format et en apprendre plus via [l'article Wikipédia de GENDEX](http://en.wikipedia.org/wiki/GENDEX) (en anglais).

- 

- 

{{-}}

#### Options Carte du lieu

![[_media/Pagesweb_sagaoptcartelieu_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pages Web Saga - Options Carte du lieu]]

-   
  Choisissez votre service cartographique pour la création des pages Carte du lieu.

  - **OpenStreetMap**
  - Google© : pour que cette option fonctionne, une doit être entrée. Pour l'obtenir, rendez-vous sur la plateforme [Google maps](https://cloud.google.com/maps-platform/) et sélectionnez le bouton «Commencer» en haut et à droite de la page puis suivez les instructions.

-  : Inclure ou non une carte du lieu sur la page des lieux, quand Latitude/Longitude sont disponibles.

-  : Ajouter ou non un lien sur la page de l'individu qui pointe vers une carte de tous les lieux de la famille. Ceci vous permettra de voir votre famille à travers le pays.

-  : Sélectionner l'option que vous souhaitez utiliser pour la carte familiale Google Maps…

  - **Liens familiaux**
  - Déposer
  - Marqueurs

- 

{{-}}

#### Autre inclusion (CMS, Calendrier internet, Php)

![[_media/Pagesweb_sagaautreinclus_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pages Web Saga - Option Autre inclusion]]

- 

- `/NAVWEB` (par défaut) - Où générer le site internet ?

  - Le bouton en bout de ligne permet de naviguer jusqu'au répertoire souhaité.

- 

  - `/WEBCAL` (default) - Où générer le calendrier internet ?

  - Le bouton en bout de ligne permet de naviguer jusqu'au répertoire souhaité.

{{-}} Voir aussi :

- [Howto:_Make_a_genealogy_website_with_Gramps#Integration_of_NarrativeWeb_in_a_CMS_or_MVS](wiki:Howto:_Make_a_genealogy_website_with_Gramps#Integration_of_NarrativeWeb_in_a_CMS_or_MVS)

{{-}}

### <u>Calendrier internet</u>

![[_media/Pagesweb_calendrier_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Page internet Calendrier - Exemple avec feuille de style Basique-Cyprès]]

Le calendrier internet affiche les évènements des individus sélectionnés sur un ensemble de mois. Vous pouvez lancer la création de ce rapport par le menu .

Il y a des options pour filtrer les individus, choisir les années à inclure (par défaut, seulement l'année en cours est incluse) ; s'il faut inclure seulement les personnes vivantes et s'il faut inclure les dates de naissance et les anniversaires de mariage  ; les notes peuvent être incluses dans les pages mensuelles et des pages de résumé des évènements peuvent être ajoutées.

Ce rapport est conçu pour fonctionner avec le rapport Pages internet [Saga (pages narratives)](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Rapports#Saga_sur_internet). Il y a un lien 'Souche' sur chaque page qui pointe vers la page principale du rapport internet Saga. Il y a aussi une option pour inclure des liens à partir des individus dans le calendrier vers cet individu dans le rapport Saga.

Travailler avec le rapport Saga suppose que les deux rapports aient été conçus de façon compatible par l'utilisateur. Il n'y a pas de vérification automatique de la compatibilité entre les deux. Si les pages ne sont pas compatibles, l'utilisateur risque d'avoir une erreur 'Page not found'.

La compatibilité dépend de :

1.  L'inclusion des mêmes individus dans les deux rapports,
2.  l'enregistrement des pages dans des répertoires compatibles.

Afin d'inclure les mêmes individus dans les deux rapports, les mêmes filtres doivent être utilisés et ainsi que des options similaires pour les individus vivants ou les données privées.

Par défaut, le site Web Saga est enregistré dans le répertoire "`~/<Nom de l'arbre>+NAVWEB`", et par défaut, le site calendrier internet est enregistré dans le répertoire "`~/<Nom de l'arbre>+WEBCAL`". Si ces valeurs par défaut sont conservées, les différents liens devraient fonctionner correctement. Si les répertoires ont été modifiés, le lien 'URL de départ' de l'onglet 'Options du contenu' et le lien 'Destination' de l'onglet 'Options du rapport' doivent être modifiés en conséquence.

Si le calendrier internet n'est pas destiné à être utilisé en association avec le site Web Saga, le texte de 'URL de départ' de l'onglet 'Options du contenu' doit être supprimé pour s'assurer qu'aucun lien vers la 'Souche' ne sera créé. {{-}}

#### Options du rapport

![[_media/Pagesweb_calendrieroptions_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Calendrier internet - Options]]

-  : Le répertoire de destination pour les fichiers internet. La valeur par défaut étant le répertoire .

-  : que vous pouvez modifier (**Mon Calendrier familial** par défaut).

-  : (Tout individu correspondant au filtre et qui n'est pas exclus par les règles de données privées sera inclus dans la sortie). Les choix possibles :

  - **Toute la base de données** (par défaut)
  - Descendants de <la personne active>
  - Familles descendantes de <la personne active>
  - Ascendants de <la personne active>
  - Individus ayant un ascendant commun avec <la personne active>
  - Tout filtre personnel que vous avez créé

-  : L'individu central pour le rapport (disponible seulement si vous ne choisissez pas toute la base de données - La personne active par défaut). Utilisez le bouton pour sélectionner un autre individu.

-  : L'extension à utiliser pour les fichiers internet.

  - **.html** (Default)
  - .htm
  - .shtml
  - .php
  - .php3
  - .cgi

-  : Le droit d'auteur à utiliser pour les pages internet.

  - **Droit d'auteur standard** (par défaut)
  - Creative Commons - Paternité
  - Creative Commons - Paternité, Pas de modifications
  - Creative Commons - Paternité, Partage des Conditions Initiales à l'identique
  - Creative Commons - Paternité, Pas d'utilisation commerciale
  - Creative Commons - Paternité, Pas d'utilisation commerciale, Pas de modifications
  - Creative Commons - Paternité, Pas d'utilisation commerciale, Partage des Conditions Initiales à l'identique
  - Pas de note de licence

-  : La feuilles de style à utiliser pour les pages internet. Il est fortement conseillé de définir une feuille de style pour la lisibilité du calendrier.

  - **Aucune feuille de style**
  - Basique-Bleu
  - Basique-Cyprès
  - Basique-Frêne
  - Basique-Lilas
  - Basique-Pêcher
  - Basique-Épicéa
  - Malvoyants
  - Mayence
  - Nebraska

{{-}}

#### Options du rapport (2)

![[_media/Pagesweb_calendrieroptions2_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Calendrier internet - Options (2)]]

- 

  
Sélection du format d'affichage pour les noms. Choisissez:

- Nom, prénom Suffixe (**par défaut**)
- Prénom Nom Suffixe
- Prénom
- Nom, Prénom Patronyme Suffixe Préfixe
- Nom, prénom usuel

-  (non coché par défaut) - S’il faut inclure les données privées.

-  (coché par défaut) - N'inclure que les individus vivants dans le calendrier.

- La traduction à utiliser pour ce rapport.

- Le format et la langue pour les dates avec des exemples

{{-}}

#### Options du contenu

![[_media/Pagesweb_calendrieroptioncontenu_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Calendrier internet - Options du contenu]]

-  (non coché par défaut). Si coché, les années à créer sont définies dans les champs suivant.

  - (par défaut, l'année en cours)

  - (par défaut, l'année en cours) ; actif seulement si la première case à cocher a été validée.

- Sélectionnez le pays pour voir les jours fériés dans le calendrier (vide par défaut)

- (par défaut **Dimanche**)

- Sélectionne le nom de famille à afficher pour les femmes mariées.

  - **L'épouse garde son nom de jeune fille** (par défaut)
  - L'épouse utilise le nom de son mari (à partir de la première famille listée)
  - L'épouse utilise le nom de son mari (à partir de la dernière famille listée)

- (**`../../Nom de l'arbre_NAVWEB/index.html`** par défaut) Le lien à utiliser pour rediriger l'utilisateur vers la page principale du site internet associé **Saga (pages narratives)**.

{{-}}

#### Options avancées

![[_media/Pagesweb_calendrieroptionavancé_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Calendrier internet - Options avancées]]

- L'encodage à utiliser pour les fichiers Web.

  - **Unicode UTF-8 (recommendé)** (par défaut)
  - ISO-8859-1
  - ISO-8859-2
  - ISO-8859-3
  - ISO-8859-4
  - ISO-8859-5
  - ISO-8859-6
  - ISO-8859-7
  - ISO-8859-8
  - ISO-8859-9
  - ISO-8859-10
  - ISO-8859-13
  - ISO-8859-14
  - ISO-8859-15
  - koi8_r

-  (non coché par défaut) Créer ou non des pages d'évènements par jour. A partir de la page «Année résumée», un clic sur un jour ouvre alors une page qui liste les évènements de ce jour.

-  (coché par défaut)

-  (coché par défaut)

-  (non coché par défaut)

-  (non coché par défaut) : s'il faut créer, dans le calendrier, des liens directs vers les pages du site Saga (chemin du site indiqué ci-dessous)

- Montrer les évènements seulement après cette année. (par défaut, c'est l'année courante - l'«espérance de vie maximale» définie dans les préférences de Gramps - exemple :2021 - 110 = 1911)

- **`../../nom de l'arbre_NAVWEB/`** Le chemin vers le site Saga.

{{-}}

#### Notes Jan - Juin

![[_media/Pagesweb_calendriernotesjanjuin_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Web Calendar - Web Pages - Jan-Jun Notes - tab default options]]

Pour chacun des six premiers mois une note existante peut être sélectionnée par le bouton en bout de ligne.

{{-}}

#### Notes Juil - Déc

![[_media/Pagesweb_calendriernotesjuildec_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Web Calendar - Web Pages - Jan-Jun Notes - tab default options]]

Pour chacun des six derniers mois une note existante peut être sélectionnée par le bouton en bout de ligne. {{-}}

Voir [Calendrier](#Calendrier)

### <u>Rapport Web local Topola</u>

![[_media/Topola_51_fr.png|Arbre en ligne Topola]] Il s'agit d'une fonctionnalité accessible avec l'extension de tierce partie [Interactive Family Tree](wiki:Fr:Interactive_Family_Tree). Elle ne crée pas un site mais utilise localement une application web pour afficher votre arbre généalogique sans avoir à exporter vos données ! La mise en page est moderne, colorée et interactive : un clic sur la case d'un individu recentre l'arbre sur cet individu.

Trois types d'arbres sont possibles et ils peuvent être imprimés ou téléchargés.

Une fois le greffon installé, cette fonction est accessible par le menu

Plus d'informations sur la page du greffon [Interactive Family Tree](wiki:Fr:Interactive_Family_Tree). {{-}}

## Rapports Express

Les **Rapports Express** sont des rapports sous forme de fenêtre contextuelle disponibles dans les menus contextuels de la plupart des vues et dans certains dialogues de modification. Ils peuvent aussi être créés par les utilisateurs, même si leurs connaissances en programmation sont limitées.

![[_media/Rapportexpress_menu_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu contextuel de rapport Express dans la vue de la catégorie Individus]]

Voir aussi le **Gramplet** [Vue Express](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Gramplets#Vue_Express) qui est paramètrable et permet d'afficher dans la barre inférieure ou la barre latérale le Rapport Express que vous voulez voir. Il sera actualisé à la volée selon l'item avec lequel vous travaillez. {{-}}

Les Rapports Express suivant sont disponibles :

- *Tableau de bord* - non disponible
  - mais vous pouvez utiliser le Gramplet [Vue Express](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Gramplets#Vue_Express)
- *Individus* et *Dialogue de modification de l'individu*
  - Frères et sœurs : liste les frères et sœurs de la personne active avec leur genre, date de naissance et le type de relation de la fratrie.
  - Lignée maternelle : liste les femmes ascendantes de la personne active qui correspond à la lignée mtDNA, c'est à dire, qui partagent le même ADN mitochondrial. Il affiche aussi les descendantes féminins.
  - Lignée paternelle  : liste les hommes ascendants de la personne active qui correspondent à la lignée Y, c'est à dire qui partagent le même chromosome Y. Il affiche aussi les descendants masculins.
  - Même nom de famille : liste tous les individus ayant le même nom de famille que la personne active, avec leur date de naissance et l'origine du nom. ![[_media/Rapportexpress_nomfamil_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Exemple de Rapport Express «Même nom de famille» pour la vue Indiviuds, avec menu contextuel]]
  - Même prénom  : liste les individus dont le prénom inclut celui de la personne active avec leur date de naissance et l'origine de leur nom.
  - Relation avec la souche  : indique le lien de parenté entre la personne active et la souche puis l'ascendant commun et le chemin détaillé vers cet ascendant commun pour la personne active et pour la souche.
  - Références (Individu) : les références enregistrées pour cet individu.
  - Tous les évènements  : tous les évènements répertoriés pour cet individu.

<!-- -->

- *Relations* - **Non disponible**

<!-- -->

- *Familles* et *Dialogue de modification de la famille*
  - Références : les références enregistrées pour la famille.
  - Tous les évènements familiaux  : tous les évènements de la famille et des individus qui la composent, parents et enfants.

<!-- -->

- *Graphiques* - **Non disponible**

<!-- -->

- *Évènements*
  - Ce jour  : les évènements du jour de l'évènement sélectionné, ceux du même mois puis de la même année qui sont enregistrés dans votre arbre.
  - Références (Évènement) : les individus, familles, etc ayant cet évènement en référence.

<!-- -->

- *Lieux*
  - Références (Lieu) : tous les évènements ayant le lieu sélectionné en référence.

<!-- -->

- *Géographie* - **Non disponible**

<!-- -->

- *Sources*
  - Références (Source) : tous les items ayant la source sélectionnée en référence.

<!-- -->

- *Citations*
  - Références (Citation) : tous les items ayant la citation sélectionnée en référence.

<!-- -->

- *Dépôts*
  - Références du dépôt : tous les items ayant le dépôt sélectionné en référence.

<!-- -->

- *Media*
  - Références (Media) : tous les items ayant le media sélectionné en référence.

<!-- -->

- *Notes*
  - Références (Note) : tous les items ayant la note sélectionnée en référence.
  - Références lien  : s'il y a un lien dans la note, les items référencés dans ce lien.

{{-}}

### Concevoir votre propre Rapport Express

Vous pouvez créer votre propre Rapport Express même avec des connaissances limitées en programmation.

Beaucoup d'utilisateurs veulent créer rapidement une vue de leurs données pour leurs besoins, mais sont arrêtés par le fait qu'ils ne veulent pas apprendre tout le langage Python, ni les implications complexes d'un programme comme Gramps.

Ces vues sont des courts rapports textuels que l'utilisateur peut enregistrer dans Gramps pour qu'ils apparaissent dans les menus contextuels. Pour ce faire, des [API](https://fr.wikipedia.org/wiki/Interface_de_programmation) pour un [accès simple à la base de données](wiki:Simple_Access_API) et une [interface basique](wiki:Report_API) ont été construits afin de contourner au maximum la complexité.

Voir [Quick Views Coding page](wiki:Quick_Views) pour créer le vôtre.

{{-}}

[R](wiki:Category:Fr:Documentation)
