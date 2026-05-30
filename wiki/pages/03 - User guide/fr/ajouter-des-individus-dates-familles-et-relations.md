---
title: Fr:Manuel wiki pour Gramps 6.0 - Ajouter des individus, dates, familles et
  relations
categories:
- Fr:Documentation
managed: false
source: wiki-scrape
wiki_revid: 111179
wiki_fetched_at: '2026-05-30T18:39:12Z'
lang: fr
---

{{#vardefine:chapter\|7.1}} {{#vardefine:figure\|0}}

La section précédente vous a proposé un aperçu rapide pour entrer et éditer les données dans Gramps. Cette section prolonge cette description mais avec plus de détails.

## Introduction

Comme nous l'avons vu plus haut, Gramps vous permet plusieurs vues. Chacune vous offre la possibilité d'entrer et d'éditer l'information. En fait, vous obtenez souvent la même information dans différentes vues.

Dans Gramps, l'information est entrée et éditée dans un dialogue. Nous utilisons ce terme fréquemment, voici sa définition :

Un dialogue est une fenêtre pop-up qui propose au minimum un formulaire pour entrer et éditer des données correspondant à une catégorie. Par exemple Gramps inclut un dialogue et un dialogue , parmi d'autres.

Un dialogue inclut souvent une série d'"onglets" qui regroupe les informations dans des sous-catégories. Par exemple, le dialogue d'édition d'individu a pour sous-catégories : événements, attributs, adresses, et notes, parmi d'autres.

Afin de ménager de l'espace précieux à l'écran, les boutons , , et ne sont pas marqués avec le texte. Ils sont respectivement remplacés par les icône , et une icône dépeignant un stylo sur une feuille de papier.

## L'information personnelle

### Un aperçu des éléments

![[_media/Edit_person_2-42-fr.png.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Édition de l'individu]]

La modification des informations sur un individu se fait dans l'. Ce dialogue peut être appelé depuis différentes vues :

- Depuis la [vue Individus](wiki:Gramps_6.0_Wiki_Manual_-_Categories/fr#Individus)

  
  
Double-cliquez sur la personne dont vous voulez modifier les données.

<!-- -->

  
  
Sélectionnez le nom avec un simple clic, puis demander la modification par l'icône de la barre d'outils.

<!-- -->

  
  
Vous pouvez aussi lancer la modification en appuyant sur après l'avoir sélectionnée.

<!-- -->

  
  
Enfin, vous pouvez choisir du menu de Gramps

<!-- -->

  
  
Sélectionnez dans le menu contextuel activé en cliquant avec le bouton droit de la souris.

- Depuis la [vue Relations](wiki:Gramps_6.0_Wiki_Manual_-_Categories/fr#Relations) : pour éditer les données de la personne active, cliquer sur le bouton à côté du nom de la personne active.

<!-- -->

- Depuis les [vues Graphiques](wiki:Gramps_6.0_Wiki_Manual_-_Categories/fr#Graphiques) : mettez la souris dans la zone de la Personne Active, puis double-cliquez, ou encore utilisez les sous-menus décrits ci-dessus.

Quelle que soit la méthode utilisée, le dialogue apparaîtra :

La partie principale de la fenêtre a deux parties : l'information de base sur le de l'individu, et la section avec le bouton sur la vie privée (pour marquer un enregistrement comme privé), le sélecteur de genre, un identifiant qui vous pouvez asigner à cet enregistrement, ainsi qu'un marqueur permettant d'indiquer l'état d'avancement de vos recherches (complet, ÀFAIRE, incertain, ....) affichant une couleur spécifique à cet enregistrement dans la vue Individus.

Cliquez sur le nom de l'onglet pour faire apparaître son contenu et donc permettre l'accès à ses données. Le bouton du bas a pour effet d'appliquer toutes les modifications dans la base de données et de fermer la fenêtre. Le bouton ferme la fenêtre sans modifier la base de données.

Si des modifications avaient été faites, une fenêtre d'avertissement proposera le choix entre fermer sans écrire les données dans la base, annuler la commande de fermeture ou écrire les données dans la base.

### La section Nom d'usage

Le nom d'usage ou nom préféré est le nom qui sera utilisé dans Gramps comme 'nom' de l'individu. Vous pouvez définir comment il sera affiché depuis les [Préférences de Gramps](wiki:Gramps_6.0_Wiki_Manual_-_Settings/fr#Affichage), et dans tout le programme vous ne verrez que le nom d'usage. Seul les rapports détaillés et le générateur de site internet afficheront les noms alternatifs. Notez que rechercher un nom va explorer tous les noms liés à cette personne, pas seulement le nom d'usage.

La section contient l'information nécessaire lors de la saisie du nom de l'individu. Toutes les informations possibles sur le nom ne sont pas affichées, seulement les plus champs de saisie importants. Pour voir les possibilités sur le nom, cliquez sur le bouton d'édition après le titre . Ceci va ouvrir l'[Éditeur de nom](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_3/fr#Noms).

Les champs nom de l' sont :

- Le , cette partie du nom indique la famille à laquelle appartient l'individu.

<!-- -->

- Le , est un préfixe optionel pour le nom de famille, ignoré pour le tri, tel que *de* ou *van*, et le , un suffixe optionel pour le nom, tel que *Jr* ou *III*.

<!-- -->

- Le , qui est un composant du nom individuel basé sur le nom de ses ascendants : père, grand-père, et , un titre utilisé par la personne, tel que *Dr* or *Me*.

<!-- -->

- Le , officiellement ceci est une partie du prénom pour un usage courant. Par exemple, une personne peut avoir 3 prénoms comme *Jean Baptiste Jules*, alors qu'en réalité seulement *Baptiste* est utilisé. En Allemagne et dans d'autres endroits, il était courant de surligner le nom usuel associé aux autres prénoms, voir également [ici](wiki:CallName). Certains vont utiliser ce champ pour le surnom, ou des modifications sur le prénom (par exemple Jeannot pour Jean), mais c'est pas l'utilisation officielle. Un nom usuel est un nom légal. Pour les surnoms, ou des variantes dans le nom, vous devriez créer un nom alternatif, avec un type de nom différent.

<!-- -->

- Le de nom (nom de naissance, nom marital...). Il est conseillé d'utiliser le nom d'usage comme celui qui apparaît le plus souvent sur les documents, et de stocker d'autres types de nom dans l'onglet de l'.

Certains de ces champs et ont une fonction de "saisie automatique" quand vous saisissez, un menu apparaissant proche du champ contenant les entrées déjà connues dans la base de données. Cela vous fournit un raccourci selon les lettres saisies à partir des données déjà connues. Vous pouvez sélectionner une entrée en utilisant votre souris ou le curseur et la touche .

Le bouton (c'est, l'icône "stylo et papier") situé près du champ d'entrée appelant le dialogue . Ce dernier vous permet d'éditer le nom préféré dans le détail (voir [Éditeur de nom](wiki:Media:Edit-an_fr.png)).

Le est un prénom descriptif utilisé à la place ou en complément du prénom officiel. Le est un nom non-officiel donné à une famille pour en distinguer des individus avec le même nom de famille. Faisant souvent référence à un nom de ferme.

### La section Général

- Général :

  
Le menu donne le choix entre , , et .

<!-- -->

  
Le champ présente l'identifiant interne que Gramps attribue à chaque individu de la base de données. La zone montre la première image de la pour cette personne (s'il y en a).

<!-- -->

  
L' vous permet de définir vos propres étiquettes et de spécifier quelque information basique sur le statut de votre recherche.

<!-- -->

  
Le bouton permet de marquer ou non les enregistrements de la personne comme étant privées.

### L'image préférée

- Image :

  
Le champ affiche la première image disponible dans la de cette personne (si il y en a).

### Les onglets de l'individu

Les onglets donnent accès aux types d'informations suivantes :

- Evénements :

  
L'onglet Événements présente les données des événements liés à la personne pour permettre leur modification. La partie du bas de la fenêtre affiche cette liste d'événements. La partie du haut montre le détail de l'événement sélectionné (si il y en a). Les boutons , , et vous permettent respectivement d'ajouter, modifier et supprimer un événements Notez que les boutons et ne sont disponibles que lors de la sélection d'une entrée dans la liste.

- Noms :

![[_media/Edit_person_names-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Noms]]

  
L'onglet affiche les informations sur les autres dénominations de la personne et permet leur modification. La partie du bas affiche la liste de tous les autres dénominations de la personne considérée. La partie du haut montre le détail de la dénomination sélectionnée s'il y a lieu. Les boutons , , et permettent respectivement l'ajout, la modification et la suppression d'une dénomination. Notez que les boutons et ne sont disponibles que lors de la sélection d'une entrée dans la liste.

<!-- -->

  
Quand vous ajoutez un nouveau nom ou éditez un nom existant, le dialogue est appelé, voir la [section Éditeur de Nom](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_3/fr#Noms).

- Citations/Sources

![[_media/Edit_person_citations-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Citations/Sources]]

  
L'onglet affiche les sources d'information sur l'individu et permet leur modification.

<!-- -->

  
Les citations/sources sont liées à la personne mais pas spécifiquement à un événement. Par exemple, le journal personnel de Tante Jeanne peut mentionner son arrière-petit-fils Paul. Dans ce cas, Paul aura comme source ce journal.

  
La partie centrale de la fenêtre montre la liste des sources associées à la personne active conservées dans la base de données. La partie du haut montre le détail de la source sélectionnée s'il y a lieu. Les boutons , , et vous permettent respectivement d'ajouter, modifier et supprimer une source pour la personne active. Notez que les boutons et ne sont disponibles qu'après avoir sélectionné une source dans la liste.

<!-- -->

  
Vous pouvez éditer ou changer les données dans la référence de la source (unique pour cet individu), aussi bien que pour l'objet source (partagé), voir [Édition de la citation](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_2/fr#.C3.89dition_de_la_citation).

- Attributs :

![[_media/Edit_person_attributes-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Attributs]]

  
L'onglet affiche les valeurs d'attributs de l'individu et permet leur modification. Un attribut est en fait n'importe quelle couple Paramètre-Valeur. Par exemple, attribut peut être défini pour décrire les caractéristiques physique ou la personnalité d'un individu.

<!-- -->

  
Notez que chaque attributs est listé dans le dialogue défini en deux parties: l'attribut lui-même et sa valeur associée. Défini comme un paire "Paramètre-Valeur" pouvant vous aider dans votre organisation et recherche. Par exemple, si vous définissez "couleur de cheveux" comme un attribut pour une personne, "couleur de cheveux" deviendra un attribut disponible à tous les autres individus. La valeur pourra être blond pour la personne A et roux ou brun pour la personne B. Dans le même esprit, vous pouvez définir un attribut comme "générosité" et utiliser la valeur "énorme" pour décrire une personne particulièrement généreuse.

<!-- -->

  
La partie du bas de la fenêtre montre la liste de tous les attributs conservés dans la base de données. La partie du haut montre le détail de l'attribut sélectionné s'il y a lieu. Les boutons , , et vous permettent respectivement d'ajouter, modifier et supprimer un attribut et sa valeur pour la personne active. Notez que les boutons et ne sont disponibles que lors de la sélection d'une entrée dans la liste.

<!-- -->

  
  
Quand vous éditer un attribut, le dialogue [Éditeur d'attribut](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_3/fr#Attributs) est ouvert.

- Adresses:

![[_media/Edit_person_addresses-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Adresses]]

  
L'onglet vous permet de voir et d'éditer les différentes adresses postales d'une personne. Il vous est conseillé d'utiliser l'événement résidence pour stocker vous informations sur la résidence d'une personne. L'onglet est surtout là pour offrir une compatibilité avec le standard GEDCOM, alors que la fonction de l'adresse n'est que l'envoi et la réception de courier.

<!-- -->

  
La partie du bas de la fenêtre montre la liste des adresses de la personne active conservées dans la base de données. La partie du haut montre le détail de l'adresse sélectionnée s'il y a lieu. Les boutons , , et vous permettent respectivement d'ajouter, modifier et supprimer une adresse pour la personne active. Notez que les boutons et ne sont disponibles que lors de la sélection d'une entrée dans la liste.

<!-- -->

  
  
Quand vous éditer une adresse, le dialogue [Éditeur d'adresse](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_3/fr#Adresses) est ouvert.

<!-- -->

  
Certains rapports vous permettent de restreindre les données sur les personnes vivantes. En particulier, les adresses sont omises.

- Notes:

![[_media/Edit_person_notes-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Notes]]

  
L'onglet affiche les notes sur l'individu et permet leur modification. Les notes sont un simple texte libre associé à la personne, ainsi que des extraits de text associés à votre arbre. Vous pouvez partager des notes entre les différents enregistrements de Gramps. La barre d'icônes offre les boutons courants : ajouter une note, sélectionner une note à ajouter, modifier une note sélectionnée, supprimer une note, et réorganiser les boutons pour changer l'ordre des notes.

<!-- -->

  
Pour modifier les notes, simplement modifiez le texte dans la zone de saisie de l'onglet.

<!-- -->

  
L'option vous permet de choisir le rendu de la note dans la sortie (édition ou bien page Web).

<!-- -->

  
Choisir "Libre" remplacera les espaces multiples, les tabulations et les changements de lignes simples par un espace. Les lignes vides (deux changements de lignes consécutifs) sont comprises comme une fin de paragraphe.

<!-- -->

  
  
Quand vous éditer une adresse, le dialogue [Éditeur de note](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_2/fr#L.27.C3.A9diteur_de_note) est ouvert.

<!-- -->

  
Si vous sélectionnez l'option formatée, le texte des rapports et pages internet apparaîtra comme dans le dialogue .

- Galerie :

![[_media/Edit_person_gallery-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Galerie]]

  
L'onglet affiche les données des objets multimédia associés à l'individu et permet leur modification. La partie centrale de la fenêtre montre tous les objets multimédia conservés dans la base de données. Les objets qui sont des fichiers-images valides sont représentés par une vignette. Les autres comme des enregistrements sonores ou vidéo sont représentés par une icône générique.

  
Les boutons , , et vous permettent respectivement d'ajouter une nouvelle image, ajouter une référence à image déjà dans la base, modifier et supprimer la référence à un objet multimédia. Notez que les boutons et ne sont disponibles qu'après avoir sélectionné un objet dans la liste. Vous accèderez à [Édition de la référence du Media](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_2/fr#Édition_des_r.C3.A9f.C3.A9rences_de_l.27object_media)

- Internet:

![[_media/Edit_person_internet-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Internet]]

  
L'onglet affiche les informations sur les adresses internet de la personne et permet leur modification, avec un champ de description pour l'emplacement internet défini et le type d'adresse internet, tel que celles utilisées pour naviguer, par exemple. <http://gramps-project.org>, messagerie, page internet, ...

<!-- -->

  
La partie du bas affiche la liste de tous les adresses Internet de la personne considérée. La partie du haut montre le détail de l'adresse sélectionnée s'il y a lieu. Les boutons , et permettent respectivement l'ajout, la modification et la suppression d'une adresse. Le bouton permet d'ouvrir une page Internet avec votre navigateur favori. Notez que les boutons , et ne sont disponibles que lors de la sélection d'une adresse dans la liste.

- Associations

![[_media/Edit_person_assoc-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Associations]]

  
L'onglet vous permet de voir et d'éditer une information sur les associations entre les individus dans la base de données.

<!-- -->

  
Les associations peuvent inclure les parrains, amis de la famille, ou tout autres types d'associations que vous souhaitez enregistrer. Utilisez plutôt les événements pour les relations spécifiques liées à une occasion ou un événement dans le temps. Les événements peuvent être partagés entre les individus, chacun ayant un rôle propre dans l'événement.

- LDS

![[_media/Edit-person-lds_34_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Mormons - Saints des Derniers Jours]]

  
L'onglet affiche les informations d'ordinances LDS de la personne et permet de les modifier. Ces informations sont héritées du format gedcom et sont spécifiques aux mormons.

<!-- -->

  
Ce sont le , la et les . Chaque ordinance est décrite par sa date, son temple mormon et son lieu.

<!-- -->

  
Un menu déroulant est en plus disponible pour les . Chaque ordinance peut ensuite recevoir un statut par le menu déroulant ainsi qu'une source et des notes par les boutons et .

{{-}}

## Édition des dates

Cette section décrit les détails des dates entrantes et de modifications. Les dates sont importantes dans la recherche généalogique, ainsi Gramps va préserver et employer n'importe quelle information de date disponible.

L'information peut être saisie directement dans le champ date ou en appelant le dialogue . Les deux méthodes seront décrites plus tard, tout d'abord, nous allons préciser comment les dates sont gérées dans Gramps.

### Types de date

Les dates dans Gramps sont classées selon les types suivants :

- Une date "normale" (régulière) est celle qui a un jour, mois, ou année.

Cela peut être complet (e.g., 6 juin 1990) ou partiel (e.g., Juillet 1977).

- Une date "avant" ne peut qu'être identifiée comme avant un certain jour, mois, ou année.

<!-- -->

- Une date "après" ne peut qu'être identifiée comme après un certain jour, mois, ou année.

<!-- -->

- Une date "étendue" décrit une période durant laquelle s'est peut être produit l'événement.

Par exemple : *entre Janvier 1932 et Mars 1932*

- Une date "incrémentée" décrit une période durant laquelle s'est produit l'événement.

Par exemple : *de 12 mai 2000 à 2 février 2002*

### Formats de date et règles de filtrage

Les entrées de dates acceptables Gramps identifient beaucoup de formats des dates exactes. Les formats numériques sont déterminés par l'environnement Gramps de défaut. La plupart des pays européens emploient JJ.mm.aaaa, les USA emploient généralement MM/jj/aaaa, et ainsi de suite.

Sans compter qu'avec les dates exactes, Gramps identifie beaucoup de dates qui ne sont pas régulières: avant, après, environ, période et estimation. Il comprend également la qualité: estimé(e) ou calculé(e). En conclusion, il soutient les dates partielles et beaucoup de calendriers alternatifs. Ci-dessous se trouve la liste de règles d'entrée à accorder pour l'analyse.

Les dates régulières peuvent être écrites comme vous les écririez dans une lettre : *24 mai 1961* ou *01/01/2004*.

Les dates qui ne sont pas régulières devraient commencer par la qualité: ou , si c'est approprié. La qualité normale n'a pas besoin d'être indiquée, car c'est le défaut.

Exemples: *est 1961,* ou *CALC 2005*.

Puis devrait apparaître le type: , , ou (ou son abréviation "~").

Les estimations sont définies avec "entre LA_DATE et LA_DATE" et les périodes avec "de LA_DATE à LA_DATE".

Exemples: *de 2001 à 2003*, *avant juin 1975*, *est vers 2000*, *CALC entre mai 1900 et 1 janvier 1990*, *~ 2009*.

Les dates partielles sont écrites simplement en omettant l'information inconnue: *mai 1961*, *2004*.

### Calendriers

Les calendriers alternatifs sont des calendriers autres que le calendrier grégorien. Actuellement, Gramps soutient l'hébreu, les calendriers alternatifs républicain, julien, islamique, suédois et persan. Pour indiquer le calendrier autre que le défaut grégorien, apposez le nom du calendrier aux caractères de datation, par exemple. "9 janvier 1905 (julien)".

### Calendrier Suèdois

Le [roi suédois](wiki:Swedish_kings), Karl XII, avait décidé que la Suède ne devait pas utiliser le calendrier Grégorien. Cependant, il était prévu de le mettre en place graduellement en sautant 11 jours entre le 29.02.1700 et 1744. Ainsi le 28.02.1700 fut suivi du 01.06.0700. Ceci eut lieu pendant la Grande Guerre Nordique et les jours sautés furent maintenu en 1704 et 1708. En janvier 1711 le même roi décida que la Suède devait ré-utiliser le calendrier Julien à la date du 01.06.0712. Pour être synchronisé, un jour additionnel est apparu le 30.02.1712. Et ce fut la fin du calendrier suèdois. La Suède adopta le calendrier Gregorian le 01.06.0753, en sautant les dates entre le 18.02.1752 et le 28.02.1753. Dans Gramps vous ne pouvez entrer des dates valides pour le calendrier suédois que entre 01.06.0700 et 30.02.1712. Toutes les autres dates sont notées comme invalides et doivent être corrigées.

### Dates doubles

Les dates doubles (également appelées "dates slash", et parfois "Ancien style/Nouveau style" de dates) apparaissent comme "23 Janvier 1735/6". Souvent prises par erreur comme une année incertaine, en fait il y une raison historique spécifique. La date double représente une période de transition lorsque ce secteur définissa le 1er Janvier comme étant le début de l'année. Ainsi 23 Janvier 1735/6 est une indication pour mieux définir quand la date fut mise en place. Dans cet exemple, "23 Janvier 1736" pourrait correspondre à après le "23 Juin 1736".

Les colonies anglaises n'ont accepté officiellement le "1er Janvier" comme début de l'année qu'à partir de 1752. Avant 1752, le gouvernement anglais acceptait officiellement le 25 Mars comme le premier jour de l'année, même si la plupart de la population anglaise utilisait le 1er Janvier comme début de l'année. Ainsi de nombreuses personnes ont écrit des dates entre le 1er Janvier et le 25 Mars dans le format des dates doubles.

Parfois, une date double peut apparaître comme une fraction, comme sur cette pierre tombale (170 et 3/4, qui veut dire 1703 et 1704):

![[_media/Gravestone.jpg|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pierre tombale]]

  
Marquer une date comme date double est possible simplement en ajoutant un slash (*/*) entre les années. Par exemple:

`   * 1721/2`  
`   * 1719/20`  
`   * 1799/800 `

Ces années-slash peuvent apparaître n'importe où pour les dates ayant une année valide.

Les dates doubles sont actuelement représentées dans le calendrier Julien, de sorte que leurs mois et jours seront les mêmes qu'avec une représentation textuelle.

### Jour de la nouvelle année alternatif

Avec les dates doubles (et d'autres dates) vous savez que la nouvelle année peut être célébrée un autre jour que le 1er Janvier. Pour indiquer ceci dans Gramps, placez votre code (mois/jour) entre parenthèses, après le calendrier (si besoin). Par exemple:

`   * 20 Janvier 1865 (Mar25)`  
`   * 20 Janvier 1750 (Julian,Mar1)`  
`   * 23 Février 1710/1 (Mar25) `

Pour indiquer le début de l'année différent du 1er Janvier, vous utiliserez les codes suivants:

`   * Jan1`  
`   * Mar1`  
`   * Mar25`  
`   * Sep1 `

Vous pouvez les saisir entre parenthèses, ou juste après le nom du calendrier (virgule, et pas d'espace).

Notez que si le premier jour de l'année n'est pas le 1er Janvier, alors Janvier suivra Décembre dans l'année. Les dates avec les codes de nouvelle année seront triées approximativement.

### Indicateurs de validité de date

Des indicateurs Gramps existent, pour indiquer la validité de la date écrite. ![[_media/Date_selection-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sélection de la date]]

Même si une date incomplète n'est pas exactement connue, elle permet quand même certaines comparaisons.

Une croix rouge signifie que la date n'est pas valide (par exemple semaine de Noël 61). Dans ce cas, la date est conservée comme une chaîne de caractères. On ne peut en conséquence pas faire de comparaison sur cette date. Il est préférable d'éviter ce genre de saisie. On peut mettre de telles informations dans une note. L'exemple considéré devrait être codé comme une date "Décembre 1961", correcte bien que incomplète, accompagnée d'une note contenant "semaine de Noël en 61."

Dans la [vue Individus](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/fr#Individus), ces dates non valides apparaissent en **gras** par défaut. Le style des dates invalides peut être modifié dans les [Préférences](wiki:Gramps_6.0_Wiki_Manual_-_Settings/fr#Dates).

### L'interface graphique pour la saisie des dates

L'interface graphique ainsi que les règles ci-dessus fournissent une manière rapide et facile pour écrire la plupart des dates, parfois il y a un besoin d'établir une date complexe ou vérifier simplement la date en utilisant l'interface utilisateur graphique. La fenêtre peut être appelée en cliquant sur l'icône à côté du champ d'entrée de date.

Le menu permet de choisir le calendrier supporté. Le menu fournit des choix de qualité : normal, estimé(e), ou calculé(e). Le menu laisse ajuster le type exact de date: normal, avant, après, vers, étendue, incrémenté(e), et texte seulement. Un ensemble de commandes marquées laisse placer le jour, le mois et l'année d'une date. Les deuxièmes commandes , laissent placer les détails de la deuxième date. Enfin, le champ d'enregistrement associe du texte avec la date.

## Édition de l'information sur les relations

L'information sur les relations est entrée et éditée dans le dialogue . Ce dialogue peut être appelé de plusieurs manières :

- Depuis la [vue Relations](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/fr#Relations): cliquer sur le bouton dans la famille que vous souhaitez éditer.

<!-- -->

- Depuis la [vue Familles](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/fr#Familles): sélectionner la famille dans la liste puis cliquer sur le bouton dans la barre d'outils, ou double-cliquer sur la famille.

<!-- -->

- Depuis les [vues Lignée](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/fr#Lignée): placez le pointeur de votre souris sur la ligne noire reliant les conjoints, un clic sur le bouton droit de la souris puis sur depuis le menu contextuel, ou cliquez deux fois sur la ligne noire.

Chacunes de ces méthodes vous conduiront au dialogue suivant :

![[_media/Edit_family-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Éditeur de famille]]

La partie supérieure de la fenêtre affiche les noms des individus dont la relation a été éditée, aussi bien que leur information de naissance et décès. La partie principale de la fenêtre affiche trois champs et sept onglets/étiquettes représentant différentes catégories d'information sur la relation. Cliquer sur un onglet pour voir ou éditer l'information qu'il contient. La partie inférieure contient les boutons et .Cliquer sur le bouton à tout moment, fermera la fenêtre en appliquant aucun changement. Si une partie quelconque des données dans n'importe quelle étiquette était modifiée, la fenêtre alerte apparaîtra avec les choix de clôturer le dialogue sans enregistrement ou de sauver les changements.

Les champs de la section ont une description basique de la relation. Le champ affiche le numéro ID de la relation dans la base de donnée. Laissez Gramps assigner cet enregistrement. Les types disponibles (comme marié, non marié, etc.) peuvent être choisi depuis le menu . Le vous permet de spécifier quelques informations basiques sur le statut de votre recherche.

Les onglets (ou étiquettes) fournissent les catégories suivantes d'informations :

- Enfants

L'onglet vous permet de voir et d'éditer une liste d'enfant dans la relation. Les boutons vous permet d'entrer une nouvelle personne à la base de données et d'ajouter cette personne comme un enfant dans cette relation. Le bouton vous permet de sélectionner une personne existante pour être un enfant dans la relation. Le bouton vous permet d'éditer la relation entre l'enfant et ses parents. Enfin le bouton vous permet d'enlever l'enfant sélectionné de la relation. Notez que le bouton et ne sont activés que quand un enfant est sélectionné dans la liste.

- Événements

![[_media/Edit_family_2-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Les événements dans l'éditeur de famille]]

L'onglet présente les informations sur les événements liés à la relation. Les boutons , et permettent respectivement d'ajouter, modifier et supprimer un événements de la base de données. Notez que les boutons et ne sont activés que lorsqu'un événements est sélectionné dans la liste.

- Citations/Sources

L'onglet vous permet de voir et éditer une liste de références aux citations/sources liées à la relation. Par exemple, des documents portant sur une relation, mais pas forcément un document officiel, si les mémoires de Tante Marthe mentionnent le couple formé par son arrière-petit-fils Paul et Clara. Dans ce cas, le couple Paul-Clara aura comme source ce journal.

Les boutons , et vous permettent respectivement d'ajouter, modifier et supprimer une source pour la relation. Notez que les boutons et ne sont disponibles qu'après avoir sélectionné une source dans la liste.

- Attributs

L'onglet vous permet de voir et éditer une information particulière sur la relation qui peut être définie comme attribut. Les boutons , et vous permettent respectivement d'ajouter, modifier et supprimer un attribut et sa valeur pour la relation. Notez que les boutons et ne sont disponibles qu'après avoir sélectionné un attribut dans la liste.

- Notes

L'onglet affiche les notes sur la relation et permet leur modification. Les notes sont un simple texte libre associé à la relation. Pour modifier les notes, changez simplement le texte dans la zone de saisie de l'onglet.

L'option vous permet de choisir le rendu de la note dans la sortie (édition ou bien page Web). Choisir "Libre" remplacera les espaces multiples, les tabulations et les changements de lignes simples par un espace. Les lignes vides (deux changements de lignes consécutifs) sont comprises comme une fin de paragraphe.

Si vous sélectionnez l'option préformatée, le texte des rapports et pages internet apparaîtra comme dans le dialogue Notes.

- Galerie

L'onglet affiche les données des objets multimédia associés au lieu et permet leur modification. La partie centrale de la fenêtre montre tous les objets multimédia conservés dans la base de données. Les objets qui sont des fichiers-images valides sont représentés par une vignette. Les autres comme des enregistrements sonores ou video sont représentés par une icône générique. Les boutons , , et vous permettent respectivement d'ajouter un fichier, une référence à un objet de la base, modifier et supprimer un objet multimedia. Notez que les boutons et ne sont disponibles qu'après avoir sélectionné un objet dans la liste.

- Mormons

L'onglet affiche les informations d'ordinance LDS de la relation et permet de les modifier. Il s'agit de la notion d' . Chaque ordinance est décrite par sa date, son Temple Mormon et son lieu. Chaque ordinance peut ensuite recevoir un statut par le menu déroulant ainsi qu'une source et des notes par les boutons et .

{{-}}

[M](wiki:Category:Fr:Documentation)
