"""
Vogliamo il numero di sequenze decimali di lunghezza n in cui
non appaiono cifre pari adiacenti. Progettare un algoritmo che prende come
parametro l'intero n e, in tempo O(n), restituisce il numero delle sequenze cui
siamo interessati.
Ad esempio:
• per n = 1 la risposta dell'algoritmo deve essere 10
• per n = 2 la risposta dell'algoritmo deve essere 75
"""

def soluzione(n):
    T = [0 for _ in range(n+1)]
    T[0] = 0
    T[1] = 10
    T[2] = 75
    for i in range(3,n+1):
        T[i] = T[i-2]*25 + T[i-1]*5
    return T[n]

print(soluzione(3))