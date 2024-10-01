def DFS(G,s):
    visitati = [0 for _ in range(len(G))]
    def ricorsione(G,x):
        for v in G[x]:
            if visitati[v] == 0:
                visitati[v] = 1
                ricorsione(G,v)

    visitati[s] = 1
    ricorsione(G,s)
    return visitati

def DFS_vettore_dei_padri(G,s):
    padri = [-1 for _ in range(len(G))]
    def ricorsione(G,x):
        for v in G[x]:
            if padri[v] == -1:
                padri[v] = x
                ricorsione(G,v)
    padri[s] = s
    ricorsione(G,s)
    return padri

def cicli(G,s):
    visitati = [0 for _ in range(len(G))]
    def ricorsione(G,x,p):
        visitati[x] = 1 
        for v in G[x]:
            if visitati[v] == 1:
                if v != p: return True
            else:
                if ricorsione(G,v,x):
                    return True
        return False
     
    return ricorsione(G,s,s)


grafo = [
    [1,3],#0
    [0,2,4],#1
    [1,4],#2
    [0],#3
    [1,2,5],#4
    [4]#5
]

print("Nodi raggiungibili con DFS",DFS(grafo,0))
print("vettore dei padri:", DFS_vettore_dei_padri(grafo,0))
print("Presenza di cicli (usando la DFS):", cicli(grafo,0))