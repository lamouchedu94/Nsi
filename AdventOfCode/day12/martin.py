def read(car="Z"):
    with open('input', 'r') as f:
        doc = f.readlines()
        tab = [[car] + [c for c in ligne if c != '\n'] + [car] for ligne in doc]
        tab.insert(0, [car for _ in range(len(doc[0])+1)])
        tab.append([car for _ in range(len(doc[0])+1)])
    return tab

def autour(tab,position):
    rep = [None]*4
    curs = 0
    for i in range(-1,2,2):
        rep[curs] = tab[position[0]+i][position[1]]
        rep[curs+1] = tab[position[0]][position[1]+i]
        curs += 2
    return rep

def minimum(tab):
    tab.sort()
    curs = 0
    while tab[curs] < 0:
        curs += 1
    return tab[curs]

def test(tab):
    if len(tab) == 0:
        return False
    return max(tab) != -1

deplacement = ((-1,0), (0,-1), (1,0), (0,1))
def chemin(carte, position, nbr_mouvement, deja_passe): 
    deplacement_pos = autour(carte,position)
    deja_passe.append(position)
    rep = []
    if 'E' in deplacement_pos and ord(carte[position[0]][position[1]]) >= 121:
        return nbr_mouvement+1
    for i in range(4):
        if abs(ord(deplacement_pos[i])-ord(carte[position[0]][position[1]])) <= 1:
            n_pos = (position[0]+deplacement[i][0], position[1]+deplacement[i][1])
            if not n_pos in deja_passe:
                rep.append(chemin(carte, n_pos, nbr_mouvement+1, deja_passe[:]))
    return minimum(rep) if test(rep) else -1

carte = read()
print(chemin(carte, (1,1), 0, []))