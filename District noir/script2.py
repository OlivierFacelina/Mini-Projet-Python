import random

# Cartes
cartes = [1, 2, 3, 4, 5, 6, 7, 8, 9, '+', '-'] * 4 + ['ville'] * 3

# Distribution du jeu
random.shuffle(cartes)
pioche = cartes[:-3]
joueur1 = cartes[-3:]
joueur2 = cartes[-6:-3]
tapis = random.sample(pioche, 2)

# Jeton camp
jeton = random.choice(['pile', 'face'])

# Fonction pour distribuer des cartes
def distribuer_cartes(joueur, pioche, nb_cartes):
    for _ in range(nb_cartes):
        carte = pioche.pop()
        joueur.append(carte)

# Distribution des cartes
distribuer_cartes(joueur1, pioche, 5)
distribuer_cartes(joueur2, pioche, 5)

def jouer_partie():
    # Initialisation des variables
    jeton_camp = ['pile', 'face'][randint(0,1)]  # Choix aléatoire du joueur qui commence
    score_j1 = 0
    score_j2 = 0
    
    # Distribution des cartes
    cartes = initialiser_cartes()
    melanger_cartes(cartes)
    pioche = cartes[:-3]
    tapis = cartes[-3:]
    main_j1 = piocher(pioche, 5)
    main_j2 = piocher(pioche, 5)
    
    # Début de la partie
    for manche in range(1, 5):
        print(f"----- Manche {manche} -----")
        # Initialisation des variables pour la manche
        tas = []
        derniers_coups = []
        
        # Tour des joueurs
        for tour in range(6):
            print(f"Tour {tour+1}")
            # Tour du joueur 1
            print("Joueur 1 :")
            jouer_carte(main_j1, tas)
            prendre_cartes(derniers_coups)
            
            # Tour du joueur 2
            print("Joueur 2 :")
            jouer_carte(main_j2, tas)
            prendre_cartes(derniers_coups)
        
        # Fin de la manche
        piocher(tas, 5, derniers_coups)
        print("Fin de la manche")
        
        # Calcul des scores
        score_j1_manche, score_j2_manche = calculer_score(main_j1, main_j
