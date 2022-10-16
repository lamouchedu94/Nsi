def fusion(l1, l2):
    #res = [0 for i in range(len(l1)+len(l2))]
    res = []
    curs1 = 0
    curs2 = 0
    while curs1 < len(l1) and curs2 < len(l2):
        if l1[curs1] < l2[curs2] :
            res.append(l1[curs1])
            curs1 += 1 
        else :
            res.append(l2[curs2]) 
            curs2 +=1 
    
    if curs1 == len(l1) and curs2 < len(l2):
        for i in range(curs2, len(l2)):
            res.append(l2[i])
    if curs2 == len(l2) and curs1 < len(l1):
        for i in range(curs1, len(l1)):
            res.append(l1[i])  

    return res

print("doit afficher [1,2,4,5] :", fusion([2,5],[1,4]))
print("doit afficher [1,4] :", fusion([],[1,4]))
print("doit afficher [2,5] :", fusion([2,5],[]))
print("doit afficher [2,2,5,5,7,7,8,8,9] :", fusion([2,5,7,8,9],[2,5,7,8]))
print("doit afficher [] :", fusion([],[]))
print("doit afficher [1,2,4,5,7,13,64] :", fusion([2,5,7,13,64],[1,4]))
