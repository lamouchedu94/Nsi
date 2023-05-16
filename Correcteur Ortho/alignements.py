# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def alignt(mot1,mot2,memo=None):
    if memo==None:
        memo={}
    if (mot1,mot2) in memo:
        return memo[(mot1,mot2)]
    if len(mot1)==0:
        memo[(mot1,mot2)]=-len(mot2)
        return -len(mot2)
    if len(mot2)==0:
        memo[(mot1,mot2)]=-len(mot1)
        return -len(mot1)
    v1=alignt(mot1[:-1],mot2[:-1],memo)
    if mot1[-1]==mot2[-1]:
        s=1
    else:
        s=-1
    v1=v1+s
    v2=alignt(mot1,mot2[:-1],memo)-1
    v3=alignt(mot1[:-1],mot2,memo)-1
    memo[(mot1,mot2)]=max(v1,v2,v3)
    return max(v1,v2,v3)

def alignement(mot1,mot2):
    if len(mot1)==0:
        return -len(mot2)
    if len(mot2)==0:
        return -len(mot1)
    v1=alignement(mot1[:-1],mot2[:-1])
    if mot1[-1]==mot2[-1]:
        s=1
    else:
        s=-1
    v1=v1+s
    v2=alignement(mot1,mot2[:-1])-1
    v3=alignement(mot1[:-1],mot2)-1
    return max(v1,v2,v3)

def alignement2(mot1, mot2, dico=None) :
    if dico == None : 
        dico = {}
    if len(mot1) == 0:
        return -len(mot2),'-'*len(mot2),mot2
    if len(mot2) == 0:
        return -len(mot1),mot1,'-'*len(mot1)
    score = 1 
    if mot1[-1] != mot2[-1]:
        score = -1
    if not (mot1[:-1],mot2[:-1]) in dico:
        dico[(mot1[:-1],mot2[:-1])] =  alignement2(mot1[:-1],mot2[:-1],dico)
    v1 = dico[(mot1[:-1],mot2[:-1])]
    if not (mot1[:-1],mot2) in dico:
        dico[(mot1[:-1],mot2)] = alignement2(mot1[:-1],mot2,dico)
    v2 = dico[(mot1[:-1],mot2)]
    if not (mot1,mot2[:-1]) in dico:
        dico[(mot1,mot2[:-1])] = alignement2(mot1,mot2[:-1],dico)
    v3 = dico[(mot1,mot2[:-1])]
    
    if v1[0]+score >= v2[0]-1 and v1[0]+score >= v3[0]-1:
        maxi = 1
    elif v2[0] > v3[0] and v2[0]-1 >= v1[0]+score:
        maxi = 2
    else:
        maxi = 3
    if maxi == 1:
        return v1[0]+score , v1[1]+mot1[-1] , v1[2]+mot2[-1]
    elif maxi == 2:
        return v2[0]-1,v2[1]+mot1[-1], v2[2]+'-'
    return v3[0]-1, v3[1]+'-', v3[2]+mot2[-1]

print(alignement2("enorme","genome"))