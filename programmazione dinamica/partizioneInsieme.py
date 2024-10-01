
"""
[Conta]
Dati due interi non negativi n è k vogliamo sapere in quanti
modi è possibile partizionare l'insieme dei numeri da 1 a n in k
sottoinsiemi non vuoti.
Ad esempio:
    per n = 1 e k = 2 la risposta è 0
    per n = 2 e k = 2 la risposta è 1. L'unica partizione
    possibile è ({1}{2})
    per n = 3, k = 2 la risposta è 3. Le 3 bipartizioni possibili
    sono ({1},{2,3}),({2}{1,3}) e ({3}{1,2}).

    Progettare un algoritmo che risolve il problema in tempo
    theta(n*k)
"""

def solution(n,k):
    T = [[0]*(k+1) for i in range(n+1)]
    T[0][0] = 1
    for i in range(1,n+1):
        for j in range(1,k+1):
            T[i][j] = j * T[i-1][j] + T[i-1][j-1]

    return T[n][k]


print(solution(2,2))



"""
spiegazione della relazione di ricorrenza

T[i][j] = j*T[i-1][j] + T[i-1][j-1]

j*T[i-1][j] : dobbiamo aggiugere il n-esimo elemento a una partizione.
    ci sono k sottoinsiemi disponibili in cui possiamo aggiungerlo
T[i-1][j-1] : dobbiamo aggiungere il n-esimo elemento come un
    nuovo sottoinsieme.
 
"""