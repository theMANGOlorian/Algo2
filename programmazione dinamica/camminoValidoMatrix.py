"""
[Conta]
Considerare una griglia n*n. Un cammino valido in questa griglia
deve partire dalla cella in alto a sinistra di coordinate (0,0)
ed arrivare alla posizione in basso a destra di coordinate
(n-1,n-1).
E' possibile muoversi su questa griglia solo su celle adiacenti,
andando di un passo verso destra oppure di un passo verso il basso.
Oltretutto nel corso del cammino è vietato toccare le celle di
coordinate (i,j) con i>j. Dato il valore di n vogliamo calcolare
il numero di cammini validi.

Ad esempio:
per n = 4 la risposta deve essere 5, abbiamo infatti i seguenti
possibili cammini:
dddbbb ddbdbb ddbbdb dbdbdb dbddbb
(dove d indica un passo verso destra e b un passo verso il basso)

Progettare un algoritmo che risolve il problema in tempo O(n^2)
"""

def soluzione(n):
    T = [[0 for j in range(n)] for i in range(n)]
    print(T)
    for i in range(n):
        for j in range(n):
            if i == 0:
                T[i][j] = 1
            elif i > j:
                T[i][j] = 0
            else:
                T[i][j] = T[i-1][j] + T[i][j-1]
    return T[n-1][n-1]

print(soluzione(5))

"""
[spiegazione soluzione]

Utilizziamo una tabella di dimesione n*n
T[i][j] = il numero di cammini che dalla cella (0,0) arrivano alla cella (i,j).
La soluzione al problema sarà T[n-1][n-1]

Ricorrenza
          { 0 se i > j
T[i][j] = { 1 se i = 0
          { T[i-1][j] + T[i][j-1] altrimenti

si ha T[i-1][j] + T[i][j-1] perche posso raggiungere (i,j) sia
dai cammini che provengono da (i-1,j) che da quelli che provengono
da (i,j-1)
"""