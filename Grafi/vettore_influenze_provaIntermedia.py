"""
[Progettazione di algoritmi - prova intermedia aprile 2024 - monti]
#Esercizio 1
Dato un grafo diretto G con n nodi e m archi e due suoi nodi a e b, in caso contrario diciamo
che x è nella sfera di influenza di quello dei due nodi che è a lui più vicino. Chiamiamo
infine vettore delle influenze rispetto ai nodi a e b il vettore D di n componenti dove D[i]
indica il nodo alla cui sfera d'influenza i appartiene e nel caso x sia equidistante da a e b
allora D[i] = -1. Progettare un algoritmo che, dato G tramite liste di adiacenza e i nodi a e b,
in tempo O(n+m) restituisce il vettore delle influenze

"""

def vettoreInfluenze(G,a,b):
    trasposto_G = trasposto(G) #O(n+m)
    distanze_a = vettore_distanze_BFS(trasposto_G,a) #O(n+m)
    distanze_b =  vettore_distanze_BFS(trasposto_G,b) #O(n+m)

    vettore_influenze = [-1 for _ in range(len(G))] #(n)
    for i in range(len(G)): #O(n)
        if distanze_a[i] == distanze_b[i]:
            vettore_influenze[i] = -1
        elif distanze_a[i] < distanze_b[i]:
            vettore_influenze[i] = a
        else:
            vettore_influenze[i] = b
    return vettore_influenze


def trasposto(G):
    n = len(G)
    Gt = [[] for _ in G]
    for u in range(n):
        for v in G[u]:
            Gt[v].append(u)
    return Gt


def vettore_distanze_BFS(G,s):
    D = [-1 for _ in range(len(G))]
    from collections import deque
    D[s] = 0
    coda = deque([s])
    while coda:
        u = coda.popleft()
        for v in G[u]:
            if D[v] == -1:
                D[v] = D[u]+1 
                coda.append(v)
    return D


G = [
    [1,2,10],#0
    [4,5,9],#1
    [7],#2
    [0,4,9],#3
    [9],#4
    [2,6,8],#5
    [4,7],#6
    [5],#7
    [0,2],#8
    [6],#9
    [9]#10
]
a,b = 2,6

print(vettoreInfluenze(G,a,b))