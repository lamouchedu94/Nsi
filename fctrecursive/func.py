def nbbits(n):
    if n == 0 :
        return 0
    return nbbits(n//2)+ (n & 1) 
print(nbbits(10))

def syracuse(u):
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