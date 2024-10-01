"""
[STAMPA]
stampa risalite: data una scala con n  2 gradini vogliamo
sapere i diversi modi che abbiamo di risalita dal primo all'ultimo gradino della
scala sapendo che ad ogni passo possiamo risalire di 1, 2 o 3 gradini. Ogni modo
di risalire `e rappresentato dalla sequenza di passi che vengono di volta in volta
e↵ettuati.
Ad esempio per una scala con n = 4 gradini la risposta sar`a data dalle 4 se-
quenze:
[1,1,1],[1,2],[2,1],[3]

Progettare un algoritmo basato sulla tecnica del backtracking che dato n stampa
i diversi modi di risalire la scala.
L'algoritmo deve avere complessit`a O(nS(n)) dove S(n) `e il numero di diversi
modi di risalire la scala
"""

def soluzione(n):
    def backtrack(lista,l):
        if l == n:
            print(lista)
            return
        for i in range(1,4):
            if (l+i) <= n:
                lista.append(i)
                backtrack(lista, l+i)
                lista.pop()

    backtrack([],1)

soluzione(5)