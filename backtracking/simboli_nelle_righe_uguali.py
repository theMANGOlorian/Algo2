"""
Dare lo pseudo-codice di un algoritmo che dato l’intero n, stampa
tutte le matrici n*n e valori in {a, b, c} con la propriet`a che i simboli
in ogni riga sono tutti uguali.

Ad esempio per n=2 le matrici da stampare sono:
aa  aa  aa
aa  bb  cc ...
L'algoritmo deve avere complessità O(n^2*S(n)) dove S(n)
è il numero di matrice da stampare. Motivare la complessità 
del vostro algoritmo.

"""

def soluzione(n):
    T = [[0 for _ in range(n)] for _ in range(n)]

    def BT(T,row,col):
        if row == n:
            print(T)
            return #ogni volta lo dimentico

        if col+1 < n:
            next_col = col+1
            next_row = row
        else:
            next_col = 0
            next_row = row+1
        
        for x in ['a','b','c']:
            if (col == 0 or x == T[row][col-1]):
                T[row][col] = x
                BT(T,next_row,next_col)      
    BT(T,0,0)

soluzione(2)