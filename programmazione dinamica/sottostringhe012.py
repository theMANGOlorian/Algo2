"""
[CONTA]
Data una stringa S sull'alfabeto {0,1,2} vogliamo contare il
numero di sottostringhe nella sequenza. ad esempio:
per s = 1210121001 la risposta deve essere 1.
per s = 0100120 la risposta deve essere 4.
progettare un algoritmo che risolve il problema in tempo theta(n)
"""

def soluzione(s):
    n = len(s)
    T = [[0 for i in range(n)] for x in range(3)]
    
    if s[0] == '0':
        T[0][0] = 1

    for i in range(1,n):
        if s[i] == '0':
            T[0][i] = T[0][i-1] + 1 
            T[1][i] = T[1][i-1]
            T[2][i] = T[2][i-1]
        elif s[i] == '1':
            T[0][i] = T[0][i-1]
            T[1][i] = T[1][i-1] + T[0][i-1]
            T[2][i] = T[2][i-1]
        elif s[i] == '2':
            T[0][i] = T[0][i-1]
            T[1][i] = T[1][i-1] 
            T[2][i] = T[2][i-1] + T[1][i-1]
    print(T)
    return T[2][n-1]



print(soluzione("10012"))

"""
[spiegazione]
usiamo una matrice T di dimesione 3*n dove :

T[0][i] conterrà il numero di zeri presenti nei primi i simboli di s
T[1][i] conterrà il numero di sottostringhe 01 prenseti nei primi i simboli di s
T[2][i] conterrà il numero di sottostringhe 012 prenseti nei primi i simboli di s

una volta riempita la matrice T la soluzione sarà nella cella T[2][n-1]
"""