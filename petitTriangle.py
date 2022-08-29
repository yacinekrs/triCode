import Hamming
import protocol

#######################################################################
# Place:  dessin un triangle dans l'array donneé en presisant
#        les indices et le sens du triangle
#        0 = bas, 1 = haut
#
#En entree: array(Matrix), int(i), int(j), int(sens)
#
#En sortie: array(arr)
#######################################################################
def petitTrangle(arr, i, j, sens):
    if sens == 0:
        arr[i][j] = arr[i][j-1] = arr[i][j+1]   = arr[i+1][j]   = 1
    if sens == 1:
        arr[i][j] = arr[i+1][j] = arr[i+1][j+1] = arr[i+1][j-1] = 1
    elif sens != 0 & sens != 1: 
        print("erreur de sens!!!!!!\nsens invalide")
    return arr


#######################################################################
# Place:  prend un array et ça taille et rajoute 2 ligne de zeros
#
#En entree: array(mat), int (n)
#
#En sortie: void()
#######################################################################
def add2Lines(mat, n):
    l2 = [[0 for x in range(n)] for y in range(2)]
    mat.append([0 for x in range(n)] )
    mat.append([0 for x in range(n)] )


#######################################################################
# Place: prend une chaine de caracteres sous forme d'array de bits et 
#       rajoute les bits de parité correctement et renvoie un array
#       contenant les bits du msg avec les bits de parité
#
#En entree: array(data)
#
#En sortie: array(data)
#######################################################################
def toHamming(data):
    Ham = []
    for d in data:
        Ham.append(Hamming.HammingUnOctet(d))
    return Ham


#######################################################################
# Place: prend un array et le divise en deux moitié et renvoie 2 array
#
#En entree: array(Ham)
#
#En sortie: array(Moitier_1), array(Moitier_2)
#######################################################################
def toSplit(Ham):
    Moitier_1 = []
    Moitier_2 = []
    for i in range(0, len(Ham)//2):
        for bit in Ham[i]:
            Moitier_1.append(bit)

    for i in range(len(Ham)//2, len(Ham)):
        for bit in Ham[i]:
            Moitier_2.append(bit)
            
    return Moitier_1, Moitier_2


#######################################################################
# Place:   prend 2 array de bits et rajoute l'octet d'arrete et les 2 
#           octets de taille 
#
#En entree: array(M1), array(M2), string(mot)
#
#En sortie: void()
#######################################################################
def addInfo(M1, M2, mot):
    for i in range(12):
       M1.append(0)
       M2.append(0)
    tmp = protocol.taillToBits(len(mot))
    for t in tmp:
        M1.append(t)
        M2.append(t)
    
    ##################faut rajouter les 2 octets de taille du msg######################### 


# commence içi la fonction qui rempli l'array des petit triangle

#######################################################################
# Place:  prend un array et ça taille creer un array de la taille donneé 
#         et dessin des petit triangles 
#
#En entree: array(moitier), int(n)
#
#En sortie: array(pix)
#######################################################################
def HamToTriangle(Moitier, n):
    pix = []
    add2Lines(pix, n)

    if n %2 == 0:
        end = n - 1
    else:
        end = n - 2

    i = 0
    j = 1
    indiceBit = 0
    sens = 0

    while indiceBit < len(Moitier):
        if j >= end:
            add2Lines(pix, n)
            i += 2
            j = 1
        if Moitier[indiceBit] == 1:
            petitTrangle(pix, i, j, sens)
        sens = abs(sens - 1)
        indiceBit += 1
        j += 2
    return pix


#######################################################################
# Place:  prend un array qu'on veut lui rajouter le msg avec les bits de
#        parité (petit triangles)
#
#En entree: 
#
#En sortie:
#######################################################################
def addHamToPic(Matrix, M1, M2):
    for m in M1:
        Matrix.insert(len(Matrix), m)
    M2.reverse()
    for m in M2:
        Matrix.insert(0, m)


#######################################################################
# Place: prend la matrice qu'on veut lui rajouter le hamming , ça taille 
#       et le mot change le mot en bit , ensuite on lui rajout les bit de
#        parité on le coupe en 2 et on mets la premier moitier en bas et 
#       la deuxieme en haut
#
#En entree: array(Matrix), string(mot), int(n)
#
#En sortie: void()
#######################################################################
def addToMatrix(Matrix, mot, n):
    motEnBit = protocol.stringToBits(mot)
    Ham = toHamming(motEnBit)
    Moitier_1 ,Moitier_2 = toSplit(Ham)
    addInfo(Moitier_1, Moitier_2, mot)
    M1 = HamToTriangle(Moitier_1, n)
    M2 = HamToTriangle(Moitier_2, n)
    addHamToPic(Matrix, M1, M2)

if __name__ == '__main__':
    n = 56
    Matrix = [[0 for x in range(n)] for y in range(n)] 
    test = "abcdefghijklmnopqrstuvwxyz"
    #print(protocol.taillToBits(len(test)))
    '''
    Ham = toHamming(test)
    Moitier_1 ,Moitier_2 = toSplit(Ham)
    print(Moitier_2)
    addInfo(Moitier_1, Moitier_2)

    M1 = HamToTriangle(Moitier_1)
    M2 = HamToTriangle(Moitier_2)

    addHamToPic(Matrix, M1, M2)
    '''
    addToMatrix(Matrix, test, n)
    protocol.afficher(Matrix)
