def conv(tab):
    i = len(tab)-1
    res = 0
    for nb in tab :
        res += nb * 2**i
        i-= 1
    return res
print(conv([1,0,1]))

def tri_insertion(tab):
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i]
        # la variable j est utilisée pour déterminer où placer la valeur à insérer
        j = i
        # tant qu'on a pas trouvé la place de l'élément à insérer
        # on décale les valeurs du tableau vers la droite
        while j > 0 and valeur_insertion < tab[j-1]:
            tab[j] = tab[j-1]
            j = j - 1
        tab[j] = valeur_insertion
liste = [2,10,17,28,12,3,6]
tri_insertion(liste)
print(liste)