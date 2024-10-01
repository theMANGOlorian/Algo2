'''
Abbiamo una lista di n attivit`a da eseguire:
• ciascuna attivit`a `e caratterizzata da una coppia con il suo tempo di inizio ed il suo tempo di fine
• due attivit`a sono compatibili se non si sovrappongono.
Vogliamo trovare un sottoinsieme di attivit`a compatibili di massima cardinalit`a.
'''

def selezione_attività(lista):
    lista.sort( key = lambda x:x[1])
    libero = 0
    soluzione = []
    for inizio, fine in lista:
        if libero <= inizio:
            soluzione.append((inizio,fine))
            libero = fine

    return soluzione

if __name__ == "__main__":
    lista = [(0,6),(1,4),(3,5),(3,8),(4,7),(5,9),(6,10),(8,11)]
    print(selezione_attività(lista))