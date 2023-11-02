from fpdf import FPDF

def creationPDF(titre1,auteur1,editeur1,description1,isbn1,cote1,resume1,image1,\
				        titre2,auteur2,editeur2,description2,isbn2,cote2,resume2,image2,\
                page,emplacement,page2,title,destinationpath):

# CREATION DU PDF
	pdf = FPDF()
	#pdf.set_font('helvetica', '', 13.0)
	pdf.add_font('noto', '', r"/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf")
	pdf.add_font('notoB', '', r"/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf")
	pdf.add_font('DejaVu', '', r"/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
	pdf.set_font('DejaVu', '', 13.0)

	pdf.add_page()
	pdf.set_font("notoB", size=12)
	pdf.set_right_margin(30)

	#### TITRE DES PAGES : ROMANS
	pdf.set_xy(0, 20)
	pdf.cell(align='C', w=210, txt=title, border=0)

	# Ligne de séparation
	pdf.set_line_width(0.0)
	pdf.line(20.0, 30.0, 190.0, 30.0)

#### PARTIE HAUTE
	# les Variables
	X=20 # position X
	Y=45 # position Y
	Z=5 # entre ligne
	W=0 # Si ligne de titre est sur 2 ligne

	#### IMAGE
	pdf.set_line_width(0.0)
#	pdf.rect(X+120.0, Y, 50.0, 90.0)
	pdf.image(image1, X+120, Y, link='', type='', w=50.0, h=80.0)
	#### TITRE : si le titre a plus de 47 caractères le mettre sur 2 lignes
	Titre1 = (titre1.upper())
	longueurTitre1 = len(Titre1)
	if longueurTitre1 > 47:
		W=14
	else:
		W=0
	pdf.set_right_margin(75)
	pdf.set_font("notoB", size=12)
	pdf.set_xy(X, Y)
	pdf.multi_cell(0 , 5, txt=Titre1)
	pdf.set_font("noto", size=10)

	#### Auteur
	pdf.set_xy(X, Y+W+Z)
	pdf.cell(align='L', w=10, txt="Auteur : ")
	pdf.set_xy(X+15, Y+W+Z)
	pdf.cell(align='L', w=98.0, txt=auteur1, border=0)

	##### Editeur
	pdf.set_xy(X, Y+W+Z*2)
	pdf.cell(txt='Editeur : ', border=0)

	##### Editeur : valeur
	pdf.set_xy(X+15, Y+W+Z*2)
	pdf.cell(txt=editeur1, border=0)

	##### Description
	pdf.set_xy(X, Y+W+Z*3)
	pdf.cell(txt='Description : ', border=0)

	##### Description : valeur
	if description1 != "N/A":
		pdf.set_xy(X+22.0, Y+W+Z*3)
		pdf.cell(txt=description1, border=0)
	else:
		pass

	##### ISBN
	pdf.set_xy(X, Y+W+Z*4)
	pdf.cell(txt='ISBN : ', border=0)

	#### ISBN : Valeur
	pdf.set_xy(X+11, Y+W+Z*4)
	pdf.cell(txt=isbn1, border=0)

	##### COTE
	pdf.set_xy(X, Y+W+Z*5)
	pdf.cell(txt='COTE : ', border=0)

	##### COTE : valeur
	pdf.set_font("notoB", size=12)
	pdf.set_xy(X+12, Y+W+Z*5)
	pdf.cell(txt=cote1, border=0)
	pdf.set_font("noto", size=10)

	#### Résumé
	pdf.set_xy(X, Y+W+Z*6)
	# Output justified text
	#        self.multi_cell(0, 5, txt)
			# Line break
	#        self.ln()
	# Mention in italics
	#        self.set_font('', 'I')
	#        self.cell(0, 5, '(end of excerpt)')

	# A FAIRE
	# SI 13 Lignes alors la cellule devrait grandir pour occuper tous l'espace
	pdf.set_right_margin(75)
	longueurresume1 = len(resume1)
	print(longueurresume1)
	resume1 = resume1[0:850]
	pdf.multi_cell(0, 5, txt=resume1, border=0)


#### PARTIE BASSE ####
	# les Variables
	X=80 # position X
	Y=170 # position Y
	Z=5
	W=0

	#### IMAGE
	pdf.set_line_width(0.0)
#	pdf.rect(X-62, Y, 50.0, 90.0)
	pdf.image(image2, X-62, Y, link='', type='', w=50.0, h=80.0)

	#### TITRE : si le titre a plus de 47 caractères le mettre sur 2 lignes
	Titre2 = (titre2.upper())
	longueurTitre2 = len(Titre2)
	if longueurTitre2 > 47:
		W=14
	else:
		W=0
	if Titre2.replace("-","ccc"):
		pdf.set_right_margin(20)
		pdf.set_font("notoB", size=12)
		pdf.set_xy(X, Y)
		pdf.multi_cell(0 , 5, txt=Titre2)
		pdf.set_font("noto", size=10)


	#### Auteur
	pdf.set_xy(X, Y+W+Z)
	pdf.cell(txt="Auteur : ")
	pdf.set_xy(X+15, Y+W+Z)
	pdf.cell(txt=auteur2, border=0)

	##### Editeur
	pdf.set_xy(X, Y+W+Z*2)
	pdf.cell(txt='Editeur : ', border=0)

	##### Editeur : valeur
	pdf.set_xy(X+15, Y+W+Z*2)
	pdf.cell(txt=editeur2, border=0)

	##### Description
	pdf.set_xy(X, Y+W+Z*3)
	pdf.cell(txt='Description : ', border=0)

	##### Description : valeur
	if description2 != "N/A":
		pdf.set_xy(X+22.0, Y+W+Z*3)
		pdf.cell(txt=description2, border=0)

	##### ISBN
	pdf.set_xy(X, Y+W+Z*4)
	pdf.cell(txt='ISBN : ', border=0)

	#### ISBN : Valeur
	pdf.set_xy(X+11, Y+W+Z*4)
	pdf.cell(txt=isbn2, border=0)

	##### COTE
	pdf.set_xy(X, Y+W+Z*5)
	pdf.cell(txt='COTE : ', border=0)

	##### COTE : valeur
	pdf.set_font("notoB", size=12)
	pdf.set_xy(X+12, Y+W+Z*5)
	pdf.cell(txt=cote2, border=0)
	pdf.set_font("noto", size=10)

	#### Résumé
	#pdf.set_font('DejaVu', '', 14)
	#pdf.set_font('noto', '', 12)
	pdf.set_xy(X, Y+W+Z*6)
	# Output justified text
	#        self.multi_cell(0, 5, txt)
			# Line break
	#        self.ln()
	# Mention in italics
	#        self.set_font('', 'I')
	#        self.cell(0, 5, '(end of excerpt)')

	# A FAIRE
	# SI 780 char -> basculee de la marge gauche a 20
	# SI 13 Lignes alors la cellule devrait grandir pour occuper tous l'espace
	pdf.set_right_margin(20)
	pdf.set_left_margin(20)
	longueurresume2 = len(resume2)
	print(longueurresume2)
	resume2 = resume2[0:850]
	pdf.multi_cell(0, 5, txt=resume2, border=0)


	#### CREATION DU PDF
	pdf.set_title(title)
	page = 100+page
	m=str(page)
	print("le numero du fichier est : " + m)
	nomfichier = destinationpath + "/" + m + '.pdf'
	print("le nom du fichier est : " + nomfichier)
	pdf.output(nomfichier)
	numero=1
	return
