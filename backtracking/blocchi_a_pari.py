"""
Dare lo pseudo-codice di un algoritmo che dato l'intero n, stampa
tutte le stringhe lunghe n con simboli in {a, b} dove i blocchi di simboli
a di lunghezza massima che appaiono nella stringa hanno lunghezza
pari.
Ad esempio per n = 1 viene stampata la sola stringa b mentre per
n = 5, le stringhe da stampare sono:
bbbbb aabbb baabb bbaab bbbaa baaaa aabaa aaaab
L'algoritmo deve avere complessità O(n*S(n)) dove S(n) è il numero di
stringhe da stampare. Motivare la complessità del vostro algoritmo.
"""
def soluzione(n):
    def backtrack(lista,index,num_a_block):
        if index == n:
            if num_a_block%2 == 0:
                print("".join(lista))
            return
        for x in ['a','b']:
            if x == 'b':
                if num_a_block%2 == 0:
                    lista.append(x)
                    backtrack(lista,index+1,0)
                    lista.pop()
            else:
                lista.append(x)
                backtrack(lista,index+1,num_a_block+1)
                lista.pop()
    backtrack([],0,0)
n = 5
soluzione(n)