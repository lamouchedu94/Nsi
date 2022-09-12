def tri(liste):
    for i in range(1,len(liste)-1):
        nb = liste[i]
        indice = i
        while indice > 0 and liste[indice-1]>nb :
            liste[indice]= liste[indice -1]
            indice -=1
        liste[indice] = nb 

l1 = [2,5,3,6,1,9]
tri(l1)