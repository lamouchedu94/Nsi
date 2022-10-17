def C(n,p):
    if p == 0 or n == p :
        return 1
    #print(n, p )
    return C(n-1,p-1) + C(n-1,p)

print(C(6, 4))