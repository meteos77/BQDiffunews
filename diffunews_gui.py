#!/usr/bin/env python3
# -*- coding: utf-8 -*-



"""
date    : "2023-09-10"
version : "0.1"

Avoir une fenetre
Avoir une fenetre d'aide



Traduction : OK
Script pour générer
Selecteur fichier : OK

-------------------------
remplir les variables extensionsourcefile ; extensiondestinationfile
changer : Mon Application
"""


import os
from pathlib import Path
import sys
import sqlite3

from PyQt5 import QtWidgets
from PyQt5.Qt import QDir
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.QtCore import QTranslator, QLocale, pyqtSlot
from PyQt5.uic import loadUi

from diffunews_cli import creation


class EcranAide(QDialog):
    """Affichage ecran Aide"""
    def __init__(self):
        super().__init__()
#        super(EcranAide,self).__init__()
        #loadUi("UI/BQimport_unimarc_aide.ui",self)
        bundle_dir = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
        loadUi(bundle_dir / 'UI/diffunews_aide.ui', self)

class MainWindow(QDialog):
    """ Fenêtre principale. """
    def __init__(self):
        super().__init__()
        #super(MainWindow, self).__init__()
############################################
        # loadUi(bundle_dir / 'BQimport_unimarc.ui', self) # ligne orignale
        # pour faire un pyinstaller --onifile
        # This checks whether the sys._MEIPASS attribute exists
        # (i.e. are we running the bundled executable?),
        # if not, we fall back to the location of the script.
        bundle_dir = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
############################################
        loadUi(bundle_dir / 'UI/diffunews.ui', self)
        global sourcefile
        global location
        global originality
        global targetaudience
        location = ""
        originality = ""
        targetaudience = ""

      # les boutons de l'interface
        self.bouton_action.clicked.connect(self.action)
        self.bouton_aide.clicked.connect(self.aide)
        self.bouton_browse_destination_file.clicked.connect(self.browsedestinationfile)
        sourcefile = self.bouton_browse_source_file.clicked.connect(self.browsesourcefile)
        self.pushButton_creation_requete.clicked.connect(self.creationrequete)
        self.bouton_exit.clicked.connect(self.exitapp)
        location = self.comboBox_location.currentTextChanged.connect(self.majselectlocation)
        originality = self.comboBox_originality.currentTextChanged.connect(self.majselectoriginality)
        targetaudience = self.comboBox_targetaudience.currentTextChanged.connect(self.majselecttargetaudience)

    def aide(self):
        """fonction qui affiche un écran d'aide."""
        EcranAide()
        self.ecranaide = EcranAide()
        self.ecranaide.show()
        print(self.tr("aide"))


    def browsedestinationfile(self):
        """fonction du sélecteur du fichier de destination."""
        """
        2023-10-10 : deactiver pour rapidider de test
        extensiondestinationfile = "pdf" # précise l'extension des fichiers du sélecteur.
        destinationfile_complet = QFileDialog.getSaveFileName(self, \
                                  self.tr("Sauver un fichier en format : ") + extensiondestinationfile,\
                                  QDir.homePath(), "*." + extensiondestinationfile)
        destinationfile = destinationfile_complet[0]
        """

        self.lineEdit_fichier_destination.setText(destinationfile)
        print(self.tr("le fichier de destination est : ") + destinationfile)


    def browsesourcefile(self):
        """fonction du sélecteur du fichier source."""
        extensionsourcefile = "sqlite" # précise l'extension des fichiers du sélecteur.

        try:
            sourcefile_complet = QFileDialog.getOpenFileName(self,\
                                                            self.tr("Selectionner un fichier"),\
                                                            QDir.homePath(), "*." + extensionsourcefile)
            global sourcefile
            sourcefile = sourcefile_complet[0]
            self.lineEdit_fichier_source.setText(sourcefile)
            # 2023-10-10 : mise en place pour test et rapiditer
            global destinationfile

            destinationfile = QDir.homePath()
            self.lineEdit_fichier_destination.setText(destinationfile)

            self.connexion(sourcefile)
        # gestion des erreurs
        except (RuntimeError,TypeError, ValueError, NameError):
            pass


    @pyqtSlot(str)
    def connexion(self, sourcefile):
        """Connexion a la base pour récuperer les informations."""
        global cur
        fname = str(sourcefile)
        print(f"fonction connexion 1 : fichier fname = {fname}")
        con = sqlite3.connect(fname)
        cur = con.cursor()
        requestnbre = "SELECT count(myoid) FROM book"
        cur.execute(requestnbre)
        nbretotalbook = cur.fetchone()[0]
        nbretotalbookstr = str(nbretotalbook)
        self.lineEdit_nbretotal.setText(nbretotalbookstr)

        request = "SELECT location FROM locations ORDER BY location"
        cur.execute(request)
        listes = cur.fetchall()
        self.comboBox_location.clear()
        for liste in listes:
            # remarque : liste = tupple
            self.comboBox_location.addItems(liste)
            self.comboBox_location.activated[str]
            # si l'index change'


        request = "SELECT * FROM book_originality ORDER BY originality"
        cur.execute(request)
        listes = cur.fetchall()
        self.comboBox_originality.clear()
        for liste in listes:
            self.comboBox_originality.addItems(liste)
            self.comboBox_originality.activated[str]

        request = "SELECT * FROM book_target_audiences ORDER BY target_audience"
        cur.execute(request)
        self.comboBox_targetaudience.clear()
        listes = cur.fetchall()
        for liste in listes:
            self.comboBox_targetaudience.addItems(liste)
            self.comboBox_targetaudience.activated[str]
        cur.close

    def creationrequete(self):
        location = self.comboBox_location.currentText()
        originality = self.comboBox_originality.currentText()
        targetaudience = self.comboBox_targetaudience.currentText()
        requestSQL = "SELECT title,author,publisher,lccontrolnumber,isbn13,callnumber,description,front_cover FROM book WHERE location = "
        requestSQL2 = requestSQL + '"' + location  + '" AND originality = "'
        requestSQL3 = requestSQL2 + originality + '"'
        requestSQL4 = requestSQL3 + " INTERSECT " + "SELECT title,author,publisher,lccontrolnumber,isbn13,callnumber,description,front_cover FROM book WHERE target_audience = " + '"' + targetaudience + '";'
        self.lineEdit_requete_sql.setText(requestSQL4)


    def exitapp(self):
        """fonction pour quitter l'application."""
        print(self.tr("merci d'avoir utiliser l'application"))
        app.quit()

    def action(self):
        """fonction qui lance l'action."""
        print(self.tr("Action"))
        sourcefile = str(self.lineEdit_fichier_source.text())
        destinationfile = str(self.lineEdit_fichier_destination.text())
        sqllocation = self.comboBox_location.currentText()
        sqloriginality = self.comboBox_originality.currentText()
        sqltargetaudience = self.comboBox_targetaudience.currentText()

        sql = str(self.lineEdit_requete_sql.text())
        titre = str(self.lineEdit_titre.text())
        print("lancement de diffunews_cli")
#        creation(sourcefile,destinationfile,sql,titre)
        creation(sourcefile, destinationfile, sqllocation, sqloriginality, sqltargetaudience, titre)


    def majselectlocation(self, s):
        global datalocation
        datalocation = s
        cur.execute("SELECT count(myoid) FROM book WHERE location = ? ", (datalocation,))
        nbretotalbook = cur.fetchone()[0]
        nbretotalbookstr = str(nbretotalbook)
        self.lineEdit_nbretotal_filtre_location.setText(str(nbretotalbook))
        return datalocation

    def majselectoriginality(self, s):
        global dataoriginality
        dataoriginality = s
        cur.execute("SELECT count(myoid) FROM book WHERE location = ? AND originality = ?", (datalocation, dataoriginality,))
        nbretotalbook = cur.fetchone()[0]
        nbretotalbookstr = str(nbretotalbook)
        self.lineEdit_nbretotal_filtre_originality.setText(str(nbretotalbook))
        return dataoriginality

    def majselecttargetaudience(self, s):
        global datatargetaudience
        datatargetaudience = s
        print("datalocation = " + datalocation)
        print("dataoriginality = " + dataoriginality)
        cur.execute("SELECT count(myoid) FROM book WHERE target_audience = ?", (datatargetaudience,))
#        cur.execute("SELECT count(title) FROM (SELECT title FROM book WHERE location = ? AND originality = ? INTERSECT SELECT title FROM book WHERE target_audience = ?", (datalocation, dataoriginality,datatargetaudience,))
#        cur.execute("SELECT count(myoid) FROM book WHERE target_audience = ? INTERSECT SELECT count(myoid) FROM book WHERE location = ? AND originality = ?", (datatargetaudience,datalocation, dataoriginality,))
        nbretotalbook = cur.fetchone()[0]
        nbretotalbookstr = str(nbretotalbook)
        self.lineEdit_nbretotal_filtre_targetaudience.setText(str(nbretotalbook))
        return datatargetaudience




app = QApplication(sys.argv)

## Debut TRADUCTIONapp = QApplication
locale = QLocale()
translators = []
for prefixeQm in ("Translations/monapplication_", "Translations/qt_", "Translations/qtbase_"):
    translator = QTranslator()
    translators.append(translator)
    translator.load(locale,prefixeQm)
    app.installTranslator(translator)
# Fin TRADUCTION

mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setWindowTitle("Diffunews")
widget.setFixedWidth(870)
widget.setFixedHeight(800)
widget.show()
rc = app.exec_()
sys.exit(rc)
