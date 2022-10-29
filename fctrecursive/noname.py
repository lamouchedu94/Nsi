def nb_chemins(l,c):
    if l == 1 or c == 1 :
        return 1
    return nb_chemins(l-1, c) + nb_chemins(l, c-1)
 
print(nb_chemins(2,3))
 
def nb_chemin_memo(l,c,memo=None):
    if memo == None :
        memo = {}
    if l == 1 or c == 1 :
        return 1
    if (l,c) in memo :
        return memo[(l,c)]
    memo[(l,c)] = nb_chemin_memo(l, c-1, memo)+nb_chemin_memo(l-1, c, memo)
    return memo[(l,c)]
print(nb_chemin_memo(122, 122))
    
 
"""
Programation récursive :
Une fonction récursive est une fonction qui s'appelle elle même.
Il lui faut une condition d'arrêt. Pour démontrer le fonctionnement 
d'une fonction récursive, il faut prouver :
    - Sa terminaison c'est à dire qu'au bout d'un certain nombre 
d'appel on atteindra forcément la condition d'arrêt ou cas de base
Il suffit en général pour cela d'exiber une suite d'entier strictement 
décroissante, liée au parametre d'appel de la fonction.
    - Correction, on démontre que la fonction calcul bien ce que l'on
veut (par récurrence).
Python permet de faire des fct récurcive mais il n'est pas optimisé
pour ça. Aussi bien en terme de vitesse que de limite dans le nb d'appel
récursif.
"""