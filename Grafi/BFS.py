from collections import deque

def BFS(G,r):
    visitati = [0 for _ in range(len(G))]
    visitati[r] = 1
    coda = deque([r])

    while coda:
        u = coda.popleft()
        print(u)
        for v in G[u]:
            if visitati[v] == 0:
                visitati[v] = 1
                coda.append(v)
    return visitati

def BFS_vettore_dei_padri(G,r):
    padri = [-1 for _ in range(len(G))]
    padri[r] = r
    coda = deque([r])

    while coda:
        u = coda.popleft()
        for v in G[u]:
            if padri[v] == -1:
                padri[v] = u
                coda.append(v)
    return padri

def BFS_vettore_distanze(G,r):
    distanze = [-1 for _ in range(len(G))]
    distanze[r] = 0
    coda = deque([r])

    while coda:
        u = coda.popleft()
        for v in G[u]:
            if distanze[v] == -1:
                distanze[v] = distanze[u]+1
                coda.append(v)
    return distanze

grafo = [
    [1,3],#0
    [0,2,4],#1
    [1,4],#2
    [0],#3
    [1,2,5],#4
    [4]#5
]

print("sequenza dei nodi con BFS + quali sono raggiungibili",BFS(grafo,0))
print("vettore dei padri:", BFS_vettore_dei_padri(grafo,0))
print("vettore distanze:", BFS_vettore_distanze(grafo,0))