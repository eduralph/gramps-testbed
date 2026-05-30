---
title: Fr:Manuel wiki pour Gramps 6.0 - Gestionnaire de greffons
categories:
- Fr:Documentation
managed: false
source: wiki-scrape
wiki_revid: 111333
wiki_fetched_at: '2026-05-30T18:46:55Z'
lang: fr
---

{{#vardefine:chapter\|9}} {{#vardefine:figure\|0}}

## Introduction au gestionnaire de greffons

Le gestionnaire de greffon est accessible depuis le menu . Plusieurs fonctionnalités du gestionnaire de greffons sont pour les développeurs, et les dialogues ci-dessous sont ceux utilisés par ces développeurs. Les fonctionnalités pour un usage normal seront précisées quand elles sont différentes.

Gramps détecte si il est lancé en mode utilisateur ou en mode développeur par l'utilisation ou non de l'argument 'optimiser':

- `python -O gramps.py`

Voir [Déboguer Gramps](wiki:Debugging_Gramps).

Gramps est constitué d'un noyau et de multiples greffons. Au démarrage, le noyau est chargé avec seulement un nombre limité de greffons.Ceci réduit le temps de démarrage de Gramps et la quantité de mémoire mobilisée. Ensuite, les greffons sont chargés seulement lorsque cela est nécessaire. Nombre d'utilisateurs n'ont pas le souci des greffons fonctionnels ou de leur chargement secondaire.

Le gestionnaire de greffons vous permet de contrôler les greffons.

## Types de greffon

Il existe deux catégories principales de greffons dans Gramps : les "*plugins/greffons utilisateur*" et les "*plugins/greffons système*". Les greffons utilisateur sont ceux que vous utilisez et contrôlez pour obtenir différentes fonctions nouvelles. Les greffons système sont utilisés par Gramps.

Les types suivants de **greffons utilisateur** sont présents dans Gramps :

1.  Les vues gramps : les vues visibles dans la fenêtre principale de Gramps.
2.  Les gramplets : de petits programmes que vous pouvez inclure dans la vue Gramplets, ou détacher et utiliser comme une fenêtre normale.
3.  Les rapports : des rapports textuels ou graphiques générés par Gramps.
4.  Des rapports express : de petits rapports disponibles dans le menu contextuel dans les vues en liste, ou via le gramplet RapportExpress.
5.  Les outils: ils sont disponibles via le menu .
6.  Les créateurs de document : des supports permettant à Gramps d'écrire les rapports (pdf, odf, texte ascii, ...).
7.  Les exportateurs : formats d'exportation disponibles via .
8.  Les importateurs : formats d'importation disponibles via .
9.  Les services cartographiques : cibles pouvant être utilisées dans la vue Lieux pour utiliser un service cartographique sur internet (le bouton *Allez à* de la barre d'outils).

Les types suivants de **greffons système** sont présents dans Gramps :

1.  base de données : moteur qui permet à Gramps de prendre en charge d'autres [types de base de données](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Arbre_Familial).
2.  Les bibliothèques greffon : bibliothèques fournissant des fonctionnalités supplémentaires.
3.  Les relations: les calculateurs de relations pour les différents langages.
4.  Règle (introduit avec Gramps 6.0.x et supérieur)

Il y a plusieurs greffons fournis avec Gramps. Cependant, tout le monde peut écrire un greffon et le partager. Ces greffons supplémentaires sont nommés "addon". Nous encourageons grandement les utilisateurs et développeurs à partager leurs créations avec les autres utilisateurs de Gramps.

## Enregistrement et chargement

Les greffons sont soit présents localement sur l'ordinateur et connus de Gramps et on dit qu'ils sont enregistrés ; ou ils sont présents sur un ordinateur distant et Gramps ne connaît que leur nom, leur type et la description et on dit que ce sont des addon.

Quand Gramps démarre, l'information quant aux greffons présents localement est lue automatiquement si bien qu'ils sont enregistrés. Le gestionnaire de greffons peut être utilisé pour télécharger des addon distant pour qu'il deviennent enregistrés.

Les greffons enregistrés (locaux) sont chargés par Gramps dans les situations suivantes :

1.  ils sont automatiquement chargés au démarrage. Certains types de greffon sont chargés au démarrage (si non dans une vue cachée) et certains peuvent avoir une balise qui force le chargement au démarrage.
2.  ils sont automatiquement chargés quand l'utilisateur a l'opportunité de cliquer sur une vue ou demande un rapport.
3.  ils sont chargés quand l'utilisateur demande explicitement le chargement dans le gestionnaire de greffons.
4.  les greffons distants sont chargés au moment où ils sont enregistrés par l'utilisation de [gestion des greffons tiers](wiki:6.0_Addons#Installing_Addons_in_Gramps) dans l'onglet **General** de .

## Cacher/Afficher

Le gestionnaire de greffons peut être utilisé pour cacher ou afficher des greffons. Certains menus n'afficheront pas des greffons cachés, si bien que l'option ne pourra pas être sélectionnée. Pas exemple, si un Gramplet est caché, il n'apparaîtra pas dans le menu contextuel «ajouter un Gramplet» qui s'affiche au clic-droit sur l'arrière-plan de l'onglet principal des Gramplets. Néanmoins, cacher certaines extensions (comme Relations ou Vue Gramps) n'aura pas d'effet ou n'est pas autorisée.

## Actions

Il existe 2 onglets dans le gestionnaire de greffons : les greffons enregistrés et les greffons chargés.

### Greffons enregistrés

![[_media/Registered_plugins-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Greffons enregistrés]]

Cet onglet présente une liste de tous les greffons que Gramps a trouvé.

Ces greffons sont une partie Gramps, tout comme les greffons supplémentaires trouvés depuis le [répertoire de l'utilisateur](wiki:Gramps_6.0_Wiki_Manual_-_Répertoire_utilisateur) dans le répertoire *plugins*.  

Le type de greffon est affiché dans la première colonne.  

Un greffon peut être caché ou affiché en utilisant le bouton . Ceci n'est intéressant que pour les greffons utilisateur.

### Greffons chargés

![[_media/Loaded_plugins-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Greffons chargés]]

Cet onglet présente la liste de l'ensemble des greffons chargés. Normalement, toutes les vues (comme la vue Relations) doivent être chargées, ainsi que l'ensemble des gramplets/rapports/outils que vous avez utilisés et qui seront chargés automatiquement.

Si une erreur est intervenue pendant le chargement d'un greffon, celle-ci sera identifiée dans cet onglet. Un double clique sur une ligne indiquant une erreur de chargement ouvre une fenêtre montrant les détails de l'erreur. Vous pouvez utiliser cela pour contacter l'auteur du greffon ou pour ouvrir un rapport de bug.

### Dialogue Information détaillée

Le dialogue «Information détaillé» permet d'afficher des informations sur chaque greffon sélectionné. Pour l'ouvrir, double-cliquer sur la ligne du greffon dans le gestionnaire ou utiliser le bouton après avoir sélectionné la ligne. Vous pouvez l'utiliser pour contacter le développeur du greffon ou liste de bogues de Gramps. Il contient les informations suivantes :

- Nom du greffon :
- Id :
- Description:
- Version :
- Auteurs:
- Adresse électronique:
- Fichier :
- Emplacement :

[M](wiki:Category:Fr:Documentation)
