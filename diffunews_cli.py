#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Script pour avoir les statistiques de la partie documents."""
import base64
import sys
import sqlite3
import os

sys.path.insert(0, './fonctions')
from fonction_creationPDF import creationPDF
###################
def creation(sourcefile, destinationpath, sqllocation, sqloriginality, sqltargetaudience, title="Titre"):
    global numero
    global page
    page=1
    numero=1
    print("Creation par BQDiffuNews")
    print("sourcefile = " + sourcefile)
    print("destinationpath = " + destinationpath)
    print("sqllocation = " + sqllocation)
    print("sqloriginality = " + sqloriginality)
    print("sqltargetaudience = " + sqltargetaudience)
    print("titre du document = " + title)



    connection = sqlite3.connect(sourcefile)
    cursor = connection.cursor()
#    sql="SELECT title,author,publisher,lccontrolnumber,isbn13,callnumber,description,front_cover FROM book WHERE location LIKE ('" + emplacement + "') ORDER BY author ASC"
#    sql="SELECT title,author,publisher,lccontrolnumber,isbn13,callnumber,description,front_cover FROM book WHERE  originality IN('DON-2023') ORDER BY author ASC" # DON2023
#SELECT title,author,publisher,lccontrolnumber,isbn13,callnumber,description,front_cover FROM book WHERE location = "RP-Romans Policier" AND originality = "BDP" INTERSECT SELECT title,author,publisher,lccontrolnumber,isbn13,callnumber,description,front_cover FROM book WHERE target_audience = "Adultes";
#    cur.execute("SELECT count(myoid) FROM book WHERE originality = ?", (data,))
    cursor.execute("SELECT title,author,publisher,lccontrolnumber,isbn13,callnumber,description,front_cover FROM book WHERE location = ? AND originality = ? INTERSECT SELECT  title,author,publisher,lccontrolnumber,isbn13,callnumber,description,front_cover FROM book WHERE target_audience = ? ORDER BY author",(sqllocation, sqloriginality, sqltargetaudience,))
    resultats = cursor.fetchall()
    i=0
    for document in resultats:
        if document[7] is not None:
            i += 1
            titre = document[0]
            auteur = document[1]
            editeur = document[2]
            description = document[3]
            isbn = document[4]
            cote = document[5]
            resume = document[6]
            resume = resume.replace("'","\'")
            image = base64.b64decode(document[7])

        if i==1:
            titre1 = titre
            print(titre1)
            auteur1 = auteur
            editeur1 = editeur
            description1 = description
            emplacement = "TEST"
            isbn1 = isbn
            cote1 = cote
            resume1 = resume
            image1 = image

        if i==2:
            titre2 = titre
            print(titre2)
            auteur2 = auteur
            editeur2 = editeur
            description2 = description
            emplacement = "TEST"
            isbn2 = isbn
            cote2 = cote
            resume2 = resume
            image2 = image
            i = 0
            page2="pleine"
            page += 1

            creationPDF(titre1,auteur1,editeur1,description1,isbn1,cote1,resume1,image1,\
                        titre2,auteur2,editeur2,description2,isbn2,cote2,resume2,image2,\
                        page,emplacement,page2,title,destinationpath)

        # if document[0] is None:
        #     print("Le document est vide")
        #     page2="vide"
        #     print("document VIDE")
        #     titre2="FIN"
        #     auteur2="FIN"
        #     editeur2="FIN"
        #     description2="FIN"
        #     isbn2="FIN"
        #     cote2="FIN"
        #     resume2="FIN"

            creationPDF(titre1,auteur1,editeur1,description1,isbn1,cote1,resume1,image1,\
                        titre2,auteur2,editeur2,description2,isbn2,cote2,resume2,image2,\
                        page,emplacement,page2,title,destinationpath)
    cursor.close
    connection.close()

def messageusage():
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("diffunews version 2023-11-02")
    print("Pour utiliser l'outil diffunews, vous devez remplir les 6 arguments")
    print("usage : ./diffunews_cli.py databse.sqlite(1) \"destinationpath\"(2) \"location_field\"(3) \"originality_field\"(4) \"target_audience_field\"(5) \"title page pdf\"(6)")
    print("Argument 1 : fichier source -> une base BiblioteQ .sqlite.")
    print("Argument 2 : le répertoire de travail de diffunews.")
    print("Argument 3 : l'emplacement des documents dans la base BiblioteQ (champ location).")
    print("Argument 4 : l'origine des documents dans la base BiblioteQ (champ originality).")
    print("Argument 5 : le public cible dans la base BiblioteQ (champ target_audience).")
    print("Argument 6 : le titre des pages générées par diffunews.")
    print("exemple :")
    print("./diffunews_cli.py Exemples/test.sqlite \"/home/user/Bureau\" \"R-Romans\" \"DONS-2023\" \"Adultes\" \"Romans : Nouveautés Octobre 2023\"")

if __name__ == "__main__":
    try:
        sourcefile = (sys.argv[1])
        destinationpath = (sys.argv[2])
        sqllocation = (sys.argv[3])
        sqloriginality = (sys.argv[4])
        sqltargetaudience = (sys.argv[5])
        title = (sys.argv[6])
        creation(sourcefile, destinationpath, sqllocation, sqloriginality, sqltargetaudience, title)
    except:
        messageusage()
