'''
Abbiamo una lista di attività, ciascuna caratterizzata da un tempo di
inizio ed un tempo di fine. Le attività vanno tutte eseguite e
vogliamo assegnarle al minor numero di aule tenendo conto che in
una stessa aula non possono eseguirsi più attività in parallelo.
'''

def selezione_attività(lista):
    from heapq import heappop, heappush
    sol = [[]]
    H = [(0,0)]
    lista.sort()
    for inizio, fine in lista:
        libera, aula = H[0]
        if libera <= inizio:
            sol[aula].append((inizio,fine))
            heappop(H)
            heappush(H,(fine,aula))
        else:
            sol.append([(inizio,fine)])
            heappush(H,(fine,len(sol)-1))
    return sol

if __name__ == "__main__":
    lista = [(1,4),(1,6),(7,8),(5,10)]
    print(selezione_attività(lista))