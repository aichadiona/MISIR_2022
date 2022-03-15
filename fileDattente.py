#not /usr/bin/python
# -*- coding: latin-1 -*-

from datetime import datetime

"""
	Classe representative des clients
"""
class Client:
	"""
		Constructeur publique d'un objet de la classe
	"""
	def __init__(self, number, arrival):
		self.number = number
		self.arrival = arrival
		self.nextClient = None
		self.previousClient = None
	
	"""
		M�thode publique pour r�cup�rer le num�ro de ticket du client
	"""
	def getNumber(self):
		return self.number
	
	"""
		Methode publique pour definir le numero de ticket du client
	"""
	def setNumber(self, number):
		self.number = number
	
	"""
		Methode publique pour recuperer l'heure d'arrivee du client
	"""
	def getArrival(self):
		return self.arrival
	
	"""
		Methode publique pour definir l'heure d'arrivee du client
	"""
	def setArrival(self, number):
		self.arrival = arrival
	
	"""
		Methode publique d'auto-insertion du client courant dans la file d'attente. La tete de file lui est transmise en parametre
	"""
	def insertIntoQueue(self, headOfTheQueue):
		# S'il n'y a personne en tete de file. Autrement dit la file est vide
		if(headOfTheQueue == None):
			return self # La cliente devient la tete de file. Et c'est termine.
		# Sinon, on cherche le dernier client ...
		currentClient = headOfTheQueue
		while(currentClient.nextClient != None):
			currentClient = currentClient.nextClient
		# ... et on se met derriere lui
		currentClient.nextClient = self
		self.previousClient = currentClient
		# On informe l'instance de la file d'attente de la tete de file retenue apres traitement
		return headOfTheQueue
	
	"""
		Methode publique d'affichage d'un client
	"""
	def show(self):
		# On recupere le numero du client courant
		text = "Ne " + str(self.number) + " (" + self.arrival + ")\n"
		# Et on demande e l'eventuel client qui suit dans la file d'attente de s'afficher
		if(self.nextClient != None):
			text += self.nextClient.show()
		return text
	
	def __str__(self):
		return "Ne " + str(self.number) + " (" + self.arrival + ")"

"""
	Classe representative des clientes en etat de grossesse
"""
class PregnantClient(Client):
	"""
		Classe representative des clientes en etat de grossess
	"""
	def __init__(self, number, arrival):
		Client.__init__(self, number, arrival)
	
	"""
		Redefinition de la methode publique d'auto-insertion de la cliente enceinte courant dans la file d'attente. La tete de file lui est transmise en parametre
	"""
	def insertIntoQueue(self, headOfTheQueue):
		# S'il n'y a personne en tete de file. Autrement dit la file est vide
		if(headOfTheQueue == None):
			return self # La cliente devient la tete de file. Et c'est termine.
		# Sinon, on parcourt les clients de la file d'attente e partir du debut
		currentClient = headOfTheQueue
		# Si la tete de file n'est pas une cliente enceinte. On se met en tete de file.
		if(not isinstance(currentClient, PregnantClient)):
			currentClient.previousClient = self
			self.nextClient = currentClient
			return self
		# Sinon, on cherche la position de la derniere client enceinte
		r = currentClient
		while(currentClient != None):
			if(isinstance(currentClient, PregnantClient)):
				r = currentClient
				currentClient = currentClient.nextClient
			else:
				break
		# Et on se met derriere elle
		self.nextClient = r.nextClient
		if(self.nextClient != None):
			self.nextClient.previousClient = self
		self.previousClient = r
		r.nextClient = self
		# On informe l'instance de la file d'attente de la tete de file retenue apres traitement
		return headOfTheQueue
	
	"""
		Redefinition de la methode publique d'affichage d'une cliente en etat de grossesse
	"""
	def show(self):
		# On recupere le numero du client courant
		text = "Femme enceinte Ne " + str(self.number) + " (" + self.arrival + ")\n"
		# Et on demande e l'eventuel client qui suit dans la file d'attente de s'afficher
		if(self.nextClient != None):
			text += self.nextClient.show()
		return text

"""
	Classe representative des clients seniors
"""
class SeniorClient(Client):
	"""
		Classe representative des clientes en etat de grossess
	"""
	def __init__(self, number, arrival):
		Client.__init__(self, number, arrival)
	
	"""
		Redefinition de la methode publique d'auto-insertion du client senior courant dans la file d'attente. La tete de file lui est transmise en parametre
	"""
	def insertIntoQueue(self, headOfTheQueue):
		# S'il n'y a personne en tete de file. Autrement dit la file est vide
		if(headOfTheQueue == None):
			return self # La cliente devient la tete de file. Et c'est termine.
		# Sinon, on parcourt les clients de la file d'attente e partir du debut
		currentClient = headOfTheQueue
		# Si la tete de file n'est pas une cliente enceinte ou un client senior. On se met en tete de file.
		print("--> ", currentClient, " : ", isinstance(currentClient, PregnantClient), " -- ", isinstance(currentClient, SeniorClient))
		if(not isinstance(currentClient, PregnantClient) and not isinstance(currentClient, SeniorClient)):
			currentClient.previousClient = self
			self.nextClient = currentClient
			return self
		# Tant qu'on voit une cliente enceinte ou un client senior, on regarde le client suivant
		r = currentClient
		while(currentClient != None):
			if(isinstance(currentClient, PregnantClient) or isinstance(currentClient, SeniorClient)):
				r = currentClient
			currentClient = currentClient.nextClient
		# On se place tout aupres e trois clients derriere le dernier client senior ou la derniere clients enceinte
		# s'il y a plusieurs autres clients derriere lui
		currentClient = r.nextClient
		count = 1
		while((currentClient != None) and (count < 4)):
			r = currentClient
			currentClient = currentClient.nextClient
			count += 1
		# On s'insere e cette position
		self.nextClient = r.nextClient
		if(self.nextClient != None):
			self.nextClient.previousClient = self
		self.previousClient = r
		r.nextClient = self
		# On informe l'instance de la file d'attente de la tete de file retenue apres traitement
		return headOfTheQueue
	
	"""
		Redefinition de la methode publique d'affichage d'un client senior
	"""
	def show(self):
		# On recupere le numero du client courant
		text = "3eme ege Ne " + str(self.number) + " (" + self.arrival + ")\n"
		# Et on demande e l'eventuel client qui suit dans la file d'attente de s'afficher
		if(self.nextClient != None):
			text += self.nextClient.show()
		return text

"""
	Classe representative de la file d'attente
"""
class FileDattente:
	"""
		Constructeur publique d'un objet de la classe
	"""
	def __init__(self, next_client_number = 1, next_pregnant_client_number = 10000, next_senior_client_number = 15000):
		self.headOfTheQueue = None
		self.next_client_number = next_client_number
		self.next_pregnant_client_number = next_pregnant_client_number
		self.next_senior_client_number = next_senior_client_number
	
	"""
		Methode publique d'ajout d'un client dans la file d'attente
	"""
	def addClient(self):
		# Affectation d'un numero de ticket au client
		number = self.next_client_number
		# Sauvegarde de l'heure d'arrivee du client
		now = datetime.now()
		arrival = now.strftime("%d/%m/%Y %H:%M:%S")
		# Creation d'une nouvelle instance de la classe <Client> avec le numero de ticket et l'heure d'arrivee
		client = Client(number, arrival)
		# Si la file est vide, le nouveau client devient la tete de la file d'attente
		if(self.headOfTheQueue == None):
			self.headOfTheQueue = client
		# Sinon la methode <insertIntoQueue> de la classe <Client> est appelee
		else:
			self.headOfTheQueue = client.insertIntoQueue(self.headOfTheQueue)
		# Incrementation du numero de ticket pour le positionnement du prochain client
		self.next_client_number += 1
		return number, arrival
	
	"""
		Methode publique d'ajout d'une client enceinte dans la file d'attente
	"""
	def addPregnantClient(self):
		# Affectation d'un numero de ticket e la cliente enceinte
		number = self.next_pregnant_client_number
		# Sauvegarde de l'heure d'arrivee de la cliente enceinte
		now = datetime.now()
		arrival = now.strftime("%d/%m/%Y %H:%M:%S")
		# Creation d'une nouvelle instance de la classe <PregnantClient> avec le numero de ticket et l'heure d'arrivee
		client = PregnantClient(number, arrival)
		# Si la file est vide, la nouvelle cliente devient la tete de la file d'attente
		if(self.headOfTheQueue == None):
			self.headOfTheQueue = client
		# Sinon la methode <insertIntoQueue> de la classe <PregnantClient> est appelee
		else:
			self.headOfTheQueue = client.insertIntoQueue(self.headOfTheQueue)
		# Incrementation du numero de ticket pour le positionnement de la prochaine cliente enceinte
		self.next_pregnant_client_number += 1
		return number, arrival
	
	"""
		Methode publique d'ajout d'un client senior dans la file d'attente 
	"""
	def addSeniorClient(self):
		# Affectation d'un numero de ticket au client senior
		number = self.next_senior_client_number
		# Sauvegarde de l'heure d'arrivee du client senior
		now = datetime.now()
		arrival = now.strftime("%d/%m/%Y %H:%M:%S")
		# Creation d'une nouvelle instance de la classe <SeniorClient> avec le numero de ticket et l'heure d'arrivee
		client = SeniorClient(number, arrival)
		# Si la file est vide, la nouvelle cliente devient la tete de la file d'attente
		if(self.headOfTheQueue == None):
			self.headOfTheQueue = client
		# Sinon la methode <insertIntoQueue> de la classe <SeniorClient> est appelee
		else:
			self.headOfTheQueue = client.insertIntoQueue(self.headOfTheQueue)
		# Incrementation du numero de ticket pour le positionnement du prochain client senior
		self.next_senior_client_number += 1
		return number, arrival
	
	"""
		Methode publique de recuperation du nombre de clients dans la file 
	"""
	def countNumberOfClients(self):
		# Initialisation du compteur du nombre de clients e zero
		count = 0
		# On parcourt la file d'attente e partir de la tete 
		currentClient = self.headOfTheQueue
		# Tant qu'on n'a pas atteint la fin de la file d'attente ...
		while(currentClient != None):
			# ... on incremente le compteur d'un pas
			count += 1
			# on se deplace sur le client suivant
			currentClient = currentClient.nextClient
		# On retourne le nombre de clients compte
		return count
	
	"""
		Methode publique de recuperation du nombre de clients dans la file 
	"""
	def getNextClient(self):
		# On recupere l'instance de la classe <Client> en tete de la file d'attente
		topClient = self.headOfTheQueue
		# On place le deuxieme de la file en tete
		if(topClient != None):
			self.headOfTheQueue = self.headOfTheQueue.nextClient
			self.headOfTheQueue.previousClient = None
		# On retourne le client en tete de file
		return topClient
	
	"""
		Methode publique d'affichage de la file d'attente 
	"""
	def showQueue(self):
		# Si la file n'est pas vide, on affiche la tete de la file d'attente
		if(self.headOfTheQueue != None):
			return self.headOfTheQueue.show()
		# Sinon, on informe que la file est vide
		else:
			return "La file est vide."

def showMenu():
	print("---------- Menu ----------")
	print(" c | C : Add a client.")
	print(" p | P : Add a pregnant client.")
	print(" o | O : Add a senior client.")
	print(" g | G : Get the first client.")
	print(" s | S : Show the list of clients.")
	print(" l | L : Give the length of the queue.")
	print(" q | Q : Quit and close.")
	print("--------------------------")

def isBadCommand(command):
	if((command == 'm') or (command == 'M')  # Si 'm' ou 'M' : Affichage du menu utilisateur
		or (command == 'c') or (command == 'C')  # Si 'c' ou 'C' : Ajout d'une nouveau client e la file d'attente
		or (command == 'p') or (command == 'P')  # Si 'p' ou 'P' : Ajout d'une cliente enceinte e la file d'attente
		or (command == 'o') or (command == 'O')  # Si 'o' ou 'O' : Ajout d'un client ege e la file d'attente
		or (command == 'g') or (command == 'G')  # Si 'g' ou 'G' : Recuperation au client en tete de la file d'attente
		or (command == 's') or (command == 'S')  # Si 's' ou 'S' : Affichage de la liste des clients en attente
		or (command == 'l') or (command == 'L')  # Si 'l' ou 'L' : Affichag de la longueur de la file d'attente
		or (command == 'q') or (command == 'Q')): # Si 'q' ou 'Q' : Quitter le programme
		return False
	else: # Sinon : commande invalide
		return True

def main():
	# Creation de l'objet "file d'attente"
	fileDattente = FileDattente()
	# Affichage du menu initial pour guider l'utilisateur
	showMenu()
	
	while True :
		# Demande du choix de l'utilisateur et contrele de saisie
		while True:
			# Demande e l'utilisateur de faire un choix en tapant une commande
			command = input("-- Faites un choix: ")
			# Recuperation de la premiere caractere correspondant au choix
			command = command[0]
			# Tant que la commande est inconnue, on lui redemande de faire un choix
			if(not isBadCommand(command)):
				break
		
		if((command == 'c') or (command == 'C')):  # Choix d'ajout d'un client dans la file d'attente  
			fileDattente.addClient()
			print("Le client a ete ajoute.")
		elif((command == 'p') or (command == 'P')):  # Choix d'ajout d'une cliente en etat de grossesse dans la file d'attente
			fileDattente.addPregnantClient()
			print("La cliente en etat de grosses a ete ajoutee.")
		elif((command == 'o') or (command == 'O')):  # Choix d'ajout d'un client senior dans la file d'attente
			fileDattente.addSeniorClient()
			print("La client senior a ete ajoute.")  
		elif((command == 'g') or (command == 'G')): # Choix de recuperation du client en tete de la file d'attente
			client = fileDattente.getNextClient() # Appel de la fonction de recuperation de la tete de liste
			client.show()
		elif((command == 's') or (command == 'S')): # Choix d'affichage des clients de la file d'attente
			text = fileDattente.showQueue() # Affichage de la liste
			print(text) # Saut de ligne e l'affichage
		elif((command == 'l') or (command == 'L')): # Choix d'affichage du nombre de clients dans la file d'attente
			print("La taille de la file = ", fileDattente.countNumberOfClients()) # Affichage de la taille de la liste
		elif((command == 'm') or (command == 'M')): # Choix de raffichage du menu
			showMenu() # Affichage du menu
		else: #((command != 'q') and (command != 'Q')) # Ou choix de quitter et fermer l'application
			break
	print("Bye not ")


# main()