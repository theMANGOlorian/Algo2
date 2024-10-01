"""
abbiamo un gruppo di n amici che debbono pernottare presso un
hotel. L'hotel dispone di stanze da 1,2,3 posti letto. progettare
un algoritmo che dato l'intero n calcola quante diverse allocazioni
delle n persone sono disponibili.

in tempo O(n)
"""

""" Algoritmo iterativo + PROGRAMMAZIONE DINAMICA """
def algo(n):
    T = [0] * (n+1) #tabella monodimesionale
    for i in range(n+1):
        if i==0 or i==1:
            T[i] = 1
        elif i==2:
            T[i] = 2
        else:
            T[i] = T[i-1] + (i-1)*T[i-2] + ((i-1)*(i-2)//2)*T[i-3]
    return T[n]

"""
T[i] rappresenta il numero di modi in cui i amici possono essere
sistemati nelle stanze dell'hotel.
Per calcolare T[i] si considerano 3 casi:
1. La persona i finisce in una stanza da sola: in questo caso devi
    sistemare i-1 persone, il che puo essere fatto in T[i-1]
2. La persona i finisce in una stanza con un'altra persona: ci sono
    i-1 modi per scegliere con chi la persona i condividerò la stanza
    una volta scelta questa persona, divi sistemare le restanti i-2 persone
    il che puo essere fatto in T[i-2] modi
3. la persona i finisce con due altre persone: in questo caso, ci sono
    (i-1)*(i-2)//2 modi per scegliere le due persone con cui i ocndividerà
    la stanza. una volta scelte queste due, devi sistemare le restanti i-3
    persone il che può essere fatto in T[i-3] modi.

N.B.
come sono arrivato alla soluzione (i-1)*(i-2)//2
C(n,k) "n scelgo k" dove n = i e k = 2 persone
C(n,k) = n!/[k!*(n-k)!]
sostituendo i valori nella formula otteniamo : [(i-1)*(i-2)]//2  (vedi img. stanzeAlbergo_Calcoli.jpg)
"""

if __name__ == "__main__":
    for n in range(1,10):
        print(f"n = {n}: ",algo(n))
