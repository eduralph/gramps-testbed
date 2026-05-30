---
title: Fr:Manuel wiki pour Gramps 6.0 - Gramplets
categories:
- Fr:Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 121061
wiki_fetched_at: '2026-05-30T18:35:51Z'
lang: fr
---

{{#vardefine:chapter\|10}} {{#vardefine:figure\|0}}

Cette page détaille les fonctionnalités des Gramplets fournis avec Gramps.

# Qu'est-ce qu'un Gramplet ?

<span id="definition">

## Définition

![[_media/DashboardCategoryView-Default_gramplets-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tableau de bord des gramplets]]

Un Gramplet Gramps est une extension du programme Gramps principal qui, normalement, travaille de façon transparente comme le ferait une fonctionnalité intégrée. Ils apportent un aperçu supplémentaire des données de votre arbre avec : une vue qui change dynamiquement pendant la navigation dans l'arbre Gramps, ou une interactivité avec vos données généalogiques.

Les Gramplets sont des greffons (aussi appelés [widgets](http://fr.wikipedia.org/wiki/Widget_interactif), plugins, addons, composants auxilliaires) propres à Gramps, intégrés comme partis de Gramps et sont visibles dans la [vue Gramplets](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/fr#Gramplets) et les barres [inférieures et latérales](#Barres_lat.C3.A9rale_et_inf.C3.A9rieure). Ils permettent tout type de fonctionnalité utile pour les recherches.</span>

## Est-ce que tous les greffons, plugins sont des gramplets ?

La différence entre les gramplets, rapports, vues express et outils ?

Tous sont du type **greffon/plugin**. Mais les gramplets sont des sous-type de greffons qui sont orientés interface-utilisateur. Gramplets ajoute une **fonction** ou un **angle différent** pour la vue. Ils sont utilisés pour améliorer le processus de travail de la vue.

Les autres greffons ont tendance à interrompre le travail en cours pour faire une autre tâche. Ils tendent aussi à être utilisés de façon plus intermittente. Un greffon peut générer un instantané statique des données (même quand il s'agit d'un lien), ou peut être un moyen de faire des modifications en masse, ou procurer un système alternatif d'importation/exportation/sortie.

Des types de greffons usuels sont :

- Les rapports : fournissent un format statique de vos données, surtout pour l'impression
- Les rapports express : fournissent un aperçu partiel, une liste interactive de vos données
- Les outils : fournissent une méthode pour travailler sur vos données
- Les Gramplets : fournissent une vue dynamique et interactive de vos données

Une compréhension plus approfondie des différents types de greffons peut être acquise en triant la [liste de greffons](wiki:6.0_Addons#Addon_List) par **Type** et en explorant les **Descriptions**.

Certains types de greffon les plus statiques peuvent être étendus pour travailler dynamiquement en tant que Gramplet.

Plusieurs greffons ont évolué en de multiples types. Certains greffons sont des shells avec une couche de fonctionnalités supplémentaires autour d'autres greffons. Le Gramplet **Rapport Express** n'est pas du type greffon [Rapport Express](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Quick_Views). C'est plutôt un shell ancrable qui montre un greffon **Rapport Express** et pousse le greffon à se rafraîchir quand le contexte change.

## Démarrer avec les Gramplets

Quand vous commencer par la Catégorie Tableau de nord, vous voyez deux Gramplets par défaut : le Gramplet et le Gramplet . {{-}}

Depuis que Gramps 4.2 a étendu certaines fonctionnalités du Tableau de bord à d'autres catégories du navigateur, nous avons des Gramplets **communs** et **specifiques**.

- Les Gramplets communs sont utilisables pour n'importe quelle vue… et l'orientation des données est fonction du contexte de la personne active et/ou de la personne souche. Ils peuvent être ancrés dans n'importe quelle vue des catégories du navigateur sans créer d'ambiguité dans la vue.
- Les Gramplets spécifiques nécessite le contexte d'une vue particulière pour donner du contexte à leur approche des données. La liste du menu d'ajout de Gramplets change selon la vue de Catégorie et les Gramplets installés.

## Utilisation et configuration des Gramplets

![[_media/Bienvenue_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Le Gramplet Bienvenue dans le Tableau de bord]] Le conteneur des boutons de contrôle des Gramplets est organisé un peu différemment dans la Catégorie Tableau de bord, par rapport aux barres latérale et inférieure. Être conscient de ces différences (ou similitudes) vous permettra de rester concentré sur vos performances plutôt que de vous demander pourquoi c'est ingérable !

Ajouté à partir de la version 3, les Gramplets de la vue de la Catégorie Tableau de bord sont organisés en un nombre configurable de colonnes. Les [panneaux séparés](wiki:Split_Views) des barres latérale et inférieure ont été sélectionnés parmi les innovations plus tardives proposés dans la [GEPS 19](wiki:GEPS_019:_Improved_Sidebar_and_Split_Views). Elles ont été conçues à partir de la barre latérale Filtre de la version 3.3. Le filtre a été converti en Gramplet et **pré-ancré dans la barre latérale**. {{-}} ![[_media/Bienvenue_detache_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vue détachée du Gramplet]]

Les panneaux séparés procurent un espace limité pour ancrer des Gamplets dans les autres Catégories du Navigateur. Et, à la différence des différentes colonnes de la vue Tableau de bord, chaque nouveau panneau séparé n'a qu'une colonne contenant un seul Gramplet. (Le panneau prend toujours en charge plusieurs Gramplets, mais utilise les onglets pour en afficher un seul à la fois.)

L'approche par panneau séparé diminue la nécessité de permuter entre les vues des Catégories… et ceci allège les requêtes à la base de données.

Néanmoins, les Gramplets peuvent être détachés (dé-ancrés, libérés) pour flotter librement à partir de n'importe quel des trois conteneurs. Quand il sont détachés, un bouton supplémentaire à la partie inférieure gauche ouvrira la page de Gramplet sur ce site. Cliquer sur le bouton au coin supérieur droit va ré-ancrer un Gramplet détaché. Cliquer sur le même bouton d'un Gramplet ancré va le supprimer du panneau. {{-}}

### La catégorie Tableau de bord

![[_media/Gramplet_detache_tdb_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vue détachée sur Tableau de bord]] Dans la catégorie [Tableau de bord](wiki:Gramps_6.0_Wiki_Manual_-_Categories/fr#Tableau_de_bord), vous pouvez glisser le bouton ⚙ (vers la gauche) dans chaque gramplet pour le repositionner dans l'aire du tableau de bord. Vous pouvez cliquer sur le bouton ⚙ pour détacher le gramplet depuis le Tableau de bord et le placer avec sa propre fenêtre. Cette fenêtre restera ouverte en tenant compte de la page (relationships, graphiques, etc). Fermer la vue détachée la ramènera à la vue Tableau de bord. Si vous quittez Gramps avec un Gramplet ouvert, quand vous redémarrer, il s'ouvre automatiquement.

Quand un ou plusieurs Gramplets sont détachés de la vue Tableau de bord, ils restent visibles pendant que vous changez pour une vue différente (les Individus ou les Graphiques, par exemple). De cette façon, vous pouvez utiliser des Gramplets pour compléter une vue particulière avec des détails supplémentaires et les fonctionnalités du Gramplet.

Vous pouvez ajouter de nouveaux gramplets par un clic droit sur un espace libre de la vue Tableau de bord. Cliquer le bouton au dessus du Gramplet pour le supprimer du Tableau de bord.

#### ⚙ Les options configurables

![[_media/Menu_config-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Le menu Affichage]] Vous pouvez aussi changer le nombre de colonnes en changeant les réglages de l'onglet *Mise en page Gramplet* dans la fenêtre *Configuration de la catégorie Tableau de bord*. Pour ouvrir la fenêtre, cliquer le bouton ![[_media/Gramps-config.png]], ou choisissez le menu , ou appuyer sur le [raccourci clavier](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Raccourcis_clavier#Raccourcis) *Configurer la vue active*. ![[_media/Config-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Onglets de configuration des Gramplets]] Chaque Gramplet ancré dans le Tableau de bord aura un onglet de configuration ajouté. (Mais le même Gramplet peut ne pas avoir d'options ou onglet de configuration quand il est ancré dans la barre latérale ou la barre inférieure.) Le Tableau de bord procure des options supplémentaires pour chaque Gramplet pour permettre de le renommer, fixer une dimension verticale fixe, ou maximiser la hauteur verticale dans sa colonne. L'onglet de configuration pour les Gramplets ancrés dans le Tableau de bord affiche au minimum ces options.

Un double-clic sur le titre d'un Gramplet ancré dans la Catégorie Tableau de bord permet d'en changer le titre affiché.

### Le panneau séparé des barres latérale & barre inférieure

![[_media/menu_gramplet-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Panneaux des Gramplets avec la barre de menu Gramplet et la flèche vers le bas  et son menu déroulant]] Chacun de ces panneaux séparés est un conteneur d'onglets de Gramplets juxtaposés. Comme des fenêtres avec des onglets, chacune ne peut afficher qu'un onglet à un moment t. Mais des onglets peuvent être ajoutés, ré-ordonnés, détachés ou désactivés de la même façon qu'avec le Tableau de bord. Néanmoins, à la place du menu contextuel, chaque dans les panneaux séparés a un bouton type *flèche vers le bas* pour afficher la même liste déroulante d'options.

Pour ajouter un Gramplet aux onglets juxtaposés, sélectionner le dans le sous-menu .

Pour détacher un onglet, cliquez sur le titre de l'onglet et tirer le en dehors du panneau séparé jusqu'en haut de la fenêtre Gramps. Pour le ré-ancrer, cliquez le bouton fermer ou le bouton 'X'.

Pour enlever le Gramplet des onglets juxtaposés, sélectionnez le dans le sous-menu (alternative : un bouton fermer sera visible si l'option 'Afficher le bouton de fermeture dans les onglets de la barre gramplet' a été sélectionnée dans les préférences).

Étonnament, les même Gramplets peuvent être en onglets dans les différents panneaux de la vue mais être configurés pour afficher les informations de façon différente. Il est important de se rappeler que chaque Gramplet (qu'il soit justaposé en onglet ou détaché et flottant) diminue les performances de Gramps. Utiliser moins de Gramplets rend Gramps plus réactif.

Les listes de Gramplets disponibles pour un ajout dans un panneau séparé sont filtrés pour ne laisser que ceux qui sont appropriés.

#### ⚙ Les options configurables

En complément, il y a de nombreux Gramplets développés par des tiers que vous pouvez facilement installer et utiliser. Ils comprennent :

- Nouvelles - les dernières nouvelles de Gramps
- Gramplet données saisies - permet de modifier le nom de la personne active, les dates et lieux de naissance, les date et lieux de décès et d'ajouter des individus
- Shell Python - un shell Python
- Gramplet Note - voir et modifier les notes de la personne active

et plein d'autres. Voir [<strong>greffons tiers</strong>](wiki:6.0_Addons) pour plus de détails.

{{-}}

## Liste des Gramplets disponibles

Cette section décrit 36 des Gramplets intégrés par défaut, leur catégories dans lesquels ils peuvent être utilisés.

Suivant les Catégories, les Gramplets peuvent être ajoutés ou supprimés :

- par le menu contextuel au clic droit pour la Catégorie Tableau de bord
- dans toutes les autres catégories, le menu déroulant dans la barre inférieure ou latérale

{{-}}

| Gramplet | ![[_media/22x22-gramps-gramplet.png]] Tableau de bord | ![[_media/22x22-gramps-person.png]] Individus | ![[_media/22x22-gramps-relation.png]] Relations | ![[_media/22x22-gramps-family.png]] Familles | ![[_media/22x22-gramps-pedigree.png]] Graphiques | ![[_media/22x22-gramps-event.png]] Évènements | ![[_media/22x22-gramps-place.png]] Lieux | ![[_media/22x22-gramps-geo.png]] Géographie | ![[_media/22x22-gramps-source.png]] Sources | ![[_media/22x22-gramps-citation.png]] Citations | ![[_media/22x22-gramps-repository.png]] Dépôts | ![[_media/22x22-gramps-media.png]] Media | ![[_media/22x22-gramps-notes.png]] Notes |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| id="31" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="2" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="20" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="3" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="4" \| |  | ✔ | ✔ | ✔ | ✔ | ✔ |  | ✔ | ✔ | ✔ |  | ✔ |  |
| id="33" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="5" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="7" \| |  | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |  | ✔ |  |
| id="9" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="10" \| |  | ✔ | ✔ |  | ✔ |  | ✔ | ✔ |  |  | ✔ |  |  |
| id="18a" \| |  |  |  |  |  |  | ✔ |  |  |  |  |  |  |
| id="18b" \| |  |  |  |  |  |  | ✔ |  |  |  |  |  |  |
| id="6" \| |  | ✔ | ✔ | ✔ | ✔ |  |  | ✔ |  |  |  |  |  |
| id="23" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="34" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="11" \| |  | ✔ | ✔ | ✔ | ✔ |  |  | ✔ |  |  |  |  |  |
| id="11a" \| |  | ✔ | ✔ | ✔ | ✔ |  |  | ✔ |  |  |  |  |  |
| id="12" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="14" \| |  |  | ✔ |  | ✔ |  |  |  |  |  |  |  |  |
| id="15" \| |  | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |  |
| id="17" \| |  |  |  |  |  |  |  |  |  |  |  | ✔ |  |
| id="27" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="21" \| |  |  |  |  |  |  |  |  |  |  |  | ✔ |  |
| id="30" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="19" \| |  | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |  |
| id="32" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="16" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="25" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="24" \| |  | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="26" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="0" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="13" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="8" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="28" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="29" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="1" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="35" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="22" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="xx" \| |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |

Pour des informations plus détaillées sur l'utilisation des Gramplets intallés, voire [Gramplets](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/fr). {{-}}

# Gramplets

## Âge à la date

![[_media/AgeOnDate-Detached_gramplet-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet Âge à la date]]

Ce gramplet vous permet de saisir une date dans le champ de saisie. Si vous cliquez sur le Gramplet calculera les âges de tous les individus de votre arbre familial à cette date. La date doit être entrée dans un format accepté par Gramps.

- Pas d'option de configuration pour ce Gramplet.

{{-}} ![[_media/AgeOnDate-QV_ResultExample-Detached_gramplet-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport express Âge à la date]]

Dans la fenêtre Rapport Express des résultats, vous pouvez trier sur les colonnes individu, âge et état. Un clic-droit sur un rang ouvre un menu contextuel qui permet de *copier tous* les rangs dans le presse-papiers, ou de *voir les détails de l'individu* dans une fenêtre de modification, ou d'en faire la personne active. {{-}}

- Vous pouvez aussi tirer une date du [Gramplet calendrier](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Gramplets#Calendrier) sur le champ de saisie du Gramplet pour saisir cette date.
- Voir aussi le [greffon tiers](wiki:Third-party_Addons) [Gramplet Date Calculator](wiki:Addon:DateCalculator) qui vous permet de faire des calculs de date.

{{-}}

## Âge statistiques

![[_media/Gramplet_agestat-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet Statistiques âge]]

Le gramplet Âge statistiques affiche des statistiques sous forme de trois graphiques textes avec des résultats regroupés par tranches de 5 ans (utiliser l’ascenseur pour faire défiler les graphes) :

- **Répartition de l'espérance de vie** - pour tous les individus ayant des dates de naissance et décès valides.
- **Père à l'âge de…** - affiche la différence d'âge entre l'enfant et le père quand les deux ont des dates de naissance valides.
- **Mère à l'âge de…** - affiche la différence d'âge entre l'enfant et la mère quand les deux ont des dates de naissance valides.

Le survol de chaque ligne avec la souris affichera le nombre d'individus correspondant à la plage de la ligne.

Un double-clic sur une ligne de n'importe quel graphe ouvre un rapport express listant les individus correspondant à la plage de cette ligne. Vous pouvez trier cette liste par nom, date de naissance ou type de nom.

Un clic-droit sur une ligne de la liste du rapport express affiche un menu contextuel pour copier toute la liste, ouvrir le dialogue de modification de l'individu ou définir cet individu comme la personne active.

{{-}}

#### ⚙ Options configurables

![[_media/Config_grampletagestat-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Options du gramplet]]

Les limites de l'échelle du graphique sont réglables dans l'onglet de configuration du Gramplet que vous pouvez ouvrir avec le bouton ![[_media/Gramps-config.png]] :

- Âge maximum 1-150 ; (*110 par défault*)
- Âge maximum de la mère à la naissance : 1-150 ; (*40 par défault*)
- Âge maximum du père à la naissance : 1-150 ; (*60 par défault*)
- Largeur du graphique : 1-150 ; (*60 default*)

{{-}}

## À faire

![[_media/ToDoList_sidebar-Detached_gramplet-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet À faire]]

Le gramplet À faire est une aire de texte libre. Vous pouvez l'utiliser pour y mettre quelques notes, remarques, pensées pour vos recherches. Il y a plusieurs programmes « To Do » (par exemple Tomboy) mais ce gramplet est utile car les informations restent dans Gramps.

Ce Gramplet vous permet de créer des notes et de les lier à des objets Gramps. Par exemple, vous pouvez ajouter un Gramplet « À faire » dans la barre latérale de la Catégorie Individus. Les notes ajoutées en utilisant ce Gramplet seront alors attachées à la personne active en cours. Il y a un Gramplet « À faire » pour chaque type d'objet primaire de Gramps.

Ce texte est persistant entre les sessions.

Voir aussi le [greffon tiers](wiki:Third-party_Addons) expérimental.

- Le Gramplet « À faire » disponible dans le Tableau de bord liste toutes les notes « À faire » de la base de données avec les objets auxquels elles sont liées.

{{-}}

### À faire Individus

{{-}}

### À faire Famille

{{-}}

### À faire Évènement

{{-}}

### À faire Lieux

{{-}}

### À faire Source

{{-}}

### À faire Citations

{{-}}

### À faire Dépôts

{{-}}

### À faire Media

{{-}}

## Arbre

![[_media/Pedigree-Detached_gramplet-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Image: Gramplet Arbre]]

Le gramplet Arbre affiche une vue compressée de l'individu actif et de ses ascendants directs. Par défaut il regarde sur 100 générations. Un clic sur un nom en fait la personne active, un clic-droit ouvre la fenêtre de modification de l'individu. Ce gramplet montre également en bas le nombre d'individus par génération. Cliquez deux fois sur la génération retournera les individus correspondants.

L'utilisation du contenu de la fenêtre dans un autre programme est un peu laborieuse. Ouvrez un menu contextuel par un clic-droit dans la fenêtre (sauf sur un lien) et choisissez Tout sélectionner, ou commencer à tracer une sélection en commençant dans une zone vide de la fenêtre. Copiez le texte sélectionné par le menu contextuel (le raccourci clavier 'copier' ne marche pas). Quand vous collez le texte dans une autre application de traitement de texte, vous pouvez changer pour une police non proportionnelle pour préserver l'indentation. Certains services en ligne réduisent les espaces en début de ligne quand vous publiez un fragment de texte. Préserver l'indentation pour ce type de service nécessite de remplacer les doubles espaces avec un double caractère qui occupe la place… comme ..

#### ⚙ Options de configuration

- Maximum de générations : 1 à 100 ; (*100*)
- Case à cocher Montrer les dates ; (*désélectionnée*)
- Type de ligne : <abbr title="Unicode Transformation Format graphical symbols">UTF</abbr>, <abbr title="American Standard Code for Information Interchange text symbols">ASCII</abbr>; (*UTF*)

{{-}}

## Ascendants

![[_media/Gramplet_ascendants_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet Ascendants]] Le Gramplet Ascendants affiche les ancêtre de la personne active. {{-}}

## Attributs

### Attributs Individus

![[_media/Attributes-Detached_gramplet-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet Attributs]] Ce Gramplet Attributs affiche tous les attributs pour la personne active. Ciquez deux fois sur le nom de l'attribut, et vous lancerez la affichant tous les individus porteur de cet attribut, ainsi que les valeurs s'y référant. Vous pouvez trier la d'après la valeur de l'attribut en cliquant sur le nom de la colonne. {{-}} ![[_media/Attributes-QV-Detached_gramplet-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vue Express Attributs]] Dans la Vue Express, sélectionnez l'entrée pour en faire la personne active (ce qui va actualiser le Gramplet Attributs) et double-cliquez l'entrée pour ouvrir la fenêtre de modification de l'individu. Vous pouvez aussi utiliser le menu contextuel. {{-}}

### Attributs Familles

{{-}}

### Attributs Évènements

{{-}}

### Attributs Sources

{{-}}

### Attributs Citations

{{-}}

### Attributs Media

{{-}}

## Bienvenue

![[_media/Bienvenue_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet Bienvenue]]

Le gramplet Bienvenue affiche un message de présentation aux nouveaux utilisateurs, et quelques instructions de départ.

Le message de bienvenue décrit ce qu'est Gramps, que le programme est libre (Open Source) et comment commencer un [arbre familial](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/fr).

Cette information est également disponible sur la [page principale de Gramps](wiki:Main_Page/fr) {{-}}

## Calendrier

![[_media/Calendar-Detached_gramplet-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Calendrier]]

Le Gramplet Calendrier affiche un calendrier mensuel. Un double-clic sur un jour lance le Rapport Express avec les évènements du jour.

Avec les boutons et de l'angle supérieur gauche (mois) vous pouvez changer pour le mois précédent et suivant.

Avec les boutons et de l'angle supérieur droit (année) vous pouvez changer pour l'année précédente et suivante.

La fenêtre de Rapport Express vous affiche les **Évènements** du jour sélectionné : évènements de cette date exacte et les autres évènements de ce mois/jour dans l'historique ainsi que les autres évènements de l'année.

L'information est présentée dans un tableau avec :

- La date
- Le type
- Le lieu
- La référence

Vous pouvez également tirer la date vers le champ date dans le Gramplet [Âge à la date](#Gramplet_.C3.82ge_.C3.A0_la_date) pour entrer cette date. {{-}}

## Citations

### Citations pour un individu

![[_media/Gramplet_citations_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet Citations pour un individu]] Gramplet affichant les citations pour la personne active avec 3 colonnes : Source/Citation avec un regroupement par Source, Auteur, Publieur. Un clic sur l'en-tête d'une colonne permet de les reclasser selon cet item.

Un double-clic sur une ligne de citation ouvre la fenêtre de modification de la citation. {{-}}

### Citations pour une famille

{{-}}

### Citations pour un évènement

{{-}}

### Citations pour un lieu

{{-}}

### Citations pour un media

{{-}}

## Code SoundEx

![[_media/Gramplet_soundex_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}Gramplet SoundEx]] Le Gramplet génère des codes SoundEx pour les noms des individus dans la base de données.

Dans la fenêtre du Gramplet SoundEx vous pouvez choisir un dans la liste déroulante en cliquant sur la flèche vers le bas (en forme de triangle) ou vous pouvez taper directement un nom dans le champ.

Le nom que vous tapez peut être n'importe quel nom… même un nom absent de votre arbre familial.

Le résultat apparaît automatiquement, par ex : le code SoundEx pour *Simpson* est *S512*. {{-}}

### SoundEx, qu'est ce que c'est ?

SoundEx est l'[algorithme phonétique](https://fr.wikipedia.org/wiki/Algorithme_phonétique) le plus largement reconnu pour indexer les mots par leur son comme ils se prononcent en **langue anglaise**. Ceci a donc un intérêt beaucoup plus limité pour des francophones puisque le résultat peut être incohérent avec notre prononciation.

Voir le chapitre homogue [SoundEx](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#SoundEx) en langue anglaise pour plus de détails.

Le soundex est un nom de famille codé basé sur les sonorités et l'orthographe proche. Les noms qui semblent les mêmes, mais qui s'écrivent autrement, comme SMITH et SMYTH qui auront le même code mais sont classés différement. Le système de codage soundex a été développé pour pouvoir trouver un nom de famille avec différentes orthographes.

Appliqué pour la première fois au recensement de 1880, le soundex est un index phonétique, pas seulement alphabétique. La fonction clé étant que les codes des noms sont plus basés sur les sonorités plutôt que sur l'écriture. C'était pour aider les chercheurs à trouver un nom rapidement malgré différentes orthographes.

- **Règle de base sur le codage Soundex :**

Chaque code soundex est composé d'une lettre et de trois chiffres, comme par exemple W-252. La lettre est toujours la première lettre du nom de famille. Les chiffres sont assignés en fonction des lettres restantes du nom de famille selon le guide soundex détaillé ci-après. Des zéros peuvent être assignés à la fin du code pour le compléter à trois chiffres dans le cas d'un nom de famille court. Les lettres supplémentaires du nom de famille sont ignorées. Exemple :

- Washington est codé W-252 (W, 2 pour le S, 5 pour le N, 2 pour le G, les lettres suivantes ne sont pas prises en compte).
- Lee est codé L-000 (L, 000 est ajouté pour compléter le code avec trois chiffres).

| Le chiffre | Représente les lettres |
|------------|------------------------|
| 1          | B, F, P, V             |
| 2          | C, G, J, K, Q, S, X, Z |
| 3          | D, T                   |
| 4          | L                      |
| 5          | M, N                   |
| 6          | R                      |

Ne pas faire attention aux lettres A, E, I, O, U, H, W, et Y.

- **Règles additionnelles sur le codage Soundex :**

<!-- -->

- - Les noms avec lettres doubles : si le nom de famille a deux lettres qui se suivent, ceci apparaîtra comme une lettre. Par exemple :

Gutierrez est codé G-362 (G, 3 pour le T, 6 pour le premier R, le second est ignoré, 2 pour le Z).

- - Les noms avec les lettres ayant le même numéro de code soundex que la précédente : si le nom de famille a différentes lettres ayant le même code soundex, alors une seule sera prise en compte d'après le guide de codage. Exemples :
    - Pfister est codé P-236 (P, F ignoré, 2 pour le S, 3 pour le T, 6 pour le R).
    - Jackson est codé J-250 (J, 2 pour le C, K est ignoré, S est ignoré, 5 pour le N, le zéro est ajouté).
    - Tymczak est codé T-522 (T, 5 pour le M, 2 pour le C, z est ignoré, 2 pour le K). Tant que la voyelle "A" sépare le Z et le K, alors le K est codé.

<!-- -->

- - Names with Prefixes: If a surname has a prefix, such as Van, Con, De, Di, La, or Le, code both with and without the prefix because the surname might be listed under either code. Note, however, that Mc and Mac are not considered prefixes.For example, VanDeusen might be coded two ways:V-532 (V, 5 for N, 3 for D, 2 for S) or D-250 (D, 2 for the S, 5 for the N, 0 added).

<!-- -->

- - Consonant Separators: If a vowel (A, E, I, O, U) separates two consonants that have the same soundex code, the consonant to the right of the vowel is coded. <Example:Tymczak> is coded as T-522 (T, 5 for the M, 2 for the C, Z ignored (see "Side-by-Side" rule above), 2 for the K). Since the vowel "A" separates the Z and K, the K is coded. If "H" or "W" separate two consonants that have the same soundex code, the consonant to the right of the vowel is not coded. Example: Ashcraft is coded A-261 (A, 2 for the S, C ignored, 6 for the R, 1 for the F). It is not coded A-226.

{{-}}

## Coordonnées des évènements

![[_media/Gramplet_coordonneesevnts_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet Coordonnées des évènements]] Ce Gramplet affiche les coordonnées des évènements de la personne active (ou de la famille sélectionnée selon la Catégorie avec laquelle vous travaillez). Un clic-droit sur une ligne ouvre un menu contextuel pour la modification du lieu ou de l'évènement. {{-}}

## Descendants

![[_media/Descendant-Detached_gramplet-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet Descendants]]

Le gramplet Descendants affiche les descendants directs de la personne active.

L'ordre des conjoints et enfants est défini dans l'éditeur. Pour changer l'ordre des conjoints, cliquez sur dans la vue . Pour changer l'ordre des enfants, un [*glisser-déposer*](http://fr.wikipedia.org/wiki/Glisser-d%C3%A9poser) permet de définir un ordre dans la fenêtre d'édition de la famille.

Ce gramplet est basé sur le [rapport de descendants](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Rapports#Liste_simplifiée_des_descendants), disponible dans les rapports textuels.

Le gramplet Descendant se mettra à jour quand vous changerez de personne active,ou changerez d'arbre familiaux. Il ne se met pas à jour automatiquement pour les éditions ou ajouts car les rapports prennent du temps pour fonctionner.

La minimisation d'un gramplet l'empêchera de se mettre à jour.

Passer la souris sur un individu affichera une info-bulle avec sa date de décès. {{-}}

## Détails

![[_media/Gramplet_details_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet Détails - exemple détaché]]

Gramplet affichant des détails sur la personne active.

Procure un bref résumé non modifiable de l'individu sélectionné, par exemple :

- *Nom*: de l'individu
- *alias :*
- *Autre nom :*
- *Père :*
- *Mère :*
- *Naissance :*
- *Décès :*
- *Inhumation :*
- *Image*: Si disponible, la première image sera affichée à côté les détails, sinon une croix indiquera une image manquante ; vous pouvez dlouble-cliquer l'image pour l'ouvrir dans un visionneur externe. Pour changer la première image active, voire : [Changer image galerie](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Ajouter_des_individus,_dates,_familles_et_relations#L&#39;image_préférée).

Vous pouvez sélectionner et copier individuellement les lignes de texte . {{-}}

## Enfants

![[_media/Gramplet_enfants_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet Enfants]] Le Gramplet Enfants affiche les enfants de la personne active.

Comment changer l'ordre des enfants ? Utilisez :

- L'onglet Enfants de la fenêtre de modification de la [famille](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Ajouter_des_individus,_dates,_familles_et_relations#Édition_de_l&#39;information_sur_les_relations) pour changer l'ordre des enfants dans la famille.
- Le greffon tiers [Birth Order Tool](wiki:Addon:BirthOrderTool) qui permet une mise à jour en masse de l'ordre des enfants.

{{-}}

### Enfants d'un individu

Affiche aussi les enfants des conjoints s'ils existent.

### Enfants d'une famille

## Enregistrements

![[_media/Records-Detached_gramplet-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet Enregistrements]]

Le Gramplet Enregistrements affiche un nombre de faits intéressants (la plupart sur l'âge) dans votre base de données. Cette liste fournit le podium des 3 premiers pour chaque élément.

- Enregistrements d'Individus
  - Individus vivants les plus jeunes
  - Individus vivants les plus âgés
  - Individus décédés les plus jeunes
  - Individus décédés à un âge avancé
  - Individus mariés jeunes
  - Individus mariés à un âge avancé
  - Individu divorcés jeunes
  - Individu divorcés à un âge avancé
  - Plus jeunes pères
  - Plus jeunes mères
  - Plus vieux pères
  - Plus vieilles mères
- Enregistrement Familles
  - Couples avec le plus d'enfants
  - Couples vivants mariés le plus récemment
  - Couples vivants mariés il y a le plus longtemps
  - Mariage les plus courts
  - Mariage les plus longs

{{-}} La liste n'est pas seulement intéressante en elle-même, elle est aussi un bon contrôle de la qualité de vos données. Pour certains items, vous aurez à compléter des informations.

L'exemple suivant montre qu'il y eu un évènement mariage mais aucun des individus n'avait de date de décès. Même si la date n'est pas connue, saisir seulement l'évènement décès pour un des conjoints et la liste sera corrigée.

**Couple vivant mariés il y a très longtemps**

1.  van Dosselaere, Egidius and Rechters, Petronella (382 ans, 1 mois)
2.  de Richter, Petrus and Asscericx, Catharina (379 ans, 9 mois)

{{-}}

Un [Rapport d'enregistrements](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Rapports#Rapport_d&#39;enregistrements) est aussi disponible.

## Et Maintenant ?

![[_media/WhatIsNext-Detached_gramplet-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet Et Maintenant ?]]

Le Gramplet Et Maintenant ? affiche une liste des premières informations manquantes dans votre arbre familial. Il est basé sur les hypothèses suivantes :

- Vous voulez connaître le nom et le prénom, la date et le lieu de naissance, et le lieu et la date de décès de chaque individu.
- Vous voulez connaître le père, la mère, la date et le lieu de mariage, et - en cas de divorce - le lieu et la date pour chaque famille avec des parents mariés.
- Vous voulez connaître au moins la mère d'une famille non marié.
- La relation la plus proche de la souche, l'information manquante la plus "urgente" à trouver.
- Plus l'individu souche et l'ancêtre commun sont proches, plus l'information est "urgente" (c-à-d les neveux sont considérés comme plus "urgents" que les oncles, même s'ils ont la même distance de 3 degrés, car pour les neveux, l'ascendant commun est nos parents, alors que pour les oncles, l'ascendant commun est nos grands-parents)
- Les données de mariage et informations personnelles sur le conjoint sont légèrement moins "urgentes" que les informations personnelles de parenté directe.
- Demi-frères et sœurs sont moins "urgents" que les frères et sœurs.

Vous pouvez copier le texte à l'intérieur de ce Gramplet en le sélectionnant et en le collant dans un document vierge. {{-}} ![[_media/config_etmaintenant_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}Onglet de configuration - Gramplet Et maintenant ?]] Le Gramplet peut ignorer des évènements antérieurement vérifiés en utilisant des étiquettes personnalisées. Les étiquettes sont sélectionnées dans la configuration des Gramplets. Par exemple, vous pouvez étiqueter pour les ignorer :

- qu'un individu est complet
- qu'une famille est complète
- qu'une personne ou une famille doivent être ignorés pour raccourcir la liste.

{{-}}

## Évènements

### Évènements des Individus

![[_media/Gramplet_evenement_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Individus - Gramplet Évènements]] Le Gramplet Évènements affiches les évènements pour la personne active.

Un double-clic sur une ligne permet de modifier cet évènement. {{-}}

### Évènements des Familles

## Filtre

Gramplet fournit un filtre spécifique pour chaque Catégorie. Le Gramplet filtre est affiché par défaut dans la barre latérale droite.

Voir également [Quel filtre dans la catégorie ?](wiki:Gramps_6.0_Wiki_Manual_-_Filters/fr) {{-}}

### Filtre Individus

![[_media/Gramplet_filtre_individu_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Individus - Gramplet Filtre - détaché - par défaut]] Complétez les champs par lesquels vous souhaitez restreindre la liste des individus affichée. Cliquez sur le bouton pour afficher les résultats dans la fenêtre principale.

Une case à cocher vous permet d'utiliser les [expressions rationnelles](https://fr.wikipedia.org/wiki/Expression_régulière) dans les paramètres. {{-}}

### Filtre Familles

![[_media/Gramplet_filtre_familles_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Familles - Gramplet Filtre - détaché - par défaut]] Complétez les champs par lesquels vous souhaitez restreindre la liste des familles affichée. Cliquez sur le bouton pour afficher les résultats dans la fenêtre principale.

Une case à cocher vous permet d'utiliser les [expressions rationnelles](https://fr.wikipedia.org/wiki/Expression_régulière) dans les paramètres. {{-}}

### Filtre Évènements

![[_media/Gramplet_filtre_evenements_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Évènements - Gramplet Filtre - détaché - par défaut]] Complétez les champs par lesquels vous souhaitez restreindre la liste des évènements affichée. Cliquez sur le bouton pour afficher les résultats dans la fenêtre principale.

Une case à cocher vous permet d'utiliser les [expressions rationnelles](https://fr.wikipedia.org/wiki/Expression_régulière) dans les paramètres. {{-}}

### Filtre Lieux

![[_media/Gramplet_filtre_lieux_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Lieux - Gramplet Filtre - détaché - par défaut]] Complétez les champs par lesquels vous souhaitez restreindre la liste des lieux affichée. Cliquez sur le bouton pour afficher les résultats dans la fenêtre principale.

Une case à cocher vous permet d'utiliser les [expressions rationnelles](https://fr.wikipedia.org/wiki/Expression_régulière) dans les paramètres. {{-}}

### Filtre Sources

![[_media/Gramplet_filtre_sources_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sources - Gramplet Filtre - détaché - par défaut]] Complétez les champs par lesquels vous souhaitez restreindre la liste des sources affichée. Cliquez sur le bouton pour afficher les résultats dans la fenêtre principale.

Une case à cocher vous permet d'utiliser les [expressions rationnelles](https://fr.wikipedia.org/wiki/Expression_régulière) dans les paramètres. {{-}}

### Filtre Citations

![[_media/Gramplet_filtre_citations_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Citations - Gramplet Filtre - détaché - par défaut]] Complétez les champs par lesquels vous souhaitez restreindre la liste des citations affichée. Ici, on peut filtrer sur des éléments de la citation ou sur des caractéristiques des sources correspondantes. Cliquez sur le bouton pour afficher les résultats dans la fenêtre principale.

Une case à cocher vous permet d'utiliser les [expressions rationnelles](https://fr.wikipedia.org/wiki/Expression_régulière) dans les paramètres. {{-}}

### Filtre Dépôts

![[_media/Gramplet_filtre_depots_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dépôts - Gramplet Filtre - détaché - par défaut]] Complétez les champs par lesquels vous souhaitez restreindre la liste des dépôts affichée. Cliquez sur le bouton pour afficher les résultats dans la fenêtre principale.

Une case à cocher vous permet d'utiliser les [expressions rationnelles](https://fr.wikipedia.org/wiki/Expression_régulière) dans les paramètres. {{-}}

### Filtre Media

![[_media/Gramplet_filtre_media_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Media - Gramplet Filtre - détaché - par défaut]] Complétez les champs par lesquels vous souhaitez restreindre la liste des media affichée. Cliquez sur le bouton pour afficher les résultats dans la fenêtre principale.

Une case à cocher vous permet d'utiliser les [expressions rationnelles](https://fr.wikipedia.org/wiki/Expression_régulière) dans les paramètres. {{-}}

### Filtre Notes

![[_media/Gramplet_filtre_notes_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Notes - Gramplet Filtre - détaché - par défaut]] Complétez les champs par lesquels vous souhaitez restreindre la liste des notes affichée. Cliquez sur le bouton pour afficher les résultats dans la fenêtre principale.

Une case à cocher vous permet d'utiliser les [expressions rationnelles](https://fr.wikipedia.org/wiki/Expression_régulière) dans les paramètres. {{-}}

## Foire aux questions

![[_media/Gramplet_faq_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet FAQ en 2021]] Le Gramplet Foire aux questions affiche une liste de questions fréquentes avec les liens vers leurs réponses dans le WiKi Gramps (connexion à Internet nécessaire). Cette liste est organisée manuellement en fonction des questions qui reviennent de façon répétée dans la mailing-list des utilisateurs Gramps.

L'idée est de rendre les réponses plus accessibles avec l'objectif principal de faciliter le démarrage des nouveaux utilisateurs de Gramps.

### voir aussi

- Rapport de bogue : les liens de la FAQ du tableau de bord sont obsolètes (résolu)
- Rapport de bogue : comment ajouter/mettre à jours les FAQs

{{-}}

## Graphique en roue

### Roue des ascendants

![[_media/FanChart-Detached-gramplet-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet Roue des ascendants]]

Le gramplet Roue des ascendants affiche les ascendants directs de la personne active dans un format circulaire. Ceci est similaire à la [vue Arbre généalogique](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/fr#Arbre_généalogique), mais depuis un individu central, la personne active, et plusieurs générations tout autour.

Cliquez sur un parent dans le graphique et il sera développé ou contracté au-dessus de l'enfant. Avec un clic-droit de la souris sur un individu, vous pouvez:

- sélectionner cet individu pour qu'il devienne la personne active
- modifier l'individu ce qui permet, par la fenêtre de modification de l'individu, d'ajouter des enfants aux familles de l'individu
- sélectionner la personne active parmi les individus de la parenté
- ajouter des conjoints (familles) à l'individu
- copier dans le presse-papiers nom, date de naissance et de décès de l'individu

Cliquer dans une aire vide (sans individu) et tirer le curseur de la souris vous permet de faire tourner le graphique autour de son centre.

Une bordure noire à l'extérieur du graphique indique qu'il y a des parents pour cet individu. Un cercle noir dans le centre indique que la personne active a des enfants.

Le Gramplet Roue des ascendants se met à jour quand vous changez de personne active, ou d'arbres familiaux.

Minimiser le Gramplet l'empêche de se mettre à jour.

Voir aussi [Vue graphique en roue](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Catégories#Vue_Roue_des_ascendants).

### Roue des descendants et Roue 2 sens

Le gramplet Roue des descendants et Roue deux sens utilisent la même logique. {{-}} ![[_media/Gramplet_rouedescendants_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet Roue des descendants]] ![[_media/Gramplet_roue2chemins_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet Roue des 2 chemins]] {{-}}

## Galerie

![[_media/Gramplet_galerie_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet galerie]] Ce Gramplet affiche un aperçu d'un objet media.

Par un clic-droit sur le media d'un personnage, on peut en faire la personne active. Un double-clic permet d'ouvrir une image dans un visualiseur externe. {{-}}

## Inclus

![[_media/Gramplet_inclus_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet Inclus]] Gramplet affichant les lieux qui sont inclus dans un autre. Ceci concerne la Catégorie Lieux. La liste obtenue dépend du niveau du lieu sélectionné dans la vue Lieux : si vous sélectionnez un département, vous verrez toutes les villes, communes qui ont été définies comme faisant partie de ce département. Si vous sélectionnez un pays, vous verrez de façon hiérarchique, les départements, communes, villes qui sont inclus dans ce pays.

Un double-clic sur la ligne d'un lieu ouvre la fenêtre de modification de ce lieu. {{-}} ![[_media/Lieu_modification_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet Inclus]] Pour que cet affichage soit cohérent, cela suppose que pour chaque lieu saisi, soit renseigné l'onglet 'Partie de' dans la fenêtre de modification du lieu.

Voir aussi le Gramplet [Partie de](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Gramplets#Partie_de). {{-}}

## Journal de session

![[_media/SessionLog-Detached_gramplet-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet Journal de session]]

Le journal de session conserve une trace de l'activité de votre session. Il liste les objets sélectionnés et modifiés.

Cliquez sur un nom pour faire de cette personne l'individu actif. Un double clic sur un nom ou une famille ouvre la fenêtre de de cet objet. De plus, si vous voulez modifier un individu mais ne voulez pas en faire la personne active, vous pouvez faire un clic-droit sur le nom de cet individu.

C'est très maniable car vous pouvez changer rapidement la personne active ou modifier un objet à partir de la liste de la session. {{-}}

## Métadonnées image

![[_media/ImageMetadata-Detached_gramplet-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Image Metadata Gramplet]] Le Gramplet Métadonnées image propose une interface pour voir les [données Exif](https://fr.wikipedia.org/wiki/Exchangeable_image_file_format) de vos images (\*.jpg, \*.png. \*.tiff, \*.exv, \*.nef, \*.psd, \*.pgf). {{-}} Voir aussi le greffon tiers :

- [Addon:Edit Image Exif Metadata](wiki:Addon:Edit_Image_Exif_Metadata)

### Prérequis

Une fois installé pyexiv2, voir plus bas les instructions pour télécharger et installer ce greffons.  
Pyexiv2 peut aussi être utilisé en ligne de commande (cli) et dans un script Python :  

1.  importer la bibliothèque pyexiv2
      
    de pyexiv2 importer ImageMetadata, ExifTag
2.  indiquer votre image
      
    image = ImageMetadata("/home/utilisateur/image.jpg")
3.  lire l'image
      
    image.read()

Les référence pour les étiquettes de métadonnées Exif, IPTC, XMP peuvent être trouvées [ici](http://www.exiv2.org/metadata.html).  
Exemple :

<hr>

image\["Exif.Image.Artist"\] \# Artiste  
Smith and Johnson's Photography Studio  
image\["Exif.Image.DateTime"\] \# Date et Heure  
1826 Apr 12 14:00:00  
image\["Exif.Image.DateTime"\] = datetime.datetime.now() \# Ajouter date et heure  
image.write() \# écrire les métadonnées  

### Scénario d'usage

Le cheminement souhaitable pour utiliser ce greffon :

1.  installer pyexiv2  
2.  Installer ce greffon  
3.  Redémarrer Gramps  
4.  Cliquer Affichage dans la barre des menus et sélectionner Vue des média  
5.  Oubrez la barre latérale  
6.  Glisser la vue vide à droite jusqu'à la moitié de l'écran  
7.  Clic-droit sur le texte de l'onglet de la barre latérale et sélectionner 'Ajouter un Gramplet'  
8.  Selectionner le Gramplet Métadonnées Image  
9.  Selectionner une image de la vue des média à gauche  

### L'interface

#### Les champs de données

Photographer:

  
The name of the person or company taking the image

Select Date

  
Will bring up a calendar, and double-click on a date. The time will be filled in as the current time  

Date

  
The Date/ Time needs to be typed in as a very specific format:  

Year Mon Day Hour:Minutes:Seconds  

11826 Apr 12 14:06:00  

Copyright

  
Can be anything that you please... Ex: (C) 2010 Smith and Wesson  

Subject

  
Please enter keywords that describe the picture. Do NOT add a space after the comma. Ex. : Census,Milwaukee,Oregon

Latitude/ Longitude

  
Latitude/ Longitude data can be entered in one of two ways:  
\# Degrees Minutes Seconds Ex.: 10 59 14

\#:In this format, you will need to select latitude reference, and longitude reference  
\#:If the Latitude begins with a negative number, select 'S' as Lat. Ref. or 'N' if a positive number. If the Longitude begins with a negative number, select 'W' as the Long. Ref. or 'E' if a positive number.

1.  Decimal, Ex. : -36.05954
      
    In this format, the Latitude and Longitude reference will be selected for you after you click Convert GPS Coordinates or press the Save button. For foreign countries that might use a ", " instead of a ".", please use the "."

Description

  
Type in something about the image, the people in it or the location of the image. Non-latin characters are NOT allowed. ASCII characters only...

#### Boutons

1.  Save  
    :Will write the metadata to the image, and convert latitude/ longitude if it is in decimal format.
2.  Clear  
    :Will clear all data fields
3.  Convert GPS Coordinates  
    :will convert Latitude/ Longitude if it is in decimal format

My favorite source for GPS Coordinates is: [GPS Visualizer](http://www.gpsvisualizer.com/geocode) {{-}}

## Notes

### Notes pour un individu

![[_media/Gramplet_notes_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet Notes]] Le Gramplet Notes affiche les notes de la personne active. S'il y a plusieurs notes pour l'individu, en haut de la fenêtre, sur la gauche, 2 flèches \< \> permettent de faire défiler les notes. Un clic-droit permet d'activer la vérification orthographique (si disponible), de sélectionner tout le texte ou de faire une recherche sur Internet à partir d'une sélection.

Voir aussi :

- [Gramplet Note](wiki:Addon:NoteGramplet) - Greffon tiers qui permet de modifier les notes.

{{-}}

### Notes pour une Famille

### Notes pour un Évènement

### Notes pour une Citation

### Notes pour un Lieu

### Notes pour une Source

### Notes pour un Dépôt

### Notes pour un Media

## Nuage de noms de famille

![[_media/SurnameCloud-Detached_gramplet-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet Nuage de noms]]

Le Gramplet Nuage de noms de famille affiche le top 100 (par défaut) des noms de famille utilisés. La taille de la police de caractères des noms est proportionnelle à la quantité d'individus porteurs de ce nom.

Cliquer deux fois sur le nom va lancer le . Ceci ouvre une fenêtre , laquelle indique les individus qui correspondent ou porteurs de ce nom alternatif. L'individu, sa date de naissance et le type de nom donné apparaîtront.

Si votre souris est au-dessus du nom, vous verrez le pourcentage et le nombre rencontré. {{-}} ![[_media/Config_nuagenom_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Configuration Gramplet Nuage de noms]] Changez le nombre de noms affichés par l'onglet de configuration du Gramplet, accessible notamment pas le bouton ![[_media/Gramps-config.png]] . {{-}}

## Nuage de prénoms

![[_media/GivenNameCloud-Detached_gramplet-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet Nuage de prénoms]]

Comme le gramplet [Nuage de noms](#Gramplet_Nuage_de_noms), le gramplet Nuage de prénoms affiche les prénoms les plus populaires de votre arbre familial. La taille du prénom indique sa fréquence. Placez la souris au-dessus du prénom pour connaître la valeur de cette fréquence, ainsi que le pourcentage d'individus porteur de ce prénom dans votre arbre familial.

Le gramplet sépare les prénoms dans des mots (séparés par des espaces). Par exemple "Sarah Elizabeth" apparaîtra comme "Sarah" et "Elizabeth".

Cliquez deux fois de suite sur le prénom pour appeler la pour afficher les individus correspondants. {{-}}

## Parenté

![[_media/Relatives-Detached-gramplet-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet Parenté]]

Ce gramplet affiche la parenté directe de l'individu actif. Son intension est d'aider à la navigation, une méthode alternative pour se déplacer dans la base de données GRAMPS. Si vous détachez le Gramplet, et le placez à côté de GRAMPS, il vous permettra de changer facilement le contenu de la [vue Individus](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/fr#Individus) en cours.

Si vous travaillez avec un arbre de la [vue Graphiques](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/fr#Lignée), l'individu actif est le plus à gauche. En cliquant sur un nom dans le gramplet Parenté, vous changerez facilement cet individu actif et toutes les personnes affichées dans la fenêtre du Gramplet seront mises à jour. Comme le Gramplet Parenté montre tous les conjoints, tous les enfants et tous les parents, il offre une méthode alternative pour naviguer dans vos données.

Les noms affichés dans ce Gramplet permettent également d'appeler la fenêtre de modification de l'individu directement par un clic-droit sur un de ces noms.

Le Gramplet Parenté peut être ajouté aux Catégories suivantes :

- Individus
- Relations
- Graphiques
- Lieux (certaines vues seulement)

{{-}}

## Partie de

![[_media/Gramplet_partiede_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet 'Partie de' pour une ville américaine.]]

Le Gramplet 'Partie de' affiche les lieux dans lesquels le lieu sélectionné est inclus. Exemple : une ville fait partie d'une commune, qui fait partie d'un département, qui fait partie d'un pays.

Un double-clic sur la ligne d'un lieu ouvre la fenêtre de modification de ce lieu.

Comme pour le Gramplet [Inclus](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Gramplets#Inclus), cela suppose que l'onglet 'Partie de' de la fenêtre de modification des lieux ait bien été renseignée. {{-}}

## Principaux noms de famille

![[_media/TopSurnames-Detached_gramplet-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Principaux noms de famille]]

Le Gramplet Principaux noms de famille montre les 10 (par défaut) noms de famille les plus utilisés de la base de données.

Les principaux noms sont présentés comme suit :

- Nom de famille
- pourcentage
- le nombre

Cette liste affiche également le total de noms de famille uniques dans la base de données ainsi que le nombre d'individus de la base de données. {{-}} ![[_media/Rapportexpress_nomfamille_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport express résultats]]

Cliquer deux fois sur le nom va lancer le Rapport express . Il répertorie les individus avec ce nom de famille. La fenêtre comprend un tableau avec les individus correspondant à ce nom ou ce nom alternatif. On peut voir le nom de l'individu et son numéro d'identification, sa date de naissance et le type de nom. {{-}}

Configuration avancée :

- Changez le nombre de noms affiché en modifiant cette section dans ~/.gramps/gramplets.ini

{{-}}

## Résidence

![[_media/Gramplet_residence_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet Résidence]] Gramplet qui affiche les évènements Résidence pour la personne active. Un double-clic sur la ligne permet d'ouvrir la fenêtre de modification de cet évènement. {{-}}

## Statistiques

![[_media/Statistics-Detached_gramplet-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet Statistiques]]

Le gramplet Statistiques lance le rapport Statistiques. Cliquer deux-fois sur les lignes vous retournera les informations correspondantes.

Les informations suivantes sont dans ce gramplet :

- Individus
  - Nombre d'individus
  - Hommes
  - Femmes
  - Individus sans genre connu
  - Individus avec un nom incomplet
  - Individus sans date de naissance
  - Individus déconnectés
- Familles
  - Nombre de famille
  - Noms de famile uniques
- Objets media
  - Individus avec un objet medium
  - Nombre total d'objet medium
  - Nombre d'objet medium unique
  - Taille des objets media
  - Objets media manquants

Les informations données par ce gramplet sont les mêmes que le rapport [Résumé de la base de données](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Rapports#Résumé_de_la_base_de_données). {{-}}

## Uncollected Objects

![[_media/UncollectedObjects-Gramplet-detached-example-60.png|Fig {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Uncollected Objects Gramplet - detached example]]

Le Gramplet a pour objectif de faire la liste des objets Python de bas-niveau qui reste en mémoire et ne peuvent pas être (facilement) supprimés alors qu'ils ne sont plus utilisés. Les développeurs l'utilisent pour essayer d'identifier les causes des 'fuites' de mémoire qui font que Gramps utilise de plus en plus de mémoire à mesure que vous l'utilisez.

Comme l'outil essaie d'afficher des objets qui devraient avoir été supprimés, il a parfois quelques problèmes. {{-}}

## Vue Express

![[_media/QuickView-RelationToHomePersonQV-detached-gramplet-40.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet Vue Express]]

Le gramplet Vue Express vous permet d'utiliser des rapports express, en mettant à jour les données quand vous vous déplacez de personne à personne. (Quand le Gramplet a été créé, il ne prenait en charge les rapports express que pour la Catégorie Individus. Désormais les autres catégories sont prises en charge).

Vous pouvez utiliser n'importe lequel des [rapports express](wiki:Quick_Views) de l'individu. {{-}}

#### ⚙ Options de configuration

![[_media/Config_grampletrapportexpress_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet Vue Express]] Pour chaque type de Catégorie, vous pouvez définir le contenu du rapport express dans l'onglet des options de configuration du Gramplet que vous pouvez ouvrir avec le bouton ![[_media/Gramps-config.png]] . {{-}}

[M](wiki:Category:Fr:Documentation)
