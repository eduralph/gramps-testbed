---
title: Fr:Manuel wiki pour Gramps 6.0 - Outils
categories:
- Fr:Documentation
managed: false
source: wiki-scrape
wiki_revid: 111078
wiki_fetched_at: '2026-05-30T18:38:07Z'
lang: fr
---

{{#vardefine:chapter\|12}} {{#vardefine:figure\|0}}

Ce chapitre décrit les différents outils disponibles dans Gramps.

## Introduction

![[_media/Boutonoutils_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Bouton &quot;Ouvrir le dialogue d&#39;outils&quot;]] Les outils de Gramps vous permettent d'exécuter divers types d'analyses de vos données généalogiques. Typiquement, les outils ne produisent pas de sortie sous la forme d'imprimés ou de fichiers. Au lieu de cela, ils produisent une sortie d'écran immédiatement disponible pour le chercheur. Cependant, quand cela est approprié, vous pouvez enregistrer le résultat de l'outil dans un fichier.

Les outils peuvent être consultés par le menu . Vous pouvez aussi avoir accès à la liste complète des outils avec leur brève description en utilisant l'icône de la barre d'outils.

## Analyse et exploration

Ce groupe comprend les outils qui analysent et explorent la base de données sans la modifier. Les outils suivants sont actuellement disponibles dans Gramps :

### <u>Comparaison d'événements individuels</u>

![[_media/Outils_analysecomparaison_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Comparaison d'événements individuels" - "sélection du filtre"]]

Cet outil compare des événements parmi un ensemble d'individus.

Vous pouvez utiliser cet outil via le menu qui va ouvrir le dialogue .

Les individus à prendre en compte sont choisis par des filtres personnalisés préalablement définis en sélectionnant la liste déroulante avec par défaut *Toute la base de données*. Ou en sélectionnant le bouton , pour créer des filtres personnalisés dans l'éditeur . Pour lancer cet outil sélectionnez et les résultats seront affichés dans le dialogue . {{-}}

Depuis le dialogue vous pouvez voir les résultats ou forme d'un tableur (format ODS). Sélectionnez pour quitter. {{-}} ![[_media/Outils_analysecomparaisonresult_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Comparaison d&#39;événements individuels&quot; - &quot;Résultats des comparaisons d&#39;événements individuels&quot; - exemple étendu]] {{-}}

## Modification de l'arbre familial

Cette section décrit des outils qui peuvent modifier la base de données. Les outils décrits ici servent principalement à trouver et corriger les erreurs dans les données. Les outils suivants sont actuellement disponibles dans Gramps :

### <u>Extraire les descriptions de l'événement</u>

![[_media/Outils_modifextrdescriptevt_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Extraire les descriptions de l&#39;événement - Fenêtre de résultats]] Cet outil essaye d'extraire les descriptions de l'événement depuis ses données, utilisant le modèle :

`{type d'événement} de {Nom de famille}, {Prénom}`

Si une description de l'événement est absente, alors l'outil utilisera ce modèle de description de l'événement.

Accédez à cet outils par le menu

L**'Avertissement sur l'historique d'annulation** va s'afficher et vous pouvez soit soit .

Un fois que vous avez cliqué sur , il va balayer et modifier l'arbre familial puis afficher une fenêtre indiquant le nombre total de descriptions d'évènements ajoutés. {{-}}

### <u>Extraire l'information des noms</u>

L'outil recherche dans toute la base de données et tente d'extraire les titres et surnoms qui peuvent être imbriqués dans le prénom d'un individu. Si une information peut être extraite, les propositions pour de correction seront présentées dans le tableau. Vous pouvez alors décider ceux que vous voulez corriger selon les propositions et ceux que nous ne voulez pas modifier.

Accédez à cet outils par le menu .

L**'Avertissement sur l'historique d'annulation** va s'afficher et vous pouvez soit soit .

![[_media/Outils_modifextrinfonomparam_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Extraire l'information des noms - Paramètres]]

Le dialogue s'affiche et vous pouvez modifier chacune des options :

- `de, van, von, di, le, du, dela, della, des, vande, ten, da, af, den, das, dello, del, en, ein, elet, les, lo, los, un, um, una, uno, der, ter, te, die` (par défaut)

- `e, y` (par défaut)

- `de, van` (par défaut)

Une fois terminé, cliquez pour lancer l'outil. {{-}}

![[_media/Outils_modifextrinfonomresult_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Extraire l'information des noms - Résultats]]

Une fois le rapport terminé, le dialogue des résultats s'affiche. Pour chaque nom dans la liste, vous pouvez garder sélectionnée la ligne ou non. En cliquant sur le bouton , vous allez lancer les corrections pour les lignes sélectionnées. {{-}}

### <u>Fusion des citations</u>

You can select this via menu .

L**'Avertissement sur l'historique d'annulation** va s'afficher et vous pouvez soit soit . {{-}} ![[_media/Outils_modificationfusioncitationsparam_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fusion des citations - paramètres]]

Ensuite, le dialogue (Titre du dialogue : *Les notes, objets media et données des deux citations seront combinés.*) est affiché.

Les options suivantes sont disponibles :

- Liste déroulante  :
  - Correspondance à page/volume, date et confiance
  - **Ignorer la date** (par défaut)
  - Ignorer le niveau de confiance
  - Ignorer la date et le niveau de confiance

- -  (non coché par défaut)

{{-}} ![[_media/Outils_modificationfusioncitationsresult_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fusion des citations - Résultat]]

Sélectionner pour lancer l'outil ; une fois l'opération terminée, un rapport indique le . {{-}} Voir aussi les options de [Fusion de citations](wiki:https://gramps-project.org/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_3#Merge_Citations) disponibles dans la vue de la catégorie Citations. {{-}}

### <u>Recherche des doublons</u>

![[_media/Outils_modificationdoublonsparam_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Recherche des doublons - paramètres]] Cet outil parcourt la base de données et cherche les enregistrements qui pourraient décrire en réalité la même personne.

Vous pouvez accéder à cet outil via .

Le dialogue s'affiche et vous pouvez modifier les options :

-  : choisir entre Élevé, Moyen, et **Bas** (par défaut) depuis le menu déroulant. (Note : la probabilité de correspondance est calculée en nombre à virgule flottante. Si la probabilité est supérieure au seuil, la correspondance est alors rapportée. Les seuils sont définis à Bas = 0,25, Moyen = 1 et Élevé = 2. Ainsi, avec le seuil haut, moins de correspondances sont attendues)

-  case à cocher permettant d'activer ou non l'utilisation des codes SoundEx pour rechercher les doublons d'individus. Cette option a un intérêt pour les noms à consonance anglaise. (coché par défaut)

Seulement trois boutons sont présents : l' vous conduisant à cette page, pour arrêter le processus et le bouton pour lancer l'outil.

Si vous cliquez sur le bouton , les données suivront deux étapes.

- Étape 1 : Construction d'une liste préliminaire
- Étape 2 : Calcul des correspondances possibles.

Une barre de progression s'affichera et sa rapidité dépendra de votre processeur et de nombre d'individus dans votre base de données, ceci pouvant prendre un peu de temps. {{-}} ![[_media/Outils_modificationdoublonsresult_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Recherche des doublons - résultats]] Finalement une fenêtre sera présentée. Elle affiche une liste avec trois colonnes :

- Évaluation : ceci vous donne une idée de la ressemblance entre les deux individus. Plus l'indice est élevé, plus la probabilité est grande que ce soit un doublon.
- Le premier individu
- Le second individu

Trois boutons sont présents : vous conduisant à cette page, pour quitter et le bouton .

Si vous sélectionnez une ligne, vous pourrez vérifier les détails avec le bouton (ou cliquez deux fois sur la ligne). Une nouvelle fenêtre s'affiche avec les détails de comparaison. si vous cliquez le bouton les individus seront fusionnés. Voir pour les détails [fusion des individus](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Fonctionnement_des_attributs,_adresses,_noms,_et_la_fusion#Fusion_des_individus). {{-}}

### <u>Renommer les types d'événement</u>

![[_media/Changeventype-52-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Changement de type]] Cet outil renomme tous les événements d'un type vers un nouveau type.

Accédez à cette outil par le menu

La fenêtre est affichée.

- Type d'événement original : saisir dans le champ texte ou utilisez le menu déroulant et sélectionnez le type d'événement à renommer.
- Nouveau type d'évènement : saisir dans le champ texte (vous pouvez créer un type d'événement nouveau) ou utilisez le menu déroulant et sélectionnez le type d'événement de remplacement.

L'exemple montre le changement de l'événement **Baptême religieux** vers l'événement **Baptême**.

Cliquez sur pour poursuivre, pour abandonner. A la fin de cette tâche, l'outil affiche un dialogue de résultats indiquant le nombre d'évènements modifiés.

Voir aussi :

- [Éditer les informations des évènements](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Fonctionnement_des_événements,_sources,_lieux,_dépôts_et_notes#Édition_de_l&#39;information_sur_les_événements)

{{-}}

### <u>Réorganiser les identifiants Gramps</u>

Cet outil réordonne les identifiants des objets de la base de données Gramps et peut aussi permettre d'en modifier le format. Plusieurs options sont disponibles.

Accédez à cette outil par le menu

L**'Avertissement sur l'historique d'annulation** va s'afficher et vous pouvez soit soit .

![[_media/Outils_modificationordidparam_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Réorganiser les identifiants Gramps]] La colonne 'Objet' liste les types d'identifiant. A la gauche de cette colonne, des cases à cocher permettent d'activer les changements pour chaque type d'objet. Quand elle est cochée, le type d'objet sera **ré-ordonné**. L'étiquette 'Objet' est en fait un bouton qui peut être utilisé pour inverser toutes les cases à cocher en une seule fois.

La colonne 'Actuel' affiche un exemple de l'identifiant en cours. La colonne 'Quantité' affiche le nombre d'objet de ce type.

La colonne 'Format' est utilisée pour **modifier** le format de l'identifiant pour chaque type d'objet. Notez que le format consiste en un préfixe, le '%04d' et un suffixe. Il DOIT y avoir au moins un préfixe ou un suffixe, les deux étant autorisés. Il est recommandé de garder des identifiants assez courts. Le '%04d' définit la longueur de la portion numérique de l'identifiant, le '4' peut être changé, de '3' (permettant des nombres de 000-999) à '9' (000000000-999999999) est autorisé. Les modifications faites ici sont les mêmes que dans le menu par l'onglet [Formats ID](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Formats_ID). L'étiquette 'Format' est en fait un bouton qui réinitialise tous les formats à la dernière valeur utilisée.

La colonne 'Modifier' contient des cases à cocher pour chaque type d'objet. Si coché, l'identifiant de cet objet sera remplacé par le nouveau 'Format' à moins que la case 'Conserver' ne soit aussi cochée ; dans ce cas, l'identifiant est ré-ordonné en tenant compte du numéro de départ et de l'étape, définis dans les champs suivants. Si aucune case n'est cochée, le format de l'identifiant n'est PAS mis à jour mais l'identifiant est recalculé. L'étiquette 'Modifier' est en fait un bouton qui permet d'inverser toutes les cases à cocher en une fois.

Le champ 'Démarrer' indique le numéro de départ utilisé pour l'opération de renumérotation. L'étiquette 'Démarrer' est en fait un bouton qui permet de basculer entre démarrer à 0 et démarrer après le dernier numéro en cours.

Le champ 'Étape' indique l'intervalle entre les numéros pour la renumérotation. '1' est un incrément simple, '2' va incrémenter par 2, etc. L'étiquette 'Étape' est en fait un bouton qui permet de basculer entre '1', '2', '5' et '10'.

La colonne 'Conserver' contient des cases à cocher pour chaque type d'objet. Si cette case et celle de la colonne 'Modifier' sont cochées, le format d'identifiant pour cet objet sera conservé mais l'identifiant sera recalculé en tenant compte des 2 champs précédents. L'étiquette 'Conserver' est en fait un bouton qui permet d'inverser toutes les cases à cocher en une fois.

Si vous cliquer le bouton le processus sera lancé et une fenêtre affichera une barre de progression.

Les identifiants sont ré-ordonnés en plusieurs étapes : les identifiants individuels, les identifiants familiaux, les identifiants événements, les identifiants objets media, les identifiants sources, les identifiants citations, les identifiants lieux, les identifiants dépôts et enfin les identifiants notes.

L'étape suivante consiste à rechercher les identifiants non-utilisés et les assigner.

Durant ce processus, l'outil examine chaque identifiant pour voir s'il correspond à la personnalisation, s'il ne correspond pas au format d'identifiant précédent ou au format par défaut. Ce peut être le cas si l'utilisateur a saisi son propre texte dans le champ de l'identifiant lors de la modification d'un objet. Ceci peut aussi arriver si les greffons tiers [GetGOV](wiki:Addon:GetGOV) ou [GeoName](wiki:Addon:GetGOV) ont été utilisés puisque cet outil enregistre l'identifiant GOV dans le champ de l'identifiant Gramps. Si un identifiant 'personnalisé' est trouvé, il va demander à l'utilisateur s'il veut réellement le remplacer. Le dialogue permet aussi à l'utilisateur d'avoir la même réponse pour les autres identifiants personnalisés qui seront retrouvés. {{-}}

### <u>Réparer la casse des noms de famille</u>

Cet outil recherche dans la base de données les noms de famille pour les normaliser. Le but est d'avoir la norme conventionnelle : première lettre en capital et des minuscules pour le reste du nom de famille. Si des déviations à cette règle sont détectées, les candidats pour la modification seront présentés dans un tableau. Vous pouvez alors décider de les modifier ou non.

Vous pouvez utiliser cet outil via .

Vous pouvez choisir le bouton ou . ![[_media/Capnames_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Correction de la casse]] Si des changements sont possibles sur les lettres capitales vous verrez la fenêtre . Elle affiche une liste des noms de famille pouvant être convertis par Gramps (vérifiez que ceci est correct pour vous). Dans la liste il y a trois colonnes :

-  : cochez ou non si vous acceptez ou non la recommandation de correction

- : le nom tel qu'il est actuellement enregistré.

- : le nom avec la modification si le changement est appliqué.

Sélectionnez les noms que vous souhaitez modifier, puis appuyez sur le bouton . Ou utilisez le bouton pour ne rien changer.

Vous pouvez aussi installer le greffon [Réparer la casse des prénoms](wiki:Addon:Fix_Capitalization_of_Given_Names) qui, une fois installé, fonctionne sur le même principe pour les prénoms.

### <u>Trier les événements</u>

Les événements de l'onglet dans les ou de la ne sont pas triés dans un ordre particulier autre que celui de la saisie. La raison pour ne pas forcer une quelconque règle de tri, particulièrement par date, étant de permettre pour chaque événement connu d'avoir lieu sans en connaître la date dans la chronologie. Importer ou fusionner une donnée depuis une source extérieure peut générer des événements extérieurs, pouvant être ajoutés, mais sans règle de tri, aux évènements existants pour les individus ou familles.

Les événements peuvent être ré-ordonnés manuellement par un [*glisser-déposer*](http://fr.wikipedia.org/wiki/Glisser-d%C3%A9poser) ou par l'utilisation des boutons réordonner dans l'onglet , lesquels permettent à un événement d'être monté ou descendu dans la liste des événements et Gramps se souviendra de l'ordre dès lors que les changements seront sauvés. Le nouveau tri sera utilisé partout dans Gramps, tel que dans les rapports.

L'ordre des événements dans l'onglet peut également être modifié en cliquant sur l'en-tête/titre des colonnes. Ainsi, cliquer sur la colonne 'Date' triera les événements selon les dates. Néanmoins cette méthode de tri des événements est temporaire et les changements ne sont pas conservés quand vous quittez la fenêtre.

L'approche du [*glisser-déposer*](http://fr.wikipedia.org/wiki/Glisser-déposer) pour classer les événements est bonne pour changer l'ordre d'un petit nombre d'événements mais n'est pas très pratique pour un grand nombre de modifications dans la chronologie des événements. C'est pour ce type de modifications que l'outil peut être utilisé. Il a été conçu pour le tri de tous les événements de la base de données ou ceux associés à une sélection ciblée d'individus choisie à l'aide d'un filtre.

Vous pouvez utiliser cet outil via .

![[_media/Trier_les_événements_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tri des événements]] La première option de l'outil est prévu pour définir l'étendue des individus sur lesquels l'outil va appliquer le tri. Le premier choix dans la liste étant d'appliquer les changements à tous les individus de la base de données. Les choix alternatifs étant d'appliquer les modifications aux ascendants et descendants de la personne choisie par le filtre ou un ensemble d'individus sélectionné par un filtre personnalisé. Après la désignation des individus à trier, l'étape suivante est de définir la règle du tri. La première option étant de trier par date. C'est probablement le choix le plus courant, mais d'autres attributs des événements peuvent également être choisis. Les dernières options sont pour le choix du tri, croissant ou décroissant, et d'appliquer ou non le tri sur les événements familiaux des individus sélectionnés. {{-}}

<span ID="Edit_Database_Owner_Information">

### <u>Éditer l'information sur le propriétaire de la base de données</u>

</span> ![[_media/Outils-modificationproprio_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Information sur le propriétaire]] Cet outil permet de modifier toutes les informations existante sur le chercheur.

Cliquer sur , ouvre la fenêtre de , dans laquelle vous pouvez saisir les informations.

- Nom :
- Rue :
- Lieu-dit :
- Ville :
- Province/Comté :
- Pays :
- Code postal :
- Téléphone :
- Courriel :

Ces informations sont spécifique à cet arbre familial et seront utilisées lors d'une exportation au format GEDCOM.

Deux choix sont disponibles à partir du menu contextuel (clic droit) :

- 

- 

{{-}}

## Réparation de l'arbre familial

### <u>Reconstruire les seconds indices</u>

![[_media/Outil_repar2ndindiceresult_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Seconds indices reconstruits]] Cet outil reconstruit les seconds indices.

Vous pouvez utiliser cet outil via . Une fois terminé, un dialogue est affiché. {{-}}

### <u>Reconstruire les statistiques du prénom d'après le genre</u>

![[_media/Outil_reparstatgenrenom_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Seconds indices reconstruits]] Cet outil reconstruit les statistiques de genre d'après le genre probable du prénom.

Vous pouvez utiliser cet outil via .

Une fois terminé, un dialogue est affiché. {{-}}

### <u>Reconstruire les tables de références</u>

![[_media/Outil_repartablereferresult_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Seconds indices reconstruits]] Ce outil reconstruit les tables de référence (item *Références* dans les fenêtres de saisie).

Vous pouvez utiliser cet outil via .

Une fois terminé, un dialogue est affiché. {{-}}

### <u>Supprimer les objets non référencés</u>

Cet outil parcourt votre base de données à la recherche d'éléments d'informations non connectés à quoi que ce soit d'autre, puis vous permettre de les modifier pour les rattacher à un autre élément ou les supprimer.

Vous pouvez utiliser cet outil via . {{-}} ![[_media/Outil_reparobjetnonrefparam2_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Objets non référencés - Recherche]] Le dialogue est présenté.

Choisissez parmi les options de recherche dans la section supérieure de la boite de dialogue  :

-  (coché par défaut)

-  (coché par défaut)

-  (coché par défaut)

-  (coché par défaut)

-  (coché par défaut)

-  (coché par défaut)

-  (coché par défaut)

Selectionnez le bouton pour lancer le rapport et une fois terminé, les résultats, s'il y en a, s'affiche dans la section inférieure de la fenêtre avec les colonnes suivantes :

- Sélectionne le rang si vous voulez supprimer l'objet (non coché par défaut)

- \- Une icône représentant le type d'objet.

- \- L'identifiant Gramps interne de l'objet.

- \- de l'objet.

Pour examiner un objet, double-cliquez sur son rang va ouvrir la fenêtre de modification de l'objet appropriée pour la corriger si nécessaire.

les objets que vous voulez supprimer soit en utilisant les cases à cocher individuelles soit en utilisant les boutons :

- 

- 

- 

Une fois vos choix de suppression faits, sélectionner le bouton pour supprimer les objets.

When finished you may then use the button to exit the tool. {{-}}

### <u>Vérifier et réparer la base de données</u>

Cet outil vérifie la base de données en recherchant les problèmes d'intégrité et en corrigeant ceux qu'il peut corriger. Dans le détail, cet outil détecte les défauts suivants :

- Liens familiaux rompus. Ceci arrive quand l'enregistrement d'un individu référence à une famille alors que l'enregistrement de la famille n'a pas de référence pour cet individu, et vice versa.

<!-- -->

- Media introuvables. Un medium introuvable est un objet multimedia dont le fichier est référencé dans la base de données mais absent. Ceci arrive quand le fichier est supprimé, renommé ou bien encore déplacé.

<!-- -->

- Familles vides. Ce sont les entrées de famille qui n'ont aucune référence à un individu en tant que membre.

<!-- -->

- Liens erronés entre parents. Ceci vérifie toutes les familles pour s'assurer que père et mère ne sont pas mélangés. Le sexe des parents doit aussi être différent. S'ils sont du même genre, alors leur relation est modifiée en "Partenaires".

Vous pouvez utiliser cet outil via .

Vous pouvez choisir le bouton ou . {{-}} ![[_media/Outil_reparverifmedia_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vérification de l&#39;arbre - media non trouvé]] ![[_media/Outil_reparverifresult_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Résultats de la vérification de l&#39;intégrité]]

Les anomalies retrouvées sont automatiquement corrigées mais une boite de dialogue peut s'afficher pour les media non retrouvés. Vous pouvez alors supprimer la référence ou indiquer le nouveau chemin si le medium a simplement été déplacé. Une case à cocher permet de répercuter la même modification pour les autres fichiers media non trouvé.

En fin de processus, une fenêtre de résultats s'affichera alors pour résumer les corrections s'il y en a eu. {{-}}

## Utilitaires

Cette section contient des outils vous permettant d'effectuer une opération simple sur une partie de données. Les résultats peuvent être sauvés dans votre base de données, mais ils ne modifieront pas vos données existantes. Les utilitaires suivants sont actuellement disponibles dans Gramps:

### <u>Calcul relationnel</u>

Cet utilitaire affiche la liste de tous les individus connectés, **mais pas forcément en relation** avec la personne active. Pour calculer la relation avec un individu différent, fermer la fenêtre, faire de cet individu la personne active et relancer l'outil. ![[_media/Outil_utilcalculrelat_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Relations avec &#39;…&#39; &quot; - Boite de dialogue montrant les résultats de l&#39;outil «Calcul relationnel»]] Accéder à cet outils par le menu .

Sélectionnez un individu dans la liste filtrée obtenue pour voir si une relation existe. La relation exacte sera affichée dans la partie inférieure de la fenêtre ainsi que l'ancêtre commun de cette relation. Seuls les liens du sang seront affichés (à l'exception des relations époux-épouse). Noter que les relations «par alliance» ne sont pas affichées.

La liste filtrée est affichée groupée et par ordre alphabétique des noms de famille (quelque soit les réglages de groupage dans la vue de la catégorie Individus). Les colonnes ne peuvent pas être triées.

Le degré de séparation (nombre de générations) qui sera pris en compte est réglé par le *Nb. max. de générations à parcourir entre 2 générations* de l'onglet *Général* du menu . (La valeur par défaut de 15 générations va rapporter des arrières grands-parents au 12e degré mais pas leurs parents. La personne active est compté comme une génération.)

Fondamentalement, deux individus sont liés directement par un lien du sang s'ils ont un ancêtre commun. Un de ces individus peut être l'ancêtre du second - comme un arrière grand-parent. Même dans le cas d'oncles et de tantes, vous pouvez toujours calculer la relation en recherchant l'ancêtre commun. Dans ce cas le père ou la mère de la tante ou de l'oncle sera un grand-parent du neveu ou de la nièce.

Le lien du sang le plus évident à travers les ancêtres est celui des frères et sœurs qui sont juste une génération en dessous de l'ancêtre commun. Une autre relation particulière est celle d'un individu de cette fratrie avec les descendants d'une autre individu de la fratrie. Si la personne active est le petit-fils ou la petite-fille de l'ancêtre commun, le frère ou la sœur d'un parent sera un oncle ou une tante. Au delà de cette génération de descendants, la fille des arrières grands-parents sera appelée grande tante. Cet individu est une arrière grande tante pour le second arrière petit-enfant qui est à quatre générations de l'ancêtre commun. La relation inverse d'une tante ou d'un oncle est un neveu ou une nièce.

Les cousins germains sont à deux générations de l'ancêtre commun par des fratries différentes. Les cousins issus-de-germains sont eux, à trois générations de l'ancêtre commun, et ainsi de suite.

Ensuite, tout le monde est dénommé «cousin» mais pour indiquer qu'ils ne sont pas de la même génération, on peut utiliser le terme «degré» pour indiquer la distance entre les générations.

S'il y a des liens de sang multiples, ils seront tous rapportés.

Une liste textuelle complète des liens du sang et les conjoints peut être vue avec le [Rapport de parenté](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Rapports#Rapport_de_parenté). {{-}}

### <u>Gérer les Media</u>

![[_media/Outil_utilgermedia1_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Outil «Gérer les media» - Introduction]] Cet outil est un ensemble de quatre outils différents utilisables par un assistant avec des fenêtres de dialogue. Il est accessible par le menu qui va afficher un premier dialogue **Introduction** avec les informations suivantes sur les actions de l'outil.

{{-}}

De la page **Introduction**, sélectionnez le bouton (ou utilisez le raccourci clavier ) pour afficher la fenêtre de la page **Sélection**.

![[_media/Outil_utilgermedia2_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Outil «Gérer les media» - Sélection]]

A partir de cette page **Sélection**, sélectionner une des quatre actions que vous souhaitez faire puis sélectionnez le bouton  :

- (par défaut)

- 

- 

- 

{{-}}

#### Remplacement une partie du chemin

![[_media/Outil_utilgermedia3_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Outil «Gérer les media» - Paramètres du remplacement de sous-chaîne]]

Cet outil permet le remplacement spécifique de sous-chaînes dans le chemin des objets media par une autre sous-chaîne. Ceci est utile quand vous déplacez les fichiers d'un répertoire vers un autre.

Tapez la chaîne de caractères correspondant à la partie de chemin à remplacer dans le champ et la chaîne correspondant au nouveau chemin dans le champ . A n'importe quel moment, vous pouvez cliquer sur le bouton ou le bouton . Cliquez sur le bouton ouvre la fenêtre de . {{-}}

#### Convertir les chemins relatifs en chemins absolus

![[_media/Outil_utilgermedia4_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Outil «Gérer les media» - Convertir les chemins relatifs en absolus]]

Cet outil permet de convertir les chemins relatifs vers les media en chemins absolus. Il utilise pour cela le prédéfini indiqué dans l'onglet *Général* du menu ou, s'il n'est pas renseigné, le répertoire racine de l'utilisateur. {{-}}

#### Convertir les chemins absolus en chemins relatifs

![[_media/Outil_utilgermedia5_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Outil «Gérer les media» - Convertir les chemins absolus en relatifs]]

Cet outil permet de convertir les chemins absolus vers les fichiers media en chemins relatifs. Le chemin relatif est relatif vis-à-vis du chemin de la base défini dans l'onglet *Général* du menu ou, s'il n'est pas renseigné, le répertoire racine de l'utilisateur. Un chemin relatif permet de lier la localisation des fichiers au chemin de la base qui pourra être modifié selon vos besoins. {{-}}

#### Ajouter les images non présentes à cette base de données

![[_media/Outil_utilgermedia6_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Outil «Gérer les media» - Ajouter les images]]

Vérifie les répertoires à la recherche d'images non incluses dans la base de données. Cet outil ajoute les images des répertoires référencés par les images déjà connues dans la base de données. Vous aurez à importer un item media pour chaque sous-répertoire manuellement. Le gestionnaire de media n'inclus pas les sous-répertoires automatiquement. Tous les chemins de répertoire affichés par l'outil seront explorés. {{-}}

### <u>Nettoyage des données saisies</u>

C'est un outil qui supprime les espaces en début ou en fin de nom. Il va rechercher les noms de lieux, les noms de famille et les prénoms avec des espaces inutile en début ou fin de nom.

Utilisez le menu .

Une fenêtre de résultats vous affiche les anomalies retrouvées pour les individus en partie supérieure et les lieux en partie inférieure.

Gramps prévient ce type d'anomalie en supprimant ces espaces inutiles lors de la saisie. {{-}}

### <u>Non lié</u>

![[_media/Notrelated_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Non lié]] Ce rapport va trouver les individus non reliés à la personne active sélectionnée. Les connexions comprennent les liaisons par une chaîne de références ou les liens créés avec l'[éditeur de liens](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Fonctionnement_des_événements,_sources,_lieux,_dépôts_et_notes#Éditeur_de_lien) dans les notes.

Vous pouvez l'utiliser via le menu .

Vous obtenez une fenêtre dans laquelle une liste affichera tous les individus **NON** liés à la personne sélectionnée.

Cette liste vous fournit :

- *Nom*
- *Identifiant*
- *Parents*
- *Marqueur*

Dans la colonne des noms, le bouton et le bouton permettent de déployer ou de refermer la liste des *Noms*. Un double-clic sur un individu ouvrira le dialogue de modification individuel ou familial.

Si vous sélectionnez un individu vous pouvez utiliser le champ texte dans la section inférieure de la fenêtre : vous pouvez saisir le texte que vous voulez ou choisir dans la liste déroulante une étiquette existante, c-à-d A Faire ou Non lié. Avec le bouton vous marquez les individus sélectionnés. Ce marqueur sera alors affiché dans la colonne de droite. {{-}}

### <u>Trouver une boucle dans la base de données</u>

![[_media/Outil_utilboucle_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Exemple simple de boucle dans un arbre avec la fenêtre de recherche de boucle]]

Cet outil permet de recherche une boucle parmi les ancêtres dans votre arbre généalogique.

Cliquez sur pour lancer la vérification.

La fenêtre de résultats affiche un tableau avec cinq colonnes ,, , , .

1.  Le premier Identifiant Gramps se réfère au parent.
2.  Parent est l'individu pour lequel nous recherchons la boucle.
3.  Le second Identifiant Gramps se réfère à l'enfant.
4.  L'enfant (le descendant) à l'origine de la boucle.
5.  Identifiant de la famille est la référence à la famille correspondante.

{{-}} Pour plus d'informations sur les boucles, lire (en anglais) :

- [Finding Ancestral Loops : Modern Software Experience](https://www.tamurajones.net/FindingAncestralLoops.xhtml)
- [Ancestral Loops : Louis Kessler's Behold Blog](http://www.beholdgenealogy.com/blog/?p=1309)

### <u>Vérifier les données</u>

![[_media/Outil_utilverifdonneesparam_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vérification des données - Paramètres]] Cet utilitaire permet de vérifier les données de la base selon des critères spécifiés par l'utilisateur.

Par exemple, vous voulez vous assurer qu'aucune personne dans votre base n'a des enfants à l'âge de 98 ans. Ceci serait le résultat d'une erreur de saisie de toute évidence, mais ne serait pas une erreur de structure de la base de données. A côté de cela, quelqu'un pourrait avoir un enfant à 98 ans même si c'est très improbable. L'outil de vérification affiche tout ce qui ne répond pas à vos critères pour que vous puissiez vérifier plus à fond les données.

Cliquez sur pour ouvrir la fenêtre . Ce dialogue a cinq onglets, , , , . Ces derniers affichent une liste de critères dont vous pouvez modifier les valeurs. Dans la liste ci-dessous, voici quelques valeurs *réalistes*.

#### Général

-  : 90

-  : 17

-  : 50

-  : 3

-  : 30

-  : 99

<!-- -->

-   permet à l'outil d'accepter une date de baptême si la date de naissance n'est pas connue et d'accepter la date d'inhumation si la date de décès n'est pas connue. Elle permet aussi à l'outil d'accepter les dates «inexactes» (c-à-d toute date Gramps «légitime» qui n'est pas une date complète - avec un jour, un mois et une année explicites).

-   : vérifie si les dates sont valides.

#### Femmes

-  : 17

-  : 48

-  : 12

#### Hommes

-  : 18

-  : 65

-  : 15

#### Familles

-  : 30

-  : 8

-  : 25

#### Résultat de la vérification des données

![[_media/Outil_utilverifdonneesresult_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vérification des données - Résultat]] Si vous êtes d'accord avec les critères, cliquez sur le bouton (ou le raccourci clavier et vous obtiendrez une fenêtre .

Selon vos critères et données une liste sera affichée. Plusieurs types de résultat sont listées ci-dessous. Mais il en existe d'autres.

- Individus non reliés (sans parents ou conjoint ou enfants ou fratrie)
- père à un âge avancé ou décédé
- mariage après le décès ou avant la naissance
- grand écart d'âge entre les enfants
- mariage précoce ou tardif
- mère jeune ou pas encore née
- conjoint portant le même nom de famille
- mariage entre individus du même sexe / mère de genre masculin
- …

Au bas de la fenêtre, il y a quatre boutons pour faciliter la sélection : , , , et .

Double-cliquer sur une ligne permet de voir et/ou d'éditer vos données.

Avec le bouton (ou le raccourci clavier ) vous fermez la fenêtre .

#### Exemple

Pour démontrer à quel point cet est maniable, voici deux exemples tirés de données existantes :

- La mise en garde affichait « mère de genre masculin » : en vérifiant les données il y avait une famille ayant pour père : Anna Roelants. Heureusement dans la on pouvait lire : *Le mariage de Adam Roelants et de Cornelia Crabbe*. C'était une faute de frappe : Anna étant Adam. Sans cet **Outil** il aurait été difficile de mettre à jour cette erreur.
- La mise en garde affichait « mariage tardif », en vérifiant les données : homme né en 1738, femme née en 1756, mariage en 1804 \[Calendrier Grégorien\], tout semblait valide, mais ils avaient 66 et 48 ans ! L'alerte s'affiche parce que dans les **critères généraux** la limite a été définie à **60** ans.

[O](wiki:Category:Fr:Documentation)
