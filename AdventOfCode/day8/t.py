def read(nomfichier):
    file= open(nomfichier, 'r')
    ligne = file.readlines()
    return ligne

foret = read('input.txt')

print(foret[0])

def arbre_visible_droite(ligne,position_arbre):
    #bon
        arbres_visibles=False
        cpt=1
        for i in range(position_arbre,len(ligne)-1):
            if ligne[position_arbre]>ligne[i+1]:
              cpt+=1
        if cpt==len(ligne)-position_arbre:
            arbres_visibles=True
        return arbres_visibles

def arbre_visible_gauche(ligne,position_arbre):
    #bon
    arbres_visibles=False
    cpt=0
    for i in range(position_arbre):
        if ligne[position_arbre]>ligne[i]:
          cpt+=1
    if cpt==position_arbre:
        arbres_visibles=True
    return arbres_visibles

def arbre_visible_haut(foret,x,y):
    arbre_visible=False
    cpt=0
    for i in range(y):
        print(foret[i][x])
        if foret[y][x]>foret[i][x]:
            cpt+=1
        if  cpt==y:
            arbre_visible=True
    return  arbre_visible

def arbre_visible_bas(foret,x,y):
    arbre_visible=False
    cpt=0
    for i in range(y+1,len(foret)):
        print(foret[i][x])
        if int(foret[y][x])>int(foret[i][x]):
            cpt+=1
        if  cpt==(len(foret)-1)-y:
            arbre_visible=True
    return  arbre_visible
print(foret[2][0])
print(arbre_visible_bas(foret, 0, 2))