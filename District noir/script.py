import random

# Initialisation des variables
cartes_type = [5,6,7,8]
cartes_soutien = []

# Boucle pour ajouter autant de fois de carte que son type
for i in range(5):
    cartes_soutien.append(cartes_type[0])
for i in range(6):
    cartes_soutien.append(cartes_type[1])
for i in range(7):
    cartes_soutien.append(cartes_type[2])
for i in range(8):
    cartes_soutien.append(cartes_type[3])
# print(cartes_soutien)

cartes_alliance = ["+2", "+3", "+4", "+2", "+2", "+3", "+3"]
cartes_trahison = ["-3", "-3", "-3", "-1", "-1", "-3", "-2", "-2", "-2"]
cartes_lieu = ["Lieu 1", "Lieu 2", "Lieu 3"]
cartes = cartes_soutien + cartes_alliance + cartes_trahison + cartes_lieu
# print(cartes)
pioche = []
jeu = [[], []]
tapis = []
score = [0, 0]
jeton = random.choice(["Recto", "Verso"])

# Pour définir le fait que la pioche soit égale aux cartes (dont les 3 qu'on a retiré)
pioche = cartes

# Mélanger les cartes
def melanger_cartes():
    random.shuffle(cartes)
    return cartes
melanger_cartes()

# Retirer 3 cartes de la pioche
def retirer_cartes_pioche():
    for i in range(3):
        pioche.remove(pioche[-1])
    return pioche
retirer_cartes_pioche()

# Distribuer les cartes aux joueuses
def distribuer_cartes():
    for i in range(5):
        jeu[0].append(cartes[i])
        jeu[1].append(cartes[i + 5])
    del cartes[:10]
    return jeu
distribuer_cartes()
hand_player1 = jeu[0]
hand_player2 = jeu[1]
print(f"Main du joueur 1 : {hand_player1}")
print(f"Main du joueur 2 : {hand_player2}")

# Piocher 2 cartes pour le tapis
def piocher_tapis():
    for i in range(2):
        tapis.append(pioche[-1])
        del pioche[-1]
    return tapis
piocher_tapis()
print(f"Le tapis est : {tapis}")

# Pour déterminer qui commence la manche
def determiner_premiere_joueuse():
    choice = input("Choisissez un camp : recto ou verso.")
    if jeton == choice:
        return "Le joueur 1 commence la partie"
    else:
        return "Le joueur 2 commence la partie"
print(determiner_premiere_joueuse())

# Pour jouer une carte
def jouer_carte(joueuse, carte):
    jeu[joueuse].remove(carte)
    # print(jeu[joueuse])
    tapis.append(carte)
    return tapis
""" En fonction du joueur qui doit commencer, on peut changer le premier paramètre
lors de l'appel de la fonction. 0 : joueur 1 / 1 : joueur 2 """ 
print(f"Le tapis actuel est :",jouer_carte(0,7))

# Fonction pour prendre les dernières cartes jouées
def prendre_dernieres_cartes(joueuse):
    derniere_carte = len(tapis) - 1
    if derniere_carte >= 0:  # vérifier si le tapis n'est pas vide
        for i in range(5):
            if derniere_carte >= 0:
                carte = tapis[derniere_carte]
                tapis.remove(carte)
                jeu[joueuse].append(carte)
                derniere_carte -= 1
            else:
                break
    return jeu[joueuse]
print(f"Nouvelle main du joueur 2 :",prendre_dernieres_cartes(1))

def trouver_type_carte(carte):
    if carte in cartes_soutien:
        return "Soutien"
    elif carte in cartes_lieu:
        return "Lieu"
    elif carte in cartes_alliance:
        return "Alliance"
    elif carte in cartes_trahison:
        return "Trahison"
    else:
        return None

# Fonction pour calculer le score
# Fonction pour calculer le score
def calculer_score(hand_player1, hand_player2, cartes_type):
    nb_cinq_player1 = 0
    nb_cinq_player2 = 0
    score_player1 = 0
    score_player2 = 0
    
    for i in hand_player1:
        if i in cartes_type:
            nb_cinq_player1 += i
            score_player1 += i
            print(f"Score 1 : {score_player1}")
            
    for i in hand_player2:
        if i in cartes_type:
            nb_cinq_player2 += i 
            score_player2 += i
            print(f"Score 2 : {score_player2}")
            
    if nb_cinq_player1 > nb_cinq_player2:
        score_player1 += cartes_type[3]
    elif nb_cinq_player1 < nb_cinq_player2:
        score_player2 += cartes_type[3]
        
    return (score_player1, score_player2)
        
print(calculer_score(hand_player1, hand_player2, cartes_type))
















































# def jouer_partie():
#     # Initialisation des variables
#     tas = []
#     jeton_camp = random.choice(["pile", "face"])
#     score_joueur1 = 0
#     score_joueur2 = 0
#     joueur1_a_les_lieux = False
#     joueur2_a_les_lieux = False
    
#     # Déroulement des 4 manches
#     for manche in range(1, 5):
#         print(f"\n==== Manche {manche} ====")
        
#         # Mélange du paquet et distribution des cartes
#         paquet = ["SOUTIEN_" + str(i) for i in range(5, 9)] * 6 + \
#                  ["ALLIANCE"] * 7 + \
#                  ["TRAHISON"] * 9 + \
#                  ["VILLE"] * 3
#         random.shuffle(paquet)
#         pioche = paquet[:-3]
#         tapis = paquet[-3:]
#         main_joueur1 = pioche[:5]
#         main_joueur2 = pioche[5:10]
#         pioche = pioche[10:]
        
#         # Tour des joueurs
#         joueur_courant = 1 if jeton_camp == "face" else 2
#         nb_tours_restants = 6
#         dernieres_cartes = []
#         while nb_tours_restants > 0:
#             print(f"\n--- Tour {6 - nb_tours_restants + 1} ---")
#             print(f"Tapis : {tapis}")
#             print(f"Main Joueur 1 : {main_joueur1}")
#             print(f"Main Joueur 2 : {main_joueur2}")
#             print(f"Dernières cartes : {dernieres_cartes}")
#             carte_jouee = None
#             prendre_tas = False
            
#             # Demande à l'utilisateur de saisir une action valide
#             while not carte_jouee and not prendre_tas:
#                 action = input("Jouer une carte ou prendre le tas (j/p) : ")
#                 if action == "j":
#                     index_carte = input("Indiquez l'index de la carte à jouer : ")
#                     if joueur_courant == 1:
#                         try:
#                             carte_jouee = main_joueur1.pop(int(index_carte))
#                         except:
#                             print("Indice de carte invalide.")
#                     else:
#                         try:
#                             carte_jouee = main_joueur2.pop(int(index_carte))
#                         except:
#                             print("Indice de carte invalide.")
#                 elif action == "p":
#                     if len(tas) > 0:
#                         dernieres_cartes = tas[-5:]
#                         tas = tas[:-5] if len(tas) > 5 else []
#                         prendre_tas = True
#                     else:
#                         print("Le tas est vide.")
            
#             # Ajout de la carte jouée ou du tas dans la liste des dernières cartes
#             if prendre_tas:
#                 dernieres_cartes.reverse()
#             elif joueur_courant == 1:
#                 dernieres_cartes.append(carte_jouee)
#             else:
#                 dernieres_cartes.append(carte_jouee)
            
#             # Passage au joueur suivant ou fin de tour
#             if joueur_courant == 1:
#                 joueur_courant = 2
#             else:
#                 nb_tours_restants -= 1
#                 joueur_courant = 1
        
#         #