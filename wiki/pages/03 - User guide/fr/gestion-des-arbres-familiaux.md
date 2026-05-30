---
title: Fr:Manuel wiki pour Gramps 6.0 - Gestion des arbres familiaux
categories:
- Fr:Documentation
managed: false
source: wiki-scrape
wiki_revid: 120296
wiki_fetched_at: '2026-05-30T18:46:31Z'
lang: fr
---

{{#vardefine:chapter\|5}} {{#vardefine:figure\|0}} Abordons l'exploration détaillée pour utiliser Gramps au quotidien. Dans ce chapitre voici un aperçu détaillé pour gérer vos arbres familiaux, ainsi que la méthode pour partager vos données avec les autres généalogistes.

## Commencer un nouvel arbre familial

Pour démarrer avec un nouvel arbre familial, choisissez ou sélectionnez le bouton depuis la barre d'outils ou utilisez la raccourci clavier . Ceci ouvrira le gestionnaire d'arbre familial.

Sélectionnez le bouton et Gramps ajoutera un nouvel arbre familial dans la liste. Pour changer le nom *Arbre familial 1* défini par défaut, cliquez sur le nom et cliquez sur le bouton pour saisir le nouveau nom.

Pour ouvrir le nouvel arbre vide, sélectionnez-le puis cliquez le bouton ou double-cliquez sur son nom.

{{-}}

### Gestion des arbres familiaux

![[_media/Gestion_arbres_Focal-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fenêtre de gestion des arbres familiaux]]

Le bouton ouvre la fenêtre de gestion des qui permet de gérer et travailler sur vos arbres familiaux.

Par cette fenêtre, vous pouvez créer un nouvel arbre familial, renommer un arbre existant, supprimer un arbre familial, ou charger un arbre familial ou contrôler les informations à propos de cet arbre. Tous les noms de vos arbres familiaux apparaissent dans la liste. Si un arbre familial est ouvert, une icône apparaît à côté le nom dans la colonne statut. Le type de base de données ainsi que la date et l'heure du dernier accès sont affichés.

- crée un nouvel arbre familial.

- affiche des informations à propos de l'arbre sélectionné.

- l'arbre familial sélectionné. Une boite d'alerte avec une confirmation finale à sélectionner va s'afficher.

- l'arbre familial existant sélectionné.

- l'arbre familial existant sélectionné.

- l'arbre familial existant. Disponible seulement pour les bases de données anciennes BSDDB. Voir : [Converting a BSDDB Family Tree to SQlite](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Converting_a_BSDDB_Family_Tree_to_SQlite)

- l'arbre familial existant sélectionné, disponible seulement si Gramps a détecté un problème.

- option présente seulement si [GNU Revision Control System](http://www.gnu.org/software/rcs/) (RCS) est installé.

- utilisé avec le bouton et l'option est présente seulement si [GNU Revision Control System](http://www.gnu.org/software/rcs/) (RCS) is installed.

- \- cette section.

- \- Ferme la fenêtre de gestion des

- l'arbre familial existant sélectionné.

{{-}}

## Ouvrir un arbre familial

Pour ouvrir un arbre familial, choisissez ou cliquez sur le bouton dans la barre d'outils. Le s'ouvrira et vous verrez une liste des arbres familiaux disponibles dans Gramps. Une icône s'affichera dans la colonne à côté d'un arbre familial actuellement ouvert. Sélectionnez l'arbre que vous désirez ouvrir et cliquez le bouton . Vous pouvez également cliquer deux fois sur l'arbre choisi.

Pour ouvrir un arbre récemment ouvert, choisissez ou la flèche du bas après le bouton et sélectionnez l'arbre familial depuis la liste.

## Ouvrir des bases de données XML ou GEDCOM

Gramps vous permet d'ouvrir certaines bases de données qui n'ont pas été enregistrées au format de Gramps depuis une ligne de commande, voir les [références en ligne de commande](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/fr#Options_d.27ouverture). Ceci comprend les bases de données XML et GEDCOM. Mais vous devez être attentif car si ces bases sont volumineuses, vous risquez de rencontrer des problèmes de performance et en cas de crash vos données peuvent être corrompues. Ainsi, il vaut mieux créer un nouvel arbre familial (base de données) et y importer vos données XML/Gedcom.

## Supprimer un arbre familial

Sélectionnez l'arbre familial que vous voulez supprimer, et cliquez sur le bouton .

Ceci supprimera **complétement** l'arbre, sans possibilités pour récupérer vos données. Pensez à faire une sauvegarde de vos données en exportant au format Gramps XML, et gardez ce fichier.

## Renommer un arbre familial

Vous pouvez renommer un arbre familial (ou une archive) en sélectionnant l'arbre que vous voulez renommer et cliquer sur . Vous pouvez également cliquer sur le nom dans la liste des arbres.

Dans tous les cas, vous avez simplement à saisir le nouveau nom.

## Sauvegarder un arbre familial

- La méthode la plus sûre pour sauvegarder votre arbre familial Gramps est d'exporter sans les options de vie privée et les filtres au format **Gramps XML** (ou **paquet Gramps** qui inclut vos objets media) et copiez le fichier dans un emplacement sûr, de préférence en dehors de votre site de travail.

### Fenêtre de sauvegarde

![[_media/MakeBackup_GrampsXMLBackup-42-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Faire une sauvegarde]]

Sélectionnez le menu .

Vous pouvez choisir d'inclure ou non les media.

Vous pouvez saisir le chemin de sauvegarde manuellement ou par le sélecteur en bout de ligne.

Vous pouvez saisir le nom manuellement ou laisser le nom généré automatiquement.

- Vous pouvez utiliser la fonction Archivage (voir la section suivante) pour stocker un instantané de votre arbre. Ces instantanés peuvent être utilisés pour de simples sauvegardes, utiles si vous voulez essayer quelque chose qui pourra être annulé plus tard. Néanmoins, cette méthode ne devrait pas être utilisée pour des sauvegardes standards, car elles ne peuvent pas survivre à un problème de disque dur ou autres catastrophes pouvant survenir sur votre ordinateur.

<!-- -->

- *Pour les utilisateurs avancés* : chaque base de données est stockée dans son propre sous-répertoire sous ~/.gramps. Une sauvegarde manuelle est possible en sauvegardant ce répertoire. Ce n'est pas recommandé. Il vous est vivement recommandé de plutôt faire la sauvegarde au format Gramps XML.

<!-- -->

- Vous pouvez également définir un schéma de nommage pour la sauvegarde en définissant la variable *paths.quick-backup-filename* dans le fichier ~/.gramps/gramps51/gramps.ini key tel que :

`[paths]`  
`quick-backup-filename='%(filename)s_%(year)d-%(month)02d-%(day)02d.%(extension)s'`

Il faut supprimer les `;;` en début de ligne pour qu'elle soit prise en compte et utiliser n'importe lesquels de ces mots clés dans votre schéma de nommage : year, month, day, hour, minutes, seconds, filename, extension (.gpkg par défaut si vous incluez les media, .gramps si vous excluez les media).

  

## Archiver un arbre familial

Vous pouvez archiver vos arbres familiaux avec Gramps pour garder une copie avant toute modification importante et pour être capable de retourner à une version précise.

Pour faire une archive :

![[_media/ManageFamilyTrees-Archive-RevisionComment-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Exemple d'archivage d'un arbre familial]]

1.  Chargez votre arbre familial
2.  Cliquez sur le bouton (le logo gramps qui affiche la quand vous êtes dessus).
3.  Cliquez sur la base de données que vous venez de charger: le bouton devrait apparaître.
4.  Cliquez sur le bouton et l'on vous demandera un nom de version pour votre archive.

Après l'archivage, la liste de vos arbres familiaux s'affichera avec un triangle sur la gauche.

- Cliquez sur le triangle pour afficher le nom de l'archive.
- Cliquez une nouvelle fois pour refermer la liste d'archives.

Les archives peuvent être supprimés, renommées et extraites.

{{-}}

## Restaurer une archive de l'arbre familial

![[_media/ManageFamilyTrees-Archive-Selected-to-Extract-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sélection de la version à restaurer]]

Simplement activez l'archive que vous voulez restaurer, et sélectionnez le bouton. Gramps va transférer l'archive dans un nouvel arbre familial. Le nom de l'arbre familial est basé sur le nom originel et le nom de l'archive. (voir également [Archiver un arbre familial](#Archiver_un_arbre_familial))

Si vous cliquez sur une archive, le bouton sera visible. Cliquez dessus pour restaurer votre archive. Elle apparaîtra dans la liste comme *\<nom de l'arbre familial\>:\<nom de l'archive\>* et est un arbre indépendant. Ceci peut être une démarche pour préserver une archive, car les archives disparaissent si l'arbre familial est supprimé; et elles ne sont pas incorporées dans l'exportation de l'arbre au format [XML](wiki:XML).

![[_media/ManageFamilyTrees-Archive-Extracted-version-selected-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Version restaurée]]

{{-}}

## Débloquer un arbre familial

Gramps est une application de base de données mono-utilisateur et elle va identifier le fichier de l'arbre en cours d'utilisation avec un ![[_media/22x22-gramps-lock.png]]'verrou'. Quand Gramps ouvre un arbre, il crée un fichier **lock** (avec le nom de l'utilisateur et le domaine) dans le sous-dossier de l'arbre du répertoire **grampsdb** lui-même dans le répertoire Gramps de l'utilisateur, empêchant vous (ou quelqu'un d'autre) d'ouvrir cet arbre au même moment. Une seconde instance de Gramps pourra ouvrir un autre arbre familial mais tous les arbres déjà ouverts s'affichent avec l'icône verrou dans la colonne de statut de la fenêtre de gestion des arbres familiaux. Le fermeture de l'arbre dans la première instance supprime le fichier *lock* et rend l'arbre disponible pour l'ouverture dans une nouvelle instance

Si vous pouvez ouvrir le même arbre familial dans deux instances de Gramps en même temps, alors vos données risquent d'être corrompues puisque chacun peut écraser le travail de l'autre.

#### Voir aussi :

- [Ligne de commande : forcer le déblocage](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/fr#Option_pour_forcer_le_déblocage)

Si malheureusement un crash devait arriver dans Gramps, l'arbre familial sera verrouillé. Pour enlever le verrou de l'arbre, sélectionnez ce dernier, et cliquez sur le bouton qui sera disponible.

## Réparer un arbre familial corrompu

![[_media/FamilyTreesManager-Dialog-ShowingRedErrorStatusIcon-Sample-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Réparer un arbre familial]]

Si votre arbre familial est abîmé ou corrompu pour plusieurs raisons, le gestionnaire de base de données affichera un logo rouge d'erreur dans la colonne .

Pour demander à Gramps d'essayer de réparer les dégâts, sélectionnez l'arbre et cliquez sur le bouton .

Gramps tentera de reconstruire un arbre depuis vos fichiers de sauvegarde créés automatiquement à la sortie.

  

## Convertir un arbre familial de BSDDB à SQlite

![[_media/ManageFamilyTrees-Convert-the-database-dialog-example-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Convert the 'Family Tree Name' database?</strong> dialog with <em>Family Trees (Manager)</em> - Dialog shown in background]]

Si vous avez un ancien **type de base de données** au format BSDDB visible dans la fenêtre du *gestionnaire d'arbres familiaux* pour n'importe quel arbre, la sélection de cet arbre va rendre le bouton actif.

Quand vous êtes prêt, cliquez le bouton et la boite de dialogue va s'afficher avec le message **Voulez vous convertir cet arbre familial en base de données SQlite ?**; Vous pouvez choisir pour arrêter ou pour commencer la procédure. Une fois finie, la fenêtre du *gestionnaire d'arbres familiaux* va afficher une nouvelle entrée : la copie convertie de votre arbre familial avec le *Type de base de données* SQlite. Vous devrez ensuite ouvrir cet arbre familial converti et le sauvegarder.

Vous pouvez alors renommer l'arbre BSDDB original avec le mot **ANCIEN** ou vous pouvez le supprimer pour éviter les confusions, puis renommer la nouvelle base de données SQlite.

{{-}}

## Sauver les changements dans votre arbre familial

Gramps enregistre vos changements dès qu'ils ont lieu. Par exemple, chaque fois que vous cliquez sur le bouton dans Gramps, vos changements sont immédiatement enregistrés et sauvés. Il n'y a pas de commande séparée pour "sauver".

Vous pouvez annuler vos changements effectués en sélectionnant Si vous sélectionnez cette commande plusieurs fois, vos changements les plus récents seront annulés l'un après l'autre. Pour effectuer ces multiples commandes en une fois, vous pouvez utiliser le dialogue disponible depuis le menu .

Si vous voulez retourner à la base de données telle qu'elle était, choisissez . Ce qui est analogue à "quitter sans sauver" dans d'autres programmes.

Si vous souhaitez une copie de votre arbre familial sous un autre nom, vous devrez l'exporter pour l'importer dans un nouvel arbre familial. Le format de base de données *Gramps XML* est recommandé pour ce genre d'opération.

## Importation des données

L'importation permet de récupérer des données provenant d'autres programmes de généalogie dans une base de données Gramps. Actuellement, Gramps accepte les formats suivants :

- Gramps XML (extension de fichier `.gramps`)
- Paquet XML Gramps (extension de fichier `.gpkg`)
- Tableur Gramps CSV - valeurs séparées par des virgules (extension de fichier `.csv`)
- Base de données Gramps V2.x (extension de fichier `.grdb`)
- GEDCOM (extension de fichier `.ged`)
- GeneWeb (extension de fichier `.gw`)
- Pro-Gen (extension de fichier `.def`) - Pro-Gen est très populaire aux Pays-Bas et dans le nord-ouest de l'Allemagne, utilisé depuis des dizaines d'années par des personnes qui ont collecté et enregistré des données dans un programme basé sur DOS (toujours d'actualité, adapté jusqu'à Windows 10).

Vous devez commencer par créer un nouvel arbre vide. Ensuite, sélectionnez ou le raccourci clavier pour importer les données ou restaurer un arbre préalablement sauvegardé. Le dialogue **d'importation** s'ouvrira vous demandant de spécifier le fichier que vous voulez importer.

Si vous tentez d'importer dans un arbre existant, la boite de dialogue d' s'ouvre et vous permet d'arrêter l'importation et de créer un nouvel arbre familial, à moins que vous ne vouliez réellement fusionner les données.

### Importation de base de données Gramps V2.x

La base de données Gramps V2.x (grdb) est le format antérieur à la version 3.0. Ce format natif de la base de données Gramps était une forme spécifique de la base de données Berkeley (BSDDB) avec une structure de tables particulière. Ce format était binaire et dépendant du système. Il était très rapide et efficace, mais non portable entre ordinateurs ayant une architecture différente (par exemple i386 et alpha).

L'importation de la base de données Gramps V2.x n'est pris en charge que par la version 3.0.x de Gramps. L'importation de V2.x vers Gramps V3.0.x ne perdra aucune donnée.

### Importation Gramps XML et paquet XML

Les bases de données Gramps XML et le paquet Gramps XML sont les formats natifs de Gramps. Il n'a pas de risque de perte d'information quand vous importez (restaurez) ou exporter avec ces formats.

- Gramps [XML](wiki:XML) (.gramps) : Le fichier Gramps XML est le format standard d'échange de données et de sauvegarde, et il était le format par défaut avant les versions 2.x de Gramps. Contrairement au format grdb, son architecture est indépendante et lisible par l'être humain. La base de données peut alors avoir des références à des objets media externes, c'est pourquoi il n'est pas garanti qu'elle soit complétement portable (pour une portabilité intégrale comprenant les objets media, utilisez le paquet Gramps XML (.grdb)). La base de données Gramps [XML](wiki:XML) est créée en exportant vers ce format par ().

<!-- -->

- Le paquet Gramps [XML](wiki:XML) (.gpkg) : est une archive compressée comprenant le fichier Gramps [XML](wiki:XML) et tous les objets media (des images, des fichiers sons, etc...), toutes les références de la base. Comme il contient tous les media, ce format est complètement portable. Le paquet Gramps est créé par l'exportation () dans ce format.

Si vous importez des informations d'une base de données Gramps ou Gramps [XML](wiki:XML), vous verrez une barre de progression dans la fenêtre principale de Gramps. Quand l'importation est terminée, une fenêtre de rapport affiche le nombre d'objets importés. Si les données importés sont issues du même arbre familial que celui dans lequel vous importez les données, le rapport d'importation vous fait des suggestions sur ce qui peut être fusionné. La fusion n'est **pas** faite automatiquement pour vous ! Si vous voulez fusionner des données généalogiques basiques automatiquement, utiliser plutôt l'exportation/importation avec un tableur CSV.

### Importation Gramps CSV

Le format Gramps CVS tableur permet d'exporter (et importer) une partie de ses données Gramps dans un simple format de tableur. Voir [Importation et Exportion CSV](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees:_CSV_Import_and_Export) pour plus de détails.

### Importation Gedcom

Vous devez commencer par créer un nouvel arbre vide. Ensuite, sélectionnez ou le raccourci clavier pour spécifier le fichier GEDCOM que vous voulez importer. Suivant le type de fichier, un boite de dialogue peut s'afficher.

Quand vous importez des données à partir d'un fichier Gedcom, une barre de progression sur la fenêtre principale de Gramps vous montrera la progression du traitement. A la fin de celui-ci, une fenêtre de statistiques sur l'importation s'affiche puis une fenêtre de rapport.

#### Boite dialogue Encodage GEDCOM

![[_media/GEDCOM_Encoding_dialog-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} GEDCOM Encoding - dialog]]

la boite de dialogue va s'afficher quand le fichier GEDCOM que vous allez importer est identifié comme utilisant un encodage ANSEL. parfois, c'est une erreur. Si après l'importation, vous remarquez que vos données comprennent des caractères anormaux, annuler l'importation et ne tenez pas compte du jeu de caractères en sélectionnant un encodage différent dans la liste proposée.

- **par défaut**
- ANSEL
- ANSI (iso-8859-1)
- ASCII
- UTF8

{{-}}

#### Boite de dialogue Rapport d'importation GEDCOM

Elle rend compte de la plupart des lignes qui auront été ignorées ou incomprises (le plus souvent car elles ne sont pas conformes au standard GEDCOM 5.6.0). Le contenu de chaque ligne (ou des lignes dans le cas de lignes de continuation) apparaîtra également. Dans certains cas, le contenu pourra être un peu différent de celui des lignes du fichier Gedcom, ces lignes étant reconstituées lors du traitement.

![[_media/GEDCOM-import-report-result-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapport d'import GEDCOM]]

Gramps utilise un modèle de représentation des données différent de celui de Gedcom et de ce fait, certaines informations Gedcom ne peuvent être importées dans Gramps :

Les principales exceptions sont :

- Certaines structures d'attributs Gedcom sont traitées comme des Gramps, avec l'impossibilité d'enregistrer plusieurs catégories Gedcom.
- Les informations DATA liées à SOURCE_RECORD (événements archivés et entités responsables de leur conservation) sont ignorées.
- Toutes les citations de sources dans des notes sont ignorées.
- Plusieurs catégories Gedcom n'ont pas exactement les mêmes données associées dans Gramps. Elles sont alors enregistrées comme ou avec des noms appropriés, en principe ceux portés dans Gedcom. Cela est particulièrement le cas pour les catégories Gedcom de HEADer, SUBMitter et SUBmission et plus particulièrement pour des informations comme REFN, RFN, RIN et AFN.

![[_media/Source-Note-GEDCOMImportNote-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Import report:Example of a note indicating omitted data]]

Les informations avec le statut 'ignored' (ignoré) : sont signalées en fin de traitement, avec une note attachée à l'objet correspondant.

Les informations avec le statut 'silently ignored' (ignoré muet) : ne sont pas signalées et pas renseignées dans une note (pour l'instant - cela peut être considéré comme une lacune)

#### Limitations à l'importation GEDCOM

Cette section décrit les données Gedcom qui ne peuvent pas être directement représentées dans le modèle de données Gramps, et la façon dont elles sont traitées. Pour plus d'information, (Voir [Gramps et GEDCOM](wiki:Gramps_and_GEDCOM)).

#### HEADer, SUBMitter et SUBmissioN

Gramps n'a pas de représentation directe de ces données. Toutes les informations importées seront stockées dans d'autres objets. Selon vos [préférences générale](wiki:Gramps_6.0_Wiki_Manual_-_Settings/fr#Général) définies, un objet 'source par défaut' peut être créé. Si c'est le cas, la plupart de ces données seront enregistrées dans cette , ou dans un attaché à cette source.

{{-}}

`   HEADER:=`  
`        n HEAD                                          {1:1}`  
`          +1 SOUR `<APPROVED_SYSTEM_ID>`                  {1:1}  (Onglet Données de votre 'source par défaut')`  
`            +2 VERS `<VERSION_NUMBER>`                    {0:1}  (Onglet Données de votre 'source par défaut')`  
`            +2 NAME `<NAME_OF_PRODUCT>`                   {0:1}  (Onglet Données de votre 'source par défaut')`  
`            +2 CORP `<NAME_OF_BUSINESS>`                  {0:1}  (Dépôt de votre 'source par défaut')`  
`              +3 <`<ADDRESS_STRUCTURE>`>                  {0:1}  (Dépôt de votre 'source par défaut')`  
`            +2 DATA `<NAME_OF_SOURCE_DATA>`               {0:1}  (Onglet Données de votre 'source par défaut')`  
`              +3 DATE `<PUBLICATION_DATE>`                {0:1}  (Onglet Données de votre 'source par défaut')`  
`              +3 COPR `<COPYRIGHT_SOURCE_DATA>`           {0:1}  (Onglet Données de votre 'source par défaut')`  
`          +1 DEST `<RECEIVING_SYSTEM_NAME>`               {0:1*} (Onglet Données de votre 'source par défaut')`  
`          +1 DATE `<TRANSMISSION_DATE>`                   {0:1}  (Onglet Données de votre 'source par défaut')`  
`            +2 TIME `<TIME_VALUE>`                        {0:1}  (Onglet Données de votre 'source par défaut')`  
`          +1 SUBM @`<XREF:SUBM>`@                         {1:1}  (Onglet Données de votre 'source par défaut')`  
`                                                               (Également utilisé pour déterminer) `  
`                                                               (l'enregistrement SUBMITTER_RECORD)`  
`                                                               (qui sera le propriétaire de la base)`  
`          +1 SUBN @`<XREF:SUBN>`@                         {0:1}  (ignoré)`  
`          +1 FILE `<FILE_NAME>`                           {0:1}  (Onglet Données de votre 'source par défaut')`  
`          +1 COPR `<COPYRIGHT_GEDCOM_FILE>`               {0:1}  (stocké comme Information de publication de votre`  
`'source par défaut')`  
`          +1 GEDC                                       {1:1}`  
`            +2 VERS `<VERSION_NUMBER>`                    {1:1}  (Onglet Données de votre 'source par défaut')`  
`            +2 FORM `<GEDCOM_FORM>`                       {1:1}  (Onglet Données de votre 'source par défaut')`  
`          +1 CHAR `<CHARACTER_SET>`                       {1:1}  (Onglet Données de votre 'source par défaut')`  
`            +2 VERS `<VERSION_NUMBER>`                    {0:1}  (Onglet Données de votre 'source par défaut')`  
`          +1 LANG `<LANGUAGE_OF_TEXT>`                    {0:1}  (Onglet Données de votre 'source par défaut')`  
`          +1 PLAC                                       {0:1}`  
`            +2 FORM `<PLACE_HIERARCHY>`                   {1:1}  (voir ci-dessous)`  
`          +1 NOTE `<GEDCOM_CONTENT_DESCRIPTION>`          {0:1}  (note attachée à la 'source par défaut')`  
`            +2 [CONT|CONC] `<GEDCOM_CONTENT_DESCRIPTION>` {0:M}`  
`            `  
`   * NOTE: Submissions à Family History Department pour les `  
`     fichier Ancestral (Mormons) ou autre ordinances de temple`  
`     doivent avoir une DESTination de fichier ou temple existant.`

Le PLAC FORM est stocké en interne et est utilisé pour l'interprétation des lieux (d'après la spécification Gedcom).

Le SUBMISSION_RECORD (il ne doit en avoir qu'un, mais non-vérifié) est stocké comme dans l'onglet de la 'source par défaut'.

`    SUBMISSION_RECORD:=`  
`        n @`<XREF:SUBN>`@ SUBN                            {1:1]`  
`          +1 SUBM @`<XREF:SUBM>`@                         {0:1}`  
`          +1 FAMF `<NAME_OF_FAMILY_FILE>`                 {0:1}`  
`          +1 TEMP `<TEMPLE_CODE>`                         {0:1}`  
`          +1 ANCE `<GENERATIONS_OF_ANCESTORS>`            {0:1}`  
`          +1 DESC `<GENERATIONS_OF_DESCENDANTS>`          {0:1}`  
`          +1 ORDI `<ORDINANCE_PROCESS_FLAG>`              {0:1}`  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`

Les SUBMITTER_RECORDs (il peut y en avoir plus d'un) sont stockés comme dans l'onglet de la 'source par défaut' sauf pour les exceptions en gras ci-dessous. Le SUBMITTER_RECORD qui correspond à l'enregistrement de l'en-tête (HEADER) est utilisé pour définir le [propriétaire de la base de données](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Outils#.C3.89diter_les_informations_sur_le_propri.C3.A9taire_de_la_base_de_donn.C3.A9es).

`   SUBMITTER_RECORD:=`  
`        n @`<XREF:SUBM>`@   SUBM                          {1:1}`  
`          +1 NAME `<SUBMITTER_NAME>`                      {1:1}`  
`          +1 <`<ADDRESS_STRUCTURE>`>                      {0:1}`  
`          `**`+1 <`<MULTIMEDIA_LINK>`> {0:M}`**  
`          `**`+1 LANG `<LANGUAGE_PREFERENCE>` {0:3}`**  
`          `**`+1 RFN `<SUBMITTER_REGISTERED_RFN>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- Le lien Mutimedia est ignoré
- LANG est ignoré
- RFN et RIN sont ignorés

#### INDIvidu

L'enregistrement INDIVIDUAL_RECORD est stocké comme un Gramps, avec des exceptions marquées en gras ci-dessous.

`   INDIVIDUAL_RECORD: =`  
`        n @`<XREF:INDI>`@  INDI                           {1:1}`  
`          +1 RESN `<RESTRICTION_NOTICE>`                  {0:1}`  
`          +1 <`<PERSONAL_NAME_STRUCTURE>`>                {0:M}`  
`          +1 SEX `<SEX_VALUE>`                            {0:1}`  
`          +1 <`<INDIVIDUAL_EVENT_STRUCTURE>`>             {0:M}`  
`          `**`+1 <`<INDIVIDUAL_ATTRIBUTE_STRUCTURE>`> {0:M}`**  
`          +1 <`<LDS_INDIVIDUAL_ORDINANCE>`>               {0:M}`  
`          +1 <`<CHILD_TO_FAMILY_LINK>`>                   {0:M}`  
`          +1 <`<SPOUSE_TO_FAMILY_LINK>`>                  {0:M}`  
`          `**`+1 SUBM @`<XREF:SUBM>`@ {0:M}`**  
`          +1 <`<ASSOCIATION_STRUCTURE>`>                  {0:M}`  
`          +1 ALIA @`<XREF:INDI>`@                         {0:M}`  
`          `**`+1 ANCI @`<XREF:SUBM>`@ {0:M}`**  
`          `**`+1 DESI @`<XREF:SUBM>`@ {0:M}`**  
`          +1 <`<SOURCE_CITATION>`>                        {0:M}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 RFN `<PERMANENT_RECORD_FILE_NUMBER>`         {0:1}`  
`          +1 AFN `<ANCESTRAL_FILE_NUMBER>`                {0:1}`  
`          +1 REFN `<USER_REFERENCE_NUMBER>`               {0:M}`  
`            `**`+2 TYPE `<USER_REFERENCE_TYPE>` {0:1}`**  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`  
`   `

- Les liens vers le submitter (SUBM), indication de 'ancestor interest' (ANCI) et indication de 'descendant interest' (DESI) sont ignorés avec le statut 'ignoré muet'.
- L'indication d'alias (indication pour relier des enregistrements qui pourraient être la même personne) est importée comme une avec le nom 'Alias'.
- Les indications de référence REFN et REFN:TYPE sont importées comme de l' , mais s'il y avait plusieurs REFN, il pourrait y avoir une incertitude sur le REFN auquel TYPE est associé.

Le traitement de l' INDIVIDUAL_ATTRIBUTE_STRUCTURE est plus compliqué. Les tags suivants :

- EDUC (Niveau d'enseignemlent atteint),
- NMR (Nombre de mariages),
- OCCU (Profession ou occupation),
- PROP (Possessions),
- RELI (Religion),
- RESI (Résidence) et
- TITL (Titre nobiliaire)

sont tous traités comme des s Gramps et les informations associées sont stockées dans la structure Événement. Les détails suivant le tag principal (indiqué entre parenthèses ci-dessus) sont stockés comme de l' . L' <EVENT_DESCRIPTOR> suivant le tag de TYPE viendra remplacer la si l' <EVENT_DESCRIPTOR> n'est pas le nom de l'attribut.

Les tags suivants :

- CAST (Caste),
- DSCR (Description physique),
- INDO (Numéro d'identification national),
- NATI (Nationalité ou origine clanique),
- NCHI (Nombre d'enfants) and
- SSN (Numéro de sécurité sociale)

sont tous traités comme des s Gramps et la plupart des champs sauf ceux suivant le tag principal (indiqué entre parenthèse ci-dessus), la citation de source et les notes sont ignorés, comme cela est indiqué en gras ci-dessous.

`   INDIVIDUAL_ATTRIBUTE_STRUCTURE: =`  
`        n  CAST `<CASTE_NAME>`                            {1:1}`  
`          +1 <`<EVENT_DETAIL>`>                           {0:1}`  
`             etc.`  
`   `  
`   EVENT_DETAIL: =`  
`        `**`n TYPE `<EVENT_DESCRIPTOR>` {0:1}`**  
`        `**`n DATE `<DATE_VALUE>` {0:1}`**  
`        `**`n <`<PLACE_STRUCTURE>`> {0:1}`**  
`        `**`n <`<ADDRESS_STRUCTURE>`> {0:1}`**  
`        `**`n AGE `<AGE_AT_EVENT>` {0:1}`**  
`        `**`n AGNC `<RESPONSIBLE_AGENCY>` {0:1}`**  
`        `**`n CAUS `<CAUSE_OF_EVENT>` {0:1}`**  
`        n  <`<SOURCE_CITATION>`>                          {0:M}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`        `**`n <`<MULTIMEDIA_LINK>`> {0:M}`**  
`        n  <`<NOTE_STRUCTURE>`>                           {0:M}`  
`        `  
`        `

- Les informations INDIVIDUAL_ATTRIBUTE_STRUCTURE, TYPE, DATE, PLACE_STRUCTURE, ADDRESS_STRUCTURE, AGE_AT_EVENT, RESPONSIBLE_AGENCY, CAUSE_OF_EVENT et MULTIMEDIA_LINK sont toutes ignorées.

#### FAM_RECORD

Les FAM_RECORD sont importés dans Gramps sous forme d'enregistrements .

`   FAM_RECORD:=`  
`        n @`<XREF:FAM>`@   FAM                            {1:1}`  
`          +1 <`<FAMILY_EVENT_STRUCTURE>`>                 {0:M}`  
`          +1 HUSB @`<XREF:INDI>`@                         {0:1}`  
`          +1 WIFE @`<XREF:INDI>`@                         {0:1}`  
`          +1 CHIL @`<XREF:INDI>`@                         {0:M}`  
`          +1 NCHI `<COUNT_OF_CHILDREN>`                   {0:1}`  
`          +1 SUBM @`<XREF:SUBM>`@                         {0:M}`  
`          +1 <`<LDS_SPOUSE_SEALING>`>                     {0:M}`  
`          +1 <`<SOURCE_CITATION>`>                        {0:M}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 REFN `<USER_REFERENCE_NUMBER>`               {0:M}`  
`            +2 TYPE `<USER_REFERENCE_TYPE>`               {0:1}`  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- Les liens vers SUBMitter sont ignorés avec le statut 'ignoré muet'.
- Les indications de référence REFN et REFN:TYPE sont importées comme de la , mais s'il y avait plusieurs REFN, il pourrait y avoir une incertitude sur le REFN auquel TYPE est associé.

#### SOURCE_RECORD

Les SOURCE_RECORD sont stockés dans Gramps sous forme d'enregistrements , sauf les exceptions marquées en gras ci-dessous.

`   SOURCE_RECORD:=`  
`        n @`<XREF:SOUR>`@ SOUR                            {1:1}`  
`          `**`+1 DATA {0:1}`**  
`            `**`+2 EVEN `<EVENTS_RECORDED>` {0:M}`**  
`              `**`+3 DATE `<DATE_PERIOD>` {0:1}`**  
`              `**`+3 PLAC `<SOURCE_JURISDICTION_PLACE>` {0:1}`**  
`            `**`+2 AGNC `<RESPONSIBLE_AGENCY>` {0:1}`**  
`            `**`+2 <`<NOTE_STRUCTURE>`> {0:M}`**  
`          +1 AUTH `<SOURCE_ORIGINATOR>`                   {0:1}`  
`            +2 [CONT|CONC] `<SOURCE_ORIGINATOR>`          {0:M}`  
`          +1 TITL `<SOURCE_DESCRIPTIVE_TITLE>`            {0:1}`  
`            +2 [CONT|CONC] `<SOURCE_DESCRIPTIVE_TITLE>`   {0:M}`  
`          +1 ABBR `<SOURCE_FILED_BY_ENTRY>`               {0:1}`  
`          +1 PUBL `<SOURCE_PUBLICATION_FACTS>`            {0:1}`  
`            +2 [CONT|CONC] `<SOURCE_PUBLICATION_FACTS>`   {0:M}`  
`          +1 TEXT `<TEXT_FROM_SOURCE>`                    {0:1}`  
`            +2 [CONT|CONC] `<TEXT_FROM_SOURCE>`           {0:M}`  
`          +1 <`<SOURCE_REPOSITORY_CITATION>`>             {0:1}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 REFN `<USER_REFERENCE_NUMBER>`               {0:M}`  
`            +2 TYPE `<USER_REFERENCE_TYPE>`               {0:1}`  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- Les informations DATAs et leurs attributs associés sont ignorés.

#### REPOSITORY_RECORD

Les REPOSITORY_RECORD sont stockés dans Gramps sous forme d'enregistrements , sauf les exceptions marquées en gras ci-dessous.

`   REPOSITORY_RECORD: =`  
`        n @`<XREF:REPO>`@ REPO                            {1:1}`  
`          +1 NAME `<NAME_OF_REPOSITORY>`                  {0:1}`  
`          +1 <`<ADDRESS_STRUCTURE>`>                      {0:1}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          `**`+1 REFN `<USER_REFERENCE_NUMBER>` {0:M}`**  
`            `**`+2 TYPE `<USER_REFERENCE_TYPE>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- REFN, REFN:TYPE et RIN sont ignorés

#### MULTIMEDIA_RECORD

Les MULTIMEDIA_RECORD sont stockés dans Gramps sous forme d'enregistrements , sauf les exceptions marquées en gras ci-dessous.

`   MULTIMEDIA_RECORD:=`  
`        n @`<XREF:OBJE>`@ OBJE                            {1:1}`  
`          +1 FORM `<MULTIMEDIA_FORMAT>`                   {1:1}`  
`          +1 TITL `<DESCRIPTIVE_TITLE>`                   {0:1}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 <`<SOURCE_CITATION>`>                        {0:M}`  
`          `**`+1 BLOB {1:1}`**  
`            `**`+2 CONT `<ENCODED_MULTIMEDIA_LINE>` {1:M}`**  
`          +1 OBJE @`<XREF:OBJE>`@     /* chain to continued object */  {0:1}`  
`          `**`+1 REFN `<USER_REFERENCE_NUMBER>` {0:M}`**  
`            `**`+2 TYPE `<USER_REFERENCE_TYPE>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**

- En principe, il y a un tag 'FILE' pour indiquer le fichier contenant l'objet multimedia. Cet usage date de la version GEDCOM 5.6.0, mais la possibilité GEDCOM 5.6.0 d'avoir plusieurs <MUTIMEDIA_FILE_REFN> et de disposer d'informations associées FORM, TYPE et TITL attachées à FILE n'est pas prévue (une autre ligne FILE rencontrée pourra venir écraser les informations de la première - sans détection d'erreur).
- BLOB est ignoré
- REFN, REFN:TYPE et RIN sont ignorés

#### NOTE_RECORD

Les NOTE_RECORD sont stockés dans Gramps sous forme d'enregistrements , sauf les exceptions marquées en gras ci-dessous.

`   NOTE_RECORD:=`  
`        n @`<XREF:NOTE>`@ NOTE `<SUBMITTER_TEXT>`           {1:1}`  
`          +1 [ CONC | CONT] `<SUBMITTER_TEXT>`            {0:M}`  
`          `**`+1 <`<SOURCE_CITATION>`> {0:M}`**  
`          `**`+1 REFN `<USER_REFERENCE_NUMBER>` {0:M}`**  
`            `**`+2 TYPE `<USER_REFERENCE_TYPE>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- SOURCE_CITATION est ignoré
- REFN, REFN:TYPE et RIN sont ignorés

## Exportation des données

![[_media/ExportAssistant_ChooseTheOutputFormat_wizard-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} l'assistant d'exportation : sélection du format]]

L'exportation permet de partager une partie des données de votre base Gramps avec d'autres généalogistes ainsi que de transférer vos données vers un autre ordinateur. Actuellement, Gramps peut exporter vers les formats suivants : Gramps [XML](wiki:XML), GEDCOM, paquet Gramps [XML](wiki:XML), Web Family Tree, GeneWeb,VCalendar, VCard et tableur Gramps CSV.

Pour exporter des données, choisissez ou le raccourci clavier . Ceci appellera l'. Ses pages vous guideront pour le choix de format, le choix du fichier, avec des options spécifiques d'exportation (voir ci-dessous). Après une page finale de confirmation, l'exportation sera exécutée selon les choix que vous avez faits. À tout moment, vous pouvez cliquer et modifier vos choix, puis recommencer l'exportation. Le bouton permettant de revenir en arrière.

### Options d'exportation

![[_media/Options_Export_Focal-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Assistant d'exportation - Options d'exportation - Boite de dialogue (avec les valeurs par défaut pour le format "Comma Separated Values Spreadsheet(CSV)"). La section inférieure contenant des options spécifiques au format de fichier est surlignée]]

Après avoir choisi vos options dans les deux sections.

- Section supérieure : [Filtres et vie privée](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Filters_and_privacy)
- Section inférieure : Options spécifiques au format de fichier

Cliquez le bouton pour continuer. {{-}}

### Filtres et vie privée

Gramps peut exporter votre arbre familial vers différents formats. Les options d'exportation vous permettent de définit précisément votre exportation. Les filtres vous permettent d'exporter un volume limité de données défini selon vos critères.

#### Filtre privée

: cochez cette case pour empêcher l'inclusion des données privées dans le fichier d'exportation.

#### Filtre vivant

Cette option restreint les données et limite les informations exportés sur les personnes vivantes. Cela veut dire que toutes les informations sur leur naissance, adresses, autres événements, etc..., seront absentes de l'exportation. Si vous choisissez cette option, vous aurez d'autres options pour limiter les données sur les personnes vivantes. Par exemple, vous allez utiliser le mot **Vivant** pour le prénom (voir vos [Préf érences](wiki:Gramps_6.0_Wiki_Manual_-_Settings/fr#Texte)); exclure les notes et les sources pour les [personnes vivantes](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive/fr).

Parfois, il n'est pas évident de savoir [si une personne est toujours en vie](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive/fr). Gramps utilise un algorithme avancé pour le déterminer. Rappelez-vous, Gramps fait de son mieux pour deviner, et n'a peut être pas toujours raison. S'il vous plaît vérifiez deux fois vos données.

Choisissez parmi les options suivantes :

- (par défaut)

- 

- 

- 

#### Filtre sur l'individu

Sélectionnez parmi les options suivantes :

- (par défaut)

- 

- 

- 

- 

- Créer un filtre personnalisé en sélectionnant l*'icône de modification* pour afficher la boite dialogue de définition du filtre.

#### Filtre Note

Sélectionnez parmi les options suivantes :

- (par défaut)

- Créer un filtre personnalisé en sélectionnant l*'icône de modification* pour afficher la boite dialogue de définition du filtre.

#### Filtre référence

Sélectionnez parmi les options suivantes :

- (par défaut)

- 

### Exportation aux formats Gramps

- Exportation de base de données Gramps [XML](wiki:XML) : l'exportation vers le format de Gramps [XML](wiki:XML) produira une base de données compatible avec les versions précédentes de Gramps. Car XML est un format lisible pour l'homme basé sur du texte, vous pouvez également l'employer pour jeter un coup d'oeil à vos données.

<!-- -->

- Exportation de paquet Gramps : l'export en paquetage Gramps crée une archive tar compressée par gzip (appelée fréquemment tarball) contenant la base de données, les objets multimédia locaux et une copie des objets multimédia externes. Ce format est pratique pour déplacer vos données entre ordinateurs ou pour les partager avec quelqu'un d'autre sans dégrader les informations.

<!-- -->

- Exporter vers un CD : prépare un répertoire avec toutes les données, prêt à être mis sur un CD. Ceci se fait par **burn:///** dans Nautilus. Après l'exportation, allez-y en sélectionnant **Aller à-\>Créateur de CD** dans le menu de Nautilus. Votre répertoire de base de données exportée apparaîtra alors. Pour l'enregistrer sur le CD, cliquez sur l'icône de CD dans la barre d'outils de Nautilus, ou sélectionnez **Fichier-\>Écrire un CD** dans le menu de Nautilus.

Si un fichier media n'est pas trouvé pendant l'exportation, le dialogue apparaîtra.

### Exportation au format GEDCOM

Gramps peut exporter une base de données au format GEDCOM conventionnel. Il n'y a pas d'options spécifiques d'exportation pour GEDCOM.

Pour plus d'information sur GEDCOM, voir :

- <https://fr.wikipedia.org/wiki/GEDCOM>
- <https://www.familysearch.org/developers/docs/gedcom/>

Voir le chapitre sur [Gramps et GEDCOM](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Gestion_des_arbres_familiaux#Ouvrir_des_bases_de_donn.C3.A9es_XML_ou_GEDCOM) pour avoir plus de détails sur ce qui n'est pas exporté quand vous le faîtes vers GEDCOM. (Utilisez le format Gramps XML pour une sauvegarde de votre arbre familial)

### Exportation vers d'autres formats

- L'exportation au format Web Family Tree : crée un fichier que le programme WFT peut lire. Utilisez le menu déroulant Filtre pour restreindre l'ensemble de données exportées selon votre choix. Cochez Restreindre les informations sur les personnes vivantes pour réduire les données portant sur des personnes vivantes.

<!-- -->

- L'exportation vers GeneWeb : sauvera une copie de vos données dans un format populaire de généalogie. Pour découvrir GeneWeb et de son format, visitez <http://cristal.inria.fr/~ddr/GeneWeb/fr/>.

<!-- -->

- VCalendar et VCard: l'exportation vers vCalendar ou le vCard sauvera l'information dans un format utilisé dans beaucoup d'applications avec carnet d'adresse, parfois appelées PIM pour gestionnaire personnel d'information.

<!-- -->

- Gramps CVS format tableur : permet d'exporter (et importer) une partie de ses données Gramps dans un simple format de tableur. Voir [Importation et Exportion CSV](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees:_CSV_Import_and_Export/fr) pour plus de détails. Voir également [Exporter l'affichage](wiki:FR:Manuel_wiki_pour_Gramps_6.0_-_R%C3%A9glages#Exporter_l.27.C3.A9cran).

{{-}}

[M](wiki:Category:Fr:Documentation)
