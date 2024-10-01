"""
[Conta]
Dato un intero n, con n ≥ 2, vogliamo contare il numero
di modi in cui `e possibile ottenere n partendo dal numero 2 e potendo effettuare
le sole 3 operazioni di incremento di 1, prodotto per 2 e prodotto per 3.
Ad esempio per n = 10 la risposta `e 9. Infatti le sequenze possibili sono:
(2, 3, 4, 5, 6, 7, 8, 9, 10), (2, 3, 4, 5, 10), (2, 3, 4, 8, 9, 10), (2, 3, 6, 7, 8, 9, 10),
(2, 3, 9, 10), (2, 4, 5, 10), (2, 4, 5, 6, 7, 8, 9, 10), (2, 4, 8, 9, 10), (2, 6, 7, 8, 9, 10).
"""
def soluzione(n):
    T = [0]*(n+1)
    T[2] = 1
    T[3] = 1
    for i in range(4,n+1):
        T[i] = T[i-1]
        if i%2 == 0:
            T[i] += T[i//2]
        if i%3 == 0:
            T[i] += T[i//3]
    return T[n]

print(soluzione(6))