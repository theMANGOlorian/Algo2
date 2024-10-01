def ex1(G):
    def DFS(G,n,livello,T):
        T[livello] += 1
        for x in G[n]:
            T = DFS(G,x,livello+1,T)
        return T
    T = [0] * len(G)
    T = DFS(G,0,0,T)
    tot = 0
    for i in T:
        if i%2 == 0 and i!= 0:
            tot+=1
    print(tot)
    print(T)

def ex1_BFS(G):
    from collections import deque

    def BFS(x, G):
        coda = deque([x])
        livello_nodi = []
        while coda:
            livello_corrente = len(coda)
            livello_nodi.append(livello_corrente)
            for _ in range(livello_corrente):
                u = coda.popleft()
                for y in G[u]:
                    coda.append(y)
        return livello_nodi

    # Iniziamo la BFS dal nodo 0
    T = BFS(0, G)
    
    # Calcoliamo il numero di livelli con un numero pari di nodi
    tot = sum(1 for i in T if i % 2 == 0 and i != 0)
    
    print(tot)
    print(T)

def count_even_levels(adj_list, n):
    # Dizionario per contare i nodi per livello
    level_count = {}

    # Funzione ricorsiva per DFS
    def dfs(node, level):   

        if level in level_count:
            level_count[level] += 1
        else:
            level_count[level] = 1
        
        for child in adj_list[node]:
            dfs(child, level + 1)
    
    # Avviare DFS dalla radice (nodo 0) a livello 0
    dfs(0, 0)
    
    # Contare i livelli con un numero pari di nodi
    even_level_count = 0
    for count in level_count.values():
        if count % 2 == 0:
            even_level_count += 1

    return even_level_count

albero = [
        [1, 2, 3],  # Nodo 0
        [4, 5],     # Nodo 1
        [],         # Nodo 2
        [6],        # Nodo 3
        [],         # Nodo 4
        [],         # Nodo 5
        []          # Nodo 6
    ]
ex1(albero)
#ex1_BFS(albero)
print(count_even_levels(albero,6))