"""
[STAMPA]
dato un intero n>=1 e un intero K>=1
vogliamo stampare tutte le stringhe non decrescenti di lunghezza n sull’alfabeto
{0, 1, . . . k-1}.
Ad esempio per n = 5 e k = 1 bisogna stampare la sola stringa 00000 mentre
per n = 3 e k = 3 bisogna stampare le seguenti 10 stringhe:
000, 001, 002, 011, 012, 022, 111, 112, 122, 222.
Progettare un algoritmo basato sulla tecnica del backtracking che, dati gli in-
teri n e k stampi tutte le stringhe non decrescenti di lunghezza n sull’alfabeto
{0, 1, . . . k-1}.
L’algoritmo deve avere complessit`a O(k · n · S(n)) dove S(n) `e il numero di
stringhe da stampare
"""

def soluzione(n,k):
    def backtracking(lista,index):
        if n == index:
            print(''.join(lista))
            return 
        s=0
        if index>0:
            s = int(lista[-1])
        for i in range(s,k):
                lista.append(str(i))
                backtracking(lista,index+1)
                lista.pop()


    backtracking([],0)


soluzione(5,1)