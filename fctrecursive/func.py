import math
 
def nbbits(n):
    assert n >= 0 and type(n) == int
    if n == 0 :
        return 0
    return nbbits(n//2)+ (n & 1) 
print("Doit afficher 1 : ",nbbits(1))
print("Doit afficher 1 : ", nbbits(2))
print("Doit afficher 2 : ", nbbits(3))
print("Doit afficher 2 : ", nbbits(10))
print("Doit afficher 8 : ",nbbits(255))
 
def syracuse(u,tab=None):
    assert u > 0
    if tab == None :
        tab = []
    tab.append(u)
    if u == 1 :
        return tab
    if u%2 == 0 :
        return syracuse(u//2, tab)
    return syracuse(3*u+1, tab)
 
print("\nTest 1")
print(syracuse(10))
print("Test 2")
print(syracuse(4))
 
def exp(x):
    u =1 
    for i in range(x) :
        u = u*math.exp(-u)    
    return u
 
print(exp(100))
 
def exp_r(n, u=1):
    if n == 0 :
        return u
    return exp_r(n-1,u*math.exp(-u))
 
print(exp_r(100))