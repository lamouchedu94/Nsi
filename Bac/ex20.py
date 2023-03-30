def ajoute_dictionnaires(d1, d2) :
    """
    Paramètres : Deux dictionnaires dont les clés sont des nombres
    Revoi : La fusion des deux dictionnaires     
    """
    res = {}
    for val in d1 :
        res[val] = d1[val]
        if val in d2 :
            res[val] += d2[val]
    for val in d2 :
        if val not in res :
            res[val] = d2[val]
    return res
    

assert ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}) == {1: 5, 2: 16, 3: 11}
assert ajoute_dictionnaires({}, {2: 9, 3: 11}) == {2: 9, 3: 11} 
assert ajoute_dictionnaires({2: 9, 3: 11}, {}) == {2: 9, 3: 11}
assert ajoute_dictionnaires({1: 5, 2: 7}, {2 : 2}) == {1: 5, 2: 9}

from random import randint
def nbre_coups():
    """
    Aucun paramètre
    Renvoi : Nombre de lancers aléatoires nécessaires pour terminer le jeu.  
    """
    n = 0
    cases_vues = [0]
    case_en_cours = 0
    nbre_cases = 12
    while len(cases_vues) < nbre_cases:
        x = randint(1, 6)
        case_en_cours = (case_en_cours + x) % 12
        if case_en_cours not in cases_vues :
            cases_vues.append(case_en_cours)
        n = n + 1 
    return n

print(nbre_coups())