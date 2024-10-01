"""
Dato un intero n vogliamo sapere quante sono le sequenze a cifre
decimali non decrescenti lunghe n.

"""

def soluzione(n):
    T = [[0]*10 for _ in range(n+1)]
    for j in range(10):
        T[1][j] = 1
    for i in range(2,n+1):
        for j in range(10):
            for k in range(j+1):
                T[i][j]+=T[i-1][k]
    return sum(T[n])

print(soluzione(3))
    