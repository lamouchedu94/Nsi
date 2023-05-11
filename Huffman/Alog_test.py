import math
def occurence(chaine) :
    dico = {}
    for car in chaine :
        if car in dico :
            dico[car] += 1
        else : 
            dico[car] = 1
    return dico
print(occurence("aaabccdeeeee"))

class Noeud :
    def __init__(self, frequence, gauche, droite, lettre) :
        self.frequence = frequence
        self.gauche = gauche
        self.droite = droite
        self.lettre = lettre

chaine = "this is an example of a huffman tree"
dico = occurence(chaine)

def tri(dico) :
    res = []
    while len(dico) > 0 :
        max = -math.inf
        car_min = ""
        for occu in dico :
            if dico[occu] > max :
                max = dico[occu]
                car_min = occu
        res.append((car_min, dico[car_min]))
        del(dico[car_min])
    
    return res



def n(dico):
    tab_noeud = tri(dico)
    while len(tab_noeud) > 1 :
        derniers = ((tab_noeud[-1],tab_noeud[-2]),tab_noeud[-1][1] + tab_noeud[-2][1] )
        poid_derniers = derniers[1]
        tab_noeud = tab_noeud[0:len(tab_noeud)-2]
        trouve = False
        for i in range(len(tab_noeud)):
            if poid_derniers > tab_noeud[i][1] :
                temp = tab_noeud[0:i] 
                temp.append(derniers)
                
                temp += tab_noeud[i:len(tab_noeud)]
                tab_noeud = temp
                trouve = True
                break
        if not trouve :
            tab_noeud.append(derniers)

    return tab_noeud

tab = n(dico)
print(tab[0])
def codage(noeud, res, chemin):
    if type(noeud[0]) == str :
        res[noeud[0]] = chemin
        return
    codage(noeud[0][0], res, chemin + "0") 
    codage(noeud[0][1], res, chemin + "1")

def encode(tab) :
    res = {}
    codage(tab[0], res, "")
    print(res)
    codee = ""
    for car in chaine :
        codee += res[car]
    return codee, res
codee, dico = encode(tab)
print(codee)

def decode(codee, dico) :
    enclair = ""
    while len(codee) > 0 :
        for cles in dico:
            if codee[0:len(dico[cles])] == dico[cles] :
                enclair += cles
                codee = codee[len(dico[cles]):]
    return enclair

print(decode(codee,dico))



