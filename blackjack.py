import os
import time 
import random
import cards

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# Temps/Délais d'affichage
MSG_DURATION=1		# Temps d'affichage des messages
CARD_DELAY=1		# Délai entre l'affichage des cartes

# Splash
def splash():
    print()
    print("  ██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗")
    print("  ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝")
    print("  ██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝ ")
    print("  ██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗ ")
    print("  ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗ █████╔╝██║  ██║╚██████╗██║  ██╗")
    print("  ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝")
    print("  by SK                                                              v3.1c")

# Jeu de cartes
def new_jeu(n):
	global jeu
	spades='♠'
	hearts='♥'
	clubs='♣'
	diamonds='♦'
	jeu=[['A',spades],[2,spades],[3,spades],[4,spades],[5,spades],[6,spades],[7,spades],[8,spades],[9,spades],[10,spades],['J',spades],['Q',spades],['K',spades],['A',hearts],[2,hearts],[3,hearts],[4,hearts],[5,hearts],[6,hearts],[7,hearts],[8,hearts],[9,hearts],[10,hearts],['J',hearts],['Q',hearts],['K',hearts],['A',clubs],[2,clubs],[3,clubs],[4,clubs],[5,clubs],[6,clubs],[7,clubs],[8,clubs],[9,clubs],[10,clubs],['J',clubs],['Q',clubs],['K',clubs],['A',diamonds],[2,diamonds],[3,diamonds],[4,diamonds],[5,diamonds],[6,diamonds],[7,diamonds],[8,diamonds],[9,diamonds],[10,diamonds],['J',diamonds],['Q',diamonds],['K',diamonds]]
	if n==1:
		print("Jeu épuisé. Ouverture d'un nouveau jeu.")
		time.sleep(MSG_DURATION)

# Tirage carte
def tirage_carte(player):
	global jeu
	global cartes_joueur
	global cartes_banquier
	
	if len(jeu)==0:	# Vérifie que le jeu n'est pas épuisé, si oui, nouveau jeu
		new_jeu(1)
	tirage=random.choice(jeu)	# Choisit une carte de manière aléatoire dans le jeu
	jeu.remove(tirage)			# puis la supprime du jeu

	if player=="joueur":
		cartes_joueur.append(tirage)

	if player=="banquier":
		cartes_banquier.append(tirage)

# Compte les points du joueur
def comptage_joueur():
	global val_joueur
	val_cartes=0

	for i in range(0,len(cartes_joueur)):	# Comptage des points
		if cartes_joueur[i][0]=='A':															# As
			A=0
			if checkifsup21()==True:
				val_cartes+=1
			else:
				while A!=1 and A!=11:
					try:
						A=(int(input("Choisissez la valeur de "+str(cartes_joueur[i])+" (1 ou 11): ")))
					except ValueError:
						print("Saisie invalide.", end=' ')
					if A==1:
						val_cartes+=1
					elif A==11:
						val_cartes+=11
					else:
						print("Veuillez entrer soit la valeur 1 ou soit la valeur 11.")
						time.sleep(MSG_DURATION)
		elif cartes_joueur[i][0]=='K' or cartes_joueur[i][0]=='Q' or cartes_joueur[i][0]=='J':	# Figures
			val_cartes+=10
		else:																					# Autres cartes
			val_cartes+=cartes_joueur[i][0]

	val_joueur=val_cartes

# Vérifie que la valeur totale minimale des cartes du joueur ne dépasse pas 21pts
def checkifsup21():
	val_cartes=0

	for i in range(0,len(cartes_joueur)):	# Compte tous les points normalement avec A toujours égal à 1
		if cartes_joueur[i][0]=='A':
			val_cartes+=1
		elif cartes_joueur[i][0]=="K" or cartes_joueur[i][0]=="Q" or cartes_joueur[i][0]=="J":
			val_cartes+=10
		else:		
			val_cartes+=cartes_joueur[i][0]
	
	if val_cartes>21:
		return True
	else:
		return False

# Tirage d'une carte supplémentaire
def cartesupp():
	global fin_tour_joueur
	while checkifsup21()==False:	# Tant que le jeu du joueur ne dépasse pas 21
		ask=' '
		while ask!='o' and ask!='n' and ask!='':
			ask=input("Souhaitez-vous tirer une nouvelle carte ? [o] (o/n) ")
		if ask=='o' or ask=='':
			if len(jeu)==0:	# Si le jeu est épuisé,
				new_jeu(1)	# nouveau jeu.
			tirage_carte("joueur")
			time.sleep(CARD_DELAY)
			cards.afficher_cartes_joueur(cartes_joueur,cartes_banquier,"dir",val_joueur,fin_tour_joueur)
		elif ask=='n':
			break
		else:
			print("Erreur cartesupp()")
	fin_tour_joueur=1

	if checkifsup21()==True:	# Si jeu du joueur dépasse 21, affiche message et passe au tour du banquier
		print("La valeur totale minimale de vos cartes dépassent 21 points.\nVous ne pouvez plus tirer de carte supplémentaire.")
		time.sleep(MSG_DURATION)
		print("C'est au tour du banquier.")
		time.sleep(MSG_DURATION)

# Compte les points du banquier
def comptage_banquier():
	global val_banquier
	val_cartes=0
	nb_A=0

# Comptage des points
	for i in range(0,len(cartes_banquier)):
		if cartes_banquier[i][0]=='A':																	# Compte le nombre d'as
			nb_A+=1
		elif cartes_banquier[i][0]=='K' or cartes_banquier[i][0]=='Q' or cartes_banquier[i][0]=='J':	# Figures
			val_cartes+=10
		else:																							# Autres cartes
			val_cartes+=cartes_banquier[i][0]

# Gestion du comptage des as
	if nb_A>0:							# S'il y a un ou plusieurs as,
		if val_cartes+11+(nb_A-1)<=21:	# et si un as vaut 11 et les éventuels autres valent 1,
			val_cartes+=11+(nb_A-1)		# on ajoute 11 plus le nombre d'as restants à la valeur du jeu.
		else:							#
			val_cartes+=nb_A			# Sinon tous les as valent 1

	val_banquier=val_cartes

# Tour du banquier
def tour_banquier():
	if checkifsup21()==False:
		print("C'est au tour du banquier.")
	time.sleep(MSG_DURATION)
	while True:
		comptage_banquier()			# Comptage des points du banquier
		if checkifsup21()==True:	# Si le joueur a dépassé 21pts,
			break					# le banquier ne tire pas de carte supplémentaire.

		elif checkifsup21()==False and val_banquier<17:							# Si val_joueur<=21 et val_banquier<17
			if len(jeu)==0:	# (On vérifie s'il reste des cartes dans le jeu,	#
				new_jeu(1)	# sinon on utilise un nouveau jeu.)					#
			tirage_carte("banquier")											# le banquier tire une carte.				
			comptage_banquier()
		else:
			break
	fin_tour_banquier=1

# Affiche le score
def score():
	global pts_joueur
	global pts_banquier
	# Affichage message victoire/défaite
	if (val_joueur>val_banquier and val_joueur<=21) or (val_joueur<val_banquier and val_banquier>21):
		print("Bravo ! Vous avez gagné ! :)")
		pts_joueur+=1
	else:
		print("Vous avez perdu ! :(")
		pts_banquier+=1

	# Affichage score
	print("Le score est de "+str(pts_joueur)+" - "+str(pts_banquier)+".")
	#print("Nb cartes restantes: "+str(len(jeu)))	# Affiche le nombre de cartes restantes dans le jeu
	time.sleep(MSG_DURATION)

# Demande si l'utilisateur veut rejouer
def replay():
	global play
	replay=' '
	while replay!='o' and replay!='n' and replay!='':
		replay=input("Souhaitez-vous faire une autre partie ? [o] (o/n) ")
	if replay=='o' or replay=='':
		print("Une nouvelle partie va commencer...")
		time.sleep(MSG_DURATION)
	elif replay=='n':
		play=0
		print("À bientôt !")
		time.sleep(MSG_DURATION)



## MAIN ##

clear()
splash()
print("\nBienvenue dans le jeu du Blackjack !")
time.sleep(MSG_DURATION)

game=' '
while game!='o' and game!='n' and game!='':
	game=input("Souhaitez-vous faire une partie ? [o] (o/n) ")
if game=='o' or game=='':
	print("Votre partie va commencer...")
	time.sleep(MSG_DURATION)
	clear()

	jeu=0
	new_jeu(0)

	pts_joueur=0
	pts_banquier=0

	play=1
	# Début de la boucle du jeu #
	while play==1:

		cartes_joueur=[]
		cartes_banquier=[]

		fin_tour_joueur=0
		fin_tour_banquier=0

		val_joueur=0
		val_banquier=0

		# Distribution ♠ ♥ ♣ ♦
		tirage_carte("joueur")
		cards.afficher_cartes_joueur(cartes_joueur,cartes_banquier,"prg",val_joueur,0)

		tirage_carte("banquier")
		cards.afficher_cartes_banquier(cartes_banquier,cartes_joueur,"dir",0,val_banquier,0,0,1)

		tirage_carte("joueur")
		cards.afficher_cartes_joueur(cartes_joueur,cartes_banquier,"prg",val_joueur,0)

		tirage_carte("banquier")
		cards.afficher_cartes_banquier(cartes_banquier,cartes_joueur,"dir",0,val_banquier,0,0,1)


		# On demande si le joueur veut tirer une autre carte, on compte ses points puis on affiche ses cartes.
		cartesupp()
		comptage_joueur()
		cards.afficher_cartes_joueur(cartes_joueur,cartes_banquier,"dir",val_joueur,1)

		# Tour du banquier
		tour_banquier()

		cards.afficher_cartes_banquier(cartes_banquier,cartes_joueur,"prg",val_joueur,val_banquier,fin_tour_joueur,0,1) # Affiche cartes banquier
		print("Le banquier a fini son tour.")
		time.sleep(CARD_DELAY)
		print("Il retourne sa carte masquée...")
		time.sleep(CARD_DELAY)
		cards.afficher_cartes_banquier(cartes_banquier,cartes_joueur,"dir",val_joueur,val_banquier,fin_tour_joueur,0,0) # Réaffichage avec carte 																															 masquée visible
		time.sleep(CARD_DELAY)

		cards.afficher_cartes_banquier(cartes_banquier,cartes_joueur,"dir",val_joueur,val_banquier,fin_tour_joueur,1,0) # Réaffichage avec valeur
		time.sleep(CARD_DELAY) 

		# Fin du jeu. Affiche le score puis demande si replay.
		score()
		replay()

	# Fin de la boucle du jeu #
	
else:
	print("À bientôt !")
	time.sleep(MSG_DURATION)
