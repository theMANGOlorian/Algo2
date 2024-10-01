"""
Data una stringa S, una sua sottosequenza `e quello che si ottiene
eliminando 0 o pi`u dei suoi caratteri, possiamo rappresentare la sottosequenza
ottenuta sostituendo ciascun carattere eliminato con il simbolo .

Progettare un algoritmo basato sulla tecnica del backtraking che, data una
stringa S di n caratteri stampi tutte le sottosequenze in cui non compaiono
simboli adiacenti.
Ad esempio per S='anno' l’algoritmo stamper`a le seguenti sottosequenze (non
necessariamente nello stesso ordine):
'a_n_' 'a__o' 'a___' '_n_o' '_n__' '__n_' '___o' '____'

L'algoritmo deve avere complessità O(nS(n)) dove S(n) è il
numero di sequenze da stampare
"""

def soluzione(S):
    def backtrack(lista, index):
        if index == n:
            print(''.join(lista))
            return

        if index == 0 or lista[-1] == '_':
            lista.append(S[index])
            backtrack(lista,index+1)
            lista.pop()

        lista.append('_')
        backtrack(lista,index+1)
        lista.pop()

    n = len(S)
    backtrack([],0)

s = 'anno'
soluzione(s)