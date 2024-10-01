"""
Viene dato in input un intero positivo n. Scrivere lo pseudocodice di un algo-
ritmo che in tempo O(n) restituisce il numero di stringhe binarie lunghe n in
cui non compaiono mai tre uni consecutivi.
Ad esempio per n = 4 deve essere restituito 13, le stringhe possibili sono
infatti:
0000 1000 0100 0010 0001 1010 1001 0101 0011 1011 0110 1100 1101
"""
def soluzione(n):
    T = [0] * (n+1)
    T[0] = 1
    T[1] = 2
    T[2] = 4
    for i in range(3,n+1):
        T[i] = T[i-1] + T[i-2] + T[i-3]
    return T[n]

n = 4
print(soluzione(n))