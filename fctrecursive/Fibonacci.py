def fibo(n):
    if n <= 1 :
        return 1
    return fibo(n-2) + fibo(n-1)

#print(fibo(10))

def fibo_memo(n, memo):
    '''Memo est un tab de taille n+1, de la forme [1,1,None,None,...,None]'''
    if memo[n] != None :
        return memo[n]
    memo[n]=fibo_memo(n-1,memo) + fibo_memo(n-2,memo)
    return memo[n]

def fibo_front(n):
    memo=[1,1]+[None for _ in range(n-1)]
    return fibo_memo(n, memo)

#print(fibo_front(500))

def fibo_bt(n):
    memo = [1,1] + [None for i in range(n-1)]
    for i in range(2,1+n):
        memo[i] =memo[i-1]+memo[i-2]
    return memo[n]
#fibo_bt(1000000)
#print(fibo_bt(50000))

def minimum(liste):
    if len(liste)<=1 :
        return liste[0]
    i_med=len(liste)//2
    return min(minimum(liste[:i_med]), minimum(liste[i_med:]))
print(minimum([5,7,8,1,6,2]))

# Faire pyramide