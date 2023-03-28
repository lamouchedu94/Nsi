def nbr_occurrences(text) :
    """
    Paramètre : chaine de caractères
    Renvoi : dictionnaire des nombres d’occurrences des
    caractères de cette chaîne
    """
    dico = {}
    for car in text :
        if car in dico :
            dico[car] += 1
        else :
            dico[car] = 1
    return dico

#print(nbr_occurrences("Hello world !"))
assert nbr_occurrences("Hello world !") == {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 2, 'w': 1,
'r': 1, 'd': 1, '!': 1}
assert nbr_occurrences("abcd") == {'a':1,'b':1, 'c':1, 'd':1}
assert nbr_occurrences("aaa") == {'a':3}
assert nbr_occurrences("") == {}

def fusion(list1, list2):
    """
    Paramètres : 2 listes d'entiers triées par oerdre croissant
    Renvoi : une liste triée de la fusion des 2 listes.
    """
    
    n1 = len(list1)
    n2 = len(list2)
    lst12 = [0] * (n1 + n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and i2 < n2 :
        if list1[i1] < list2[i2] :
            lst12[i] = list1[i1]
            i1 += 1
        else :
            lst12[i] = list2[i2]
            i2 += 1
        i+=1
    while i1 < n1 :
        lst12[i] = list1[i1]
        i1 = i1 + 1
        i = i + 1
    while i2 < n2 :
        lst12[i] = list2[i2]
        i2 = i2 + 1
        i = i + 1
    return lst12

print(fusion([1, 6, 10], [0, 7, 8, 9]))
assert fusion([1, 6, 10], [0, 7, 8, 9]) == [0,1,6,7,8,9,10]
assert fusion([4,6,9,10], [1, 3, 7, 8, 14]) == [1,3,4,6,7,8,9,10,14]
assert fusion([], []) == []