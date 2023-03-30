a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], \
'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], \
'H':['','']}
def taille(a,l):
    if l == '' :
        return 0
    return 1+ taille(a, a[l][0]) + taille(a,a[l][1])
print(taille(a,"F"))

def tri_selection(tab):
    N = len(tab)
    for k in range(N):
        imin = k
        for i in range(imin , N):
            if tab[i] < tab[imin] :
                imin = i
        tab[k] , tab[imin] = tab[imin] , tab[k]
    return None
liste = [41, 55, 21, 18, 12, 6, 25]
tri_selection(liste)
print(liste)