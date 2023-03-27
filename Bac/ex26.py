def multiplication(n1, n2) :
    res = 0 
    if n1 == 0 or n2 == 0 :
        return 0 
    elif n1 > 0 and n2 > 0 :
        for i in range(n1):
            res += n2
    elif n1 < 0 and n2 < 0 :
        for i in range(abs(n1)):
            res += abs(n2)
    elif n1 < 0 and n2 > 0 :
        for i in range(n2):
            res += n1
    elif n1 > 0 and n2 < 0 :
        for i in range(n1):
            res += n2
    return res

assert multiplication(0,0) == 0 
assert multiplication(2,5) == 10
assert multiplication(-2,-2) == 4
assert multiplication(-2,6) == -12
assert multiplication(2,-6) == -12
assert multiplication(1431, 0) == 0

def dichotomie(tab, x):
    debut = 0 
    fin = len(tab) - 1
    while debut <= fin :
        m = (debut + fin) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else :
            fin = m-1
    return False

assert dichotomie([],0) == False
assert dichotomie([1],1) == True
assert dichotomie([1,2,3,4,5,6],5) == True
assert dichotomie([1,2,7,8,10],10) == True
assert dichotomie([1,2,7,8,10],1) == True
assert dichotomie([1,2,7,8,10],11) == False
