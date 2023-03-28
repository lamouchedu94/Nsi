def selection_enclos(table, num) :
    res = []
    for animaux in table :
        if animaux['enclos'] == num :
            res.append(animaux)
    return res

animaux = [ {'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2},
{'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5},
{'nom':'Tom', 'espece':'chat', 'age':7, 'enclos':4},
{'nom':'Belle', 'espece':'chien', 'age':6, 'enclos':3},
{'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]
print(selection_enclos(animaux, 5))
assert selection_enclos(animaux, 5) == [{'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5}, {'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]
assert selection_enclos(animaux, 2) == [{'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2}]
assert selection_enclos(animaux, 7) == []

def trouver_intrus(tab, g,d):
    '''
    Paramètres : 
        - tab un tableau de nombres dont tous les éléments sont présents exactement 3 fois à la suite sauf un élément qui est présent une unique fois.
        - g et d sont des entiers multiples de 3.
    '''
    if g == d :
        return ...
    else : 
        nombre_de_triplets = (d-g) // ...
        indice = g + 3 * (nombre_de_triplets // 2)
        if ... :
            return ...
        else : 
            return ... 