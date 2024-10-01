"""
Dato un intero n vogliamo contare le stringhe binarie lunghe
n in cui non compaiono 2 zeri consecutivi.

esempio:
per n = 1 sono 2: (0,1)
per n = 3 sono 5: (010, 011, 101, 110, 111)

L'algoritmo deve avere complessità O(n)
"""

#Iterativo + Programmazione dinamica
def algo(n):
    T = [0]*(n+1)
    for i in range(n+1):
        if i == 0:
            T[i] = 1
        elif i == 1:
            T[i] = 2
        else:
            T[i] = T[i-1] + T[i-2]
    return T[n]

"""
Dato un intero n vogliamo contare le stringhe binarie lunghe
n in cui non compaiono 3 zeri consecutivi.
"""
def algo2(n):
    T = [0]*(n+1)
    for i in range(n+1):
        if i == 0:
            T[i] = 1
        elif i == 1:
            T[i] = 2
        elif i == 2:
            T[i] = 4
        else:
            T[i] = T[i-1] + T[i-2] + T[i-3]
    return T[n]

if __name__ == "__main__":
    n = 3
    #print(algo(n))
    for n in range(1,10):
        print(algo2(n))