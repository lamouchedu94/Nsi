def depouille(urne):
    resultat = {"A":0,"B":0,"C":0}
    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            pass
    return resultat
def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax :
            nmax = election[candidat]
            vainqueur = candidat
        liste_finale = [nom for nom in election if election[nom] == vainqueur]
    return liste_finale

urne = ['A', 'A', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B']
election = depouille(urne)
print(election)
print(vainqueur(election))

#23 15 | 24 9 11 4 7 | 7 5 | 14 9 | 26 21 15 | 2 1 15 2 1 15
#  WO  |    XIANG    | GE  |  NI  |    ZUO   | B A O  B A  O

#24 9 1 14 7 | 75 |149 262115 21152115
#XIANG | GE | zuo 