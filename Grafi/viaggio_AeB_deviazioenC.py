"""
[GRAFI]
Abbiamo un grafo non diretto, pesato e connesso e tre suoi nodi a,b,c. i nodi del grafo sono località e il peso degli 
archi è il costo da pagare per spostarsi da un nodo all'latro. dobbiamo effettuare un viaggio da a a b e siamo 
indecisi se effettuare una eventuale deviazione e passare anche da c. passeremo da c solo se il costo del percorso 
che include c risulta inferiore a due volte quello che c'è da gapare per andare direttamente da a a b. 
descrivere un algoritmo che, dato il grafo G tramite liste di adiacenza e o tre nodi a,b, e c risolve il problema 
in tempo O(n^2) rispondendo True se la deviazione è fattibile o false altrimenti.
"""
def soluzione(G,a,b,c):
    Da = dijkstra(G,a) #O(n^2)
    Dc = dijkstra(G,c) #O(n^2)

    if Da[c] + Dc[b] < Da[b]*2:
        return True
    else:
        return False

def dijkstra(G,s): #(grafo,sorgente)
    inserito = len(G)*[False]
    from math import inf
    lista = [(inf,-1)]*len(G)
    lista[s], inserito[s] = (0,s), True
    for y, costo in G[s]:
        lista[y] = (costo,s)
    while True:
        minimo = inf
        for i in range(len(lista)):
            if not inserito[i] and lista[i][0] < minimo:
                minimo, x = lista[i][0], i
        if minimo == inf: 
            break
        inserito[x] = True
        for y, costo in G[x]:
            if not inserito[y] and minimo + costo < lista[y][0]:
                lista[y] = (minimo + costo, x)
    D = [costo for costo, _ in lista]
    return D #Lista distanze


G = [
    [(1,17),(5,4)],#0
    [(0,17),(4,5),(5,6)],#1
    [(3,12),(4,10)],#2
    [(2,12),(4,4),(5,1)],#3
    [(1,5),(2,10),(3,4)],#4
    [(0,4),(1,6),(3,1)],#5
]
a,b,c = 1,4,2

esito = soluzione(G,a,b,c)
print(esito)