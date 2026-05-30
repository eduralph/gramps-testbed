---
title: Fr:Manuel wiki pour Gramps 6.0 - Fenêtre principale
categories:
- Fr:Documentation
managed: false
source: wiki-scrape
wiki_revid: 120659
wiki_fetched_at: '2026-05-30T18:39:44Z'
lang: fr
---

{{#vardefine:chapter\|3}} {{#vardefine:figure\|0}}

## Fenêtre principale

Quand vous ouvrez un arbre familial (existant ou nouveau), la fenêtre d'accueil s'affiche avec le [Tableau de bord](wiki:Gramps_6.0_Wiki_Manual_-_Categories/fr#Tableau_de_bord) dans la zone d'affichage et les barres latérale et inférieure sont cachées.En sélectionnant la [catégorie Individus dans le navigateur](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Catégories#Catégories_du_navigateur) à gauche, vous aurez une vue de la liste des personnes comme dans l'image suivante : ![[_media/Main-window-annotated-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} La fenêtre principale de Gramps]]

La fenêtre de Gramps contient les éléments suivants :

### Barre de menu

- Barre des menus : Elle est placée tout en haut de la fenêtre et donne accès à toutes les fonctions de Gramps.
- Elle est contextuelle : les options visibles dépendent de la catégorie.
- Cliquer sur l'en-tête d'un menu ouvre un sous-menu. Les items du sous-menu peuvent être grisés (non disponibles) s'ils ne sont pas utilisables avec la catégorie en cours.

[Typographie :](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Préface#Conventions_typographiques) la sélection dans les menus va ressembler à cela dans le manuel : .

#### Menus déroulant

![[_media/menu_gramplet-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Bouton de liste déroulante flèche vers le bas  sans texte]]En dehors de la barre des menus, l'existence d'un bouton de **menu déroulant** *flèche vers le bas* indique que des options supplémentaires sont disponibles pour l'interface de l'item .

#### Menus Pop-up

![[_media/Menucontextuel_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Copie d&#39;écran - avec un exemple de menu déroulant contextuel après click droit sur une famille]]L'option la moins visible de l'interface est probablement le **menu déroulant contextuel**.

Un clic droit sur un item de l'interface va révéler des raccourcis vers des fonctions fréquemment utiles pour cet item.

![[_media/Menucontextlibre-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fenêtre d&#39;un individu - avec un exemple de menu déroulant contextuel par un click droit sur un espace libre de l&#39;en-tête]]Faire un clic droit sur des objets est commun dans les interfaces graphiques. Mais faire un clic droit sur n'importe quelle zone vide de l'en-tête de n'importe quel Éditeur d'objet est moins évident. Néanmoins, cela fait apparaître une autre menu déroulant contextuel avec d'autres raccourcis utiles vers des options de navigation ou de présentation.

### Barre d'outils

- Elle est placée juste sous la barre de menu. Elle donne accès aux fonctions les plus utilisées de Gramps.
- Les outils visibles dépendent de la catégorie active.
- ⚙ Options configurables : la plupart des affichages des Catégories ont un bouton ![[_media/Gramps-config.png]] comme alternative au menu , ou au [raccourci clavier](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Raccourcis_clavier#Vues) pour *Configurer l'affichage actuel*. Cette option ouvre une boite de dialogue avec divers choix de présentation des enregistrements pour l'affichage actuel.
- Le survol d'un outil avec la souris affiche sa fonction.
- La barre d'outils peut-être cachée ou affichée par l'option du menu .

.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Options de l'onglet Thème dans la boite de dialogue Préférences.\]\]}}

### Navigateur

- Le navigateur est une barre latérale optionnelle située sur la gauche de la fenêtre et permet de choisir les différentes catégories d'affichage. Voir [Catégories du navigateur](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Catégories#Catégories_du_navigateur).

Le navigateur est affiché par défaut mais il peut être masqué ou affiché par le menu ou le raccourci clavier . ( sur MacOS).

Voir aussi :

- [Changer de mode de navigation](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Fenêtre_principale#Changer_de_mode_de_navigation)
- Vous pouvez cacher les textes des boutons en décochant ☑ dans l'onglet du menu [Affichage](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Affichage).

### Zone d'affichage

Le plus grand espace dans la fenêtre de Gramps est la zone d'affichage. Ce qui est affiché dépend de la catégorie sélectionnée.

### Barre de progression et barre d'état

Elles se trouvent tout en bas de la fenêtre principale de Gramps.

- La barre de progression est au coin inférieur gauche de la fenêtre Gramps. Elle montre l'avancement des opérations longues comme le chargement ou l'écriture de grosses bases de données génalogiques, l'importation ou l'exportation d'autres formats ou la génération de sites web, etc. Quand vous ne réalisez pas ce types d'opérations, la barre de progression n'est pas affichée.

<!-- -->

- La barre d'état est placée à droite de la barre de progression. Elle informe sur le travail en cours avec Gramps et affiche une information contextuelle sur les éléments sélectionnés.

<!-- -->

- La barre d'état peut occasionnellement afficher une [alerte](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference#Warnings) attirant l'attention sur une situation inhabituelle. Un bouton d'information avec un résumé au survol (comme ci-dessous) sera affiché pendant trois minutes à la gauche de la barre d'état. Cliquer sur cette icône 'ampoule' affichera des détails quant à ces alertes mineures.

![[_media/Boutonalerte-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fenêtre principale de Gramps montrant le bouton d'alerte dans la barre d'état]]

{{-}}

### Barres inférieure et latérale

La est aussi connue comme Barre inférieure et Barre latérale.

- La barre inférieure est située sous la zone d'affichage.
- La barre latérale est située à droite de la zone d'affichage.

Les barre inférieures et latérale peuvent être individuellement cachées ou affichées par les options du menu ou le raccourci clavier correspondant. Si la barre latérale n'est pas affichée, la est affichée à la place.

Les barres inférieure et latérale permettent d'afficher des [gramplets](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/fr) et les [filtres](#Filtres) en même temps qu'une vue particulière.

#### Menu Barre Gramplet

![[_media/menu_gramplet-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Localisation du menu Gramplets Ajouter/Enlever/Rétablir du bouton <em>Flèche vers le bas</em> (∨) sans texte de la <strong>Barre de menu Gramplet</strong>]]

Vous pouvez aussi ajouter / retirer et restaurer les Gramplets en cliquant bouton (*Flèche vers le bas*) aussi connu comme le **Menu Barre Gramplet** en haut et à l'extrême droite de la barre de titre, puis utiliser une des options du menu déroulant soit :

- **Menu barre Gramplet**
  - \- Affiche une liste des Gramplets disponible pour l'utilisation dans cette **Barre Gramplet**

  - \- Affiche une liste des Gramplets actuellement affichés dans la **Barre Gramplet** et pouvant être enlevés.

  - \- Affiche la boite de dialogue , qui vous permet de restaurer la barre de Gramplet avec ses Gramplets par défaut.

{{-}}

##### Boite de dialogue Restaurer la barre par defaults ?

![[_media/Grampletretablir-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Boite de dialogue Rétablir les défauts ?]]

La boite de dialogue , permets de restaurer la Barre de Gramplet avec ses Gramplets par défaut. Cette action ne peut pas être annulée. Cliquer sur pour confirmer ou sur . {{-}}

##### Barre de recherche

![[_media/Searchbar-annotated-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fenêtre principale de Gramps montrant la barre de recherche]]

Si la barre latérale n'est pas affichée dans l'affichage d'une catégorie avec une liste, alors la s'affiche. Les options de recherche disponible dépendent de la catégorie sélectionnée. L'affichage d'une barre latérale rend la barre de recherche invisible. ![[_media/Filtrebarlat-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} barre latérale avec le Gramplet Filtre qui supplante la barre de recherche]] Une est disponible pour les affichages suivants et les champs de sélection pour les catégories suivantes : Individus, Familles, Évènements, Lieux, Sources, Citations, Dêpots, Média, Notes. '''Non disponible pour les catégories suivantes : Tableau de bord, Relations, Graphiques, Géographie. Taper des caractères dans la et cliquer sur le bouton va afficher seulement les lignes correspondantes au texte.

{{-}} Notez que différents ont aussi des barres de recherche :

- [Sélecteur de famille](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Catégories#Familles)

![[_media/Selecteurfamille-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sélecteur de famille - avec la barre de recherche]] {{-}}

## Changer de mode de navigation

![[_media/Navigator-mode-selection-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sélection du mode de Navigateur]]

Vous pouvez choisir le mode du navigateur dans la liste déroulante de la barre latérale :

- **Catégorie** (par défaut)
- Liste déroulante
- Extension

{{-}}

Mode navigateur **Catégorie** (par défaut)  

![[_media/Navigator-mode-selection-category-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Mode navigateur "Catégorie"]]

Une barre latérale pour permettre la sélection des catégories. {{-}}

Mode navigateur **Liste déroulante**  

![[_media/Navigator-mode-selection-drop-down-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Mode navigateur "Liste déroulante"]]

Sélection de catégories et du type d'affichage dans les listes déroulantes. {{-}}

Mode navigateur **Extension**  

![[_media/Navigator-mode-selection-expander-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Mode navigateur "Extension"]]

Sélection d'affichage dans la liste des extensions. {{-}} {{-}}

## Changer de catégorie

Gramps fournit différentes catégories standards. Ces catégories sont décrites dans la section [catégories](wiki:Gramps_6.0_Wiki_Manual_-_Catégories/fr#Catégories_du_navigateur).

La façon de changer la catégorie affichée dépend du mode du navigateur. Le plus souvent (pour la plupart des modes) vous pouvez sélectionner la catégorie que vous voulez en cliquant une icône du navigateur.

En outre, vous pouvez utiliser les raccourcis clavier [keyboard shortcuts](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#4) et ( et sur un Mac) conduit respectivement à la catégorie suivante ou précédente ou utilisez les raccourcis ( sur un Mac) qui ne sont valables que pour les 10 premières catégories (i.e. les catégories Dépôts/Média/Notes n'ont pas de raccourcis clavier.) Si vous avez désactivé le [navigateur](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Fenêtre_principale#Navigateur), ce sera le seul moyen de changer de catégorie (sauf si vous réactivez le navigateur). {{-}}

## Changer de vue

Une catégorie peut contenir différentes façons pour représenter les données, appellées vues. S'il y a plusieurs types de vues, vous pouvez passer de l'une à l'autre de façon interactive. La façon de passer de l'une à l'autre dépend de la catégorie. Les options de configuration de chaque vue sont contrôlées de façon indépendante. Dans les vues sous forme de feuille de données avec des rangs et des colonnes, les types de vues sont typiquement soit une liste hiérarchique soit une liste triable à un seul niveau. Les types de vue en feuille de données sont configurable avec [l'éditeur de colonne](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Éditeur_de_colonne) et ont des options de [tri](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Trier_les_colonnes). Dans certaines vues de catégories graphiques (comme Graphique et Géographie), il peut y avoir une grande diversité de type d'affichage.

![[_media/Navigator-mode-selection-expander-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Barre latérale Navigateur en mode Extension]]When there are multiple viewing modes, will be additional icon buttons on the toolbar to switch between those different viewing modes.

S'il existe plusieurs vues, vous pouvez basculer de l'une à l'autre depuis la barre d'outils car chaque vue a son propre bouton. Vous pouvez également utiliser le menu , ou le raccourci clavier du menu en appuyant sur les touches (Linux & Windows) ou (MacOS), où est l'ordre de la vue dans le menu de la catégorie. Les types de vue sont aussi sélectionnables à partir de la barre latérale Navigateur en mode Liste déroulante ou Extension. Le mode par défaut du Navigateur (Catégorie) n'a pas de sélecteur du type de vue. L'utilisation des modes Liste déroulante et Extension permet de voir les types de vues supplémentaires et leurs icônes.

{{-}}

## Filtres

![[_media/Side-filt_34_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Filtrage activé]]

Les bases de données généalogiques peuvent contenir des informations sur de nombreux individus, familles, lieux et objets. Comme les longues énumérations sont suceptibles d'être une longue liste difficile à traiter mentalement. Gramps vous propose deux moyens différents pour contrôler cette situation en vous permettant de filtrer une liste pour une gestion adaptée.

Ces méthodes sont **Rechercher** et **Filtrer**.

Rechercher cherchera le texte affiché dans une liste, alors que les filtres affichent les individus dont les données correspondent au critère du filtre.

Rechercher est une méthode simple mais rapide pour rechercher dans l'affichage des colonnes. Quand la barre latérale n'est **pas** affichée, la apparaît. Taper les caractères dans et cliquer sur le bouton affichera seulement les lignes où le texte est présent.

Alternativement, vous pouvez activer la . Quand la barre de filtre est affichée, la ne l'est plus. La barre de filtre vous permet de construire un ensemble de règles de filtrage interactives pouvant être appliquées à l'affichage. Le filtre est appliqué, basé sur les règles et les données, pas sur l'affichage à l'écran. Les filtres de la catégorie affichée peuvent aussi être conçus en cliquant sur 'Éditeur' dans le menu .

Plus de détails sur le fonctionnement des filtres se trouve au chapitre [Filtres](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Les_filtres).

Quand Gramps ouvre un arbre familial, aucun filtrage n'est actif. Dans la vue des individus, tout le monde est listé par défaut.

{{-}}

## Problème ou dysfonctionnement de l'interface

Si l'interface utilisateur (ce qu'il se passe à l'écran) se comporte différemment de la description de ce guide, vous pouvez avoir un problème d'installation ou de compatibilité.

Il est probable que ce problème a déjà été rencontré et qu'une solution a été identifiée.

Regardez les pages sur les [problèmes](wiki::Category:Troubleshooting) (en anglais).

Au cas où… la page [Comment je récupère mon arbre familial](wiki:Recover_corrupted_family_tree/fr) en français.

Si vous ne trouvez pas de solution dans ces pages, envoyez une description du problème à la communauté générale de Gramps par la [liste des utilisateurs](wiki:Contact#Mailing_lists). C'est l'endroit où nous nous aidons les uns les autres.

{{-}}

[M](wiki:Category:Fr:Documentation)
