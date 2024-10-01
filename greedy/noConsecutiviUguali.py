"""
ricorda che una sottolista di una lista A
si ottiene cancellando da A zero o pi`u elementi.
Data una lista di interi A vogliamo la sottolista di A pi`u lunga che non contiene
elementi consecutivi uguali.
Ad esempio per A = [3, 3, 2, 4, 4, 4, 1, 5] la sottolista cercata `e [3, 2, 4, 1, 5].
Utilizzando la tecnica greedy progettare un algoritmo che data la lista A di
lunghezza n risolve il problema in tempo theta(n) 
"""

def soluzione(A):
    T = []
    for i in A:
        if T == [] or T[-1] != i:
            T.append(i)
    return T

A = [3,3,2,4,4,4,1,5]
print(soluzione(A))

