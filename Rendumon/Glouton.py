"""def rendu(monnaie, somme):

    if somme in monnaie :
        return 1
    return 1+min([rendu(monnaie, somme-monnaie[i]) for i in range(len(monnaie)) if somme-monnaie[i]>0])

print(rendu(monnaie,1))"""
monnaie = [1,2,5,10,20]
def rendu_mon(somme, res):
    if somme in monnaie:
      res.append(somme)
      return res
    piece=0
    for i in range(len(monnaie)):
        if somme-monnaie[i]>0:
            piece=i
    res.append(monnaie[piece])
    return rendu_mon(somme-monnaie[piece], res)

def rendu(somme):
    return rendu_mon(somme,[])

#print(rendu(19))


def rendu_memo(somme):
    rendu =[None, [1]] + [None for _ in range(somme-1)]
    for i in range(2,somme+1) :
        if i in monnaie :
            rendu[i]=[i]
        else :
            mini = somme+11254
            for j in range(len(monnaie)):
                if i-monnaie[j]>0 and len(rendu[i-monnaie[j]]) < mini:
                    mini = len(rendu[i-monnaie[j]])
                    rendu[i]=rendu[i-monnaie[j]+monnaie[j]]
    return rendu[somme]

#print(rendu_memo(19))


def rendu_monnaie(monnaie,somme):
    rendu=[None,[1]]+[None for _ in range(somme-1)]
    for som in range(2,somme+1):
        if som in monnaie:
            rendu[som]=[som]
        else:
            mini=somme+1
            for i in range(len(monnaie)):
                if som-monnaie[i]>0 and len(rendu[som-monnaie[i]])<mini:
                    mini=len(rendu[som-monnaie[i]])
                    rendu[som]=rendu[som-monnaie[i]]+[monnaie[i]]
    return rendu[somme]
 
print(rendu_monnaie([11,10,1], 1254))