"""
Dare lo pseudo-codice di un algoritmo che dato un intero n, stampa
tutte le stringhe palindromi lunghe 2n con valori in {a, b}.
Ad esempio per n = 2, le stringhe da stampare sono:
aaaa abba baab bbbb
L’algoritmo deve avere complessit`a O(n*(2^n)). Motivare la complessit`a
del vostro algoritmo.
"""

def soluzione(n):
    def backtrack(lista, index):
        if index == n:
            rev = lista[::-1]
            print("".join(lista+rev))
            return
        for x in ['a','b']:
            lista.append(x)
            backtrack(lista,index+1)
            lista.pop()
    backtrack([],0)
n=2
soluzione(n)
