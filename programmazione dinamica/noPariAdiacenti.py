"""
[CONTA]
Vogliamo il numero di sequenze decimali di lunghezza
n in cui non appaiono cifre pari adiacenti. Progettare un algoritmo che prende
come parametro l’intero n e, in tempo O(n), restituisce il numero delle sequenze
cui siamo interessati.
Ad esempio:
• per n = 1 la risposta dell’algoritmo deve essere 10
• per n = 2 la risposta dell’algoritmo deve essere 75
"""

def mostraCasi(n):
    
    def backtrack(lista, index, count):
        if n == index:
            print(''.join(map(str, lista)))
            count += 1
            return count
        for i in range(10):
            if index == 0 or i % 2 != 0 or lista[-1] % 2 != 0:
                lista.append(i)
                count = backtrack(lista, index + 1, count)
                lista.pop()
        return count
    
    count = 0
    count = backtrack([], 0, count)
    print("count: " ,count)

#mostraCasi(4)# controllo conteggio

def soluzione(n):
    T = [0 for _ in range(n+1)]
    T[1], T[2] = 10, 75
    for i in range(3,n+1):
        T[i] = 5*T[i-1] + 25*T[i-2] 
        #5*T[i-1] scelte di dispari che vanno bene conl'ultima cifra
        #5*5*T[i-2] scelte pari che vanno bene prendendo in cosidereazione l'utlima e la penultima
        #   Ci sono 5 scelte per la penultima cifra (1, 3, 5, 7, 9) eCi sono 5 scelte per l'ultima cifra (0, 2, 4, 6, 8).
    return T[n]
print(soluzione(3))






