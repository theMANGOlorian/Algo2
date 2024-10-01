"""
Dare lo pseudo-codice di un algoritmo che dato l’intero n, stampa
tutte le matrici ternarie (numeri vanno da 1 a 3) n*n con la propriet`a che le righe e le colonne
della matrice risultano ordinate in modo crescente.

Ad esempio per n=2 delle 3^4 = 81 possibili matrici n*n
ne vanno stampate solo 20, vale a dire:
[ 11 ] [ 11 ]
[ 11 ],[ 12 ]...

L'algoritmo deve avere complessità O(n^2*S(n)) dove S(n)
è il numero di matrici da stampare. Motivare la complessità
del vostro algoritmo.
"""
def soluzione(n):
    T = [[0 for _ in range(n)] for _ in range(n)]
    
    def bt(T, row, col):
        if row == n:  # Se abbiamo completato tutte le righe
            print(T)
            return
        
        if col+1 < n:
            next_row, next_col = row,col+1
        else:
            next_row, next_col = row+1,0
        
        for x in range(1, 4):
            if (row == 0 or x >= T[row-1][col]) and (col == 0 or x >= T[row][col-1]):
                T[row][col] = x
                bt(T, next_row, next_col)
    
    bt(T, 0, 0)

soluzione(2)