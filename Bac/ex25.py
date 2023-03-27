def enumere(liste) :
    """
    parametre : liste nombre 
    renvoi : Dictionnaire dont les clés sont les éléments de la liste avec pour valeur associée la liste des indices de l'élément dans la liste.
    """
    dico = {}
    i = 0
    for nb in liste :
        if nb in dico :
            dico[nb].append(i)
        else : 
            dico[nb] = [i]
        i+= 1
    return dico

assert enumere([1,1,2,3,2,1]) == {1: [0, 1, 5], 2: [2, 4], 3: [3]}
assert enumere([]) == {}
assert enumere([1,1,1,1,1,1]) == {1: [0,1,2,3,4,5]}
assert enumere([1,2,3,4,5]) == {1: [0], 2:[1], 3:[2], 4:[3], 5:[4]} 
print("doit afficher {1: [0, 1, 5], 2: [2, 4], 3: [3]} :",enumere([1,1,2,3,2,1])) 

class Arbre: 
    def __init__(self, etiquette) :
        self.v = etiquette
        self.fg = None
        self.fd = None
def parcours(arbre,liste) :
    if arbre != None :
        parcours(arbre.fg, liste)
        liste.append(arbre.v)
        parcours(arbre.fd, liste)
    return liste

def insere(arbre, cle):
    if  cle < arbre.v :
        if arbre.fg != None :
            insere(arbre.fg, cle)
        else : 
            arbre.fg = Arbre(cle)
    else :
        if arbre.fd != None :
            insere(arbre.fd, cle)
        else : 
            arbre.fd = Arbre(cle)
abr = Arbre(5)
abr.fg = Arbre(2)
abr.fd = Arbre(7)
'''
abr.fd.fg = Arbre(6)
abr.fd.fd = Arbre(8)
abr.fg.fg = Arbre(1)
abr.fg.fd = Arbre(3)
#abr.fg.fd.fd = Arbre(4)
'''

insere(abr, 4)
print("Doit afficher [2, 4, 5, 7] : ",parcours(abr, []))
assert parcours(abr, []) == [2, 4, 5, 7]
abr = Arbre(5)
assert parcours(abr, []) == [5]
abr = Arbre(1)
insere(abr, 2)
insere(abr, 3)
insere(abr, 4)
assert parcours(abr, []) == [1,2,3,4]