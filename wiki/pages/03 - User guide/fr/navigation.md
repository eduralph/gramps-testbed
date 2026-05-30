---
title: Fr:Manuel wiki pour Gramps 6.0 - Navigation
categories:
- Fr:Documentation
managed: false
source: wiki-scrape
wiki_revid: 115869
wiki_fetched_at: '2026-05-30T18:37:28Z'
lang: fr
---

{{#vardefine:chapter\|8}} {{#vardefine:figure\|0}}

Tant qu'une base de données est ouverte, Gramps reste centré sur une personne désignée comme la [Personne Active](wiki:Gramps_Glossary/fr#active_person). Vous pouvez modifier ou voir les données de cette personne et de sa famille proche. La navigation dans la base de données consiste en fait à changer de personne active. Cette section décrit tous les moyens pour parcourir la base de données en utilisant l'interface utilisateur riche et pratique de Gramps. Toutes les méthodes produisent finalement le même résultat, mais le choix du meilleur outil à utiliser dépend de ce que vous faites.

## Utilisation de la catégorie Individus

La méthode la plus intuitive pour sélectionner l'individu actif est d'utiliser la [catégorie Individus](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/fr#Individus). Quand vous êtes dans ces vues, simplement sélectionnez le nom de la personne désirée depuis la liste en cliquant dessus. Cet individu devient alors actif. La barre de statut est mise à jour en tenant compte de ce changement de personne active.

Voir aussi :

[Modifier ou ajouter des individus](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Ajouter_des_individus,_dates,_familles_et_relations#L.27information_personnelle)

## Utilisation de la catégorie Relations

Quand vous êtes dans la [catégorie Relations](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/fr#Relations), vous pouvez facilement naviguer d'une personne à une autre dans la famille affichée comme suit :

Cliquer sur le nom souligné de la personne qui vous intéresse et cet individu devient le nouvel individu actif de la catégorie Relations.

Le nom de la personne active n'est pas souligné.

En plus de tout cela, Gramps propose de nombreux raccourcis-claviers pour la navigation. Lisez la documentation de référence de ces commandes dans [raccourcis clavier](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/fr).

## Utilisation de la catégorie Familles

Quand vous êtes dans la catégorie famille, vous pouvez aisément naviguer parmi les familles. La configuration de l'affichage permet de choisir les colonnes à afficher. Il est ensuite facile de classer ces familles selon le nom du père, de la mère, le type d'union… en cliquant sur l'en-tête de la colonne correspondante.

## Utilisation de la catégorie Graphiques

Gramps s'appuie beaucoup sur des écrans affichant des listes de relations. Cela suppose des liens entre vos enregistrements dans votre arbre généalogique. La **catégorie Graphiques** procure une alternative plus visuelle pour afficher ces relations. La position, la couleur, l'aspect des boites ainsi que les lignes qui les relient et les flèches peuvent mettre en évidence des liens complexes entre les individus. Les boites peuvent être simplement colorées, ou des arcs, des rubans ou d'autres formes.

La [catégorie Graphiques](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Catégories#Graphiques) permet également de vous déplacer à travers votre arbre familial. Le bénéfice de cette méthode étant que vous pouvez voir plus qu'une génération dans votre arbre. Par ailleurs, vous pouvez sauter directement d'un petit-fils à son grand-père sans passer par les générations intermédiaires.

Notez qu'après avoir changé de personne active dans les vues Graphiques, l'affichage est mis à jour en fonction de la nouvelle personne active. Dans les vues Graphiques, vous pouvez facilement naviguer entre les personnes affichées comme suit :

Pour définir une personne affichée comme étant la personne active, faire un clic-gauche sur la boîte correspondante. Un clic-droit sur une boite affiche un menu contextuel qui vous permet d'accéder à la modification de la personne de la boite mais aussi d'accéder aux conjoints, enfants, ou parents de chaque individu.

La navigation dans les graphiques dépend du type : vous pouvez soit tirer le graphique pour le déplacer vers la section qui vous intéresse, voit vous disposez de flèches qui vous permettent de vous déplacer dans les générations.

Par exemple, dans le graphique «arbre généalogique», pour naviguer vers un enfant de la personne active en cours (la racine à gauche de l'arbre), cliquez sur la flèche vers la gauche située à gauche de sa boîte. Si cette personne a plusieurs enfants, le bouton se développe en un menu déroulant proposant le choix entre les enfants. Pour déplacer le graphique d'une génération en arrière, cliquez sur le bouton correspondant à droite de l'arbre. Le bouton du haut fera suivre la lignée paternelle alors que le bouton du bas fera suivre la lignée maternelle.

Un clic droit sur ces boutons de navigation offre aussi un menu contextuel d'actions.

Il existe aussi d'autres fonctionnalités comme l'affichage «à la volée» d'information sur une relation en passant la souris sur un trait de relation ou l'ouverture d'une fenêtre de modification en double-cliquant sur un trait de relation pour une famille ou sur une boite pour un individu.

Certaines vues de cette catégorie sont décrite au chapitre [Catégories](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Catégories).

Les vues disponibles dans cette catégories peuvent être étendues par des greffons disponibles dans le gestionnaire de greffons, avec le type «vue Gramps». Certains greffons tiers ont fini par être «encastrées» (intégrées) à l'application principale. Pour les autres, la documentation est très aléatoire.

## Utilisation des Gramplets

![[_media/People_gramplets_sidebar-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Relatives gramplet into People View]]

Dans la barre latérale et la barre inférieure, vous pouvez ajouter des Gramplets pour accroitre vos options de navigation au delà d'une seule génération. Par exemple :

- le gramplet [Parenté](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Gramplets#Parenté)
- le gramplet [Descendants](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Gramplets#Descendants)
- le gramplet [Arbre](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Gramplets#Arbre)
- le gramplet [Roue_des_ascendants](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Gramplets#Roue)

Ces exemples vous offrent la possibilité à partir de la personne active, de naviguer dans les relations familiales… vers des parents proches, les ascendants, les descendants. D'autres Gramplets à venir devrait vous permettre de naviguer parmi les différents lieux géographiques, voire des corrélations [ADN](wiki:Addon:DNASegmentMapGramplet) et d'autres interconnexions à imaginer.

Les Gramplets faits de texte proposent des hyperliens pour naviguer tandis que les Gramplets graphiques utilisent plutôt les menus contextuels.

{{-}}

## Choisir le de Cujus, la souche

Un seul individu peut être sélectionné comme souche, de Cujus dans l'arbre généalogique. Une fois défini, aller à cet individu est l'affaire d'un seul clic dans n'importe quelle vue.

Pour choisir le «de Cujus», sélectionnez d'abord, par le moyen de votre choix, la personne voulue comme personne active. Faites . À partir de ce moment, vous pouvez retourner à cette personne simplement en cliquant sur l'icône dans la barre d'outils. Vous pouvez également choisir dans le menu ou choisir l'élément dans n'importe quel menu contextuel accessible par un clic droit de la souris, ou utiliser le raccourci clavier .

## Définir la personne active

La [personne active](wiki:Gramps_Glossary#active_person) est l'individu sur lequel seront centré les actions, rapports, modifications.

Dans la vue des Individus, la personne active est surlignée. Dans la vue Relations, la personne active est affichée en haut de la fenêtre, dans une section séparée. Tous les autres individus affichés en dessous ont une relation proche avec la personne active (conjoints, frères et sœurs, enfants, parents).

### Navigation par hyperlien

Habituellement, un clic sur le lien que constitue le nom d'une personne va faire que cette personne devienne la personne active. ![[_media/Vue_relation-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vue Relations]] Tous les noms de personnes dans la vue Individus ou Relations sont des hyperliens. Dans la vue Individus, la sélection d'une nouvelle personne active correspond simplement au nouvel individu surligné. Mais tous les Gramplets se mettent à jour selon cette nouvelle personne active et les vue Relations, Graphiques et Géographie seront aussi mises recentrées sur cette nouvelle personne active.

Sélectionner un nouveau nom (lien) dans la vue Relations a un effet plus visible : la représentation des données familiales est ré-arrangée selon cette nouvelle personne active ; les détails de la personne active sont affichés dans le haut de la fenêtre tandis que les autres individus ayant une relation avec la nouvelle personne active sont affichés en dessous.

{{-}}

### Navigation par menu contextuel

Néanmoins, un double-clic sur les noms de personnes dans les onglets Références et Notes (barre inférieure et dans certains Gramplets) vont seulement ouvrir la fenêtre de modification de cet individu **sans** qu'il devienne la nouvelle personne active. Ceci facilite la modification des informations d'une personne autour de la personne active sans perturber la navigation en changeant la personne ayant le focus. ![[_media/Menu_context_individu-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu contextuel de la modification d&#39;une personne]] Dans ce contexte, si vous voulez réellement faire de cette nouvelle personne la personne active, il suffit, dans la fenêtre de modification de cette personne, de faire un clic-doit sur son nom pour afficher un menu contextuel et sélectionner «Faire personne active» (Make active person).

{{-}}

### Utilisation de l'historique

![[_media/Historique-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Exemple d&#39;outil de navigation dans l&#39;historique]] Gramps dispose aussi d'un ensemble puissant d'outils reposant sur l'historique de navigation. Ces outils ressemblent à ceux des navigateur sur le Web. Ceci comprend les items et disponibles dans le menu **Aller à**, les menus contextuels et les boutons de la barre d'outils. Il y a aussi la liste des sélections récentes accessible par le menu **Aller à** qui vous permet d'aller directement vers n'importe quel item sélectionné récemment. Enfin, un clic droit de la souris sur les boutons et de la barre d'outils affiche un menu déroulant avec une partie de l'historique correspondante. Sélectionnez un item pour aller directement à lui. {{-}}

### Navigation par signets

![[_media/Gramps_Go-Home48x48_win.png]] Le bouton de la barre d'outils est un lien particulier. Il permet de faire de lapersonne souche (De Cujus) la personne active. Ceci est très fréquemment utile si bien qu'il est lié à un raccourci clavier .

![[_media/Orgbookmarks-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Organiser vos signets]] Similaire à l'action de définir la souche, vous pouvez marquer d'autres individus dans la base de données pour une navigation simplifiée. Pour marquer un individu, tout d'abord allez sur cet individu, puis choisissez . Pour aller vers cette personne n'importe quand, choisissez . Les autres catégories ont leur propre liste de signets.

Vous pouvez gérer vos signets en choisissant ou par le raccourci clavier . Ceci lance la fenêtre de avec la liste des signets et les contrôles pour modifier la liste.

Utilisez les boutons et pour changer la séquence de la liste. Utilisez le bouton pour supprimer le signet. L' vous conduit vers cette page, et vous pouvez fermer la fenêtre avec le bouton .

Les individus marqués peuvent être sélectionnés dans la catégorie individus, comme expliqué plus haut, mais sont partagés avec les catégories Relations, Graphiques.

Sur les mêmes bases vous pouvez également créer des signets dans les catégories Familles, Événements, Sources, Citations, Media, Dépôts, et Notes.

### Les notes comme raccourcis de navigation

Il y a différentes listes de signets pour chaque catégorie. Mais ce ne sont que de simples listes. Les longues listes de signets deviennent rapidement lourdes.

Des liens permanents peuvent être créés dans les notes. L'éditeur de liens accessible dans la fenêtre de création des notes permet d'organiser vos liens vers différents types d'enregistrements dans Gramps selon votre méthode de travail. ![[_media/Fr_lien_dans_note_Ubuntu_Groovy.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Éditeur de lien des notes]] Pour créer un lien dans une note, vous devez **d'abord surligner** le texte de la note qui servira de lien puis cliquer sur le bouton . Dans l'éditeur de lien, choisissez le **type de lien** dans la liste. Ensuite, sur la même ligne, vous avez le choix entre créer un nouvel objet pour ce lien avec le bouton et rechercher un enregistrement existant par le bouton .

Une fois le lien défini dans la note, il peut être utilisé comme un signet. Naviguer vers l'enregistrement lié en cliquant sur le lien tout en maintenant la touche enfoncée. Une note peut servir d'index et pointer vers d'autres notes avec des listes de liens.

Un exemple de notes avec des liens pourrait concerner une inhumation avec des liens vers les individus présents, les lieux voire des évènements. Ceci permet de naviguer vers des individus qui ont des liens indirects voire une absence de liens (porteurs, personnes présentes, officiants…).

Une autre note pourrait être la transcription de la bibliographie publiée par un autre généalogiste. Au fur et à mesure que vous faites l'asquisition de ces sources, vous pouvez les lier dans votre note pour naviguer plus facilement vers elles.

{{-}}

## Trouver les enregistrements

![[_media/Find_people-42-fr.png|350 px\|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Rechercher une donnée]] Pour trouver un enregistrement dans la base de données, tout d'abord choisissez la vue désirée pour votre enregistrement : individus, sources, lieux, media, dépôts, notes. Puis commencez par saisir le nom ou le titre que vous recherchez. Vous pouvez également utiliser pour ouvrir le mode recherche, mais commencer par saisir avec le clavier doit être suffisant.

Les premières lettres que vous tapez sont recherchées.

Activez le contrôle de filtre par , sélectionnez le filtre désiré, et cliquez sur . Voir les [filtres](wiki:Gramps_6.0_Wiki_Manual_-_Filters/fr) pour plus de détails.

## Utiliser le presse-papiers

![[_media/Clipboard-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Presse-papiers]]

Cet outil fournit une note temporaire pour stocker des enregistrements de la base de données et les réutiliser plus rapidement.

Pour une application comme Gramps, le presse-papiers est très pratique et permet de réduire des saisies à répétition.

Pour faire appel au , utilisez le menu ou cliquez dans la barre d'outils sur le bouton ou le raccourci clavier .

On peut stocker des adresses, des attributs (personnel et famille), des événements (personnel et famille), des noms, les objets media, des références, des citations, des URLs, et naturellement l'information textuelle des notes et des commentaires. Pour stocker, glisser simplement le texte dans la boîte de dialogue. Pour réutiliser l'information, glisser-la sur la fenêtre de modification correspondante, par exemple onglet d'adresse, onglet d'attribut, etc...

<u>Un exemple</u> : vous trouvez l'acte de naissance d'un individu. Ce dernier mentionne également les témoins. Cet acte est une source pour ces informations. La meilleure solution est d'ouvrir le presse-papiers et de glisser la source. Puis d'utiliser la fonction [*glisser-déposer*](http://fr.wikipedia.org/wiki/Glisser-déposer) chaque fois que vous en avez besoin.

Puis vous finalisez les informations dans l' pour cette personne. Glissez aussi cette information vers le presse-papiers.

Enfin, vous ajoutez deux individus comme témoins (si ils ne sont pas déjà présents dans la base de données). Ensuite, un simple [*glisser-déposer*](http://fr.wikipedia.org/wiki/Glisser-déposer) de l'information sur la naissance depuis le presse-papiers vers les événements du témoin. Vous changez alors le rôle de l'individu en témoin de la naissance. Vous pouvez reproduire ce schéma pour d'autres témoins.

Ceci vous évite de longues saisies et erreurs possibles.

## Principaux menus

La barre des menus affiche les menus de Gramps. Le contenu des menus peut varier suivant la catégorie sélectionnée. Les menus disponibles sont plus réduits s'il n'y a pas d'arbre généalogique ouvert.

### 

![[_media/Menu_principal-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu "Arbres familiaux"]]

- \- ouvre la [fenêtre de gestion des arbres familiaux](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Gestion_des_arbres_familiaux#Family_Trees_manager_window)

- \- un accès rapide aux arbres récemment utilisés

- \- enregistre et ferme la généalogie en cours

<hr>

- \- Ajouter les données d'autres [formats](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Gestion_des_arbres_familiaux#Importation_des_données).  
  *Faire une sauvegarde avant une importation ! Il y a des [Préférences d'importation](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Général) permettant de marquer les données importés avec une étiquette ([Tag](wiki:Gramps_Glossary#tag)) et/ou la [Source](wiki:Gramps_Glossary#source). Ces options peuvent beaucoup ralentir le processus d'importation mais sont utiles pour ensuite pour faire le tri de vos données.*

- \- [Exportation des données](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Gestion_des_arbres_familiaux#Exportation_des_données) : cela vous permet de partager n'importe quelle partie de votre arbre familial Gramps avec d'autres chercheurs ainsi que le transfert de vos données vers un autre ordinateur.

<hr>

- \- Ce menu n’apparaît que dans certaines vues si les données affichées peuvent être exportées. Gramps va exporter les données à l'écran au format de tableur **CSV** ou **Open Document** selon votre choix.

<hr>

- \- Vous permet de faire une [sauvegarde complète au format XML Gramps](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Gestion_des_arbres_familiaux#Archiver_un_arbre_familial) de votre arbre généalogique ouvert. Notez que certains paramètres de [configuration et Media sont omis](wiki:Template:Backup_Omissions) dans les sauvegardes XML.

<hr>

- \-

- \-

{{-}}

### 

![[_media/Menu_ajouter-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu AJouter]]

- \- un nouvel [objet](wiki:Glossaire_Gramps#O)  
  Voir aussi les [raccourcis clavier](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Raccourcis_clavier).

<hr>

- \- ajoute un Individu *([Objet principal](wiki:Glossaire_Gramps#O))*

- \- ajoute une [Famille](wiki:Glossaire_Gramps#F) *([Objet principal](wiki:Glossaire_Gramps#O))* - Ouvre la

- \- ajoute un [Événement](wiki:Glossaire_Gramps#.C3.89) *([Objet principal](wiki:Glossaire_Gramps#O))*

- \- ajoute un [Lieu](wiki:Glossaire_Gramps#L) *([prim. obj.](wiki:Glossaire_Gramps#O))*

- \- ajoute une Source *([Objet principal](wiki:Glossaire_Gramps#O))*

- \- ajoute une Citation *([Objet principal](wiki:Glossaire_Gramps#O))*

- \- ajoute une Dépôt *([Objet principal](wiki:Glossaire_Gramps#O))*

- \- ajoute un Media *([Objet principal](wiki:Glossaire_Gramps#O))*

- \- ajoute une Note *([Objet principal](wiki:Glossaire_Gramps#O))*

<hr>

{{-}}

### 

![[_media/Menu_edition-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu Édition pour la Catégorie Individu]]

- \-

- \-

- \- Ouvre la fenêtre

<hr>

Des options de menu supplémentaires s'affichent ici selon la vue de Catégorie sélectionnée.

- \- Voir [les étiquettes](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Les_filtres#Les_étiquettes)

<hr>

- \- Le presse-papiers offre un calepin temporaire pour enregistrer des données et les réutiliser facilement durant la session en cours.

<hr>

- \- Affiche la fenêtre des . Elle vous permet d'ajuster les principaux réglages de Gramps.

- Des options supplémentaires s'affiche ici selon la vue de Catégorie sélectionnée.

{{-}}

### 

![[_media/Menu_affichage-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu Affichage pour la catégorie Relations]]

- \- Vous permet de configurer la vue actuelle. Propose des options pour cacher, afficher ou réorganiser des éléments.

- \- Le navigateur est la barre latérale qui contient les icônes de navigation parmi les Catégories. Quand elle est sélectionnée (par défaut), cette barre latérale s'affiche à gauche de la vue active. La délectionner cache le navigateur. Si toutes les icônes de catégorie ne peuvent pas entrer dans l'espace vertical disponible, un ascenceur caché va apparaître à la partie droite de la barre latérale et se révèle au passage de la souris.  
  Le texte des étiquettes liés aux icônes peuvent être cachés via une option dans l'onglet des [préférences d'affichage](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Affichage). [Le mode d'affichage](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Fenêtre_principale#Changer_de_mode_de_navigation) des catégories peut être choisi dans la liste déroulante au pied de la barre latérale du navigateur.

- \- Affiche (ou cache) un conteneur d'icônes d'actions (fréquemment utilisées) au dessus de la fenêtre principale de la Catégorie. La sélection d'icônes varie pour s'adapter à la Catégorie affichée.  
  Des [greffons tiers](wiki:Third-party_Addons) peuvent être installés pour ajouter des préférences avec un onglet qui propose une option pour afficher le texte des étiquettes pour chaque bouton de la barre d'outils.

- \- Affiche (ou cache) un conteneur d'écran partagé pour des Gramplets à la droite de la fenêtre principale de la Catégorie en cours.

- \- Affiche (ou cache) un conteneur d'écran partagé pour des Gramplets au pied de la fenêtre principale, juste au dessus de la barre d'état.

- \- Agrandit l'affichage pour utiliser tout l'espace d'écran disponible tout en désactivant les contrôles pour déplacer ou modifier la taille de la fenêtre. La désélection restore la taille précédente de la fenêtre et réactive la possibilité de déplacer et modifier la taille de la fenêtre.

<hr width = 75%>

- Selon la vue active, d'autres items de menu peuvent s'afficher ici et modifier l'organisation des donnéees pour la vue active.

{{-}}

### 

![[_media/Menu_aller_a-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menubar - Go Overview]]

- \- pour la vue actuelle, vous ramène à la sélection *précédente* de votre historique de navigation

- \- pour la vue actuelle, vous emmène à la sélection *suivante* de votre historique de navigation

<hr>

- \- Navigue pour que la [personne active](wiki:Gramps_Glossary#active_person) de la vue actuelle corresponde à la personne [souche](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#.C3.89tablir_la_souche).

<hr>

- Une liste dynamique des 10 enregistrements les plus récents sélectionnés (Individus, Familles, etc). La liste est dépendante de la vue de Catégorie affichée.

{{-}}

### 

![[_media/Menu_signets-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu Signets]]

- \- Crée un signet pour l'item actuellement sélectionné, c-à-d : Individu, Famille, etc.

- \- Ouvre la fenêtre Édition des signets.

<hr>

- Section dynamique où les signets s'affichent.

{{-}}

### 

![[_media/Menu_rapports-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu Rapports]]

- \- Le rapport [Livre](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_3#Books) vous permet de créer un livre de généalogie personnalisé contenant un ensemble de rapports textuels ou graphiques de Gramps en un seul document.

<hr>

- \-

  - 

  - 

  - 

- \-

  - 

  - 

  - **Arbre familial…**

  - 

  - 

  - 

  - 

  - 

- \-

  - 

  - 

  - 

  - 

  - 

  - 

  - 

  - 

  - 

  - 

  - 

  - 

  - 

  - 

  - 

- \-

  - 

  - **Rapport Web Dynamique…**

  - 

{{-}}

### <span id="Tools"></span>

![[_media/Menu_outils-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu Outils]]

- \-

  - 

  - \-

- \-

  - 

  - 

  - 

  - 

  - 

  - 

  - 

  - 

  - 

  - 

- \-

  - 

  - 

  - 

  - 

  - 

- - 

  - 

  - 

  - 

  - 

  - 

  - 

{{-}}

### 

![[_media/Menu_fenetre-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu Fenêtres - exemple]]

- \- Ce menu permet un accès rapide aux fenêtres ouvertes avec lesquels vous travaillez. Il n'apparaît que si plusieurs fenêtres sont ouvertes.

{{-}}

### 

![[_media/Menu_aide-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu Aide]]

- \- Lien direct vers ce manuel utilisateur en ligne que vous êtes en train de lire. Et oui, vous avez besoin d'une connexion Internet pour consulter le manuel utilisateur.

- \- Un lien vers la [FAQ](wiki:Gramps_6.0_Wiki_Manual_-_FAQ/fr) de Gramps.

- \- Un lien vers la page de référence des [raccourcis clavier](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Raccourcis_clavier) de Gramps.

- \- Affiche la boite de l'"astuce du jour".

- \- Par ce menu, vous pourrez gérer les greffons intégrés ainsi que les [greffons tiers](wiki:6.0_Addons) que vous avez installés.

<hr>

- \- Cet item ouvre votre navigateur Internet et affiche la page du projet Gramps.

- \- Cet item ouvre votre navigateur Internet à la page de la liste de diffusion de Gramps. Dans cette page, vous pouvez naviguer parmi les archives de la liste et rejoindre la liste de diffusion des utilisateurs de Gramps pour partager votre expérience avec les autres utilisateurs de l'application.

- \- Choisir cet item pour déposer un [rapport de bogue](wiki:Using_the_bug_tracker) dans le système de traçage de bogues de Gramps. (Ceci nécessite d'avoir un compte répertorié dans le système de rapport de bogue de Gramps) (Rappelez-vous que Gramps est un projet vivant. Nous voulons connaître tous les problèmes que vous rencontrez afin que nous puissions travailler à les résoudre, pour vous et le bénéfice de tout le monde.)

- \- Un lien vers la page des [greffons tiers](wiki:6.0_Addons).

<hr>

- \- Cet item affiche une boite avec des informations générales sur la version de Gramps que vous utilisez.

[Category:Fr:Documentation](wiki:Category:Fr:Documentation)
