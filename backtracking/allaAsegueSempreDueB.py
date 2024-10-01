"""
[Stampa]
Progettare un algoritmo che, dato l’intero n, stampa
tutte le sequenze lunghe n sull’alfabeto ternario {a, b, c} dove il simbolo a `e
sempre seguito da almeno due simboli b.
L’algoritmo proposto deve avere complessit`a O(nS(n)) dove S(n) `e il numero
di sequenze da stampare.
Ad esempio per n = 4 l’algoritmo deve stampare, non necessariamente in
quest’ordine, le seguenti 20 sottosequenze:
abbb abbc babb bbbb bbbc bbcb bbcc bcbb bcbc bccb
bccc cabb cbbb cbbc cbcb cbcc ccbb ccbc cccb cccc.
"""

def soluzione(n):
    def BT(lista,index):
        if n == index:
            print(''.join(lista))
            return
        for x in ['a','b','c']:
            if x == 'a' and  index < (n-2):
                if (index < 1 or lista[-1] != 'a') and (index < 2 or lista[-2] != 'a'):
                    lista.append(x)
                    BT(lista,index+1)
                    lista.pop()
            if x == 'c' and (index < 1 or lista[-1] != 'a') and (index < 2 or lista[-2] != 'a'):
                lista.append(x)
                BT(lista,index+1)
                lista.pop()
            if x == 'b':
                lista.append(x)
                BT(lista,index+1)
                lista.pop()
    BT([],0)

soluzione(4)
