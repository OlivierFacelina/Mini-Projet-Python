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

# Fonction pour calculer le score
def calculer_score(cartes):
    soutiens = []
    lieux = []
    alliances = []
    trahisons = []
    for carte in cartes:
        if 5 <= carte.valeur <= 8:
            soutiens.append(carte)
        elif carte.type == "Lieu":
            lieux.append(carte)
        elif carte.type == "Alliance":
            alliances.append(carte.valeur)
        elif carte.type == "Trahison":
            trahisons.append(carte.valeur)
    soutiens = sorted(soutiens, reverse=True)
    score = sum([carte.valeur for carte in soutiens])
    for i in range(len(soutiens) - 1):
        if soutiens[i].valeur == soutiens[i+1].valeur:
            score += 0
    if len(set([carte.valeur for carte in soutiens])) == 4:
        score += 5
    elif len(set([carte.valeur for carte in soutiens])) == 2 and soutiens[0].valeur == soutiens[1].valeur and soutiens[2].valeur == soutiens[3].valeur:
        score += 10
    score += sum(alliances) - sum(trahisons)
    return score
joueur_1_score = calculer_score(jeu[0])
print("Le score de la première joueuse est : ", joueur_1_score)
