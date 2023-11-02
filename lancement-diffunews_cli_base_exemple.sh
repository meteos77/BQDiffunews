#!/usr/bin/bash
echo "Création des fichiers .pdf"
./diffunews_cli.py Exemples/exemple.sqlite "./Exemples" "R-Romans" "DON-2023" "Adultes" "DONS 2023 : Romans"
echo "Création du fichier.pdf de la newletter"
./diffunews_creation_newletter.py
