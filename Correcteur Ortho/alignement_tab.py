def alignement_dyn(mot1, mot2):
    scores=[[0]*(len(mot2)+1) for _ in range(len(mot1)+1)]
    for i in range(len(mot1)+1):
        scores[i][0]=-i
    for j in range(len(mot2)+1):
        scores[0][j]=-j
    for i in range(1,len(mot1)+1):
        for j in range(1,len(mot2)+1):
            if mot1[i-1] == mot2[j-1]:
                ajout=1
            else :
                ajout=-1
            scores[i][j]=max(scores[i-1][j]-1, scores[i][j-1]-1, scores[i-1][j-1]+ajout)
    return scores

def aff(tab):
    for ligne in tab :
        print(ligne)

#aff(alignement_dyn("genome","enorme"))

def retrouver_mot(mot_base1,mot_base2 ):
    tab_s = alignement_dyn(mot_base1, mot_base2)
    curs1 = len(tab_s)-1
    curs2 = len(tab_s[0])-1
    last_sc = tab_s[curs1][curs2]
    mot1 = ""
    mot2 = ""
    while curs1 >0 or curs2 > 0 :
        if tab_s[curs1][curs2-1] == last_sc + 1:
            mot2 = mot_base2[curs2-1]  + mot2
            mot1 = "_" + mot1
            curs2 -= 1
        elif tab_s[curs1-1][curs2] == last_sc + 1:
            mot1 = mot_base1[curs1-1] + mot1
            mot2 = "_" + mot2
            curs1 -= 1
        else :
            mot1 = mot_base1[curs1-1] + mot1
            mot2 = mot_base2[curs2-1] + mot2
            curs1 -= 1 
            curs2 -= 1 

        last_sc = tab_s[curs1][curs2]
        if curs1 == 0 and curs2 != 0 :
            mot2 = mot_base2[0:curs2] + mot2
            mot1 = "_"*curs2 + mot1
            return mot1, mot2,tab_s[len(tab_s)-1][len(tab_s[0])-1]
        elif curs2 == 0 and curs1 != 0 :
            mot1 = mot_base1[0:curs1] + mot1
            mot2 = "_"*curs1 + mot2
            return mot1, mot2,tab_s[len(tab_s)-1][len(tab_s[0])-1]
        
    return mot1, mot2, tab_s[len(tab_s)-1][len(tab_s[0])-1]

res = retrouver_mot("enorme","genome")
print(res[0])
print(res[1])
print(res[2])
