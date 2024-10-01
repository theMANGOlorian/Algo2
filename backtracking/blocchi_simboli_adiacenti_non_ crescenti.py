"""
[STAMPA]
Data un intero n vogliamo stampare tutte le stringhe binarie lunghe n dove i blocchi
di simboli adiacenti uguali che si incontrano nello scorrere le stringhe da sinistra
a destra hanno lunghezze NON crescenti (i.e. nella stringa un blocco di x simboli
uguali deve essere seguito da un blocco di simboli uguali di lunghezza non superiore
ad x).
Ad esempio per n = 4 verranno stampate le seguenti 10 stringhe:
0000 0001 0010 0011 0101 1010 1100 1101 1110 1111

Progettare un algoritmo che risolve il problema in tempo O(n*S(n)) dove S(n) è il
numero di stringhe da stampare.
"""
def soluzione(n):
    def backtracking(lista,index,prev_lenBlock,curr_lenBlock):
        if n == index:
            print(''.join(lista))
            return       
        for x in ['0','1']:
            if index == 0:
                lista.append(x)
                backtracking(lista,index+1,0,1)
                lista.pop()
            elif x == lista[index-1]:
                if prev_lenBlock == 0 or prev_lenBlock > curr_lenBlock:
                    lista.append(x)
                    backtracking(lista,index+1,prev_lenBlock,curr_lenBlock+1)
                    lista.pop()
            elif x != lista[index-1]:                
                lista.append(x)
                backtracking(lista,index+1,curr_lenBlock,1)
                lista.pop()
    
    backtracking([],0,0,0)

n = 3
soluzione(n)