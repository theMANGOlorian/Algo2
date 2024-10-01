"""
Data una matrice binaria di dimensioni n*n vogliamo verificare se nella matrice
`e possibile raggiungere la cella in basso a destra partendo da quella in alto a
sinistra senza mai toccare celle che contengono il numero 1.
Si tenga conto che dalla generica cella (i, j) ci si pu`o spostare solo nella cella
in basso (vale a dire la cella (i + 1, j)) o nella cella a destra (vale a dire la cella
(i, j + 1)).
Progettare un algoritmo che risolve il problema in tempo O(n^2)
"""

def soluzione(M,n):
    T = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j == 0 and M[0][0] == 0: 
                T[i][j] = 1
            elif i == 0 and j != 0 and M[i][j] == 0: 
                T[i][j] = T[i][j-1]
            elif i != 0 and j == 0 and M[i][j] == 0: 
                T[i][j] = T[i-1][j]
            elif i != 0 and j != 0 and M[i][j] == 0: 
                T[i][j] = T[i-1][j] + T[i][j-1]
    # N.B. in T[n-1][n-1] c'è il numero di percorsi possibili per raggiungere la posizione in basso a destra
    if T[n-1][n-1] != 0:
        return True
    else:
        return False
    
#N.B la matrice DEVE essere n*n
M = [
    [0,0,0],
    [0,1,0],
    [0,1,0],
]
print(soluzione(M,len(M)))