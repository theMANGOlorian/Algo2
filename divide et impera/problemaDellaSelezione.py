"""
IL PROBLEMA DELLA SELEZIONE
Data una lista A di interi distinti, il rango di un elemento in A
è il numero di elementi che sono minori o uguali ad X in A, ovvero
l'elemento di un array non ordinato che occuperebbe la posizione k se l'array fosse ordinato.


Soluzione in tempo theta(n)
"""
from math import ceil
def selezione(A,k):
    if len(A) <= 120:
        A.sort()
        return A[k-1]   
    B = [ sorted(A[5*i : 5*i+5])[2] for i in range(len(A)//5) ]
    perno = selezione(B,ceil(len(A)/10)) 
    A1, A2 = [],[]
    for x in A:
        if x < perno:
            A1.append(x)
        elif x > perno:
            A2.append(x)
    if len(A1) >= k:
        return selezione(A1,k)
    elif len(A1) == k-1:
        return perno
    return selezione(A2, k - len(A1) - 1)

if __name__ == "__main__":
    lista = [30,20,50,60,10,40,90,80,70]
    print(selezione(lista,8))