#!/usr/bin/env python
# -*- coding: utf-8 -*-
#on define une methode pour utiliser plus tard
def majuscule(mot):
    nouveau_mot = ""
    #on fait un loop qui va indiquer que pour chaque lettre dans le mot on fait la fonction
    for lettre in mot:
        #on fait une variable pour simplifier l'écriture, ca donne la valeur numérique ASCII de la lettre
        temp = ord(lettre)
        #indique que si la valeur numerique ascii est plus grande ou egale a 97 (les minuscules), on met en majuscule
        if temp >= 97:
            nouveau_mot += chr(temp-32)
        #Sinon, on ajoute la lettre au nouveau mot sans la mettre en majuscule
        else:
            nouveau_mot += lettre
    return nouveau_mot

if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
print('Voici les mots!')
