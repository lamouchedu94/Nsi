import math
def occurence(chaine) :
    dico = {}
    for car in chaine :
        if car in dico :
            dico[car] += 1
        else : 
            dico[car] = 1
    return dico
print(occurence("aaabccd"))

class Noeud :
    def __init__(self, v, g, d) :
        self.v = v
        self.g = g
        self.d = d


dico = occurence("aaabccdeeeee")
liste_Noeud = []

def plus_petit(dico) :
    res = []
    while len(dico) > 0 :
        min = math.inf
        car_min = ""
        for occu in dico :
            if dico[occu] < min :
                min = dico[occu]
                car_min = occu
        res.append((car_min, dico[car_min]))
        del(dico[car_min])
    
    return res

def arbre(tab):
    lnoeud = []
    for i in range(0,len(tab), 2) :
        n = Noeud
        n.g = tab[i]
        if len(tab)%2 == 0 :
            n.d = tab[i+1]
            n.v = tab[i][1] + tab[i+1][1]
        else :
            n.d = None
            n.v = tab[i][1]
        lnoeud.append(n)

tab = plus_petit(dico)
arbre(tab)