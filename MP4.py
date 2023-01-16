# import os

# # On demande au joueur de saisir un mot
# word = input("Joueur 1 - Saisissez un mot : ")

# # On efface la console pour cacher le mot saisi par le joueur 1
# os.system("cls")

# #Déclaration de variables
# find = "_" * len(word)
# print(find)
# attempt = 7

# while find != word and attempt != 0:
#     word2 = str(input("Joueur 2 - Saisissez une lettre : "))
#     for i in range(len(word)):
#         if word2 in word[i]:
#             find = find[:i] + word2 + find[i+1:]
#             print('Yesssss',find)
#         elif word2 not in word: 
#             attempt += -1 
#             print(f'Plus que {attempt} tentative(s)')
#             break
# if word == find:
#     print('Bravoooooooooo')
# for word2 in list:
#     print('Bien joué')

#Il faut donner l'indication des lettres
#Il faut demander au joueur 2 de saisir une lettre
#Si la lettre se trouve dans le mot : mettre le mot
#Sinon, raté

# import os

# word = input("Joueur 1 - Saisissez un mot : ")
# find = "_" * len(word)
# attempt = 7

# os.system("cls")

# while find != word and attempt != 0:
#     print(find)
#     word2 = str(input("Joueur 2 - Saisissez une lettre : "))
#     if word2 not in word: 
#         attempt -= 1 
#         print(f'Plus que {attempt} tentative(s)')
#     elif word2 == word:
#         find = word2
#     else :
#         for i in range(len(word)):
#             if word2 in word[i]:
#                 find = find[:i] + word2 + find[i+1:]
# if word == find:
#     print(f'Bravo le mot était bien {word}')
# else :
#     print(f'Perdu le mot était {word}')

import os 

word = input("Joueur 1 - Saisissez un mot :")

os.system('cls')

attempt = 7

list_letters = []
list_letters_founded = []

for letter in word:
    
    list_letters.append(letter)
    
    list_letters_founded.append("_")
    
    
while attempt != 0 and "_" in list_letters_founded:
    #On affiche les lettres trouvées jusqu'alors, séparées par des espaces
    for letter_founded in list_letters_founded:
        print(letter_founded, end=" ")
        
    letter = input("\n\nJoueur 2 - Proposez une lettre :")
    
    #Si la lettre saisie par le joueur 2 est présente dans la liste contenant les lettres
    #On ajoute la lettre dans la liste des lettres trouvées
    if letter in list_letters :
        #on remplace au bon index le "_" par la lettre trouvée
        for i in range(len(list_letters)):
            if list_letters[i] == letter:
                list_letters_founded[i] = letter
    #Sinon on décrémente le nombre de tentatives
    #On affiche "Raté" avec le nombre de tentatives restantes
    else:
        attempt = attempt - 1
        print(f"Raté : Plus que {attempt} tentative(s)")

#Si le nombre de tentatives n'a pas atteint 0
#On affiche "Gagné"       
if attempt != 0:
    print("\n\nC'est gagné !!! :)")
#Sinon on affiche "Perdu"
else:
    print("\n\n c'est perdu :(")