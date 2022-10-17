import time
def fusion(l1, l2):
    '''
    paramètre : l1, et l2 sont 2 listes triées dans l'ordre croissant
    retourne : une liste triée constitué des éléments de l1 et l2
    '''
    res = [0 for i in range(len(l1)+len(l2))]
    #res = []
    curs1 = 0
    curs2 = 0
    while curs1 < len(l1) and curs2 < len(l2):
        if l1[curs1] < l2[curs2] :
            res[curs1+curs2] = l1[curs1]
            #res.append(l1[curs1])
            curs1 += 1 
        else :
            res[curs1+curs2] = l2[curs2]
            #res.append(l2[curs2]) 
            curs2 +=1 
    
    if curs1 == len(l1) and curs2 < len(l2):
        for i in range(curs2, len(l2)):
            res[curs1+curs2] = l2[curs2]
            curs1+=1
            #res.append(l2[i])
    else : 
    #if curs2 == len(l2) and curs1 < len(l1):
        for i in range(curs1, len(l1)):
            res[curs1+curs2] = l1[curs1]
            curs1+=1
            #res.append(l1[i])  
    return res
def test1():
    print("doit afficher [1,2,4,5] :", fusion([2,5],[1,4]))
    print("doit afficher [1,4] :", fusion([],[1,4]))
    print("doit afficher [2,5] :", fusion([2,5],[]))
    print("doit afficher [2,2,5,5,7,7,8,8,9] :", fusion([2,5,7,8,9],[2,5,7,8]))
    print("doit afficher [] :", fusion([],[]))
    print("doit afficher [1,2,4,5,7,13,64] :", fusion([2,5,7,13,64],[1,4]))
 
#test1()

def fusion_rec(l1,l2,res = None, curs1 = 0 , curs2 = 0):
    if res == None : 
        res = [None for _ in range(len(l1)+ len(l2))]
    if curs1==len(l1):
        if curs2 == len(l2):         
            return res
        return res[:curs1+curs2] + l2[curs2:]
    if curs2 == len(l2) :
        return res[:curs1+curs2] + l1[curs1:]
    
    if l1[curs1]<l2[curs2]:
        res[curs1+curs2] = l1[curs1]
        return fusion_rec(l1, l2, res, curs1+1 , curs2)
    res[curs1+curs2] = l2[curs2]
    return fusion_rec(l1,l2,res,curs1, curs2+1)    

deb = time.time()
for i in range(300000):
    fusion([2,5,7,13,64],[1,3,4,11,35,52,58,61])
print(time.time()-deb)
"""
deb = time.time()
for i in range(300000):
    fusion_rec([2,5,7,13,64],[1,3,4,11,35,52,58,61])
print(time.time()-deb)
print("doit afficher [1,2,4,5] :", fusion_rec([2,5],[1,4]))
"""
 
def trifusion(liste):
    if len(liste) <= 1:
        return liste
    liste1 = trifusion(liste[0:len(liste)//2])
    liste2 = trifusion(liste[len(liste)//2:len(liste)])
    return fusion(liste1, liste2)
 
def test2():
    print("\n")
    print("doit afficher [1,2,3,4,5]:", trifusion([1,4,2,5,3]))
    print("doit afficher [1]:", trifusion([1]))
    print("doit afficher []:", trifusion([]))
    print("doit afficher [1,2,3,4,5]:", trifusion([5,4,3,2,1]))
    print("doit afficher [1,1,2,2]:", trifusion([2,2,1,1]))
 
#[1,5,7,11,2,9,31,32]
def new_fusion(l, sep):
    curs1 = 0 
    curs2 = sep+1
    #while curs1 < sep and curs2 < len(l):
    for i in range(len(l)+3):
        if l[curs1] < l[curs2] :
            curs1 += 1
        else : 
            l[curs1], l[curs2] = l[curs2], l[curs1]
            curs2 += 1
 
        print("ici")
        
    return None
l = [1,5,7,11,2,9,31,32]
#new_fusion(l, 3)
#print(l)            