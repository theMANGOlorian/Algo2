"""
[Stampa]
Dato un intero n vogliamo stampare TUTTE le stringhe ternarie
sull'alfabeto {'0','1','2'} lunghe n che non contengono 3
simboli consecutivi uguali e non contegono 3 simboli 
consecutivi diversi.

ad Esempio per n = 4 verranno stampate 36 stringhe:

progettare un algoritmo che risolva il problema in tempo O(nS(n))
dove S(n) è il numero di stringhe da stampare. 

"""

def ex1(n):
    def backtrack(str, len):
        if n == len:
            print(''.join(str))
            return
        for i in d: #costante perche scorre sempre un vettore di 3 elementi
            str.append(i) #O(1)
            if isValid(str,len+1,n):                 
                backtrack(str,len+1)
            str.pop() #O(1)

    d = ['0','1','2']
    backtrack([],0)


def isValid(str,len,n):
    # O(1)
    if len <= 2:
        return True 
    if len > n:
        return False 
    if str[-1] == str[-2] == str[-3]: #ultimi 3 non sono uguali 
        return False
    if str[-1] != str[-2] and str[-1] != str[-3] and str[-2] != str[-3]: #ultimi 3 sono diversi
        return False

    return True
    

n = 4
ex1(n)