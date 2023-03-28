def recherche_min(l):
    '''
    Paramètre : liste de nombre
    renvoi : l'indice de la première occurrence du minimum de ce tableau. Si liste vide, renvoi None
    '''
    if l == [] :
        return None
    min = l[0]
    i_min = 0
    for i in range(len(l)):
        if l[i] < min :
            min,i_min = l[i], i
    return i_min

assert recherche_min([2, 4, 1]) == 2
assert recherche_min([]) == None
assert recherche_min([5]) == 0

print("Doit afficher 2 :",recherche_min([5, 3, 2, 2, 4])) 
            
def separe(tab):
    gauche = 0
    droite = len(tab)-1
    while gauche < droite :
        if tab[gauche] == 0 :
            gauche = gauche + 1 
        else : 
            tab[gauche], tab[droite] = tab[droite], tab[gauche]
            droite = droite - 1
    return tab

assert separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]) ==  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert separe([0,0,1,1]) == [0,0,1,1]
print(separe([1, 0, 1, 0, 1, 0, 1, 0]))
