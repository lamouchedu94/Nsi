def gen_photo(long, larg) :
    res = []
    count = 0
    for _ in range(larg):
        temp = []
        for _ in range(long):
            count += 1
            temp.append(count)
        res.append(temp)
    return res

def affichage(tab):
    if tab == None :
        return
    for ligne in tab :
        print(ligne)

photo = gen_photo(3,3)
affichage(photo)

def rotation(photo):
    colone = len(photo[0])
    res = []
    for i in range(colone):
        n_ligne = []
        for j in range(len(photo) - 1, -1, -1):
            ligne = photo[j]
            n_ligne.append(ligne[i])
        res.append(n_ligne)
    return res

new = rotation(photo)
print()
affichage(new)