# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Triplet :
    def __init__(self, score, mot1, mot2) :
        self.score = score
        self.mot1 = mot1
        self.mot2 = mot2
    def __le__(self, triplet):
        return self.score <= triplet.score
    def __lt__(self, triplet) :
        return self.score < triplet.score
    def __str__(self):
        return self.mot1 + self.mot2 + str(self.score)

def alignt(mot1, mot2, sc,tab, test):
    
    if len(mot1) == 0 :
        return -len(mot2)
    if len(mot2) == 0:
        return -len(mot1)
    
    temp = 0
    if mot1[len(mot1)-1] == mot2[len(mot2)-1] :
        temp = 1 
        print(mot1,mot2)
    else :
        temp = -1
    t = Triplet(sc, mot1, mot2)
    tab.append(t)
    return max(alignt(mot1[:-1], mot2[:-1], sc, tab)+temp, alignt(mot1[:-1], mot2, sc, tab)+temp, alignt(mot1, mot2[:-1], sc, tab)+temp )
tab = []
print(alignt("GENOME","ENORME",0, tab, ""))


