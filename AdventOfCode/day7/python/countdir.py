def count(f) :
    alldir = []
    count = 0 
    for ligne in f.readlines():
        if "dir" in ligne :
            if ligne in alldir :
                count += 1
            alldir.append(ligne)
    f.close()
    return alldir, count
a,b = count(open("input1.txt"))
#print(b, "répétitions")

class repertoire :
    def __init__(self, nom) :
        self.n_subrep=[]
        self.n_fichier = []
        self.nom = nom
        return None
    def name(self) :
        return self.nom



def doublons(f) :
    with open(f, "r") as fichier :
        lignes=[ligne[:-1] for ligne in fichier.readlines()]
    vu={}
    arbre={'/': repertoire("/")}
    for ligne in lignes :
        if ligne[:3]=='dir' :
            nomdossier = ligne[4:]
            if nomdossier in vu :
                vu[nomdossier] += 1
            else :
                vu[nomdossier] = 1
            nomdossier=nomdossier+str(vu[nomdossier])
            arbre[nomdossier] = repertoire(nomdossier)
        if ligne[0].isnumeric():
            curs=0
            while ligne[curs].isnumeric():
                curs+=1
            arbre[nomdossier].n_fichier.append([ligne[curs+=1], int(ligne[curs])])
    return dossiers
v =doublons("input1.txt") 
print(v)


