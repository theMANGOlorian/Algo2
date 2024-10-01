'''
Abbiamo file di dimensioni D0,D1,..,Dk-1 che vorremmo memorizzare su un disco di capacità k .
Tuttavia la somma delle dimensioni di questi file eccede
la capacità del disco. Vogliamo dunque selezionare un
sottoinsieme degli n file che abbia cardinalità massima
e che possa essere memorizzato sul disco.
Descrivere un algoritmo greedy che risolve il problema in
tempo theta(nlogn)e provarne la correttezza.

'''

def fileNdisco(D,k):
    n = len(D)
    #crea una lista di coppie valori + indice
    lista = [(D[i],i) for i in range(n)]
    #ordina la lista
    lista.sort()
    spazio, sol = 0, []
    for d, i in lista:
        if spazio + d <= k:
            sol.append(i)
            spazio += d
        else: 
            return sol
if __name__ == "__main__":
    files = [2, 1, 3, 5]
    k = 8
    print(fileNdisco(files,k))