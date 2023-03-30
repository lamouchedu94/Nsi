def recherche(tab, n):
    """
    Paramètres :
        - Tablau d'entiers non vide
        - un nombre entier
    Revoi : Indice correspondant au nombre chercher si il est dans le tableau -1 sinon.
    """
    
    debut = 0
    fin = len(tab) - 1
    while debut <= fin :
        m = (fin + debut) // 2
        if tab[m] == n :
            return m 
        if n > tab[m] :
            debut = m + 1
        else :
            fin = m - 1
    return -1 

assert recherche([1, 2, 3, 4, 5, 6], 5) == 4
assert recherche([2, 3, 4, 6, 7], 5) == -1
assert recherche([1, 2, 3, 6, 8, 10], 1) == 0
assert recherche([1, 2, 3, 4, 5, 6], 6) == 5

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def position_alphabet(lettre):
    return ord(lettre) - ord('A')
def cesar(message, decalage):
    """
    Paramètres : 
        - Une chaine de caractère (le message)
        - Un entier
    Renvoi : une chaine de caractère qui est le nouveau message codé avec le codage de César utilisant l'entier décalage
    """
    
    resultat = ''
    for c in message:
        if 'A' <= c and c <= 'Z':
            indice = (position_alphabet(c)+decalage) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + c
    return resultat
assert cesar("BONJOUR A TOUS. VIVE LA MATIERE NSI !", 4) == 'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !'
assert cesar("AB",2) == "CD"
assert cesar("AB",1) == "BC"
assert cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5) == 'BONJOUR A TOUS. VIVE LA MATIERE NSI !'