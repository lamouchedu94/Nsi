def max_et_indice(tab) :
    max = tab[0]
    i_max  = 0
    for i in range(len(tab)) :
        if tab[i] > max :
            max = tab[i]
            i_max = i 
            #return (max, )
    return (max, i_max)

print(max_et_indice([1,7,9,3]))
assert max_et_indice([1,7,9,3]) == (9, 2)
assert max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, 3)
assert max_et_indice([-2]) == (-2, 0)

def est_un_ordre(tab):
    '''
    Renvoie True si tab est de longueur n et contient tous les
    entiers de 1 à n, False sinon
    '''
    for i in range(1,len(tab)-1):
        if i not in tab :
            return False
    return True
def nombre_points_rupture(ordre):
    '''
    Renvoie le nombre de point de rupture de ordre qui représente
    un ordre de gènes de chromosome
    '''
    assert est_un_ordre(ordre) # ordre n'est pas un ordre de gènes
    n = len(ordre)
    nb = 0
    if ordre[0] != 1: # le premier n'est pas 1
        nb = nb + 1
    i = 0
    while i < len(ordre)-1:
        if (ordre[i+1]- ordre[i]) not in [-1, 1]: # l'écart n'est pas 1
            nb = nb + 1
        i = i + 1
    if ordre[len(ordre)] != n: # le dernier n'est pas n
        nb = nb + 1
    return nb

print(est_un_ordre([1, 6, 2, 8, 3, 7]))
print(est_un_ordre([5, 4, 3, 6, 7, 2, 1, 8, 9]))