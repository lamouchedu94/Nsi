def fusion(tab1, tab2) :
    res = [0 for i in range(len(tab1) + len(tab2))]
    curs1 = 0 
    curs2 = 0
    while curs1 < len(tab1) and curs2 < len(tab2) :
        if tab1[curs1] < tab2[curs2]:
            res[curs1+curs2] = tab1[curs1]
            curs1 += 1
        else :
            res[curs1+curs2] = tab2[curs2]
            curs2 += 1
    if curs1 == len(tab1) and curs2 < len(tab2):
        for i in range(curs2, len(tab2)) :
            res[curs1+curs2] = tab2[curs2]
            curs2 += 1 
    else :
        for i in range(curs1, len(tab1)):
            res[curs1+curs2] = tab1[curs1]
            curs1 += 1
    return res 

print(fusion([1,5,9], [2,3,10]))

def palindrome(chaine):
    for i in range(len(chaine)//2):
        if chaine[i] != chaine[len(chaine)-i-1] :
            return False
    return True

def palindrome_recu(chaine) :
    if len(chaine) <= 1 :
        return True
    if chaine[0] == chaine[-1] :
        return palindrome_recu(chaine[1:-1])
    else :
        return False

print(palindrome("toaot"))
print(palindrome_recu("taoata"))