def nbbits(n):
    assert n >= 0 and type(n) == int
    if n == 0 :
        return 0
    return nbbits(n//2)+ (n & 1) 
print("Doit afficher 1 : ",nbbits(1))
print("Doit afficher 1 : ", nbbits(2))
print("Doit afficher 2 : ", nbbits(3))
print("Doit afficher 2 : ", nbbits(10))
print("Doit afficher 4 : ",nbbits(210))

def syracuse(u):
    assert u > 0
    if u == 1 :
        return 1
    if u%2 == 0 :
        u = u // 2
    else :
        u = 3*u +1 
    return syracuse(u)
print(syracuse(10))

def factorielle(n):
    if n == 0 :
        return 1
    return n*factorielle(n-1)
#print(factorielle(21))