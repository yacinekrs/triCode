
#######################################################################
# Place: rajoute les bits de parité a la sequence de bit qu'on a .
#        initial les bits de parité a 0 et r est le nb de bits de redondance
#
#En entree: array(data), int(r)
#
#En sortie: array(res)
#######################################################################
def Hamming(data, r):
    data = data[::-1]
    j = 0
    k = 1
    m = len(data)
    res = [0 for x in range(r+1)]

    for i in range(1, r+1):
        if i == 2**j:
            j += 1
        else:
            res[i] = data[-1 * k]
            k += 1
    return res[1:]


#######################################################################
# Place: transforme les bits de parité a 1 ou 0 ça depend de ce qu'est 
#        besoin et renvoie l'array modifier
#
#En entree: array(data), int(r)
#
#En sortie: array(data)
#######################################################################
def calculePariteUnOctet (data, n):
    m  = sum(data)
    n2 = 2**(n-1)
    line   = 0

    mat = [[0 for x in range(n)] for y in range(m)]

    for bit in range(len(data)):
        column = 0
        if data[bit] == 1:
            tmp = bit + 1
            for i in range(n):
                if tmp >= n2 :
                    tmp -= n2
                    mat[line][column] = 1
                column += 1
                n2 /= 2
            line += 1
            n2 = 8
    for j in range(n):
        somme = 0
        for i in range(m):
            somme += mat[i][j]
        if somme%2 != 0:
            data[int(n2)-1] = 1
        n2 /= 2
    return data


#######################################################################
# Place: prend un array de bits et rajoute les bits de parité correctement
#       et renvoie l'array modifier
#
#En entree: array(data)
#
#En sortie: array(data)
#######################################################################
def HammingUnOctet(data):
    #le transforme en hamming avec des valeur predifinie(qui correspond a notre programme)
    return calculePariteUnOctet(Hamming(data, 12), 4)

if __name__ == '__main__':

    test = [1,1,1,0,1,0,1,1]
    #print(HammingUnOctet(test))
    test = Hamming(test, 12)
    print(test)
    #on met 4 car pour 1 octet on a besoin de 4 bit de redondence
    test = calculePariteUnOctet(test, 4)
    print(test)