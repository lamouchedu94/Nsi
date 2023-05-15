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
"""def alignt2(mot1,mot2,res1='',res2='',s=0):
    if len(mot1)==0:
        return s-len(mot2),'_'*len(mot2)+res1,mot2+res2
    if len(mot2)==0:
        return s-len(mot1),mot1+res1,'_'*len(mot1)+res2
    if mot1[-1]==mot2[-1]:
        ajout=1
    else:
        ajout=-1
    v1=1+s
        return alignt2(mot1[:-1],mot2[:-1],mot1[-1]+res1,mot2[-1]+res2)
    else:
        if alignt(mot1,mot2[:-1])>alignt(mot1[:-1],mot2):
            return alignt2(mot1, mot2[:-1],'_'+res1,mot2[-1]+res2)
        else:
            return alignt2(mot1[:-1],mot2,mot1[-1]+res1,'_'+res2)
    return None"""