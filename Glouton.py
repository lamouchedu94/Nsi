"""def rendu(monnaie, somme):

    if somme in monnaie :
        return 1
    return 1+min([rendu(monnaie, somme-monnaie[i]) for i in range(len(monnaie)) if somme-monnaie[i]>0])

print(rendu(monnaie,1))"""
monnaie = [1,2,5,10,20,50,100,500]
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

print(rendu(19))
