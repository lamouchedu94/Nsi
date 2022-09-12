
import math

def tri_bulles(liste):
    """
    trie sur place la liste passée en paramètre en utilisant l'algorithme du tri à bulles'
    paramètre: liste de nombres
    retourne: None
    """
    triee=False
    nb_tries=0
    while not triee:
        triee=True
        for i in range(len(liste)-nb_tries-1):
            if liste[i]>liste[i+1]:
                liste[i],liste[i+1]=liste[i+1],liste[i]
                triee=False
        nb_tries+=1
    return None

def tri_selec(liste):
    """
    paramètre: liste de nombres
    retourne: copie triée de la liste passée en paramètre en utilisant l'algorithme du tri par selection
    """
    triee=[0 for i in range(len(liste))]
    curs=0
    lastmin=-math.inf
    while curs<len(liste):
        mini=math.inf
        for i in range(len(liste)):
            if liste[i]<mini and liste[i]>lastmin:
                mini=liste[i]
        cpt=0
        for i in range(len(liste)):
            if liste[i]==mini:
                cpt+=1
        for i in range(curs,curs+cpt):    
            triee[i]=mini
        curs+=cpt
        lastmin=mini
    return triee

def tri_selec_sur_place(liste):
    curs=0
    while curs<len(liste):
        mini=liste[curs]
        ind_mini=curs
        for i in range(curs,len(liste)):
            if liste[i]<mini:
                mini=liste[i]
                ind_mini=i
        liste[curs],liste[ind_mini]=liste[ind_mini],liste[curs]
        curs+=1
    return None

def triinsert(liste):
    triee=[-math.inf for i in range(len(liste))]
    for i in range(len(liste)-1):
        curs=0
        while liste[i]<triee[curs]:
            curs+=1
        for j in range(len(triee),curs+1,-1):
            triee[j]=triee[j-1]
        triee[curs]=liste[i]
    return None

l1 = [4,6,1,2]
triinsert(l1)
print(l1)