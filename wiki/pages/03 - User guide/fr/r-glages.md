---
title: Fr:Manuel wiki pour Gramps 6.0 - Réglages
categories:
- Fr:Documentation
managed: false
source: wiki-scrape
wiki_revid: 111103
wiki_fetched_at: '2026-05-30T18:41:13Z'
lang: fr
---

{{#vardefine:chapter\|13}} {{#vardefine:figure\|0}}

## Préférences

La plupart des paramètres de Gramps sont configurées dans la boîte de dialogue accessible via .

![[_media/Prefs_fr-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Préférences générales]]

Les onglets dans le haut de la fenêtre affichent les catégories d'option disponibles.

### Général

Cette catégorie regroupe deux sections correspondant aux préférences applicables aux opérations générales du programme. Les options sont :

#### Paramètres généraux de Gramps

- : cette option affecte l'importation des données. Si elle est établie, chaque article qui est importé contiendra une référence source au fichier importé. **Note : L'ajout d'une source par défaut peut ralentir significativement l'importation de vos données.**

-  : (par défaut : `Importé le %d/%m/%Y à %H:%M:%S` ) **Note - Ajouter une [étiquette](wiki:Gramps_Glossary#tag) à l'importation peut significativement ralentir l'importation de vos données.**

- : Cette option contrôle l'activation ou non du vérificateur d'orthographe pour les notes. Le paquet gtkspell doit être chargé pour que cette option soit possible.

- : Cette option contrôle l'activation ou non du dialogue au démarrage.

- : cette option contrôle l'activation ou non de l'affichage de la dernière vue utilisée. L'activez vous amenera à la vue que vous aviez lorsque vous avez quitté le programme la dernière fois.

- : vous permet de définir le nombre de générations à utiliser pour déterminer les relations. La valeur par défaut est **15**.

- : ici vous pouvez saisir le chemin de vos objets media. Cliquer sur le bouton ouvrira l'éditeur permettant de dans lequel vous indiquer le chemin choisi.

#### Gestion des greffons tiers

- Sélectionnez la fréquence à laquelle Gramps vérifie les mises à jour des [greffons](wiki:6.0_Addons#Installing_Addons_in_Gramps). Par défaut : *Jamais*

- Par défaut: *Seulement les nouveaux greffons*

- Par défaut : [`https://raw.githubusercontent.com/gramps-project/addons/master/gramps51`](https://raw.githubusercontent.com/gramps-project/addons/master/gramps51)

- 

-   
  Bouton pour forcer une vérificatons pour les greffons. Si des greffons sont disponibles, vous verrez alors une fenêtre où vous pouvez les choisir et les installer.

{{-}}

###### Mises à jour disponibles pour les greffons Gramps

![[_media/Pref_majgreffons_51_fr.png|Right|thumb|550px|Le fenêtre des "Mises à jour disponibles pour les greffons Gramps" - liste pour Gramps 6.0]]

La fenêtre des va afficher une liste ventilée par **Type** dans laquelle vous pouvez naviguer en déployant la colonne Sélection pour chaque "Type".

- Vous pouvez sélectionner la case à cocher des greffons que vous voulez installer.
- Puis sélectionnez le bouton pour télécharger ces greffons depuis *Internet*.
- Une fois téléchargé, dans la fenêtre de , cliquez sur le bouton
- Depuis la fenêtre sélectionnez le bouton .
- Pour utiliser les greffons vous aurez besoin de quitter Gramps. Les greffons seront alors disponibles au prochain lancement.

{{-}}

#### Fenêtre astuce du jour

![[_media/Astucejour-52-fr.png|Right|thumb|400px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Astuce du jour]]

Quand elle est activée dans , onglet la fenêtre de l' affiche des astuces utiles.

Les options suivantes sont disponibles :

-  (coché par défaut - une fois activé) - décochez pour arrêter l'apparition des astuces à l'avenir.

- \- Passe à l'astuce suivante.

- \- fermer pour cette session jusqu'au prochain redémarrage de Gramps.

{{-}}

### Arbre Familial

![[_media/Pref_arbrefamil_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Preferences - Onglet «arbre familial»]]

Cet onglet contient les préférences quant aux **paramètres et à la sauvegarde la base de données**.

- C'est le format de [base de données](https://fr.wikipedia.org/wiki/Base_de_données) dans laquelle toutes les informations que vous avez saisies dans Gramps sont enregistrées.

  - *BSDDB* - Format de base de données historique des versions précédentes.
  - [**SQLite**](https://fr.wikipedia.org/wiki/SQLite) (par défaut depuis la version 6.0) - Voir [DB-API Database Backend](wiki:DB-API_Database_Backend) (en anglais)

- Si votre base de données est installé sur un serveur distant (vide par défaut - votre base de données est installée localement sur votre poste de travail)

- sur le serveur

<!-- -->

- : le chemin par défaut où est enregistré la base de donnée est **répertoire personnel/.gramps/grampsdb**. A moins de vraiment vouloir le changer, gardez le chemin par défaut. Ce chemin est dans le [Répertoire utilisateur](wiki:Gramps_6.0_Wiki_Manual_-_Répertoire_utilisateur) déterminé par votre système d'exploitation.

- : cochez ce choix pour charger automatiquement la dernière base ouverte, lors du lancement de Gramps.

- Le répertoire dans lequel seront enregistrées les sauvegardes automatiques. Par défaut, à la racine du répertoire utilisateur.

- 

- \-

  - **Jamais** (par défaut)
  - *Toutes les 15 minutes*
  - *Toutes les 30 minutes*
  - *Chaque heure*

{{-}}

Voir également :

- [Backup omissions](wiki:Template:Backup_Omissions) - ce qui n'est pas inclus durant les sauvegardes (en anglais)
- Greffon [PostgreSQL](wiki:Addon:PostgreSQL) - Il ajoute la prise en charge de bases de données PostgreSQL.

### Affichage

![[_media/Prefs_affichage-50-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Préférences de l'affichage]]

Cet onglet contient les préférences pour l'affichage des données et des noms. Les options sont :

- : cette option contrôle l'affichage des noms dans la base de données courante (le paramètre est enregistré dans la base de données et ne touche pas le reste du système). Dans Gramps il y a deux types d'affichage des formats de nom : les formats prédéfinis et les formats personnalisés définis par l'utilisateur. Plusieurs formats prédéfinis sont disponibles : Nom, Prénom Suffixe - Prénom, Nom Suffixe - Nom, prénom (courant) etc.

  - Cliquer sur le bouton affichera une fenêtre avec la liste des options disponibles. Le format n'est qu'un exemple. Si les formats prédéfinis ne vous conviennent pas vous pouvez définir vos propres formats. Utilisez le bouton pour ajouter un format de nom à la liste. Cliquer une fois vous donnera le format : **NOM DE FAMILLE, Prénom Suffixe (usuel)** qui sera par exemple : **SMITH, Edwin Jose Sr (Ed)**. Si vous ajoutez des nouveaux formats de nom, les boutons et seront disponibles pour modifier la liste des formats de nom. (Voir les détails plus bas dans cette page).
    -  Si sélectionné, permet à Gramps de considérer les noms patronymiques ou matronymiques comme des noms de famille.

- : cette option contrôle l'affichage des dates. C'est un paramétrage global qui nécessite un redémarrage de Gramps pour être pris en compte et s'applique à l'affichage de toutes les dates de toutes les base de données de Gramps jusqu'à ce que vous le changiez à nouveau. Différents formats sont disponibles qui dépendent de la version localisée de votre système.

  - AAAA-MM-JJ (ISO) - Exemple 2021-03-28. C'est le standard international [ISO 8601](https://fr.wikipedia.org/wiki/ISO_8601) d'échange de données, utile pour partager des informations entre différents pays avec des conventions d'écriture différentes.
  - **Défaut système** (J/M/A) (*par défaut*)
  - Jour Mois Année
  - Jour MOI Année
  - Jour. Mois Année
  - Jour. MOI Année
  - Mois Jour, Année
  - MOI Jour, Année

<!-- -->

-  : cette option gère l'affichage des lieux.

  - **Complet** (par défaut)
    - Sélectionner le bouton va appeler l' (Voir les détails plus bas dans cette page).

<!-- -->

- - **Années** (*par défaut*)
  - Années, Mois
  - Années, Mois, Jours

- : (**Grégorien** par défaut)cette option contrôle l'affichage des calendriers dans les rapports, outils, gramplets, vues. Différents calendriers sont disponibles (voir [Édition des dates](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_1/fr#Édition_des_dates)). Deux dates avec deux calendriers différents n'affichera pas correctement une chronologie ou une période, (En utilisant le calendrier Grégorien comme calendrier par défaut, les utilisateurs auront une meilleure cohérence des dates affichées sur une période).

<!-- -->

- : cette option affecte le nom de l'enfant lorsqu'il est ajouté à la base de données. Par défaut, Le utilisera le nom de famille du père. Si est sélectionné, rien ne sera proposé. Sélectionner utilisera le nom du père suivi du nom de la mère. Enfin, utilisera le nom du père suivi par le suffixe "sson" (le fils de Edwin sera proposé comme Edwinsson).

.

- - **Inconnu** (*par défaut*)
  - Mariés
  - Non mariés
  - Union civile

<!-- -->

- Par défaut : **150**

<!-- -->

- : cette option contrôle l'information affichée dans la barre d'état. Cela peut être le nom de la **Nom et identifiant Gramps de l'individu actif** (par défaut) ou la **Relation avec la souche**.

<!-- -->

- : cette option contrôle si une description textuelle est affichée à côté de l'icône dans le [Navigateur](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/fr#Navigateur) de la fenêtre principale. Cette option prend effet après un redémarrage de Gramps.

<!-- -->

- *non sélectionné* (par défaut)

#### Édition de l'affichage des noms

![[_media/Param_editionaffichnom_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} La fenêtre de l&#39;éditeur de l&#39;affichage des noms - depuis le menu: &quot;Édition &gt; Préférences...&quot; - onglet &quot;Affichage&quot; -]] Les clés suivantes sont remplacées par les parties du nom appropriées :

- <b>Prénom</b> - prénom(s)
- <b>Titre</b> - titre (Dr., Me., Duc)
- <b>Usuel</b> - prénom usuel
- <b>Initiales</b> - initiales des prénoms
- <b>Principal</b>,<b>Principal\[pre\]</b>,<b>Principal\[nom\]</b>,<b>Principal\[con\]</b> - nom de famille principal complet, préfixe, nom seul, connecteur
- <b>Patronyme</b>,<b>Patronyme\[pre\]</b>,<b>Patronyme\[nom\]</b>, <b>Patronyme\[con\]</b> - patronyme complet, préfixe, nom seul, connecteur
- <b>Reste</b> - les noms de familles secondaires
- <b>NomDit</b> - surnom du nom de famille
- <b>NomsDeFamilleBrut</b> - tous les noms de famille sans préfixe et connecteurs
- <b>Nom</b> - nom (avec préfixe et connecteurs)
- <b>Suffixe</b> - suffixe (Jr., Sr.)
- <b>Surnom</b> - surnom
- <b>Courant</b> - surnom, sinon le premier prénom
- <b>Préfixe</b> - préfixe (von, de, de la)
- <b>PasPatronyme</b> - tous les noms de famille sauf le principal & le pa/matronyme

Les parenthèses supplémentaires et les virgules sont enlevées. N'importe quel autre texte apparaîtra littéralement.

![[_media/Param_editeurnom_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Éditeur de nom pour un individu - Accessible à partir de la fenêtre d'édition de l'individu, onglet Noms]]

**Exemple:** «Dr. Edwin Jose von der Smith and Weston Wilson Sr (“Ed”) - Underhills» . *Edwin Jose*: les prénoms, *von der*: le préfixe, *Smith* et *Weston*: Nom de famille, *and*: <abbr title="le connecteur">\[con\]</abbr>, *Wilson*: le nom patronymique, *Dr.*: le titre, *Sr*: le suffixe, *Ed*: le surnom, *Underhills* <abbr title="Nom-dit, sobriquet">Nom-dit</abbr>, Jose <abbr title="appelé (prénom usuel)">usuel</abbr>.

Tous les champs de cet exemple, sauf le surnom de famille, peuvent être ajoutés dans les contrôles standard de la fenêtre de modification d'un individu. Dans cette même fenêtre, utilisez l'onglet de la section inférieure ; double-cliquer sur le pour ouvrir le dialogue et accéder à des champs supplémentaires comprenant : le Nom-dit, des contrôles de regroupement, de tri et d'affichage particulier, des contrôles de dates pour l'utilisation d'un nom particulier. {{-}}

#### Éditeur de format du lieu

![[_media/Param_editeurformlieu_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogue Éditeur de format du lieu - depuis le menu : "Édition &gt; Préférences..." - onglet "Affichage"]]

Accessible depuis l'onglet [Affichage](#Affichage) l'option format du lieu.

Cet onglet contient les préférences liées à l'affichage des lieux.

- : un nom unique pour le format du lieu.

- : les noms (hiérarchie) des lieux à afficher.

Chaque niveau dans la hiérarchie est représenté par un entier positif, commençant par 0 pour le lieu sélectionné et augmentant de 1 pour chaque niveau supérieur dans la hiérarchie. Les niveaux peuvent également être représentés par des entiers négatifs, commençant par *-1* pour le plus haut niveau (généralement un pays) et diminuant de 1 pour chaque niveau inférieur dans la hiérarchie. De plus, le lieu *habité* (ville, commune, village ou hameau) est représenté par la lettre *p*; pouvant être utilisé avec des niveaux (par exemple. *p+1* ou *p-2*).

Les noms de lieux à afficher sont définis soit par une liste de valeurs séparées par des virgules (**p0,p+1,p+2** par exemple), soit par un niveau de début et un niveau de fin séparés par deux-points (**0:+3** par exemple) ; le niveau de début doit être inférieur au niveau de fin. Par défaut, si absents, les niveaux de début et de fin sont respectivement 0 et -1.

*Exemple* : vous avez suivi la hiérarchie administrative pour saisir la commune de "Montlebon", arrondissement de "Pontarlier", département du "Doubs", région "Bourgogne-Franche-Comté", pays "France" (saisir cette imbrication de lieu utilise l'onglet "Partie de" dans la saisie des lieux). Néanmoins, le libellé complet est peu lisible à l'écran ; si vous définissez les niveaux à '0,+2', vous obtiendrez "Montlebon, Doubs" assez explicite. Le résultat est néanmoins dépendant de la rigueur dans la saisie des lieux.

- : "Aucun" (par défaut), "Numéro Rue" ou "Rue Numéro". Cette option rassemble le numéro et la rue pour supprimer la virgule. Pour que cette option fonctionne, la rue doit avoir le [<strong>Type</strong>](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Fonctionnement_des_événements,_sources,_lieux,_dépôts_et_notes#Édition_de_l.27information_sur_les_lieux) *Rue* et le numéro du bâtiment doit avoir le [<strong>Type</strong>](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Fonctionnement_des_événements,_sources,_lieux,_dépôts_et_notes#Édition_de_l.27information_sur_les_lieux) *Numéro*.

- : (vide par défaut) un code à deux lettres pour la langue.

-  (non coché par défaut)

{{-}}

### Texte

![[_media/Param_texte_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Préférences de texte]]

Cette catégorie contient les préférences sur comment les noms et les enregistrements privés et manquants doivent être affichés.

- : ce champ vous permet de déterminer comment le nom de famille manquant doit être affiché. La valeur par défaut est **\[Nom de famille manquant\]**. Vous pouvez le modifier par \[--\] ou ce qui vous convient le mieux.

- : ici vous pouvez déterminer comment le prénom manquant doit être affiché. La valeur par défaut est **\[Prénom manquant\]**. Vous pouvez le modifier.

- Par défaut : **\[Informations absentes\]**

- Par défaut : **\[Vivant\]**

-  : Par défaut : **\[Vivant\]**

-  : Par défaut : **\[Enregistrement privé\]**

### Formats ID

![[_media/Param_idformat_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Préférences du format des identifiants]]

Cette catégorie contient les préférences pour la génération automatique des identifiants Gramps.

-  : fournit un modèle pour générer les identifiants pour un individu. Par défaut : **I%04d**.

- : fournit un modèle générant les identifiants pour une famille. Par défaut : **F%04d**.

- : fournit un modèle générant les identifiants pour un lieu. Par défaut : **P%04d**.

- : fournit un modèle générant les identifiants pour une source. Par défaut : **S%04d**.

- : fournit un modèle générant les identifiants pour une citation. Par défaut : **C%04d**.

- : fournit un modèle générant les identifiants pour un objet medium. Par défaut : **O%04d**.

- : fournit un modèle générant les identifiants pour un événement. Par défaut : **E%04d**.

- : fournit un modèle générant les identifiants pour un dépôt. Par défaut : **R%04d**.

- : fournit un modèle générant les identifiants pour une note. Par défaut : **N%04d**.

### Dates

![[_media/Param_dates_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Préférences des dates]]

Cette catégorie contient les préférences relatives à la gestion des dates.

- Par défaut **<b>%s</b>**

  - Les balises utiles sont :
    - <b>\<b\>Gras\</b\></b> (par défaut)
    - <big>\<big\>Agrandit la police\</big\></big>
    - <i>\<i\>Italique\</i\></i>
    - <s>\<s\>barré\</s\></s>
    - <sub>\<sub\>indice\</sub\></sub>
    - <sup>\<sup\>exposant\</sup\></sup>
    - <small>\<small\>Diminue la taille de la police\</small\></small>
    - `<tt>Police non proportionnelle</tt>`
    - <u>\<u\>Souligné\</u\></u>
      - Par exemple : \<u\>\<b\>%s\</b\>\</u\> va afficher <u><b>date en gras soulignée</b></u>.

- Par défaut : **50**

  - Définit le nombre d'années avant/après un évènement "**vers <date>**" pendant lesquels l'évènement sera valide dans un filtre.
  - Utilisé dans le calcul de l'âge des individus.

- Par défaut : **50**

  - Définit le nombre d'années après un évènement "**après <date>**" pendant lesquels l'évènement sera valide dans un filtre.
  - Utilisé dans le calcul de l'âge des individus.

- Par défaut : **50**

  - Définit le nombre d'années avant un évènement "**avant <date>**" pendant lesquels l'évènement sera valide dans un filtre.
  - Utilisé dans le calcul de l'âge des individus.

- Par défaut **110**

  - En l'absence de décès, âge au delà duquel Gramps va considérer que l'individu n'est plus vivant.

- Par défaut : **20**

- Par défaut : **13**

- Par défaut : **20**

{{-}} Voir aussi :

- [Probablement en vie](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive/fr)
- [Édition_des_dates](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_1/fr#Édition_des_dates)

{{-}}

### Informations sur le chercheur

![[_media/Param_chercheur_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Préférences des informations du généalogiste]]

Entrez vos informations personnelles dans les champs de saisie de telle façon que vous puissiez être contacté quand vous publiez votre arbre généalogique. Bien que Gramps vous interroge, cette information ne sert qu'à créer des fichiers GEDCOM valides. Le format GEDCOM a besoin de données sur l'auteur du fichier. Vous pouvez laissez les données vides mais les fichiers GEDCOM exportés ne seront pas valides.

Les champs texte disponibles sont (tous vides par défaut) :

- 

- 

- 

- 

- 

- 

- 

- 

- 

Ces informations saisies dans cet onglet des préférences jouent le rôle d'informations par défaut. Pour renseigner des informations spécifiques à un arbre familial, utilisez le menu . {{-}}

### Messages d'alerte

![[_media/Param_alerte_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Préférences des mises en garde]]

Cette catégorie contrôle l'affichage des dialogues de mise en garde, permettant de ré-activer les dialogues qui ont été désactivés.

- 

- 

- 

- 

{{-}}

### Couleurs

![[_media/Param_couleurs_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Préférences des couleurs]]

Cette catégorie permet de définir les couleurs utilisées dans les boites pour les vues graphiques. Vous pouvez sélectionner le

- *Couleurs claires*(par défaut) ou *Couleurs sombres*

  - \- restore les thèmes de couleurs par défaut.

- Couleurs pour les hommes

- Couleurs pour les femmes

- Couleurs pour les individus de genre inconnus

- Couleurs pour les nœuds familiaux

- Autres couleurs

{{-}}

#### Choisissez une couleur

![[_media/Param_choixcouleur_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogue "Choisir une couleur"]]

Sélectionnez une couleur à partir de la palette de couleur ou sélectionnez le bouton pour créer votre propre couleur soit directement par un 'code hexadécimal', soit par le curseur ou un clic de souris. {{-}}

### Symboles généalogiques

![[_media/Prefs_symboles-51-fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Préférences - Symboles généalogiques]]

Ils permettent d'utiliser des symboles généalogiques à la place d’abréviations de texte dans les rapports, graphiques de l'interface Gramps.

Cet onglet permet l'utilisation d'une police qui est capable d'afficher tous les symboles généalogiques (Une fois configuré, voir les pré-requis plus bas).

Si vous sélectionnez la case à cocher "Utilisez les symboles", Gramps va utiliser la police sélectionnée si elle existe.

Ceci est utile si vous voulez ajouter des symboles phonétiques dans une note pour montrer comment prononcer un nom ou si vous mélangez plusieurs langues comme le grec et le russe.

Vous pouvez configurer le symbole de décès seulement dans cet onglet.

  
Liste des symboles généalogiques affichés (dans l'ordre affiché en bas de la copie d'écran) :

- Femme
- Homme
- Sans sexualité, sans sexe, sans genre
- Lesbianisme
- Homosexualité masculine
- Hétérosexualité
- Transgenre, hermaphrodite (en entomologie)
- Transgenre
- Neutre

<!-- -->

- Illégitime
- Naissance
- Baptême
- Fiancé
- Mariage
- Divorce
- Partenaires non mariés
- Inhumé
- Incinéré/Urne funéraire
- Mort au combat
- Éteint

<!-- -->

- Décès

| Signification | Symbole | code Unicode | Nom |
|----|----|----|----|
| Homme | ♂ | U+2642 | Signe masculin |
| Femme | ♀ | U+2640 | Signe féminin |
| Inconnu | ⚪︎ | U+26AA | Cercle vide moyen |
| hermaphrodite | ⚥ | U+26A4 | Signes masculin féminin imbriqués |
| Neutre | ⚲ | U+26B2 | Neutre |
| Naissance | \* | U+002A | Astérisque |
| Baptême | ~ | U+007E | Tilde |
| Décès | ✝︎ | U+271D | Croix latine |
| Inhumation | ⚰︎ | U+26B0 | Cercueil |
| Crémation | ⚱︎ | U+26B1 | Urne funéraire |
| Mort-né | ✝︎\* | U+0086 U+002A | Croix latine, Astérisque |
| Naissance illégitime | \*⃝ | U+002A U+20DD | Astérisque encerclé |
| Naissance illégitime | ⊛ | U+229B | Opérateur astérisque encerclé |
| Mort au combat | ⚔︎ | U+2694 | Épées croisées |
| Extinction de la lignée | ‡ | U+2021 | Double dague |
| approximativement | ± | U+00B1 | Plus-Moins |
| avant | \< | U+003C | Symbole inférieur |
| après | \> | U+003E | Symbole supérieur |
| Fiancés | ⚬ | U+26AC | Cercle vide moyennement petit |
| Mariés | ⚭ | U+26AD | Symbole mariage |
| Divorcés | ⚮ | U+26AE | Symbole divorce |
| Non mariés | ⚯ | U+26AF | Symbole des partenaires non mariés |

{{-}}

#### Pré-requis pour utiliser les symboles généalogiques

![[_media/Param_symbolgenealog_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Préférences - Onglet «Symboles généalogiques»]]

##### Configuration initiale

Si le programme `fontconfig pour Python` prérequis est installé, dans l'onglet cliquez sur le bouton ; Gramps va essayer de détecter toute police de texte unicode utilisable.

Quand la recherche est terminée, sélectionnez une des polices dans la liste puis cocher la case :

##### Prérequis

Prérequis : **fontconfig pour Python**. L'interface Python de fontconfig et ses dépendances sont nécessaire pour afficher les symboles généalogiques.

Voir aussi:

- Les explications de Tamura Jones sur [les symboles généalogiques](https://www.tamurajones.net/GenealogySymbols.xhtml) *(la section 'Unicode' est particulièrement appropriée)*
- [GEPS 039: Genealogical symbols in gramps](wiki:GEPS_039:_Genealogical_symbols_in_gramps)
- Feature request: Gramps devrait pouvoir utiliser les symboles généalogique partout.
- Chercher dans le tableau de [gramps\gen\utils\symbols.py](https://github.com/gramps-project/gramps/blob/maintenance/gramps51/gramps/gen/utils/symbols.py)

{{-}}

## Autres paramètres

A côté du dialogue , il existe d'autre paramètres disponibles dans Gramps. Pour différentes raisons ils ont été rendus plus directement accessibles, comme énuméré ci-dessous.

### L'éditeur de colonne

![[_media/BoutonConfigvue_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Bouton Configurer la vue active…» - Barre d&#39;outils de la catégorie «Individus»]] ![[_media/Param_colonnes_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} L&#39;éditeur de colonnes pour les individus]] ![[_media/Param_colonlieux_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} L&#39;éditeur de colonnes pour les lieux]]

Les colonnes des vues en listes peuvent être ajoutées, enlevées, ou déplacées dans le dialogue .

Pour accéder au dialogue pour la vue en cours, choisissez le menu , cliquer sur le bouton ![[_media/Gramps-config.png]] de la barre d'outil ou utilisez le [raccourci clavier](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/fr#Raccourcis) *Configurer la vue active*.

Seules les colonnes cochées seront montrées dans la vue. Pour changer leur ordre, glisser n'importe quelle colonne à l'endroit désiré à l'intérieur de la fenêtre. Cliquer sur reflétera les changements pour la vue appropriée.

Le tri par défaut pour la vue (toujours croissant) se fait sur la colonne la plus à gauche (la première dans la fenêtre 'Editeur de colonne') ; ainsi, changer la colonne qui est première position va affecter l'ordre de tri.

L' a différents ensembles de colonnes suivant la vue de catégorie qui s'affiche en tableau.

Une fois les changements appliqués, cliquer une fois sur l'en-tête d'une colonne trie la liste de façon croissante selon cette colonne ; cliquer une deuxième fois sur cette même en-tête trie de façon décroissante.

Le sous-ensemble de colonnes affiché et le filtre en cours vont aussi impacter l'exportation par le menu . Les colonnes et enregistrements cachés ne seront pas exportés. {{-}}

### Trier les colonnes

![[_media/Affichagelistetri_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Catégorie «Individus» - Liste triée sur la colonne «date de naissance»]]

Par défaut, chaque vue des catégories présente les données sous forme de tableau avec des colonnes et les rangs sont triés en ordre croissant selon les données de la colonne la plus à gauche. Si le tableau est sous forme groupée, les données groupées seront sous-triées. (Les tableaux dans les onglets avec des sous-ensembles de données, les éditeurs et les sélecteurs fonctionnent de la même façon).

Cliquer une fois sur l'en-tête d'une colonne trie la liste de façon croissante selon cette colonne ; cliquer une deuxième fois sur cette même en-tête trie de façon décroissante.

Le dialogue permet d'ajouter, supprimer ou réordonner les colonnes affichées, ou de changer le tri par défaut de la vue (mais toujours croissant). {{-}}

### Définir la souche

![[_media/Définirsouche_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu définissant la <em>souche</em>]]

Pour désigner l'individu **Souche**, dans la catégorie Individus, sélectionner l'individu concerné pour en faire la personne active puis choisissez dans le menu. Alternativement, faite un clic-droit sur l'individu sélectionné puis choisissez dans le menu contextuel. Enfin, dans le haut de la fenêtre de saisie d'un individu, un clic-droit en zone vierge ouvre aussi un menu contextuel qui permet de définir l'individu comme souche.

L’individu souche est toujours la personne active dans les situations suivantes :

La souche est la personne active par défaut quand :

- l'arbre familial est ouvert.  
  *(Dans l'onglet Général des Préférences, un paramètre modifie ce comportement. L'option «Se souvenir de la dernière vue affichée» va retourner à la dernière personne active de la session précédente.)*
- le bouton de la barre d'outils est cliqué
- la souche est sélectionné depuis l'entrée du menu contextuel, après un clic du bouton droit de la souris dans les vues.
- le raccourci clavier permet de retrouver la **souche**.

Le bouton ![[_media/Gramps_Go-Home48x48_win.png]] de la barre d'outils est disponible dans les catégories Individus, Relations, Graphiques.

#### Voir aussi :

- [définir la souche](wiki:Gramps_6.0_Wiki_Manual_-_Navigation/fr#Choisir_le_de_Cujus,_la_souche)

{{-}}

### Ajustement de l'affichage

L'affichage de la barre d'outils, la barre d'état ou du filtre est défini dans le menu .

Dans les différentes vues, cliquer sur le menu affichera les boites que vous pouvez sélectionner :

- Navigateur (de catégories)
- Barre d'outils
- Barre latérale
- Barre inférieure
- Plein Écran ()

En plus, selon la vue utilisée, d'autres options sont disponibles via .

- Tableau de bord : mise en page Gramplet (1 à 3)
- Relations : et
- Géographie : la carte et les paramètres de l'animation.

Toutes les autres vues : [l'édition des colonnes](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#L&#39;éditeur_de_colonne).

### Exporter l'affichage

![[_media/Exporteraffichage_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu «Exporter affichage»]]

Dans la majorité des vues, on peut exporter les données affichées. Choisir .

Cette commande de menu n'apparaît que si les données affichées peuvent être exportées. Gramps exportera les données à l'écran selon votre choix : format **CSV** ou feuille de calcul **Open Document**. Vous pouvez ensuite l'ouvrir dans un tableur type LibreOffice Calc.

Noter que la configuration courante des colonnes visibles va déterminer les données exportées. L'exportation ne contiendra que les données des colonnes affichées (dans le même ordre) et sera limité aux enregistrements correspondant aux filtres qui ont été appliqués.

C'est une fonction puissante (*pas de limitations*), comme un rapport. ![[_media/Exportcalc_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Exportation des évènements au format ODS ouvert dans LibreOffice Calc]] {{-}}

### Modularité et greffons

Gramps a été conçu pour recevoir des extensions. L'environnement des greffons (c-à-d greffons, plug-in, extension) apporte une voie de développement par des tiers en dehors de la publication des versions principales.

La documentation pour chaque greffon est assurée en dehors des chapitres principaux de la documentation. L'interface et les fonctionnalités de ces programmes et leur documentation peuvent ne pas être conformes au style du reste de Gramps… bien que les développeurs soient encouragés à faire que leurs extensions soient aussi transparente que possible.

Une brève description avec copie d'écran de chaque greffon est disponible dans la section [Liste des greffons](wiki:6.0_Addons#Addon_List) (en anglais) de cette documentation. Les pages de documentation mises à jour pour ces greffons sont accessibles par les liens dans la première colonne.

Voir le [gestionnaire de greffons](wiki:Gramps_6.0_Wiki_Manual_-_Plugin_Manager/fr) et les [greffons supplémentaires](wiki:Plugins). {{-}}

### Personnaliser le format de sortie des rapports

![[_media/Rapporttxt_parametres_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Options des rapports : section supérieure et inférieure de la fenêtre (exemple pour la fiche familiale]] ![[_media/Stylesdoc_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialogue Styles de document]]

Quels types de personnalisation sont possibles ? La boite de dialogue permet de changer de police, la taille de police, la couleur de police, la couleur de l'arrière plan du texte et l'alignement des paragraphes du rapport.

Pour la plupart des rapports, la boite de dialogue comprend une section supérieure avec des onglets spécifiques à ce rapport. La section inférieure nommée comprend des paramètres communs aux différents rapports.

Dans la partie , la liste déroulante permet de choisir un style existant. Vous pouvez créer votre propre style en cliquant le bouton pour afficher le dialogue , puis cliquer le bouton pour ouvrir le dialogue . {{-}}

#### Éditeur de style

Le dialogue permet de personnaliser le style du document pour chaque rapport. Changez le (Nouveau style par défaut) pour un nom unique qui apparaîtra dans la liste déroulante .

![[_media/Editstyle_descript_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Description]] Dans la partie gauche de la fenêtre, la colonne affiche tous les styles de paragraphes spécifiques à ce rapport, que vous pouvez modifier. La copie d'écran ci-contre montre les styles existant pour le rapport «Arbre des ascendants»

Dans la partie droit, pour chaque style, vous avez trois onglets :

#### Description

S'affiche une courte description de l'usage du style. {{-}}

#### Options de police

![[_media/Editstyle_optpolice_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Options des polices]] Ici vous pouvez choisir le type de police, Roman or Swiss, sa taille en points, la couleur et d'autres options, gras, italique ou souligné {{-}}

#### Options de paragraphe

![[_media/Editstyle_optparag_51_fr.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Options des paragraphes]] Vous réglez l'alignement, la couleur d'arrière-plan, l'indentation (décalage à droite et à gauche), l'espacement avant et après le paragraphe, les bords du style {{-}} Enfin, vous enregistrez vos modification avec le bouton ou vous cliquez pour sortir sans enregistrer. {{-}}

### Menu contextuel

Utilisé en de multiples occasions dans Gramps, accéder au menu contextuel dépend de votre système d'exploitation :

- Avec Microsoft Windows®, vous utilisez généralement le bouton droit de la souris pour afficher ce menu contextuel ou le raccourci clavier +, ou la touche spécifique du clavier (à gauche de la touche Ctrl de droite).
- Avec Apple MacOS®, généralement, vous appuyez sur la touche pendant que vous cliquez le bouton de la souris pour afficher ce menu contextuel, ou deux doigts sur la partie gauche du trackpad. see: [Clic droit sur Mac](https://support.apple.com/fr-fr/guide/mac-help/mh35853/mac)

Voir aussi :

- [Raccourcis-clavier](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/fr)

## Personnalisation

Voici les moyens de personnaliser Gramps.

### Préférences

Voir [Préférences](wiki:Fr:Manuel_wiki_pour_Gramps_6.0_-_Réglages#Préférences) plus haut dans cette page.

### Langue

Gramps est traduit dans de nombreuses langue. Il se lance automatiquement dans votre langue comme pour les autres applications. Certains modules ou greffons peuvent ne pas être traduits et une alerte apparaîtra indiquant qu'il n'y a pas de traduction pour votre langue ; c'est l'anglo-américain, langue par défaut, qui sera alors employé. Ces alertes peuvent être envahissantes.

Si vous êtes aussi à l'aise en anglais qu'avec votre propre langue, vous pouvez traduire ces fonctionnalités pour les non anglophones. Si votre système est configuré pour une autre langue que l'anglais (comme le français, par exemple !), vous pouvez passer outre pour Gramps.

#### Linux

Si vous voulez utiliser une 'variante' de tri qui n'est pas la variante par défaut, démarrez Gramps à partir du terminal avec une variable d'environnement LC_COLLATE différente. Par exemple, la variable de tri (interclassement) pour le suédois est "reformed", mais vous pouvez choisir "standard" à sa place en tapant :

`export LC_COLLATE="sv_SE.UTF-8@collation=standard"`  
`python Gramps.py`

#### MacOS

Pour MacOS©, voir [Advanced setup](wiki:Mac_OS_X:Application_package#Advanced_setup) pour les détails quant au choix de la langue et comment choisir une langue qui n'est pas la langue par défaut, l'interclassement ou le format des dates et nombres.

#### MS Windows

Si vous voulez utiliser Gramps dans une autre langue, c'est à l'installation que vous pouvez sélectionner les langues à installer. Sinon, elles ne seront pas disponibles. Relancer le processus d'installation si nécessaire.

Plus d'information à la page [Télécharger pour Windows](wiki:Download/fr#MS_Windows).

Ensuite, utilisez la commande SET pour régler la variable d'environnement LAN à "en_GB.UTF-8" (anglais britannique). Pour y parvenir, utilisez l'interface de commande ou créer un raccourci de démarrage avec la cible suivante :

`C:\Windows\System32\cmd.exe /c "SET LANG=en_GB.UTF-8 && START /D ^"C:\Program Files\GrampsAIO64-6.0.3^" gramps.exe"`

Pour d'autres paramétrages de Windows®, voir la page correspondante en anglais [Ajouter un raccourci sur le bureau](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Add_Windows_OS_Menu_Item)

{{-}}

### Manipulation avancée des préférences

![[_media/Gramps.ini-Example-40.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Le fichier gramps.ini]]

Gramps utilise les **clés (fichiers .ini)** présentes dans le répertoire *.gramps/gramps\[XX\]* de votre dossier utilisateur sous forme de fichier texte **gramps.ini**, pour gérer les préférences de l'utilisateur. Ce fichier contient les sous-catégories suivantes :

- \[behavior\] (comportement) : les noms de clé comme : betawarn, enable-autobackup, use-tips...
- \[colors\] (couleurs)
- \[database\] (base de données) : concerne les paramètres de base de données de l'arbre familial
- \[export\] (exportation)  : répertoires d'importation / exportation
- \[geography\] (géographie)
- \[interface\] : de nombreuses clés pour la largeur et la hauteur des différents vues : event-height (hauteur pour les évènements, etc) : 450, event-ref-height : 585, event-ref-wight : 728, event-width : 712 ...
- \[paths\] (Les chemins) : les clés liées aux fichiers et répertoires récemment importés
- \[plugin\] (greffons)
- \[preferences\] (Les préférences) : les clés liées aux préférences : tous les préfixes communs, couleur du marqueur...
- \[researcher\] (chercheur) : l'information sur le propriétaire de la base de données
- \[utf8\]

{{-}}

#### Paramètres avancés nom de fichier de sauvegarde

Vous pouvez définir le modèle de nommage du fichier de sauvegarde en réglant *`paths.quick-backup-filename`* dans le fichier de clés `~/.gramps/gramps51/gramps.ini` comme suit : {{-}}

`[paths]`  
`;;quick-backup-filename='%(filename)s_%(year)d-%(month)02d-%(day)02d.%(extension)s'`

en enlevant les deux points virgules (`;;`) devant la ligne de clé et en utilisant, pour le modèle, un des mots clés suivant :

- filename : nom donné au fichier
- year : année
- month : mois
- day : jour
- hour : heure
- minutes : minutes
- seconds : secondes
- extension :
  - **.gpkg**(par défaut) si vous incluez les media.
  - *.gramps* si vous excluez les media.

Utilisez la clé de fichier appropriée ~/.gramps/gramps{XX}/gramps.ini

- Gramps version 6.0 :

`~/.gramps/gramps51/gramps.ini`

Voir aussi :

- [Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/fr#Fenêtre de sauvegarde](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/fr#Fenêtre_de_sauvegarde)
- [Gramps_6.0_Wiki_Manual_-_Command_Line/fr#Option de configuration (config)](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/fr#Option_de_configuration_(config))
- [Install_latest_BSDDB#Make_Gramps_use_bsddb3](wiki:Install_latest_BSDDB#Make_Gramps_use_bsddb3)
- [Customize_the_Genealogical_Symbols_lookup_table#Genealogy_symbols_preferences](wiki:Customize_the_Genealogical_Symbols_lookup_table#Genealogy_symbols_preferences)

{{-}}

### Thème

L'aspect de Gramps peut aussi être modifié (pages en anglais).

- [Addon:Theme Preferences](wiki:Addon:ThemePreferences)
- [Windows_AIO_themes](wiki:Windows_AIO_themes)
- [GTK 3 theme - GEPS 029: GTK3-GObject introspection Conversion](wiki:GEPS_029:_GTK3-GObject_introspection_Conversion#GTK_3_theme)
- [Overrule_Gramps_Icons](wiki:Overrule_Gramps_Icons) - pour les anciennes versions de Gramps.
- [UI style](wiki:UI_style)

Certains rapports peuvent aussi être modifiés:

- [Website report Themes](wiki:Website_report_Themes)

{{-}}

[M](wiki:Category:Fr:Documentation)
