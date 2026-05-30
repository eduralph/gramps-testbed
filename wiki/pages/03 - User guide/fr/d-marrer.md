---
title: Fr:Manuel wiki pour Gramps 6.0 - Démarrer
categories:
- Fr:Documentation
managed: false
source: wiki-scrape
wiki_revid: 120658
wiki_fetched_at: '2026-05-30T18:35:44Z'
lang: fr
---

{{#vardefine:chapter\|2}} {{#vardefine:figure\|0}}

Ce chapitre fournit les informations de base sur Gramps. Tout d'abord, nous allons décrire les concepts de base. Puis, nous allons vous montrer comment lancer Gramps et comment obtenir de l'aide si besoin.

\_\_FORCETOC\_\_

## Aperçu de Gramps

Gramps est un programme libre et gratuit conçu pour être un outil de généalogie puissant et flexible. Chacun peut l'utiliser comme il le souhaite. Il n'y a pas une seule méthode pour travailler et enregistrer ses données. Néanmoins, si vous voulez échanger avec d'autres chercheurs ou programmes, il est utile de comprendre comment Gramps fonctionne avant de sauter directement à son utilisation.

Gramps sépare toutes les informations généalogiques en 9 objets principaux :

- Individus
- Familles
- Événements
- Notes
- Media
- Citations
- Sources
- Lieux
- Dépôts

Chaque objet est considéré de façon indépendante. Cela signifie que vous pouvez compléter votre arbre familial à partir de n'importe quel objet, et dans l'ordre que vous voulez. Par exemple, vous pourriez avoir envie de saisir d'abord chaque Individu, puis les connecter en créant les Familles correspondantes plus tard. Ou bien vous pouvez commencer par les Sources, et ne créer que les Individus qui apparaissent dans ces sources. Ou encore mélanger ces façons de rentrer vos informations, en ajoutant des Notes et des Sources, puis des Familles, et plus tard revenir aux Notes et aux Sources. En un mot, vous gérez vos recherches généalogiques comme vous le voulez.

### Connexions

Ces 9 objets de base sont connectés de différentes façons. Certaines de ces connexions sont gérées de façon implicite. Par exemple, ajouter un Individu à une Famille en tant que parent, ou enfant, créé automatiquement une connexion spéciale appelée **Référence**. Vous pouvez voir les Familles auxquelles un Individu est connecté dans l'onglet Références de la fenêtre principale d'un Individu. Il y a de nombreuses autres façons de visualiser ces connexions dans Gramps, en particulier la vue Relations.

Afin d'éviter la répétition de données, Gramps vous permet de partager ou ré-utiliser les informations. Ces partages sont aussi une forme de connexion, appelée **liens**. Par exemple, un élément Individu peut être lié à un nombre quelconque de Notes. Si une note mentionne deux personnes différentes, il paraît logique de partager cette seule note entre les deux personnes.

Certains liens peuvent comporter des informations. Vous pouvez par exemple lier un Individu à l'Evénement mariage d'un autre couple, en tant que témoin. Cependant, le mari et la femme sont liés à l'Evénement mariage avec un rôle **principal**, tandis que le témoin aura un rôle différent, celui de témoin. Ce type d'information est conservé dans le lien lui-même, dans la propriété Rôle.

### Vie privée

Gramps prend en charge deux méthodes différentes pour protéger les données privées et sensibles de notre arbre familial. Ces méthodes sont utilisées pour partager nos données avec d'autres personnes, soit par la création de rapport ou l'exportation de données, soit à travers la création d'un site Web.

La première méthode protège l'information des personnes que Gramps estime en vie. Si vous n'avez pas spécifiquement indiqué que cette personne est décédée (en ajoutant un événement décès à cet individu), alors Gramps va utiliser une fonction automatique et sophistiquée pour déterminer si quelqu'un est en vie. Les données sensibles des personnes vivantes seront cachées en utilisant cette méthode. Par exemple, un individu nommé « *Martin, Jean* » peut apparaître « *Martin, \[Vivant\]* ».

La seconde méthode de protection de la vie privée est une option explicite « *enregistrement privé* » que vous pouvez utiliser avec chaque article. Par exemple, vous avez des informations sensibles, une information personnelle dans une note. Si vous marquez cette note comme privée, alors cette note n'apparaîtra pas dans les rapports textuels et narratifs ou les exportations. Sachez aussi que certains liens eux-mêmes peuvent être marqués comme privés. Ceci est utile quand vous voulez marquer comme privé une connexion d'un individu à un événement, mais souhaitez conserver cet individu et cet événement dans un rapport, une exportation, ou un site internet.

Pour activer ces deux méthodes de respect de la vie privée, vous aurez besoin de les indiquer lors de la création de certains rapports ou de l'exportation de vos données.

### GEDCOM

Gramps a hérité de la structure d'un noyau standard appelé GEDCOM[1](https://fr.wikipedia.org/wiki/GEDCOM). Néanmoins, Gramps va au delà de ce standard quand cela semble nécessaire. Si vous avez prévu d'utiliser vos données familiales avec un autre système qui utilise GEDCOM, vous devrez brider les fonctionnalités spécifiques de Gramps. D'un autre côté, si vous n'êtes pas limité par un autre logiciel de généalogie, alors vous pouvez saisir vos données tel que bon vous semble.

Vous pouvez obtenir plus de détails sur ce sujet dans la section [Gramps et GEDCOM](wiki:Gramps_and_GEDCOM).

## Lancer Gramps

le meilleur moyen d'apprendre comment fonctionne Gramps est probablement de travailler avec vos données. Commençons !

La méthode pour lancer Gramps dépend de votre système d'exploitation.

À côté de l'interface utilisateur graphique (GUI) classique décrite plus bas, il est également possible de lancer Gramps en ligne de commande (CLI). Cette interface en ligne de commande permet de générer des rapports d'erreur (non disponible avec l'interface graphique), faire des conversions, etc. sans ouvrir de fenêtre, et fournir des [informations supplémentaires](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/fr#Lors_d.27un_probl.C3.A8me) en cas de problèmes. Pour plus d'informations, voir [l'annexe Ligne de commande](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/fr)

### Linux

Seule la plateforme Linux est officiellement prise en charge car les développeurs de Gramps utilise et teste le code source sous cette plateforme.

Si vous avez installé Gramps avec votre gestionnaire de paquets standard pour votre distribution (par GUI ou par CLI), vous démarrez Gramps selon la méthode habituelle de votre distribution. Par exemple, sous Ubuntu 20.04, une icône est présente dans le Dock ou dans la liste des applications. Pour les autres distributions, une entrée est créée dans le menu Applications (habituellement dans la section Bureautique).

Démarrez Gramps en ligne de commande sur Linux est décrit [ici](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Les_lignes_de_commande).

### MS Windows

MS Windows est une plateforme [supportée par la communauté](wiki:Download/fr). Si vous installé le paquet [Windows « tout en un » (AIO)](wiki:All_In_One_Gramps_Software_Bundle_for_Windows) vous aurez un accès depuis votre bureau de même qu'un accès depuis le Menu « Démarrer » vous permettant de lancer Gramps.

Démarrer Gramps depuis le CLI sous MS Windows est possible via [l'interface en ligne de commande](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/fr).

Il y a d'autres moyens d'installer Gramps sous MS Windows, mais ils ne seront pas développés ici.

### Mac OS X

Mac OS X est une plateforme [supportée par la communauté](wiki:Download/fr). Si vous téléchargez l'image disque pour Mac OS X (.dmg), alors il vous suffit de glisser l'application vers votre répertoire d'applications (ou là où vous souhaitez placer Gramps) puis lancez Gramps en cliquant deux-fois sur l'application, de manière standard.

Démarrer Gramps depuis le CLI sous Mac OS X est possible via [l'interface en ligne de commande](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/fr).

Il y a d'autres moyens d'installer Gramps sous Mac OS X, mais ils ne seront pas développés ici.

## Choisir un arbre familial

![[_media/First_open-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fenêtre principale]]

Si Gramps a démarré sans arbre familial sélectionné, l'interface offrira peu de possibilités. La plupart des opérations ne seront pas disponibles. Pour charger un arbre familial (la base de données), allez dans le menu , ou cliquez sur l'icône de l' dans la barre d'outils. Gramps garde une trace des arbres récemment ouverts, et ceux-ci peuvent être sélectionnés en cliquant sur la flèche à côté du bouton puis choisir dans la liste.

Pour des informations détaillées sur le gestionnaire d'arbre familial et le menu Arbres Familiaux, voir le chapitre dédié à la [gestion des arbres familiaux](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/fr).

  

## Dites-moi comment commencer, maintenant !

Nous vous encourageons à lire et parcourir le manuel pour prendre connaissance de tous les détails concernant Gramps. La généalogie prend du temps, aussi connaître vos outils n'est pas du temps perdu.

Cependant, si vous souhaitez vraiment ne savoir que le minimum pour commencer, alors lisez :

- [Entrer et modifier ses données - Sommaire](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Édition_sommaire)
- [Débuter sa généalogie‎](wiki:Débuter_sa_généalogie‎).

## Obtenir de l'aide

![[_media/Menubar-Help-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Barre de menu - Aide]]

Gramps a un menu qui peut être consulté à chaque instant. Il inclut les liens suivants :

- Le : est le lien vers ce manuel. Actuellement il est nécessaire d'avoir une connexion internet.

<!-- -->

- : est un lien vers les [questions fréquemment posées](wiki:Gramps_6.0_Wiki_Manual_-_FAQ/fr) à propos de Gramps.

<!-- -->

- Les : est un lien vers les [raccourcis clavier](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/fr) de Gramps.

<!-- -->

- : affiche le dialogue de l'« Astuce du jour ».

<!-- -->

- Le : permet d'afficher l'état d'un plugin/greffon que vous avez décidé d'ajouter.

<!-- -->

- La : est le lien qui appellera votre navigateur internet pour vous connecter au site internet du projet Gramps.

<!-- -->

- Les : est le lien qui appellera votre navigateur internet pour accéder à la page des listes de courrier Gramps. Sur cette page vous pourrez naviguer à travers les archives ou rejoindre la liste gramps-users.

<!-- -->

- : choisissez ce lien pour signaler un bogue dans le système de [suivi de bogue](wiki:Using_the_bug_tracker). (Rappelez-vous, Gramps est un projet vivant. Nous voulons connaître les problèmes rencontrés, tout le monde pourra en bénéficier.)

<!-- -->

- : cet article affiche un dialogue avec les informations générales sur la version de Gramps que vous utilisez.

[M](wiki:Category:Fr:Documentation)
