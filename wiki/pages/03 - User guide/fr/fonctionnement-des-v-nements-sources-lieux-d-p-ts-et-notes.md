---
title: Fr:Manuel wiki pour Gramps 6.0 - Fonctionnement des événements, sources, lieux,
  dépôts et notes
categories:
- Fr:Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 120407
wiki_fetched_at: '2026-05-30T18:40:31Z'
lang: fr
---

{{#vardefine:chapter\|7.2}} {{#vardefine:figure\|0}}

## Édition de l'information sur les événements

Les événements sont modifiés dans la fenêtre d'édition d'un . Cette fenêtre est également disponible depuis le dialogue d' ou le dialogue .

Le haut de la fenêtre contient le nom de la personne dont un événement est en cours de modification.

![[_media/Edit_event-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Éditeur d'événement]]

La partie haute permet la modification des caractéristiques les plus communes de l'événement :

1.  Le type est choisi dans une liste déroulante prédéfinie, accessible par le menu , par exemple: *inhumation, baptême, ...* .

2.  La d'un événement peut être exacte, une période (*de ..à .., entre*) ou moins précise (*vers*).

3.  Laissez le champ vide si vous n'en avez pas besoin ou si vous souhaitez utiliser l'[outil d'ajout automatique des descriptions](wiki:Gramps_6.0_Wiki_Manual_-_Tools/fr#Extrait_les_descriptions_de_l.27.C3.A9v.C3.A9nement_depuis_ses_donn.C3.A9es).

4.  L' est un enregistrement unique pour identifier l'événement, laissez Gramps le désigner.

5.  

Cochez la case pour marquer cet événements comme privé. Ceci sera utilisé dans les rapports, pour ne pas montrer les événementss privés si tel est votre choix lors de l'activation de l'édition.

La seconde partie de la fenêtre montre des onglets présentant différentes informations. Les onglets donnent accès aux types d'informations suivantes :

- Sources

L'onglet affiche les sources d'information sur l'événement et permet leur modification. La partie centrale de la fenêtre montre la liste des sources associées à l'événements, conservées dans la base de données. La partie du haut montre le détail de la source sélectionnée s'il y a lieu. Les boutons , et vous permettent respectivement d'ajouter, modifier et supprimer une source pour l'événements. Notez que les boutons et ne sont disponibles qu'après avoir sélectionné une source dans la liste.

- Note

L'onglet contient les notes concernant l'événement. Si vous voulez ajouter ou modifier des notes, il vous suffit de modifier le contenu de la zone de texte.

La partie du bas contient les boutons et .

Les boutons a pour effet d'appliquer toutes les modifications dans la base de données et de fermer la fenêtre. Le bouton ferme la fenêtre sans modifier la base de données.

## Édition des références à l'événement

![[_media/Add_event-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Information sur l'événement]]

Les références à l'événement connectent un événement à un individu et vous permettent de détailler des informations sur l'événement.

Quand vous ajoutez une référence d'événement à une personne, le dialogue suivant apparaît:

Ce dialogue comprend deux sections différentes, et .

- La partie affiche : , , , , , .
- La partie indique les détails associés à un référence de cet événement: , , .

Pour le rôle de l'individu pour cet événement, utilisez *Principal* pour les acteurs majeurs, sinon utilisez un rôle descriptif (Ex., *Témoin, Célébrant, Déclarant ...*).

## Édition de l'information sur les objets media

![[_media/Edit_media-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Éditeur de propriété du medium]]

Pour changer les propriétés d'un objet multimedia, allez dans la vue et sélectionnez celui que vous voulez. Double-cliquez ou cliquer sur le bouton dans la barre d'outils pour afficher la fenêtre de dialogue :

Sous le titre de la fenêtre, vous trouvez une vignette de l'objet et un résumé de ses propriétés (ID, chemin, date et type d'objet).

1.  Un descriptif utilisé pour cet objet.

2.  est un enregistrement unique pour identifier cet objet, laissez Gramps le désigner.

3.  La peut être pour une image, la date de l'objet.

4.  Le de ce medium sur votre ordinateur. Gramps ne stocke pas le fichier en interne, il ne stocke que le chemin ! Définissez le [chemin relatif](wiki:Gramps_6.0_Wiki_Manual_-_Settings/fr#G.C3.A9n.C3.A9ral) dans les pour éviter de saisir à chaque fois le répertoire de base dans lequel vos fichiers sont stockés. L'outil [Gestionnaire de Media](wiki:Gramps_6.0_Wiki_Manual_-_Tools/fr#Gestionnaire_de_Media...) peut vous aider à gérer les chemins de votre collection d'objets media.

5.  La valeur correspond à l'extension de cet objet.

La partie centrale de la fenêtre contient des onglets pour diverses catégories d'informations. La partie du bas contient les boutons et . Le bouton a pour effet d'appliquer toutes les modifications dans la base de données et de fermer la fenêtre. Le bouton ferme la fenêtre sans modifier la base de données.

Les onglets donnent accès aux types d'informations suivants :

- Général

L'onglet permet la modification du titre qui identifie l'objet dans la base de données. Il est saisi dans une zone de saisie de texte libre. Le champ permet d'entrer une date LED à l'aide du , pour une saisie plus graphique.

- Attributs

L'onglet présente les informations sur les attributs des objets multimédia. La partie du bas affiche la liste de tous les attributs de l'objet considéré. La partie du haut montre le détail de l'attribut sélectionné s'il y a lieu. Les boutons , , et permettent respectivement l'ajout, la modification et la suppression d'un attribut. Notez que les boutons et ne sont disponibles que lors de la sélection d'un attribut dans la liste.

- Notes

L'onglet affiche les notes sur l'objet multimédia modification. Les notes sont un simple texte libre associé à la relation. Pour modifier les notes, changez simplement le texte dans la zone de saisie de l'onglet.

- Références

L'onglet liste les objets de la base de données qui font référence à l'objet multimédia. Si cet objet n'est jamais référencé, la liste est vide. Si au contraire il est référencé de nombreuses fois, la liste montrera tous les éléments de la base de données concernés. Elle peut être triée par n'importe quelle colonne, en cliquant sur son en-tête : , , ou . Double-cliquer sur un objet de la liste permet d'ouvrir l'éditeur de medium.

## Édition des références de l'objet medium

![[_media/Mediaobj_ref-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Références de l'objet medium]]

Les références de l'objet medium lient un [object medium](http://fr.wikipedia.org/wiki/M%C3%A9dia) à un autre objet.

- Région (coins x1, x2, y1, y2)

La partie permet de sélectionner une région spécifique de l'objet medium.

Vous pouvez utiliser le curseur de la souris sur l'image pour sélectionner une région, ou utiliser les valeurs à définir en partant du haut à gauche vers le bas à droite d'une région. Le point (0,0) est en haut à gauche de l'image, et le point (100,100) est le coin en bas à droite.

- Vie privée

Le bouton permet de marquer un enregistrement comme étant privé. Cliquez sur l'icône pour rendre cet enregistrement privé.

  

## Édition de l'information sur les lieux

![[_media/Edit_plc-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Éditeur de lieu]] Pour modifier les données sur un lieu, allez dans la vue , sélectionner celui que vous voulez puis double-cliquez ou utilisez l'icône dans la barre d'outils pour lancer la fenêtre de dialogue :

Les champs suivants sont disponibles :

- Le titre en haut affiche la description du lieu qui sera utilisé dans les rapports. Gramps va le générer pour vous. Voir les [Préférences &gt; Affichage &gt; Active la génération automatique du titre du lieu](wiki:Gramps_6.0_Wiki_Manual_-_Settings/fr).

Le haut de la fenêtre contient:

- Le : le nom complet du lieu.

- : le type de lieu. Tous les types **Personnalisés** saisis comme **Type** sont affichés en bas de la liste. Choisissez l'un des **Types** fournis par défaut :

<!-- -->

- - Borough (Arrondissement)
  - Bourg
  - Comté (Départ.)
  - District (Arrondissement)
  - Département
  - Ferme
  - Hameau
  - Immeuble
  - **Inconnu** (défaut)
  - Lieu-dit
  - Municipalité
  - Quartier
  - Numéro- Voir [Suppression de la virgule dans une adresse saisie](wiki:Gramps_6.0_Wiki_Manual_-_Settings/fr)
  - Paroisse
  - Pays
  - Province
  - Province (Région)
  - Région
  - Quartier
  - Région
  - Rue
  - Village
  - Ville

- L' : un enregistrement unique pour identifier le lieu. Laissez Gramps le désigner.

-   
  la position du lieu par rapport à l'équateur, en notation décimale ou en degrés. Des exemples de valeurs valides : *12.0154*, *50°52'21.92"N*, *N50º52'21.92"* ou *50:52:21.92*. Vous pouvez définir ces valeurs via la vue Géographie en cherchant ce lieu, ou via un service cartographique dans la vue Lieux.

-   
  la position relative du lieu par rapport au méridien Premier, ou Greenwich, en notation décimale ou en degrés. Des exemples de valeurs valides : *-124.3647*, *124°52'21.92"E*, *E124º52'21.92"* ou *124:52:21.92*. Vous pouvez définir ces valeurs via la vue Géographie en cherchant ce lieu, ou via un service cartographique dans la vue Lieux.

{{-}}

### Formats de Longitude/Latitude supportés

Quand vous créez ou modifiez un lieu, les formats supportés pour la longitude/latitude sont :

`       'D.D4'    : notation degré, 4 décimales `  
`                   ex : `*`+12.0154 , -124.3647`*  
`       'D.D8'    : notation degré, 8 décimales (précision ISO-DMS) `  
`                   ex : `*`12.01543265 , -124.36473268`*  
`       'DEG'     : notation degré, minutes, secondes`  
`                   ex : `*`50°52'21.92"N , 124°52'21.92"E (° a le code UTF-8 c2b00a)`*  
`                   ou `*`N50º52'21.92" , E124º52'21.92" (° a le code UTF-8 c2ba0a)`*  
`                   Le caractère seconde peut être " ou deux '.`  
`                   Les lettres N/S/W/E peuvent être placées avant ou après les valeurs.`  
`       'DEG-:'   : notation degré, minutes, secondes avec :`  
`                   ex : `*`-50:52:21.92 , 124:52:21.92`*  
`       'ISO-D'   : notation ISO 6709 degré`  
`                   ex : `*`±DD.DDDD±DDD.DDDD`*  
`       'ISO-DM'  : notation ISO 6709 degré, minutes`  
`                   ex : `*`±DDMM.MMM±DDDMM.MMM`*  
`       'ISO-DMS' : notation ISO 6709 degré, minutes, secondes`  
`                   ex : `*`±DDMMSS.SS±DDDMMSS.SS`*

### Onglets de la fenêtre de modification

![[_media/Lieuedit3-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Onglets de l'éditeur de lieu]]

Les onglets donnent accès aux types d'informations suivants :

- Partie de

Les lieux dans Gramps sont enregistrés de façon hiérarchique. L'onglet permet lier un lieu à un autre, de rang supérieur dans la hiérarchie et qui le contient.Chaque lien est un lieu avec éventuellement une période. Les boutons , , et permettent d'ajouter (si le lieu n'a pas déjà été créé), partager (sélectionner un lieu déjà créé), modifier ou supprimer un lien. Un pays représente le sommet de la hiérarchie et ne fera pas partie d'un autre lieu.

Ainsi, par exemple, un village français - *partie de* -\> une commune - *partie de*-\> un arrondissement - *partie de* -\> un département.

L'enregistrement de ces informations est utile pour distinguer des lieux (village, commune,…) qui peuvent avoir le même nom dans des régions différentes, mais aussi pour les localiser plus facilement : il n'est pas aisé de savoir où se situe le hameau « La Cudraz », mais c'est plus facile si l'on sait qu'il fait partie de la commune de « La Léchère », arrondissement d'Albertville en Savoie, France. {{-}}

- Noms alternatifs

![[_media/Lieux_lang_date-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Les noms alternatifs suivant date de langue]] L'onglet permet de saisir des équivalences et variantes orthographiques pour ce lieu ainsi que les périodes pour chaque nom. L'exemple typique est la ville de Saint Pétersbourg qui s'est appelé Léningrad à une période puis Pétrograd à une autre. Ainsi, suivant la date des évènements, ils pourront afficher le nom correspond du lieu à cette époque. Le nom de la ville peut aussi varier avec les langues. On peut donc associé un nom à une langue en utilisant une abréviation pour cette langue dans le champ correspondant ; exemple « Londres » avec « fr » pour la langue et « London » avec « en » pour la langue.

- Note

L'onglet contient les notes concernant le lieu. Si vous voulez ajouter ou modifier des notes, il vous suffit de modifier le contenu de la zone de texte.

- Citations

L'onglet affiche les sources d'information en lien avec le lieu et permet leur modification. La partie centrale de la fenêtre montre la liste des sources associées au lieu, conservées dans la base de données. La partie du haut montre le détail de la source sélectionnée s'il y a lieu avec sa date. Les boutons , et vous permettent respectivement de créer une nouvelle source, sélectionner une source existante ou supprimer une source pour le lieu. Notez que les boutons et ne sont disponibles qu'après avoir sélectionné une citation dans la liste.

- Galerie

L'onglet affiche les données des objets multimédia associés au lieu et permet leur modification. La partie centrale de la fenêtre montre tous les objets multimédia conservés dans la base de données. Les objets qui sont des fichiers-images valides sont représentés par une vignette. Les autres comme des enregistrements sonores ou video sont représentés par une icône générique. Les boutons , , et vous permettent respectivement d'ajouter un fichier, une référence à un objet de la base, modifier et supprimer un objet multimedia. Notez que les boutons et ne sont disponibles qu'après avoir sélectionné un objet dans la liste.

- Internet

L'onglet présente les informations sur les adresses Internet (URL) associées aux lieux. La partie du bas affiche la liste de tous les adresses Internet du lieu considéré. La partie du haut montre le détail de l'adresse sélectionnée s'il y a lieu. Les boutons , et permettent respectivement l'ajout, la modification et la suppression d'une adresse. Le bouton permet d'ouvrir une page Internet avec votre navigateur favori. Notez que les boutons , et ne sont disponibles que lors de la sélection d'une adresse dans la liste.

- Références

L'onglet liste les objets de la base de données qui font référence à ce lieu. On ne peut pas modifier les liens des objets de la base de données vers les lieux à l'aide de l'. Il faut ouvrir l'objet citant le lieu (par exemple un événement de naissance) puis modifier la référence de lieu.

La partie du bas contient les boutons et . Le bouton a pour effet d'appliquer toutes les modifications dans la base de données et de fermer la fenêtre. Le bouton ferme la fenêtre sans modifier la base de données.

Voir aussi [Lieux dans Gramps](wiki:Lieux_dans_Gramps).

## Édition de l'information sur les sources

Pour modifier les données sur les sources, allez dans la vue et sélectionnez celle que vous voulez modifier. Double-cliquez sur la ligne voulue ou cliquez sur le bouton dans la barre d'outils pour lancer le dialogue : ![[_media/Edit_src-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Éditeur de source]]

Le haut de la fenêtre contient le titre . La partie principale de la fenêtre contient des onglets pour afficher différentes catégories d'information.

L'information générale en haut de la fenêtre vous permet de préciser les informations basiques sur une source:

1.  : le titre de la source.

2.  : les auteurs de la source.

3.  : un enregistrement unique pour identifier la source.

4.  : fournit un simple titre utilisé pour trier, classer et trouver les enregistrements de la source.

5.  : des informations telles que un village, l'année de publication, le nom de l'organisme publiant cette source, ...

Vous pouvez saisir directement l'information dans les champs adjacents.

Les onglets donnent accès aux types d'informations suivants :

- Note

L'onglet contient les notes concernant la source. Si vous voulez ajouter ou modifier des notes, il vous suffit de modifier le contenu de la zone de texte.

- Galerie

L'onglet affiche les données des objets multimédia associés à la source et permet leur modification. La partie centrale de la fenêtre montre tous les objets multimédia conservés dans la base de données. Les objets qui sont des fichiers-images valides sont représentés par une vignette. Les autres comme des enregistrements sonores ou vidéo sont représentés par une icône générique. Les boutons , , et vous permettent respectivement d'ajouter un fichier, une référence à un objet déjà dans la base, modifier et supprimer un objet multimedia. Notez que les boutons et ne sont disponibles qu'après avoir sélectionné un objet dans la liste.

- Données

L'onglet montrent les paires de "clés/valeurs" qui peuvent être associées à la source. Elles sont semblables aux "attributs" utilisés pour d'autres types d'enregistrement. La différence reste que les attributs peuvent avoir des références, des sources et des notes, les données ne peuvent pas.

La partie centrale montre la liste de toutes les paires de valeurs clefs éventuelles. Les boutons et vous permettent également d'ajouter et enlever des paires. Pour modifier le texte, choisissez d'abord l'entrée désirée (peut être une entrée vide). Cliquez alors à l'intérieur du champ. Quand vous avez fini, cliquer en dehors de la cellule pour sortir.

![[_media/Add_repository_2-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Éditeur de dépôt]]

- Dépôts

L'onglet liste les références aux dépôts dans lesquels une source est contenue. Cette liste peut être triée par n'importe quelle en-tête de colonne: , , , et . Double-cliquer sur une source de la liste permet de voir et d'éditer l'enregistrement. Vous pouvez également éditer la référence. Les boutons sur le côté vous permettent d'ajouter un nouveau dépôt, d'éditer la référence au dépôt, ou d'enlever une référence.

- Références

L'onglet liste les objets de la base de données qui font référence à la source. Si cette source n'est citée dans aucun objet, la liste est vide. Si au contraire elle est citée de nombreuses fois, la liste les montrera tous. Elle peut être triée par n'importe quelle colonne, en cliquant sur son en-tête : , , ou . Double-cliquer sur une source de la liste permet d'ouvrir l'éditeur de l'enregistrement correspondant.

Le bas de la fenêtre contient les boutons et . Le bouton a pour effet d'appliquer toutes les modifications dans la base de données et de fermer la fenêtre. Le bouton ferme la fenêtre sans modifier la base de données.

## Édition de la citation

Citations connect a Source to another object and allow you to provide additional information about the source. Citations can be attached to a large number of objects,

- [L'information sur l'individu](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_1/fr) (tel que le nom, un attribut, une adresse, etc),
- [Les relations (familles)](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_1/fr),
- [Événements et diverses informations sur l'événement](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_2/fr),
- [Objets media et ses attributs](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_2/fr),
- [Lieux et informations liées](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_2/fr),
- [Adresses et dépôts](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_2/fr).

For each object, a common set of buttons are provided:

- (Create and add a new citation and a new source). This brings up an empty Citation dialog.

- (Add an existing citation or source). This brings up the Source or Citation selection dialog box.

- (Edit the selected citation). This brings up the Citation dialog pre-populated with the Citation and source information.

- (Remove the existing citation). This removes the citation from the object. It does not delete the citation itself, which could then be connected to another object.

Note that the and buttons become available only when a citation has been selected.

{{-}}

Quand vous avez besoin d'ajouter une citation ou une source la fenêtre suivante s'ouvre :

![[_media/Citation-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Éditeur de citation]]

Ce dialogue est constitué de deux parties, la et les . La affiche le de la source, son , et les . Le peut être sélectionné depuis la liste des sources dans le menu déroulant. Si la sourcé référencée n'est pas encore présente dans la base de données, vous pouvez la saisir en cliquant sur .

La section indique les détails associés à une référence particulière à cette source: , le , la et les . Vous pouvez choisir le niveau de confiance depuis la liste déroulante . Les détails peuvent être saisis dans les champs texte correspondants.

1.  : la date associée avec la référence de la source. Typiquement utilisé pour stocker la date à un temps donné (quand le texte a été ajouté à la source originale).

2.  : un emplacement spécifique avec l'information référencée. Pour un travail de publication, ceci peut correspondre au volume d'un travail en plusieurs parties et le numéro de(s) page(s). Pour un périodique, ceci peut correspondre à un volume, et les numéros de pages. Pour un journal, ceci correspond à un numéro de colonne et de page. Pour une source non-publiée, ceci peut être le numéro de feuillet, le numéro de page, de partie, etc. Un enregistrement pour le recensement peut avoir un numéro de ligne ou la localisation d'une famille en supplément du numéro de page.

3.  : traduit la confiance placée dans la qualité de la source transmise ou la crédibilité de cette partie d'information, basé sur les preuves. Il ne vise pas à éliminer les besoins de vérifier les preuves.

    1.  Très faible = sans preuve ou des données estimées.
    2.  Faible = une preuve qui amène à un questionnement (interviews, recensements, généalogies orales, une auto-biographie).
    3.  Élevé = une preuve secondaire, des données officiellement enregistrées parfois après un événement.
    4.  Très élevé = une preuve directe et principale, ou une preuve infaillible.

A warning icon is displayed if the citation is shared.

The tabs provide the following information categories of citation data:

- Note

The tab provides a place to record notes or comments about the citation. The central part of the window lists all notes for this citation, and gives you a preview of the beginning of the note. The buttons , , , , and let you add a new note, share the selected note, edit the selected note, remove the selected note and move the selected note up or down the list of notes. Note that the , , , and boutons become available only when a media object is selected from the list. Removing a note only removes the note from this citation, it does not delete the note itself. Please refer to [détails sur l'édition des notes](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_2/fr#Editing_information_about_notes).

- Galerie

L'onglet vous permet store and display photos and other media objects associated with a given citation (for example, a photo of a page of a book or a page of a census). The central part of the window lists all such objects and gives you a thumbnail preview of image files. Other objects such as audio files, movie files, etc., are represented by a generic Gramps icon. The buttons , , and let you add a new image, add a reference to an existing image, modify an existing image, and remove a media object's link to the citation. Note that the and buttons become available only when a media object is selected from the list. Please refer to [détails sur les références du support medium](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_2/fr).

- Données

The tab displays "Key/Value" pairs that may be associated with the citation. These are similar to the "Attributes" used for other types of Gramps records. The difference between these Key/Value pairs and Attributes is that Attributes may have source citations and notes, while Key/Value data may not.

The central part of the window lists all existing Key/Value pairs. The buttons and let you add and remove pairs. To modify the text of Key or Value, first select the desired entry. Then press the button to select the Key, or click in either the Key or Value cell of that entry and type your text. When you are done, click outside the cell to exit editing mode.

- Références

The tab lists all the database records that refer to this source, if any. The list can be ordered by any of its column headings: , , or . Double-clicking an entry allows you to view and edit the record.

### Information partagée de la source

displays the of the Source, its , and . A warning icon is displayed if the source is shared. Editing the source information in this dialog is just the same as [édition des informations sur les sources](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_2/fr).

## Édition de l'information sur les dépôts

![[_media/Edit_repo-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Éditeur de dépôt]]

La partie du haut permet de saisir:

1.  Le du dépôt.
2.  L': un enregistrement unique pour identifier le dépôt. Laissez Gramps le désigner.
3.  Le de dépôt, par exemple: *une bibliothèque, une archive*...

- Note

L'onglet fournit un emplacement pour les notes et commentaires sur le dépôt. Pour ajouter ou modifier une note existante simplement éditez le texte dans le champ texte.

- Adresses:

L'onglet vous permet de voir et éditer les adresses de votre dépôt.

La partie basse de la fenêtre liste toutes les addresses stockées dans la base de données. La partie du haut affiche les détails de l'adresse actuellement sélectionnée dans la liste. Les boutons , , et vous permettent de respectivement ajouter, modifier, et enlever une adresse de la base de données. Notez que les boutons et ne sont seulement disponibles lorsqu'une adresse est sélectionnée dans la liste.

- Internet:

L'onglet affiche les liens internet liés à ce dépôt. La partie basse liste les adresses internet et leurs descriptions. La partie haute de la fenêtre affiche les détails de la sélection. Les boutons , , et vous permettent d'ajouter, de modifier, et supprimer une adresse internet. Le bouton (représenté par l'icône avec une flèche verte et un cercle jaune) ouvre votre navigateur internet et vous conduit à l'adresse sélectionnée. Notez que les boutons , et sont seulement disponibles lorsqu'une adresse est sélectionnée dans la liste.

- Références

L'onglet liste les objets de la base de données qui font référence à la source. Si le dépôt n'est citée dans aucune source, la liste est vide. Si au contraire il est cité de nombreuses fois, la liste affichera ces sources. La liste peut être triée par n'importe quelle colonne, en cliquant sur son en-tête : , , ou . Double-cliquer sur une ligne de la liste permet d'ouvrir l'éditeur de la source.

## Édition de l'information sur les notes

### L'onglet Note

L'onglet est l'emplacement pour ajouter des notes aux individus, sources, .... L'onglet vous permet de trier les notes. Comme les autres onglets, vous pouvez ajouter des notes, partager des notes existantes avec l'objet se lequel vous travaillez ou enlever des notes (elles ne seront pas supprimer de votre base de données).

### L'éditeur de note

![[_media/Edit_note-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Éditeur de note]] Quand vous créez une nouvelle note, ou quand vous éditez une note, l'éditeur de note est nécessaire. Il y a deux onglets, l'onglet , et l'onglet .

- L'onglet Note

L'onglet a les éléments suivants :

:\* Une barre d'outils pour le style de vos notes. Vous pouvez sélectionner et appliquer un des boutons, ou définir une valeur pour commencer à saisir.

::\* Défaire, Refaire:

::\* *italique*, **gras**, <u>souligné</u> : fonctions courantes des éditeur de texte

::\* La sélection de la police de caractère : un simple sélecteur de police affichant les polices de caractère disponibles sur votre système.

::\* La taille de la police de caractère : la taille de la police utilisée

::\* La couleur de la police : écrire la police dans une certaine couleur

::\* La couleur d'arrière-plan : ajoute une couleur d'arrière plan au texte saisi

::\* Effacer les balises : ceci enlèvera toutes les balises placées dans votre note

::\* Lien : ceci permet de créer un lien vers un objet Gramps, tel qu'un individu, une famille, un événement, une note, etc...

:\* Un menu contextuel dans l'aire du texte.

  
  
L'entrée la plus pratique dans le menu contextuel est la sélection de l'orthographe. Vous disposez du choix des langages installés sur votre système avec la vérification orthographique activée.

:\* L'aire du texte permettant de saisir la note

:\* Quelques propriétés de votre note :

::\* : un identifiant unique pour la note. Si vous ne saisissez rien un identifiant automatique sera utilisé d'après votre choix défini dans les préférences.

::\* : une valeur marqueur pour la note : Complet, ÀFaire. Vous pouvez ajouter votre propre marqueur en le saisissant dans le champ vide.

::\* : le type de note. Vous pouvez ajouter une valeur personnalisée.

::\* un choix : les notes dans Gramps peuvent être mises en forme pour une belle présentation dans les rapports. Par défaut, les nouvelles lignes et espaces blancs seront automatiquement ignorés pour générer un paragraphe complet, lequel est défini par une ligne vide entre deux blocs de texte. Quand la note est , Gramps prendra en considération les espaces blancs et entrées utilisés dans la note. Utilisez cette option pour les tableaux, la transcription littérale, ... . Ne pas utilisez si vous en avez pas besoin, les rapports gagneront en cohérence visuelle. Utilisez la police de caractère monospace pour conserver le préformatage.

:\*\* : comme pour les autre objets, vous pouvez définir une note comme étant privée pour être certain(e) que cette note puisse être ignorée d'un seul clic lors de l'exportation.

- Références

L'onglet indique tous les objets liés à cette note. Cette liste peut être triée d'après l' en-tête de colonne: , , ou . Cliquez deux fois sur une entrée vous permet de voir et éditer l'enregistrement correspondant.

##### Éditeur de lien

![[_media/Note-showing-tooltip-for-link-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Éditeur de liens - Linking text]] ![[_media/Note-LinkEditor-dialog-default-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Éditeur de lien - dialogue - exemple]]

The has the following options:

- allows you to create an external link to an Internet Address (\[<https://en.m.wikipedia.org/wiki/URL>\|<abbr title="Uniform Resource Locator, also known as a web address">URL</abbr>\]) or an item in Gramps, comme un événement, famille, medium, note, individu, lieu, dépôt, source, ou citation\]\].

-  button : opens the selector dialog for existing items in the category specified in the Link Type.

  - button

- - button : opens the editor dialog for the specified Gramps item

- 

### Balise et préformaté dans les rapports

Une balise (**gras**, couleur, <u>souligné</u>, ...) peut être ajoutée aux notes. Une note peut être préformatée ou non. Ceci influence l'affichage de la note. Voici un aperçu de ce que vous pouvez obtenir.

1.  **Pdf** et **Impression directe** (vers une imprimante ou un fichier) supportent totalement les balises et les préférences du formatage.
2.  **Texte** va enlever toutes les balises des notes car ce format ne les supporte pas.
3.  **LaTeX** va tenter de supporter les balises de son mieux. LaTeX n'est pas vraiment un langague pour définir le type et ajouter un style personnalisé. Ceci casserai les possibilités permises par LaTex. Par conséquent :

:\* **gras**, <u>souligné</u> et *italique* sont supportés

:\* la taille de la police est enregistrée de la même manière que sous LaTeX.

:\* Les polices Mono comme une police Mono avec espaces

:\* La couleur et la police ne sont pas supportées

:\* Le préformatage est géré correctement

1.  Le rapport internet **Saga**. De nombreuses personnes utilisent le rapport Saga comme un moyen simple de travailler avec leurs données. Ce rapport essaye de suivre les balises des notes.
2.  Le format **ODF** ne supporte pas les balises pour le moment. Ceci sera ajouté par la suite.
3.  Le format **RTF** ne supporte pas les balises pour le moment.
4.  Le format **html** ne supporte pas les balises pour le moment.

La conclusion étant de n'utiliser les balises dans les notes que pour un gain dans les informations déjà présentes. **Gramps n'est pas un éditeur de texte**.

[M](wiki:Category:Fr:Documentation)
