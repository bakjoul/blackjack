import os
import time

## DEBUG
"""
# Permet l'affichage des symboles sur Windows
if os.name=="nt":
	import sys
	from io import TextIOWrapper
	
	os.system('set "PYTHONIOENCODING=UTF-8"')
	os.system('chcp 65001')
	
	sys.stdout = TextIOWrapper(sys.stdout.buffer, encoding='UTF-8', errors='replace')
"""

MSG_DURATION=1		# Temps d'affichage des messages
CARD_DELAY=1		# Délai entre l'affichage des cartes

# clear
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# Appelle la bonne carte à dessiner
def which_card(liste,i):
	if liste[i][0]=='A':
		ace(liste[i][1])
	elif liste[i][0]=='K' or liste[i][0]=='Q' or liste[i][0]=='J':
		fig(liste[i][0],liste[i][1])
	elif liste[i][0]==10:
		ten(liste[i][1])
	elif liste[i][0]==9:
		nine(liste[i][1])
	elif liste[i][0]==8:
		eight(liste[i][1])
	elif liste[i][0]==7:
		seven(liste[i][1])
	elif liste[i][0]==6:
		six(liste[i][1])
	elif liste[i][0]==5:
		five(liste[i][1])
	elif liste[i][0]==4:
		four(liste[i][1])
	elif liste[i][0]==3:
		three(liste[i][1])
	elif liste[i][0]==2:
		two(liste[i][1])
	else:
		print("which_card: carte invalide")

# Fonction générique d'affichage en ligne d'une liste de cartes
def afficher_cartes(liste,hide):
	line=[0]*9						# Initialisation de la liste 
	for i in range(0,len(line)):	# dans laquelle on va écrire 
		line[i]=[]					# les lignes des cartes à afficher.

	for i in range(0,len(liste)):	# Parcourt la liste des cartes
		which_card(liste,i)			# et détermine il s'agit de quelle carte.

		if i==1 and hide==1:		# Si 2ème carte du banquier,
			hidden()				# on la masque.
						
		for j in range(0,9):		# Ajoute ligne à ligne le dessin des cartes
			line[j].append(card[j]) # à la liste initialisée en début de fonction.

	for i in range(0,9):			# Affiche la liste
		print(' '.join(line[i]))
	print()

# Affiche les cartes du joueurs suivi du réaffichage des cartes initiales du banquier
	# liste: cartes du joueur; liste2: cartes du banquier; mode: progressif(prg) ou direct(dir);
	# vj: valeur des cartes du joueur; fin_tour_joueur: var booléenne indiquant si le joueur a fini son tour.
def afficher_cartes_joueur(liste,liste2,mode,vj,fin_tour_joueur):
	line=[0]*9
	for i in range(0,len(line)):
		line[i]=[]

	for i in range(0,len(liste)):
		which_card(liste,i)
						
		for j in range(0,9):
			line[j].append(card[j])

		# Affichage progressif avec un délai entre l'affichage des cartes
		if mode=="prg":
			clear()
			print("Vos cartes:")
			for k in range(0,9):		
				print(' '.join(line[k]))
			print()
			print("Cartes du banquier:")
			afficher_cartes(liste2,1)
			time.sleep(CARD_DELAY)

	# Affichage direct de toutes les cartes
	if mode=="dir":
		clear()
		print("Vos cartes:", end=' ')
		if fin_tour_joueur==1:				# Si le joueur a fini son tour,
			print("("+str(vj)+")")			# affiche la valeur de ses cartes.
		else:
			print()

		for i in range(0,9):		
			print(' '.join(line[i]))
		print()
		print("Cartes du banquier:")
		afficher_cartes(liste2,1)

# Affiche les cartes du banquier en réaffichant au préalable les cartes du joueur
	# liste: cartes du banquier; liste2: cartes du joueur; mode: progressif(prg) ou direct(dir); vj: valeur des cartes du joueur;
	# vb: valeur des cartes du banquier; fin_tour_joueur: booléen indiquant fin du tour joueur; fin_tour_banquier: booléen indiquant fin tour banquier;
	# hide: booléen qui masque la carte du banquier
def afficher_cartes_banquier(liste,liste2,mode,vj,vb,fin_tour_joueur,fin_tour_banquier,hide):
	line=[0]*9
	for i in range(0,len(line)):
		line[i]=[]

	for i in range(0,len(liste)):
		which_card(liste,i)

		if i==1 and hide==1:	# Si 2ème carte du banquier,
			hidden()			# on la masque.
			
		for j in range(0,9):
			line[j].append(card[j])

		# Affichage progressif des cartes du banquier
		if mode=="prg":
			clear()
			print("Vos cartes:", end=' ')
			if fin_tour_joueur==1:
				print("("+str(vj)+")")
			else:
				print()
			afficher_cartes(liste2,0)
			print("Cartes du banquier:")
			
			for k in range(0,9):		
				print(' '.join(line[k]))
			print()
			if i>=2: # L'affichage progressif ne commence qu'à partir de la 3ème carte
				time.sleep(CARD_DELAY)

	# Affichage direct de toutes les cartes des joueurs avec leur valeur
	if mode=="dir":
		clear()
		print("Vos cartes:", end=' ')
		if fin_tour_joueur==1:
			print("("+str(vj)+")")
		else:
			print()
		afficher_cartes(liste2,0)
		print("Cartes du banquier:", end=' ')
		if fin_tour_banquier==1:
			print("("+str(vb)+")")
		else:
			print()
		for k in range(0,9):		
			print(' '.join(line[k]))
		print()


## DESSINS DES CARTES ##

# Symboles
spades='♠'
hearts='♥'
clubs='♣'
diamonds='♦'

# Couleurs
red="\033[1;31;47m"
black="\033[1;30;47m"
white="\033[1;37;47m"
end="\033[0m"

# Lignes communes
top=black+"┌─────────┐"+end
empty=black+"|         |"+end
bottom=black+"└─────────┘"+end
def lowtop(x,c):
	if c=='r':
		return black+"|"+red+str(x)+"        "+black+"|"+end
	if c=='b':
		return black+"|"+str(x)+"        |"+end
def hibot(x,c):
	if c=='r':
		return black+"|"+red+"        "+str(x)+black+"|"+end
	if c=='b':
		return black+"|        "+str(x)+"|"+end

# As
def ace(s):
	global card
	x=s
	if s==spades or s==clubs:
		c='b'
		bc=black
	if s==hearts or s==diamonds:
		c='r'
		bc=red
	card=[0]*9

	card[0]=top
	card[1]=lowtop('A',c)
	card[2]=black+"|"+bc+str(x)+"        "+black+"|"+end
	card[3]=empty
	card[4]=black+"|"+bc+"    "+str(x)+"    "+black+"|"+end
	card[5]=empty
	card[6]=black+"|"+bc+"        "+str(x)+black+"|"+end
	card[7]=hibot('A',c)
	card[8]=bottom

# Figures
def fig(r,s):
	global card
	x=s
	if s==spades or s==clubs:
		bc=black
	if s==hearts or s==diamonds:
		bc=red
	mid=black+"| |     | |"+end
	card=[0]*9

	card[0]=top
	card[1]=black+"|"+bc+str(r)+black+"┌─────┐ |"+end
	card[2]=black+"|"+bc+str(x)+black+"|"+bc+str(x)+black+"    | |"+end
	card[3]=mid
	card[4]=mid
	card[5]=mid
	card[6]=black+"| |    "+bc+str(x)+black+"|"+bc+str(x)+black+"|"+end
	card[7]=black+"| └─────┘"+bc+str(r)+black+"|"+end
	card[8]=bottom

# Autres cartes de 10 à 2
def ten(s):
	global card
	x=s
	if s==spades or s==clubs:
		bc=black
	if s==hearts or s==diamonds:
		bc=red
	card=[0]*9

	card[0]=top
	card[1]=black+"|"+bc+"10"+str(x)+"   "+str(x)+black+"  |"+end
	card[2]=black+"|"+bc+str(x)+"   "+str(x)+black+"    |"+end
	card[3]=black+"|  "+bc+str(x)+"   "+str(x)+black+"  |"+end
	card[4]=black+"|  "+bc+str(x)+"   "+str(x)+black+"  |"+end
	card[5]=black+"|    "+bc+str(x)+black+"    |"+end
	card[6]=black+"|  "+bc+str(x)+"   "+str(x)+" "+str(x)+black+"|"+end
	card[7]=black+"|       "+bc+"10"+black+"|"+end
	card[8]=bottom

def nine(s):
	global card
	x=s
	if s==spades or s==clubs:
		c='b'
		bc=black
	if s==hearts or s==diamonds:
		c='r'
		bc=red
	card=[0]*9

	card[0]=top
	card[1]=lowtop(9,c)
	card[2]=black+"|"+bc+str(x)+" "+str(x)+"   "+str(x)+"  "+black+"|"+end
	card[3]=black+"|  "+bc+str(x)+"   "+str(x)+black+"  |"+end
	card[4]=black+"|    "+bc+str(x)+black+"    |"+end
	card[5]=black+"|  "+bc+str(x)+"   "+str(x)+black+"  |"+end
	card[6]=black+"|  "+bc+str(x)+"   "+str(x)+black+"  |"+end
	card[7]=hibot(9,c)
	card[8]=bottom

def eight(s):
	global card
	x=s
	if s==spades or s==clubs:
		c='b'
		bc=black
	if s==hearts or s==diamonds:
		c='r'
		bc=red
	card=[0]*9

	card[0]=top
	card[1]=lowtop(8,c)
	card[2]=black+"|"+bc+str(x)+" "+str(x)+"   "+str(x)+black+"  |"+end
	card[3]=black+"|    "+bc+str(x)+black+"    |"+end
	card[4]=black+"|  "+bc+str(x)+"   "+str(x)+black+"  |"+end
	card[5]=black+"|    "+bc+str(x)+black+"    |"+end
	card[6]=black+"|  "+bc+str(x)+"   "+str(x)+" "+str(x)+black+"|"+end
	card[7]=hibot(8,c)
	card[8]=bottom

def seven(s):
	global card
	x=s
	if s==spades or s==clubs:
		c='b'
		bc=black
	if s==hearts or s==diamonds:
		c='r'
		bc=red
	card=[0]*9

	card[0]=top
	card[1]=lowtop(7,c)
	card[2]=black+"|"+bc+str(x)+" "+str(x)+"   "+str(x)+black+"  |"+end
	card[3]=black+"|    "+bc+str(x)+black+"    |"+end
	card[4]=black+"|  "+bc+str(x)+"   "+str(x)+black+"  |"+end
	card[5]=empty
	card[6]=black+"|  "+bc+str(x)+"   "+str(x)+" "+str(x)+black+"|"+end
	card[7]=hibot(7,c)
	card[8]=bottom

def six(s):
	global card
	x=s
	if s==spades or s==clubs:
		c='b'
		bc=black
	if s==hearts or s==diamonds:
		c='r'
		bc=red
	card=[0]*9

	card[0]=top
	card[1]=lowtop(6,c)
	card[2]=black+"|"+bc+str(x)+" "+str(x)+"   "+str(x)+black+"  |"+end
	card[3]=empty
	card[4]=black+"|  "+bc+str(x)+"   "+str(x)+black+"  |"+end
	card[5]=empty
	card[6]=black+"|  "+bc+str(x)+"   "+str(x)+" "+str(x)+black+"|"+end
	card[7]=hibot(6,c)
	card[8]=bottom

def five(s):
	global card
	x=s
	if s==spades or s==clubs:
		c='b'
		bc=black
	if s==hearts or s==diamonds:
		c='r'
		bc=red
	card=[0]*9

	card[0]=top
	card[1]=lowtop(5,c)
	card[2]=black+"|"+bc+str(x)+" "+str(x)+"   "+str(x)+black+"  |"+end
	card[3]=empty
	card[4]=black+"|    "+bc+str(x)+black+"    |"+end
	card[5]=empty
	card[6]=black+"|  "+bc+str(x)+"   "+str(x)+" "+str(x)+black+"|"+end
	card[7]=hibot(5,c)
	card[8]=bottom

def four(s):
	global card
	x=s
	if s==spades or s==clubs:
		c='b'
		bc=black
	if s==hearts or s==diamonds:
		c='r'
		bc=red
	card=[0]*9

	card[0]=top
	card[1]=lowtop(4,c)
	card[2]=black+"|"+bc+str(x)+" "+str(x)+"   "+str(x)+black+"  |"+end
	card[3]=empty
	card[4]=empty
	card[5]=empty
	card[6]=black+"|  "+bc+str(x)+"   "+str(x)+" "+str(x)+black+"|"+end
	card[7]=hibot(4,c)
	card[8]=bottom

def three(s):
	global card
	x=s
	if s==spades or s==clubs:
		c='b'
		bc=black
	if s==hearts or s==diamonds:
		c='r'
		bc=red
	card=[0]*9

	card[0]=top
	card[1]=lowtop(3,c)
	card[2]=black+"|"+bc+str(x)+"   "+str(x)+black+"    |"+end
	card[3]=empty
	card[4]=black+"|    "+bc+str(x)+black+"    |"+end
	card[5]=empty
	card[6]=black+"|    "+bc+str(x)+"   "+str(x)+black+"|"+end
	card[7]=hibot(3,c)
	card[8]=bottom

def two(s):
	global card
	x=s
	if s==spades or s==clubs:
		c='b'
		bc=black
	if s==hearts or s==diamonds:
		c='r'
		bc=red
	card=[0]*9

	card[0]=top
	card[1]=lowtop(2,c)
	card[2]=black+"|"+bc+str(x)+"   "+str(x)+black+"    |"+end
	card[3]=empty
	card[4]=empty
	card[5]=empty
	card[6]=black+"|    "+bc+str(x)+"   "+str(x)+black+"|"+end
	card[7]=hibot(2,c)
	card[8]=bottom

def hidden():
	global card
	card=[0]*9
	hidden=black+"|░░░░░░░░░|"+end
	
	card[0]=top
	card[1]=hidden
	card[2]=hidden
	card[3]=hidden
	card[4]=hidden
	card[5]=hidden
	card[6]=hidden
	card[7]=hidden
	card[8]=bottom
	
# TESTS # ♠ ♥ ♣ ♦
"""
acee=[['A',spades],['A',hearts],['A',clubs],['A',diamonds]]
king=[['K',spades],['K',hearts],['K',clubs],['K',diamonds]]
queen=[['Q',spades],['Q',hearts],['Q',clubs],['Q',diamonds]]
jack=[['J',spades],['J',hearts],['J',clubs],['J',diamonds]]
dix=[[10,spades],[10,hearts],[10,clubs],[10,diamonds]]
neuf=[[9,spades],[9,hearts],[9,clubs],[9,diamonds]]
huit=[[8,spades],[8,hearts],[8,clubs],[8,diamonds]]
sept=[[7,spades],[7,hearts],[7,clubs],[7,diamonds]]
sixx=[[6,spades],[6,hearts],[6,clubs],[6,diamonds]]
cinq=[[5,spades],[5,hearts],[5,clubs],[5,diamonds]]
quatre=[[4,spades],[4,hearts],[4,clubs],[4,diamonds]]
trois=[[3,spades],[3,hearts],[3,clubs],[3,diamonds]]
deux=[[2,spades],[2,hearts],[2,clubs],[2,diamonds]]

afficher_cartes(acee,0)
afficher_cartes(king,0)
afficher_cartes(queen,0)
afficher_cartes(jack,0)
afficher_cartes(dix,0)
afficher_cartes(neuf,0)
afficher_cartes(huit,0)
afficher_cartes(sept,0)
afficher_cartes(sixx,0)
afficher_cartes(cinq,0)
afficher_cartes(quatre,0)
afficher_cartes(trois,0)
afficher_cartes(deux,0)
"""
