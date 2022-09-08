# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

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
    indice_trie=0
    while liste!=[]:
        mini=liste[0]
        ind=0
        for i in range(len(liste)):
            if liste[i]<mini :
                mini=liste[i]
                ind = i
        triee[indice_trie] = mini 
        indice_trie +=1
        liste.pop(ind)
        
    return triee


def tri_selec2(liste):
    """
    paramètre: liste de nombres
    retourne: copie triée de la liste passée en paramètre en utilisant l'algorithme du tri par selection
    """
    triee=[0 for i in range(len(liste))]
    cpt=0
    lastmin=-math.inf
    while liste!=[]:
        mini=liste[0]
        ind=0
        for i in range(len(liste)):
            if liste[i]<mini and liste[i]>=lastmin:
                mini=liste[i]
                ind = i
        cpt1=0
        for i in range(len(liste)):
            if liste[i]==mini:
                cpt1+=1
        for i in range(cpt,cpt+cpt1-1):    
            triee[i]=mini
        triee[cpt] = mini
        cpt+=cpt1
        liste.pop(ind)
        lastmin=mini
        
    return triee


def tri_selec3(liste):
    """
    paramètre: liste de nombres
    retourne: copie triée de la liste passée en paramètre en utilisant l'algorithme du tri par selection
    """
    triee=[]
    cpt=0
    #lastmin=-math.inf
    while liste!=[]:
        mini=liste[0]
        ind=0
        for i in range(len(liste)):
            if liste[i]<mini :
                mini=liste[i]
                ind = i
        triee.append(mini)
        liste.pop(ind)
        
    return triee

            
        
        

l1=[1,2,3,4,5,6]
print(tri_selec(l1))
print(l1)
l2=[]
print(tri_selec(l2))
print(l2)
l3=[4,9,3,6,3,1,5]
print(tri_selec(l3))
print(l3)
l4=[2,5,1,9,3,6]
print(tri_selec(l4))
print(l4)