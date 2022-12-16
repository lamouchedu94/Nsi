# -*- coding: utf-8 -*-
 
def read(name) :
    with open(name, "r") as file :
        data = file.readlines()
        file.close()
    return data
 
 
def tab_mot(ligne) :
    i=0
    res = ""
    tab = []
    for l in ligne :
        for car in l :    
            if car != "," and car != " ":
               res+=car
               if not car.isdecimal() and car != "_" :
                   i+=1
            else :
               if len(res) > 0 :
                   res = str(i) + "_" + res
                   tab.append(res)
                   res = ""
                   i=0
    res = str(i) + "_" + res
    tab.append(res)
    return tab
 
def conv_int(mot):
    res = ""
    for car in mot :
        if car.isdecimal() :
            res+= car
        else :
            return int(res)
 
def tri_num(tab):
 
    #tri nombres
    triee=False
    nb_tries=0
    while not triee:
        triee=True
        for i in range(len(tab)-nb_tries-1):
            if conv_int(tab[i])>conv_int(tab[i+1]):
                tab[i],tab[i+1]=tab[i+1],tab[i]
                triee=False
 
        nb_tries+=1 
    return None
 
def tri_lettre(tab):
    for j in range(len(tab)-1):
        for i in range(j, len(tab)-1) :
            if conv_int(tab[i]) == conv_int(tab[i+1]):
                #si le 2 plus grand
                if not mot_plus_petit(tab[i], tab[i+1]) :
                    tab[i],tab[i+1]=tab[i+1],tab[i]
    return None
 
def mot_plus_petit(mot1,mot2):
    #True si mot1 plus petit
    for i in range(len(mot1)):
        if ord(mot1[i])>ord(mot2[i]):
            return False
    return True
 
print(mot_plus_petit("6", "7_azerty")) 
 
mot = read("test1.txt")
#print(read("test.txt"))
tab = tab_mot(mot)
print(tab)
tri_num(tab)
tri_lettre(tab)
#print(tri(tab))
print(tab)