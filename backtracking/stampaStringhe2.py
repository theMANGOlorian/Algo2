'''
una stringa S su alfabeto
ternario {0, 1, 2} si dice buona se ogni simbolo che vi compare diverso da 2
risulta adiacente al simbolo 2. Ad esempio la stringa 12101 non `e buona per
due motivi:
• l’unica occorrenza del simbolo 0 non `e adiacente al simbolo 2
• l’ultima occorrenza del simbolo 1 non `e adiacente al simbolo 2
Progettare un algoritmo basato sulla tecnica del backtracking che, dato un intero
n stampi tutte le stringhe buone di lunghezza n.
Ad esempio per n = 4 l’algoritmo stamper`a le seguenti stringhe (non necessari-
amente nello stesso ordine):
2222 2220 2221 2202 2212 2022 2020 2021 2002 2012 2122 2120 2121
2102 2112 0222 0220 0221 0202 0212 1222 1220 1221 1202 1212
L’algoritmo deve avere complessit`a O(nS(n)) dove S(n) `e il numero di sequenze
da stampare.
'''
def soluzione(n):
    def backtrack(lista, i):
        if n == i:
            print(''.join(lista))
            return
        
        lista.append('2')
        backtrack(lista,i+1)
        lista.pop()
        if (i==0 and n!=1) or (0<i==n-1 and lista[-1]=='2') or (0<i<n-1 and lista[-1] == '2') or (1<i<n-1 and lista[-2] == '2'):
            for x in ['0','1']:
                lista.append(x)
                backtrack(lista,i+1)
                lista.pop()
    backtrack([],0)

soluzione(4)

