import os

word = input("Joueur 1 - Saisissez un mot : ")
find = "_" * len(word)
attempt = 7

os.system("cls")

while find != word and attempt != 0:
    print(find)
    word2 = str(input("Joueur 2 - Saisissez une lettre : "))
    if word2 not in word: 
        attempt -= 1 
        print(f'Plus que {attempt} tentative(s)')
    elif word2 == word:
        find = word2
    else :
        for i in range(len(word)):
            if word2 in word[i]:
                find = find[:i] + word2 + find[i+1:]
if word == find:
    print(f'Bravo le mot était bien {word}')
else :
    print(f'Perdu le mot était {word}')