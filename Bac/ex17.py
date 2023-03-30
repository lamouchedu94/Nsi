def moyenne(liste):
    coef = 0
    res = 0
    for note in liste :
        res += note[0] * note[1]
        coef += note[1]
    return res / coef

print(moyenne([(15, 2), (9, 1), (12, 3)]))

def pascal(n):
    triangle= [[1]]
    for k in range(1,n+1):
        ligne_k = [1]
        for i in range(1, k):
            ligne_k.append(triangle[k-1][i-1] + triangle[k-1][i])
        ligne_k.append(1)
        triangle.append(ligne_k)
    return triangle

print(pascal(4))