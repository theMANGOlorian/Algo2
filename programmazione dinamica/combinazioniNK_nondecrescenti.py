def count_sequences(n, k):
    T = [[1] * (k) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, k):
            T[i][j] = T[i][j-1] + T[i-1][j]
    return T[n][k-1]
    

# Esempio di utilizzo
n = 2
k = 5
print(count_sequences(n, k)) 

# Non sono sicuro di questa soluzione
