"""
[Conta]
Progettare un algoritmo che data una astringa A di lunghezza n ed una stringa B di lunghezza m trova il costo minimo
per trasformare A in B. La trasformazione deve avvenire utilizzando le seguenti tre operazioni ciascuna di costa
unitario:
    + Inserimento: inserisce un carattere in A
    + Cancellazione: cancella un carattere da A
    + Sostituzione: sostituisce un carattere da A con un diverso carattere

Ad esempio:
    per A = 'casa' e B = 'ala' il costo è 2
    per A = 'vetro' e b = 'eroe' il costo è 3
La complessità deve essere O(n*m)
"""
def soluzione(A,B):
    n = len(A)
    m = len(B)

    # casi base
    T = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        T[i][0] = i
    for i in range(m+1):
        T[0][i] = i
    
    for i in range(n+1):
        for j in range(m+1):
            if A[i-1] == B[j-1]:
                T[i][j] = T[i-1][j-1]
            else:
                T[i][j] = min(
                    T[i-1][j-1] + 1,
                    T[i-1][j] + 1,
                    T[i][j-1] + 1
                )
    return T[n-1][m-1]
print("Numero minimo di operazione:", soluzione("vetro","eroe"))

#Alla fine non era così difficile >:C