def tri_insertion(liste : list) :
    test = []
    
    for i in range(1,len(liste)-1):
        nb = liste[i]
        
        indice = i
        while indice > 0 and liste[indice-1] > nb :
            liste[indice] = liste[indice - 1]
            indice -= 1
        liste[indice] = nb
        test.append(nb)
    return None


l1 = [2,5,3,6,1,9]
tri_insertion(l1)
print(l1)