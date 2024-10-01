"""
Dare lo pseudo-codice di un algoritmo che dato l’intero n, stampa
tutte le stringhe lunghe n con simboli in {a, b} che contengono un
numero dispari di simboli a ed un numero dispari di simboli b.
Ad esempio per n = 3 non viene stampato nulla mentre per n = 4, le
stringhe da stampare sono:
abbb babb bbab bbba baaa abaa aaba aaab
L’algoritmo deve avere complessit`a O(n*S(n)) dove S(n) `e il numero di
stringhe da stampare. Motivare la complessit`a del vostro algoritmo.
"""

def soluzione(n):
    def backtrack(lista,index,counta,countb):
        if index == n:
            if counta%2==1 and countb%2==1:
                print("".join(lista)) 
            return
        for x in ['a','b']:
            lista.append(x)
            if x == 'a':
                backtrack(lista,index+1,counta+1,countb)
            else:
                backtrack(lista,index+1,counta,countb+1)
            lista.pop()
    backtrack([],0,0,0)
n = 4
soluzione(n)