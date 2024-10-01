"""
Viene dato in input un intero positivo n. Scrivere lo pseudocodice di un algo-
ritmo che in tempo O(n) restituisce il numero di stringhe binarie lunghe n in
cui non compaiono mai uni consecutivi.
Ad esempio per n = 4 deve essere restituito 8, le stringhe possibili sono
infatti:
0000 1000 0100 0010 0001 1010 1001 0101
"""

def soluzione(n):
    T = [1]*(n+1)
    T[1] = 2
    for i in range(2,n+1):
        T[i] = T[i-1] + T[i-2]
    print(f"T:{T}")
    return T[n]
n = 4

print(soluzione(n)) 