def _score_mot(mot1,mot2,dico):
    if len(mot1) == 0:
        return -len(mot2),'-'*len(mot2),mot2
    if len(mot2) == 0:
        return -len(mot1),mot1,'-'*len(mot1)
    s = 1 
    if mot1[-1] != mot2[-1]:
        s = -1
    if not (mot1[:-1],mot2[:-1]) in dico:
        dico[(mot1[:-1],mot2[:-1])] =  _score_mot(mot1[:-1],mot2[:-1],dico)
    if not (mot1[:-1],mot2) in dico:
        dico[(mot1[:-1],mot2)] = _score_mot(mot1[:-1],mot2,dico)
    if not (mot1,mot2[:-1]) in dico:
        dico[(mot1,mot2[:-1])] = _score_mot(mot1,mot2[:-1],dico)
    v1 = dico[(mot1[:-1],mot2[:-1])]
    v2 = dico[(mot1[:-1],mot2)]
    v3 = dico[(mot1,mot2[:-1])]
    if v1[0]+s >= v2[0]-1 and v1[0]+s >= v3[0]-1:
            maxi = 1
    elif v2[0] > v3[0] and v2[0]-1 >= v1[0]+s:
        maxi = 2
    else:
        maxi = 3
    if maxi == 1:
        return v1[0]+s , v1[1]+mot1[-1] , v1[2]+mot2[-1]
    elif maxi == 2:
        return v2[0]-1,v2[1]+mot1[-1], v2[2]+'-'
    return v3[0]-1, v3[1]+'-', v3[2]+mot2[-1]


def score_mot(mot1,mot2):
    dico = {}
    score = _score_mot(mot1, mot2,dico)
    print('Score :', score[0])
    print(score[1])
    print(score[2])
    return None

chaine1 = 'je suis en train de tester pour voir si ca va vite'
chaine2 = 'et j espere que ca va marcher parce que je l ai bien code'
score_mot(chaine1,chaine2)