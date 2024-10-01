def kruskal(G):
    '''parto con il grafo T che contiene tutti i nodi di G e nessun arco di G'''
    T = [[] for _ in G]
    '''prendo tutti gli archi  di G in ordine di costo crescente, (c,u,v) '''
    A = [(c,u,v) for u in range(len(G)) for v,c in G[u] if u<v]
    A.sort() #l'ordinamento avverrà in base al primo elemento di ciascuna tupla, questo caso il costo dell'arco.

    '''aggiungi ogni arco di A in T, se forma un ciclo allora rimuovilo'''
    for i in A: 
        c,x,y = i
        if not ciclo(T,x,y): #se non forma un ciclo
            T[x].append(y) #allora aggiungi l'arco a T
            T[y].append(x)
    return T

def ciclo(T,x,y):
    ''' basta fare una visita e controllare se da x posso raggiungere y,x
        se si allora aggiungere l'arco sarebbe ridondante
        se no allora aggiungi l'arco
    '''
    def cicloR(a,b,T):
        visitati[a] = 1
        for z in T[a]:
            if z == b: return True
            if not visitati[z] and cicloR(z,b,T): return True
        return False
    visitati = [0] * len(T)
    return cicloR(x,y,T)

#Grafo pesato non diretto
grafo = [
    [(1,8),(3,2)],#0
    [(0,8),(2,5),(4,7)],#1
    [(1,5),(4,3)],#2
    [(0,2)],#3
    [(1,7),(2,3),(5,6)],#4
    [(4,6)]#5
]
print("copertura minima:",kruskal(grafo))