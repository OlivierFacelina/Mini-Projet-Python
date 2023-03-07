import random

def init_cards():
    lst_colors = [(chr(3)),(chr(4)),(chr(5)),(chr(6))]
    lst_numbers = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi']
    lst_cards = [(color, number) for color in lst_colors for number in lst_numbers]
    random.shuffle(lst_cards)
    return lst_cards

def draw(lst_cards):
    card = lst_cards.pop()
    return card, lst_cards

def get_value_cards(lst_cards):
    value = 0
    nb_as = 0
    for card in lst_cards:
        if card[1] in ['Valet', 'Dame', 'Roi']:
            value += 10
        elif card[1] == 'As':
            nb_as += 1
            value += 1
        else:
            value += int(card[1])
    if nb_as > 0 and value + 10 <= 21:
        value += 10
    return value

def display_cards(player, lst_cards, value):
    print(player + ' :')
    for card in lst_cards:
        print('- ' + card[1] + card[0])
    print('Total : (' + str(value) + ')')

def to_bet(cash):
    while True:
        bet = int(input('Combien souhaitez-vous miser ? '))   
        while bet < 20:
            print("Non ! Le montant est invalide, mise de 20€ minimum ! ")
            bet = int(input('Combien souhaitez-vous miser ? '))
        if bet <= cash:
            return cash - int(bet), int(bet)
        elif bet < 20:
            return "Montant non valide"
        print('Veuillez saisir un montant valide.')

# Initialisation
cash = 200
bet = 0
quit_game = False
lst_cards = init_cards()
lst_player_cards = []
lst_croupier_cards = []

# Premier tour
cash, bet = to_bet(cash)
card, lst_cards = draw(lst_cards)
lst_player_cards.append(card)
card, lst_cards = draw(lst_cards)
lst_croupier_cards.append(card)
card, lst_cards = draw(lst_cards)
lst_player_cards.append(card)

display_cards('Croupier', lst_croupier_cards, get_value_cards(lst_croupier_cards))
display_cards('Joueur', lst_player_cards, get_value_cards(lst_player_cards))

if get_value_cards(lst_player_cards) == 21:
    print("Vous êtes arrivés du premier coup à 21 ! Bravo.")
    quit_game = True
    cash += bet + bet
    print(f'Il vous reste : {cash} euros.')

# Boucle de jeu
while quit_game == False:
    choice = input('Souhaitez-vous tirer une carte ? (o/n) ')
    if choice == 'o':
        card, lst_cards = draw(lst_cards)
        lst_player_cards.append(card)
        display_cards('Joueur', lst_player_cards, get_value_cards(lst_player_cards))
        if get_value_cards(lst_player_cards) > 21:
            print('Vous avez perdu !')
            quit_game = True
            cash -= bet - bet
            print(f'Il vous reste : {cash} euros.')
        elif get_value_cards(lst_player_cards) == 21:
            print("Incroyable, vous êtes arrivés directement à 21 ! Bravo.")
            quit_game = True
            cash += bet + bet
            break
    else:
        while get_value_cards(lst_croupier_cards) < 21:
            card, lst_cards = draw(lst_cards)
            lst_croupier_cards.append(card)
        display_cards('Croupier', lst_croupier_cards, get_value_cards(lst_croupier_cards))
        if get_value_cards(lst_player_cards) > get_value_cards(lst_croupier_cards) or get_value_cards(lst_croupier_cards) > 21 or get_value_cards(lst_player_cards) == 21:
            print('Vous avez gagné !')
            quit_game = True
            cash += bet + bet
            print(f'Il vous reste : {cash} euros.')
        elif get_value_cards(lst_player_cards) < get_value_cards(lst_croupier_cards):
            print('Vous avez perdu !')
            
    # # Demander au joueur s'il souhaite continuer de jouer la partie
    # print("Souhaitez-vous continuer la partie ? (o/n)")
    # stop_game = input("--> ")
    # if stop_game == "o":
    # cash, bet = to_bet(cash)
    # card, lst_cards = draw(lst_cards)
    # lst_player_cards.append(card)
    # card, lst_cards = draw(lst_cards)
    # lst_croupier_cards.append(card)
    # card, lst_cards = draw(lst_cards)
    # lst_player_cards.append(card)
    # display_cards('Croupier', lst_croupier_cards, get_value_cards(lst_croupier_cards))
    # display_cards('Joueur', lst_player_cards, get_value_cards(lst_player_cards))
    #     quit_game = False
    #     print("\nVous avez décidé d'arrêter la partie.\n")
            
# Statistiques