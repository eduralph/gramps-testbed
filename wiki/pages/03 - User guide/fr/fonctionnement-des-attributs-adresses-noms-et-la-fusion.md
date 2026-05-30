---
title: Fr:Manuel wiki pour Gramps 6.0 - Fonctionnement des attributs, adresses, noms,
  et la fusion
categories:
- Fr:Documentation
managed: false
source: wiki-scrape
wiki_revid: 111175
wiki_fetched_at: '2026-05-30T18:47:42Z'
lang: fr
---

{{#vardefine:chapter\|7.3}} {{#vardefine:figure\|0}}

Cette section fournit un aperçu détaillé sur la saisie des objets principaux présents dans Gramps.

## Noms

Les noms sont modifiés dans la fenêtre : ![[_media/Name_editor-42-fr.png|350 px\|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Éditeur de noms]]

Le haut de la fenêtre contient son titre Affichage des autres Noms et le nom de la personne dont un autre nom est en cours de modification. La partie principale de la fenêtre montre des onglets présentant différentes informations. La partie du bas contient les boutons et . Les boutons a pour effet d'appliquer toutes les modifications dans la base de données et de fermer la fenêtre. Le bouton ferme la fenêtre sans modifier la base de données.

### Type

Une liste déroulante vous permet de sélectionner le type de nom (nom de naissance, nom marital...).

### Section Prénoms

La section Prénoms contient tout ce que Gramps peut stocker concernant le prénom de l'individu.

Les champs sont :

- Le , les prénoms de l'individu.
- Le , officiellement ceci est une partie du prénom pour un usage courant. Par exemple, une personne peut avoir 3 prénoms comme *Jean Baptiste Jules*, alors qu'en réalité seulement *Baptiste* est utilisé. En Allemagne et dans d'autres endroits, il était courant de surligner le nom usuel associé aux autres prénoms, voir également [ici](http://www.gramps-project.org/wiki/index.php?title=CallName). Certains vont utiliser ce champ pour le surnom, ou des modifications sur le prénom (par exemple Jeannot pour Jean), mais c'est pas l'utilisation officielle. Un nom usuel est un nom légal. Pour les surnoms, ou des variantes dans le nom, vous devriez créer un nom alternatif, avec un type de nom différent.
- Le , un titre utilisé par la personne, tel que *Dr* or *Me*.
- Le , un suffixe optionnel pour le nom, tel que *Jr* ou *III*.
- Le , les surnoms sont souvent des raccourcis du prénom légal ou usuel par exemple *Greg* pour *Grégory* (voir. Prénom usuel ci-dessus).

### Section Noms de famille

La section Noms de famille contient les éléments constitutifs du nom de famille. Gramps permet la saisie de plusieurs noms de famille ainsi que plusieurs types de noms de famille.

Les champs sont :

- Le , est un préfixe optionnel pour le nom de famille, ignoré pour le tri, tel que *de* ou *van*.
- Le , cette partie du nom indique la famille à laquelle appartient l'individu.
- Le , qui est un composant du nom individuel basé sur le nom de ses ascendants : père, grand-père, et .
- Le souvent utilisé pour les schémas de nom liés au matronyme et au patronyme, tel que *dotter*.
- L' indique le type de nom de famille et ses dérivés.
- Le des familles fait souvent référence à un surnom patronymique.

Voir aussi: [Names (en anglais) sur le wiki](http://www.gramps-project.org/wiki/index.php?title=Names)

Utilisez l'icône en haut à droite pour définir cet enregistrement de nom comme privé. Ceci vous permettra de cacher certains noms dans les rapports, par exemple, dans les rapports liés aux descendants.

Certains de ces champs et ont une fonction de "saisie automatique" quand vous saisissez, un menu apparaissant proche du champ contenant les entrées déjà connues dans la base de données. Cela vous fournit un raccourci selon les lettres saisies à partir des données déjà connues. Vous pouvez sélectionner une entrée en utilisant votre souris ou le curseur et la touche .

### L'onglet Général

Les permettent de grouper, trier et afficher les noms différemment.

- Le champ permet d'associer le nom à un groupe, différent du patronyme. Par exemple, les noms russes Ivanov et Ivanova sont considérés comme les mêmes, mais il existe une différence d'orthographe. Pour écrire dans ce champ, cocher la case .

  
Les individus sont affichés selon le format du nom défini dans les (le format par défaut).

<!-- -->

  
Dans cette section vous pouvez être certain(e) que le nom sera affiché d'après une règle d'affichage et un format personnalisé (des formats supplémentaires peuvent être définis dans les préférences).

- Les champs et déterminent comment le nom apparaîtra dans la vue des individus et dans les rapports. Par exemple, vous avez une branche avec des noms suédois (prénom et patronyme), mais le reste de votre base de données tri les noms selon la règle Nom de famille, Prénom. Vous pouvez indiquer ici qu'il faut toujours trier le nom comme Patronyme, Prénom.

  
L'affichage vous permet de définir comment le nom sera affiché. Vous pourriez par exemple vouloir trier un nom d'une manière spécifique, mais l'afficher selon vos préférences.

<!-- -->

  
La vue groupée des individus rassemble les porteurs d'un même nom de famille principal. Vous pouvez passer outre ce réglage en définissant une valeur pour un groupe. On vous demandera si vous souhaitez seulement grouper cet individu, ou toutes les personnes avec ce nom de famille principal.

- Le champ permet de saisir une référence temporelle. L'icône date ouvre l' [Éditeur de date](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_1/fr#.C3.89dition_des_dates). Par exemple. pour un nom marital, la date de la première utilisation de ce nom ou une date de mariage.

### L'onglet Citations

L'onglet affiche les sources d'information sur ce nom et permet leur modification. La partie centrale de la fenêtre montre la liste des sources et citations associées au nom conservées dans la base de données. Les boutons , et vous permettent respectivement d'ajouter, modifier et supprimer une source et sa citation pour le nom. Notez que les boutons et ne sont disponibles qu'après avoir sélectionné une source dans la liste. Plus d'informations sur : [Éditeur de la citation](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_2/fr#.C3.89dition_de_la_citation).

### L'onglet Note

L'onglet affiche les notes sur le nom et permet leur modification. Les notes sont un simple texte libre associé au nom. Pour modifier les notes, simplement modifiez le texte dans la zone de saisie de l'onglet.

L'option vous permet de choisir le rendu de la note dans la sortie (édition ou bien page Web). Choisir remplacera les espaces multiples, les tabulations et les changements de lignes simples par un espace. Les lignes vides (deux changements de lignes consécutifs) sont comprises comme une fin de paragraphe. Au contraire, choisir conservera à l'identique les espaces multiples, les tabulations et les changements de ligne comme ils ont été saisis dans la zone de texte. Plus d'informations sur : [Éditeur de Note](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_2/fr#L.27.C3.A9diteur_de_note).

## Attributs

Les attributs sont modifiés avec la fenêtre d' : ![[_media/Attribute_editor-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Éditeur d&#39;attribut]]

Le haut de la fenêtre présente le titre du dialogue, comprenant le nom de la personne dont les attributs sont affichés. La partie principale de la fenêtre montre des onglets contenant différents types d'informations. Le bas de la fenêtre contient les boutons et . Le bouton permet d'écrire les modifications dans la base de données et ferme la fenêtre. Le bouton ferme la fenêtre sans modifier la base de données.

Les onglets donnent accès aux types d'informations suivants :

La partie haute permet la modification des caractéristiques les plus communes de l'attribut :

1.  Le nom de l' que vous souhaitez utiliser. Par exemple: *Taille* (pour un individu), *Temps pour ce jour* (avec un événement), ... Utilisez cette possibilité pour stocker des extraits d'informations collectées et vous souhaitez correctement les lier à vos sources. Les attributs peuvent être utilisés pour les individus, les familles, les événements et les objets media.
2.  La de l'attribut. Par exemple *1.8, ou les yeux bleus*.

Toutes ces informations sont saisies dans des zones de texte. Le nom de l'attribut peut aussi être sélectionné dans le menu déroulant . Cochez la case pour marquer cet attribut comme privé. Ceci sera utilisé dans les impressions, pour ne pas montrer les attributs privés si tel est votre choix lors de l'activation de l'édition.

- Citations/Sources

L'onglet affiche les sources d'information sur l'attribut et permet leur modification. La partie centrale de la fenêtre montre la liste des citations et sources associées à l'attribut, conservées dans la base de données. Les boutons , et vous permettent respectivement d'ajouter, modifier et supprimer une source et citation pour l'attribut. Notez que les boutons et ne sont disponibles qu'après avoir sélectionné une citation/source dans la liste.

- Note

L'onglet contient les notes concernant l'attribut. Si vous voulez ajouter ou modifier des notes, il vous suffit de modifier le contenu de la zone de texte.

L'option vous permet de choisir le rendu de la note dans la sortie (édition ou bien page Web). Choisir remplacera les espaces multiples, les tabulations et les changements de lignes simples par un espace. Les lignes vides (deux changements de lignes consécutifs) sont comprises comme une fin de paragraphe. Au contraire, choisir conservera à l'identique les espaces multiples, les tabulations et les changements de ligne comme ils ont été saisis dans la zone de texte.

## Adresses

Les adresses sont modifiées en utilisant la fenêtre : ![[_media/Address_editor-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Éditeur d&#39;adresse]]

Le haut de la fenêtre contient le titre, incluant le nom de la personne dont l'adresse est en cours de modification. La partie médiane de la fenêtre contient des onglets pour différents types d'information. Le bas de la fenêtre contient les boutons et . Le bouton a pour effet d'appliquer toutes les modifications dans la base de données et de fermer la fenêtre. Le bouton ferme la fenêtre sans modifier la base de données.

Les onglets donnent accès aux types d'informations suivants :

La partie haute permet la modification des informations générales de l'adresse. Ceci comprend les zones de saisie suivantes :

1.  : date pour laquelle l'adresse est valide.

2.  : la rue de l'adresse.

3.  : le hameau, le quartier.

4.  : la ville ou le village de l'adresse.

5.  : la région ou la province de l'adresse / le département ou le comté.

6.  : le pays de l'adresse.

7.  : le code postal.

8.  : le numéro de téléphone lié à l'adresse.

Ces données sont saisies dans des zones de texte libre. Cochez la case pour marquer cette adresse comme privée. Ceci sera utilisé dans les rapports, pour ne pas montrer les adresses privées si tel est votre choix lors de l'activation de l'édition.

- Citations/Sources

L'onglet affiche les sources d'information sur l'adresse et permet leur modification. La partie centrale de la fenêtre montre la liste des sources et citations associées à l'adresse, conservées dans la base de données. La partie du haut montre le détail de la citation/source sélectionnée s'il y a lieu. Les boutons , et vous permettent respectivement d'ajouter, modifier et supprimer une source et citation pour l'adresse. Notez que les boutons et ne sont disponibles qu'après avoir sélectionné une citation/source dans la liste.

- Note

L'onglet affiche les notes sur l'adresse et permet leur modification. Les notes sont un simple texte libre associé à la personne. Pour modifier les notes, simplement modifiez le texte dans la zone de saisie de l'onglet.

L'option vous permet de choisir le rendu de la note dans la sortie (édition ou bien page Web). Choisir remplacera les espaces multiples, les tabulations et les changements de lignes simples par un espace. Les lignes vides (deux changements de lignes consécutifs) sont comprises comme une fin de paragraphe. Au contraire, choisir conservera à l'identique les espaces multiples, les tabulations et les changements de ligne comme ils ont été saisis dans la zone de texte.

## Fusionner des enregistrements

Quelque fois plusieurs enregistrements dans la base de données peuvent décrire le même objet: même personne, même lieu, ou même citation/source. Cela peut arriver soit quand les données sont entrées deux fois par erreur, soit quand une nouvelle information révèle que deux entrées réfèrent à la même personne. Cela peut également provenir de l'importation d'un GEDCOM obtenu par un parent, dont la base de donnée recouvre vos données existantes.

Quand cela se produit, la fusion est le moyen de corriger ces données.

### Fusion des individus

Quand les deux individus sont sélectionnés, choisissez pour appeler .

- Comparer et fusionner

![[_media/Merge_dialog_expanded-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Comparer les individus]]

La fenêtre vous permet de garder ou non les données de chaque individu. Si vous ne voulez pas fusionner les données, choisissez le bouton , pour fermer la fenêtre sans fusion. Sinon, sélectionnez les boutons "radio" pour définir la personne conservée, puis cliquer sur .

Les données non conservées seront des données alternatives. Tous les [Noms](#Noms) de l'autre personne deviendront des noms alternatifs de l'individu. De même, les parents, conjoints, et enfants de l'autre enregistrement deviendront parents, conjoints, et enfants alternatifs de l'enregistrement fusionné, et ainsi de suite.

![[_media/Merge_dialog_regular-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fusion rapide]]

Ce dialogue vous permet de fusionner rapidement deux enregistrements, en spécifiant l'enregistrement primaire. Les données de l'autre enregistrement seront conservées comme alternatives. Spécifiquement, tous les noms de l'autre enregistrement deviendront des noms alternatifs de l'individu. De même, les parents, conjoints, et enfants de l'enregistrement fusionné, le seront aussi.

  

### Fusion des familles

Quand deux familles sont sélectionnées, choisissez pour appeler le dialogue de .

La fenêtre vous permet de garder ou non les données de chaque familles.

Si vous ne voulez pas fusionner les données, choisissez le bouton , pour fermer la fenêtre sans fusion.

Sinon, sélectionnez les boutons "radio":

- 
- 

pour chaque enregistrement à conserver, puis cliquer sur .  

### Fusion des événements

Quand deux événements sont sélectionnés, choisissez pour appeler le dialogue de .

La fenêtre vous permet de garder ou non les données de chaque événements.

Si vous ne voulez pas fusionner les données, choisissez le bouton , pour fermer la fenêtre sans fusion.

Sinon, sélectionnez les boutons "radio":

- 
- 

pour chaque enregistrement à conserver, puis cliquer sur .

  

### Fusion des sources

![[_media/Merge_sources_regular-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fusion des sources (standard)]]

Quand deux sources sont sélectionnées, choisissez pour appeler la fenêtre de .

![[_media/Merge_sources_expanded-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fusion des sources (étendu)]]

La fenêtre vous permet de garder ou non les données de chaque sources.

Si vous ne voulez pas fusionner les données, choisissez le bouton , pour fermer la fenêtre sans fusion.

Sinon, sélectionnez les boutons "radio":

- Titre
- Auteur
- Abréviation
- Information de publication
- ID

pour chaque enregistrement à conserver, puis cliquer sur .

  

### Fusion des lieux

![[_media/Merge_places_expanded-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fusion des lieux (étendu)]]

Quand deux lieux sont sélectionnées, choisissez pour appeler le dialogue de .

![[_media/Merge_places_regular-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fusion des lieuxs (standard)]]

La fenêtre vous permet de garder ou non les données de chaque lieux.

Si vous ne voulez pas fusionner les données, choisissez le bouton , pour fermer la fenêtre sans fusion.

Sinon, sélectionnez les boutons "radio":

- Titre
- Latitude
- Longitude
- Emplacement
- ID

pour chaque enregistrement à conserver, puis cliquer sur .

  

### Fusion des objets media

Quand deux objets media sont sélectionnés, choisissez pour appeler le dialogue de .

La fenêtre vous permet de garder ou non les données de chaque objets media.

Si vous ne voulez pas fusionner les données, choisissez le bouton , pour fermer la fenêtre sans fusion.

Sinon, sélectionnez les boutons "radio":

- 
- 

pour chaque enregistrement à conserver, puis cliquer sur .  

### Fusion des dépôts

Quand deux dépôts sont sélectionnés, choisissez pour appeler le dialogue de .

La fenêtre vous permet de garder ou non les données de chaque dépôts.

Si vous ne voulez pas fusionner les données, choisissez le bouton , pour fermer la fenêtre sans fusion.

Sinon, sélectionnez les boutons "radio":

- 
- 

pour chaque enregistrement à conserver, puis cliquer sur .  

### Fusion des notes

Quand deux notes sont sélectionnées, choisissez pour appeler le dialogue de .

La fenêtre vous permet de garder ou non les données de chaque notes.

Si vous ne voulez pas fusionner les données, choisissez le bouton , pour fermer la fenêtre sans fusion.

Sinon, sélectionnez les boutons "radio":

- 
- 

pour chaque enregistrement à conserver, puis cliquer sur . {{-}}

## Étiquettes

![[_media/Menu_Edit_Tag_OrganizeTagsWindow-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Organiser les étiquettes]] ![[_media/EditPersonEditor_TagSelectionWindow-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sélection d&#39;étiquettes dans l&#39;éditeur d&#39;individu]] {{-}}

[M](wiki:Category:Fr:Documentation)
