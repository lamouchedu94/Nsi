class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None

a=Arbre(1)
a.fg=Arbre(4)
a.fd=Arbre(0)
a.fd.fd=Arbre(7)

def taille(a) :
    if a == None :
        return 0
    return 1 + taille(a.fg) + taille(a.fd)

def hauteur(a):
    if a == None :
        return 0 
    return 1 + max(hauteur(a.fg), hauteur(a.fd))

print(taille(a))
print(hauteur(a))



def ajoute(indice, element, liste):
    nbre_elts = len(liste)
    L = [0 for i in range(nbre_elts + 1)]
    if indice <= nbre_elts:
        for i in range(indice):
            L[i] = liste[i]
        L[indice] = element
        for i in range(indice + 1, nbre_elts + 1):
            L[i] = liste[i-1]
    else:
        for i in range(nbre_elts):
            L[i] = liste[i]
        L[indice-1] = element
    return L

print(ajoute(4, 4, [7, 8, 9]))
assert ajoute(3, 4, [7, 8, 9]) == [7,8,9,4]
assert ajoute(4,4, [7,8,9]) == [7,8,9,4]
assert ajoute(1, 4, [7, 8, 9]) == [7,4,8,9]