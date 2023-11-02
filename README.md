I'm not a developer, so there's no guarantee that it will work for you.

Je ne suis pas développeur donc aucune garantie que cela fonctionne bien chez vous.

------------------------------------------------------------
> Merci à "Textbrowser" pour son superbe logiciel de gestion de bibliothèque : BiblioteQ.
------------------------------------------------------------
### BQDiffunews : version 2023-11-02 : EN COURS DE CRÉATION ###
------------------------------------------------------------
## BQDiffunews est un outil pour créer une newletter sous forme d'un document pdf.
------------------------------------------------------------
## Description
Pour créer la newletter, l'outil a besoin que les champs des documents soient remplis.

* 1 : Titre (BQ : title)
* 2 : Auteur (BQ : author)
* 3 : Editeur (BQ : publisher)
* 4 : Description physique (BQ : lccontrolnumber)  ( attention : choix personnel)
* 5 : ISBN13 (BQ : isbn13)
* 6 : Cote (BQ : callnumber)
* 7 : Résumé (BQ : description)
* 8 : Image couverture (BQ : front_cover)

------------------------------------------------------------

## la commande diffunews_cli.py prend 6 paramètres
./diffunews_cli.py databse.sqlite(1) "destinationpath"(2) "location_field"(3) "originality_field"(4) "target_audience_field"(5) "title page pdf"(6)

*  1 : une base BiblioteQ .sqlite
*  2 : le répertoire de travail
*  3 : l'emplacement (BQ : location)
*  4 : l'origine des documents  (BQ : originality)
*  5 : le public cible (BQ : target_audience)
*  6 : le titre des pages`

exemple :
./diffunews_cli.py Exemples/test.sqlite "/home/user/Bureau" "R-Romans" "DONS-2023" "Adultes" "Romans : Nouveautés Octobre 2023"

1 - il créer des images 102.pdf 103.pdf ...

2 - le script **diffunews_creation_newletter.py**
 permet de regrouper les pdf (102; 103; ...) pour ne former qu'un seul fichier newletter.pdf

------------------------------------------------------------
### EN COURS :
- [ ] automatiser la création d'un seul document.
- [ ] créer interface gui.
------------------------------------------------------------
##Installation testé sur LinuxMint21.2

* ### paquets .deb à installer avec qpt-get
    * python3.12
        * base64
        * os
        * sqlite3
        * sys

* ### modules python à installer
    * pip install fpdf2

------------------------------------------------------------
## Distribution (dans répertoire Distribution)
* ### PAS ACTIF
------------------------------------------------------------

------------------------------------------------------------
## Exemple de résultat :
![Texte alternatif](Exemples/exemple.png)


[Exemple de résultat en pdf](Exemples/newletter.pdf)


