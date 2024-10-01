"""
Data una stringa S sull'alfabeto {0,1,2} vogliamo contare il
numero di sottostringhe 012 presenti nella sequenza. ad esempio:
per S = 1210121001 la risposta deve essere 1, abbiamo solamente
un 012
per S = 0100120 la riposta è 4
Progettare un algoritmo che risolve il problema in tempo theta(n)
"""
def soluzione(S):
    n = len(S)
    T = [[0 for _ in range(3)] for _ in range(n)]
    for i in range(n):
        for k in range(3):
            T[i][k] = T[i-1][k]
            if S[i] == "0" and k == 0:
                T[i][0] += 1
            if S[i] == "1" and k == 1:
                T[i][1] = T[i][0] + T[i-1][1]
            if S[i] == "2" and k == 2:
                T[i][2] = T[i][1] + T[i-1][2]
    return T[n-1][k]
stringa = "001122"
print(soluzione(stringa))