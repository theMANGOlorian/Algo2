"""
[CONTA]
data una scala con n  2 gradini vogliamo
sapere il numero di modi che abbiamo di salire dal primo all'ultimo gradino
della scala sapendo che ad ogni passo possiamo risalire di 1, 2 o 3 gradini.
Ad esempio per una scala con n = 4 gradini la risposta deve essere 4 infatti,
rappresentando ogni salita tramite la sequenza di passi che vengono di volta in
volta e↵ettuati abbiamo le seguenti 4 sequenze
[1,1,1],[1,2],[2,1],[3]

Progettare un algoritmo basato sulla tecnica della programmazione dinamica
che dato n risolve il problema in tempo O(n)
"""
def soluzione(n):
    T = [0]*(n+1)
    T[2] = 1
    T[3] = 2
    T[4] = 4
    for i in range(5,n+1):
        T[i] = T[i-1] + T[i-2] + T[i-3]
    return T[n]

print(soluzione(5))
