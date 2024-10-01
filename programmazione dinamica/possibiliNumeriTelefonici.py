"""
[Conta]
Esercizio sul tastierino dei numeri telefonici
"""

def soluzione(n):
    T = [[0 for j in range(10)] for i in range(n+1)]
    
    for i in range(n+1):
        for j in range(10):

            if i == 1: T[i][j] = 1
            elif j == 0: T[i][j] = T[i-1][8]
            elif j == 1: T[i][j] = T[i-1][2] + T[i-1][4] 
            elif j == 2: T[i][j] = T[i-1][1] + T[i-1][3] + T[i-1][5]
            elif j == 3: T[i][j] = T[i-1][2] + T[i-1][6]
            elif j == 4: T[i][j] = T[i-1][1] + T[i-1][7] + T[i-1][5] 
            elif j == 5: T[i][j] = T[i-1][2] + T[i-1][4] + T[i-1][6] + T[i-1][8] 
            elif j == 6: T[i][j] = T[i-1][3] + T[i-1][5] + T[i-1][9]
            elif j == 7: T[i][j] = T[i-1][4] + T[i-1][8]
            elif j == 8: T[i][j] = T[i-1][7] + T[i-1][5] + T[i-1][9] + T[i-1][0]
            elif j == 9: T[i][j] = T[i-1][6] + T[i-1][8] 
    return sum(T[n])

print(soluzione(4))