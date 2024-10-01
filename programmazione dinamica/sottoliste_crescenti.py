"""
Esercizio 2. [Conta]
Data una lista S di cifre decimali, vogliamo calcolare il numero di sottoliste crescenti che è possibile ottenere cancellando da S 
un numero arbitrario di elementi.
Ad esempio, dato S=[3,1,3,9,2] la risposta deve essere 11. Infatti, le sottoliste crescenti di S sono:
[9],[3],[1],[3],[3,9],[1,2],[1,9],[1,3],[3,9],[2],[1,3,9]
Si noti che alcune sottoliste compaiono più volte poiché possono essere ottenute in modi diversi.
Progettare un algoritmo che risolva il problema in tempo O(n).
"""
"""
Spiegazione:
Innanzitutto, creeremo un array dp di lunghezza uguale a quella della lista S. 
L'elemento dp[i] conterrà il numero di sottoliste crescenti che terminano con l'elemento S[i].
Inizializziamo tutti gli elementi di dp a 1, poiché ogni singolo elemento è una sottolista crescente di lunghezza 1. 
Quindi, per ogni coppia di indici i e j tali che 0 <= i < j < len(S), se S[j] > S[i], incrementiamo dp[j] di dp[i]. 
Questo perché possiamo estendere tutte le sottoliste crescenti che terminano in S[i] aggiungendo l'elemento S[j].
Infine, sommiamo tutti gli elementi di dp per ottenere il risultato finale.
"""

def count_increasing_sublists(S):
    n = len(S)
    dp = [1] * n
    for i in range(n): # Θ(n)
        for j in range(i): # Iterara al più a 9
            if S[j] < S[i]:
                dp[i] += dp[j]
    return sum(dp)

"""
## BACKTRACKING ##
stampare tutte le sottoliste crescenti che è possibile ottenere cancellando un numero 
arbitrario di elementi da una lista SS di nn cifre decimali, possiamo utilizzare 
un approccio di backtracking. L'obiettivo è progettare un algoritmo che funzioni in tempo 
O(nS(n)), dove S(n) è il numero di sottoliste da stampare.

"""
def stampa_sottoliste_crescenti(S):    
    def backtrack(start, path):
        length = len(S)
        # Stampiamo ogni percorso valido trovato
        if path:
            print(path)
        
        # Esploriamo tutte le possibili sottoliste
        for i in range(start, length):
            if not path or S[i] > path[-1]:
                path.append(S[i])
                backtrack(i + 1, path)
                path.pop()  
    
    backtrack(0, [])

# Esempio di utilizzo
S = [3,1,2]

#Conta (PD)
print(count_increasing_sublists(S))
#Stampa (BT)
stampa_sottoliste_crescenti(S)






