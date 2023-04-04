def vlad_recu(tab, deb, fin):
    if deb >= fin :
        return None
    if tab[deb] == 1 :
        tab[fin], tab[deb] = tab[deb], tab[fin]
        return vlad_recu(tab,deb, fin-1)
    tab[fin], tab[deb] = tab[deb], tab[fin]
    return vlad_recu(tab,deb+1, fin)

tab = [0,1,0,1,1,1,0,0,0,1,1]
print(vlad_recu(tab, 0, len(tab)))