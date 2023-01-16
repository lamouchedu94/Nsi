def nb_arbre(nb_noeuds):
    if nb_noeuds <= 1 :
        return 1
    res = 0
    for g in range(nb_noeuds) :
        res += nb_arbre(g)*nb_arbre(nb_noeuds-g-1)
    return res

print(nb_arbre(10))

class Noeud :
    def __init__(self, v,gauche=None, droite= None):
        self.v = v
        self.g = gauche
        self.d = droite


arbre = Noeud(1, Noeud(2, None, Noeud(4)), Noeud(3, Noeud(5), None))

def prefix(arbre, val):
    arbre.v

prefix(arbre)

"""
12345 pre
24153 in
42531 post
"""