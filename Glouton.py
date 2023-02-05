def rendu(monnaie, somme):

    if somme in monnaie :
        return 1
    return 1+min([rendu(monnaie, somme-monnaie[i]) for i in range(len(monnaie)) if somme-monnaie[i]>0])

monnaie = [1,2,5,10,20]
print(rendu(monnaie,1))

def solution(somme, res=None):
    if res == None :
        res = []
    if somme in monnaie:
      res.append(somme)
      return res
    tab=[]
    for i in range(len(monnaie)):
        if somme-monnaie[i]>0:
            tab.append(i)
    res.append(monnaie[len(tab)-1])
    return solution(somme-monnaie[len(tab)-1], res)

print(solution(99))