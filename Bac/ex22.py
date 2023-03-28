def liste_puissances(a,n) :
    """
    Paramètres :
        - un nombre entier strictement positif
        - Un autre entier strictement positif n et qui renvie la liste de ses puissances. 
    Renvoi : liste de ses puissances
    """
    temp = a
    res = []
    for i in range(n) :
        for j in range(i) :
            temp *= a
        res.append(temp) 
        temp = a
    return res 
    
print(liste_puissances(3,5))
assert liste_puissances(-2, 4) == [-2,4,-8,16]
assert liste_puissances(3,5) == [3,9,27,81,243]

def liste_puissances_borne(a, borne) :
    temp = a
    res = []
    for i in range(borne) :
        for j in range(i) :
            temp *= a
        if temp >= borne :
           return res
        res.append(temp) 
        temp = a
    return res 

assert liste_puissances_borne(2, 16) == [2,4,8]
assert liste_puissances_borne(2, 17) == [2,4,8,16]
assert liste_puissances_borne(5, 5) == []

dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
"G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
"M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
"R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
"W": 23, "X": 24, "Y": 25, "Z": 26}

def est_parfait(mot) :
    """
    Paramètre : chaine de caractères en majuscules
    Renvoi :
        - Code alphabétique concaténé
        - Code additionné de mot
        - Un booléen qui idique si mot est parfait ou non 
    """
    
    # mot est une chaîne de caractères (en lettres majuscules)
    code_concatene = ""
    code_additionne = 0
    
    for c in mot :
        code_concatene = code_concatene + str(dico[c])
        code_additionne = code_additionne + dico[c]
    code_concatene = int(code_concatene)
    if code_concatene % code_additionne == 0:
        mot_est_parfait = True
    else :
        mot_est_parfait = False
    return code_additionne, code_concatene, mot_est_parfait

assert est_parfait("PAUL") == (50, 1612112, False)
assert est_parfait("ALAIN") == (37, 1121914, True)
assert est_parfait("THOMAS") == (76, 2081513119, False)
assert est_parfait("A") == (1, 1, True )
assert est_parfait("AB") == (3, 12, True)
