#matrice double dim carrée
#bites => petit triangle blanc = 0, noir = 1
#longeur, la fin, les erreurs
import numpy as np
import matplotlib.pyplot as plt
import math
import petitTriangle
import Hamming

#######################################################################
# Place:  prend un char, le transforme en ascii et redonne une liste 
#         de bit representer la valeur de la lettre
#
#En entree: char (lettre)
#
#En sortie: list (liste)
#######################################################################
def lettreToBit(lettre):
    list = [0 for x in range(8)]
    lettre = ord(lettre)
    x = 128
    for i in range(8):
        if lettre >= x:
            list[i] = 1
            lettre -= x
        x /= 2
    list.reverse()
    return list
    

#######################################################################
# Place:  la fonction prend un chaine de caractere, fait appel a la  
#         fonction lettreToBit() en renvoie une liste de chaque caractere  
#         que est une liste de bits
#
#En entree: sting (msg)
#
#En sortie:  liste(list)
#######################################################################
def stringToBits(msg):
    list = []
    for i in range(len(msg)):
        list.append(lettreToBit(msg[i]))
    return list


#######################################################################
# Place:  la fonction prend un int et renvoie ça representation binaire
#         en form de liste de taille 16 (donc 2 octets)
#
#En entree: int(taille)
#
#En sortie: list(list)
#######################################################################
def taillToBits(taille):
    list = [0 for x in range(16)]
    x = 32448
    for i in range(16):
        if taille >= x:
            list[i] = 1
            taille -= x
        x /= 2
    list.reverse()
    return list


#######################################################################
# Place: dessin un triangle dans l'liste donneé en presisant
#        les indices et le sens du triangle
#        1 = droite, 3 = gauche, 2 = bas, 4 = haut
#
#En entree:   liste(Matrix), int(i), int(j), int(sens)
#
#En sortie:   void()
#######################################################################
def triangle(Matrix, i, j, sens):
    for x in range(i-1, i+2):
        Matrix[x][j] = 1
    for x in range(j-1, j+2):
        Matrix[i][x] = 1
    if sens == 1:
        for x in range(i-2, i-2+5):
            Matrix[x][j-1] = 1
    if sens == 3:
        for x in range(i-2, i-2+5):
            Matrix[x][j+1] = 1
    if sens == 2:
        for x in range(j-2, j-2+5):
            Matrix[i-1][x] = 1
    if sens == 4:
        for x in range(j-2, j-2+5):
            Matrix[i+1][x] = 1
 

#######################################################################
# Place:  on parcour un liste de zeros (par pas de 7) appellé Matrix et 
#         les bits a dessiner (bit par bit) qui sont dans une liste qui
#         contien la chaine de caractere en forma bits si le bit est zero 
#         on ne fait rien sinon on met un triangle
#         liste contien les indices ou le logo sera, donc les indices qui
#         qui ne faut pas ecrire dessus
#
#En entree: liste(Matrix), int(n) :la taille, list(msg), list(liste)
#
#En sortie: int( 1 ):si tout est ok
#######################################################################
def parcourirAvecLogo(Matrix, n, msg, liste):
    indiceLettre = 0
    indiceMot    = 0

    for i in range(3, n+1, 7):
        for j in range(3, n+1, 7):

            if indiceLettre == 8: 
                indiceLettre = 0
                indiceMot += 1
            if indiceMot >= len(msg):
                return 1

            sens = 1
            if j>liste[0] and j <liste[1] and i>liste[2] and i<liste[3] :
                j = j+7    
            else :
                if msg[indiceMot][indiceLettre] == 1:
                    triangle(Matrix, i, j-2, sens)
                sens += 1
                indiceLettre += 1
                if msg[indiceMot][indiceLettre] == 1:
                    triangle(Matrix, i-2, j, sens)
                sens += 1
                indiceLettre += 1
                if msg[indiceMot][indiceLettre] == 1:
                    triangle(Matrix, i, j+2, sens)
                sens += 1
                indiceLettre += 1
                if msg[indiceMot][indiceLettre] == 1:
                    triangle(Matrix, i+2, j, sens)
                sens += 1
                indiceLettre += 1
    return 1

#######################################################################
# Place: exactement comme la fonction d'avant mais sans la contrainte de 
#        logo
#
#En entree: liste(Matrix), int(n) :la taille, list(msg)
#
#En sortie: int (1)
#######################################################################
def parcourirSansLogo(Matrix, n, test):
    indiceLettre = 0
    indiceMot    = 0

    for i in range(3, n+1, 7):
        for j in range(3, n+1, 7):

            if indiceLettre == 8: 
                indiceLettre = 0
                indiceMot += 1
            if indiceMot >= len(test):
                return 1

            sens = 1
            if test[indiceMot][indiceLettre] == 1:
                triangle(Matrix, i, j-2, sens)
            sens += 1
            indiceLettre += 1
            if test[indiceMot][indiceLettre] == 1:
                triangle(Matrix, i-2, j, sens)
            sens += 1
            indiceLettre += 1
            if test[indiceMot][indiceLettre] == 1:
                triangle(Matrix, i, j+2, sens)
            sens += 1
            indiceLettre += 1
            if test[indiceMot][indiceLettre] == 1:
                triangle(Matrix, i+2, j, sens)
            sens += 1
            indiceLettre += 1
    return 1


#######################################################################
# Place:   prend la chaine de caracteres en forma de liste de bits et 
#          rajoute l'octet d'arrete et les 2 octets de taille 
#
#En entree: liste(G), string(mots)
#
#En sortie: void()
#######################################################################
def addInfoG(G, mots):
    G.append([0,0,0,0,0,0,0,0])
    G.append(taillToBits(len(mots)))


#######################################################################
# Place: mets des point la ou on souhaite parcourir(au milleu du carrée
#        formé par 4 triangle)
#
#En entree: int(n)
#
#En sortie: void()
#######################################################################
def point(n):
    Matrix = [[0 for x in range(n)] for y in range(n)]
    for i in range(3, n+1, 7):
        for j in range(3, n+1, 7):
            Matrix[i][j] = 1
    afficher(Matrix)


#######################################################################
# Place: creer 2 list de longeur (n) et rajoute des triangle(Grande et 
#       Petite) en sens qui indique le haut a gauche
#
#En entree: int(n)
#
#En sortie: list(G), list(P)
#######################################################################
def position(n):
    G = [[0 for x in range(n)] for x in range(5)]
    P = [[0 for x in range(n)] for x in range(2)]
    for i in range(1, n-1, 3):
        triangle(G, 2, i, 1)
    for i in range(1, n-1, 3):
        petitTriangle.petitTrangle(P, 0, i, 0)
    return G, P


#######################################################################
# Place: prend le mot et nous calcule le dimension da la matrice en 
#        prenant en conte le logo
#
#En entree: string(text)
# 
#En sortie: int (la dimension du carree)
#######################################################################
def tailleAvecLogo(text):
    n = len(text)
    x = 56
    if n >= 1 and n <= 25:
        return x
    if n >= 26 and n <= 109:
        return x *2
    if n >= 110 and n <= 445:
        return x *2 *2
    if n >= 446 and n <= 1789:
        return x *2 *2 *2
    if n >= 1790 and n <= 7166:
        return x *2 *2 *2 *2
    if n >= 7167 and n <= 28670:
        return x *2 *2 *2 *2 *2
    else:
        print("ERROR : le message n'a pas une taille acceptable")


#######################################################################
# Place: prend le mot et nous calcule le dimension da la matrice
#
#En entree: string(text)
#
#En sortie: int (la dimension du carree)
#######################################################################
def tailleSansLogo(text):
    #l'octet d'arrete et les deux octets de taille
    nbCellules = (len(text) + 3)
    n = int(math.sqrt(nbCellules * 2) * 7)
    tmp = n
    if n % 7 != 0:
        while tmp > 7:
            tmp -= 7
        n += 7 - tmp
    return int(n)


#######################################################################
# Place: prend un matrice et ça taille et dessin le rectangle ou on peut
#        mettre le logo et renvoie les indice qu'il faut eviter quand on
#        parcour l'liste
#
#En entree: liste(Matrix), int(n)
#
#En sortie: list(liste)
#######################################################################
def logo(Matrix, n):
    if n == 56:
        largeur = 4
        hauteur = 2
    if n > 56:
       new = n//56
       largeur = new * 4
       hauteur = new * 2
    #--------------------- hauteur
    test = n/7
    ordonee = test - hauteur
    ordonee = ordonee/2
    ordonee = ordonee*7
    ordonee = ordonee+4
    #--------------------- largeur

    abscisse = test - largeur
    abscisse = abscisse/2
    abscisse = abscisse*7
    abscisse = abscisse+4

    #------------------- rectangle milieu
    abscisse = int(abscisse)
    ordonee = int(ordonee)
    for i in range(abscisse - 4, abscisse - 4 +(largeur*7)):
        Matrix[ordonee-4][i] = 1

    for i in range(ordonee - 4, ordonee - 4 +(hauteur*7)):
        Matrix[i][abscisse-4] = 1

    for i in range(abscisse - 4, abscisse - 4 +(largeur*7)):
        Matrix[ordonee+2+((hauteur-1)*7)][i] = 1

    for i in range(ordonee - 4, ordonee - 4 +(hauteur*7)):
        Matrix[i][abscisse+2+((largeur-1)*7)] = 1
    
    #----------------------------------------    affichage  triangle dans le rectangle du milieu ---------------------------
    #affichage GRAND triangle GAUCHE dans le rectangle du milieu
    condition = -3
    descente = 0
    while condition != -6 :
        for i in range(abscisse-2 + descente, abscisse+3 -descente) :
            Matrix[ordonee - 4 +(hauteur*7)+condition][i]=1
        condition = condition -1
        descente = descente +1

    #affichage GRAND triangle DROIT dans le rectangle du milieu
    condition = -3
    descente = 0
    while condition != -6 :
        for i in range(abscisse-11 + (largeur *7) + descente, abscisse-6 + (largeur *7) -descente) :
            Matrix[ordonee - 4 +(hauteur*7)+condition][i]=1
        condition = condition -1
        descente = descente +1

    #affichage PETIT triangle GAUCHE dans le rectangle du milieu
    condition = -3
    descente = 0
    while condition != -5 :
        for i in range(abscisse+4 + descente, abscisse+7 -descente) :
            Matrix[ordonee - 4 +(hauteur*7)+condition][i]=1
        condition = condition -1
        descente = descente +1

    #affichage PETIT triangle GAUCHE dans le rectangle du milieu
    condition = -3
    descente = 0
    while condition != -5 :
        for i in range(abscisse-15 + (largeur *7) + descente, abscisse-12 + (largeur *7) -descente) :
            Matrix[ordonee - 4 +(hauteur*7)+condition][i]=1
        condition = condition -1
        descente = descente +1
    

    liste = [abscisse - 4, abscisse - 4 +(largeur*7), ordonee - 4, ordonee - 4 +(hauteur*7)]
    
    return liste 


#######################################################################
# Place: prend la matrice et ça taille et rajoute les info indicant 
#        l'orientation et la taille des triangles
#
#En entree: liste(Matrix), int(n)
#
#En sortie: void()
#######################################################################
def addPosition(Matrix, n):
    G, P = position(n)
    G2, P2 = position(n)
    P2.reverse()
    G2.reverse()


    for g in G:
        Matrix.append(g)
    for p in P:
        Matrix.append(p)

    
    for g in G2:
        Matrix.insert(0, g)
    for p in P2:
        Matrix.insert(0, p)


#######################################################################
# Place: prend le mot et ça taille qu'on veut representer en photo et apres
#        d'avoir appliquer le protocol elle l'affiche
#        et aussi un boolean True pour faire le cadre pour le logo ou False
#
#En entree: string(mots), int(n), bool(pic)
#
#En sortie: void()
#######################################################################
def HALcode(mots, n, pic=False):
    Matrix = [[0 for x in range(n)] for y in range(n)] 
    motEnBits = stringToBits(mots)
    addInfoG(motEnBits, mots)
    if pic:
        restriction = logo(Matrix, n)
        parcourirAvecLogo(Matrix, n, motEnBits, restriction)
    else:
        parcourirSansLogo(Matrix, n, motEnBits)
    
    petitTriangle.addToMatrix(Matrix, mots, n)
    addPosition(Matrix, n)
    afficher(Matrix)


#######################################################################
# Place: prend en paramettre la matrice et l'afficher et on peut rajouter 
#        3 valeurs pour les couleur 3 valeur entre 0. et 1.
#
#En entree: liste(Matrix), int(c1, c2, c3)
#
#En sortie: void()
#######################################################################
def afficher(Matrix, c1=0., c2=0., c3=0.):
    for line in Matrix:
        for i in range(len(line)):
            if line[i] == 0:
                line[i] = (1., 1., 1.)
            else:
                line[i] = (c1, c2, c3)

    image1 = np.asarray(Matrix)

    plt.imshow(image1, interpolation="none")
    plt.axis('off')
    plt.show()


######################        MAIN      ###############################
if __name__ == '__main__':

    #introduiser le msg souhaiter de en transformer en protocol
    msg = "Created By: Hadi, Alexis, and Lamine"
    pic = 0
    
    #point(56)

    if pic:
        n = tailleAvecLogo(msg)
    else:
        n = tailleSansLogo(msg)

    HALcode(msg, n, pic)
