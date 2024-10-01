"""
[CONTA]
Pavimentazione: Dobbiamo pavimentare un corridoio di dimen-
sione 4*n e disponiamo di mattonelle di dimensioni 4*1. Possiamo inserire
una mattonella o in orizzontale o in verticale. Vogliamo contare i diversi modi
che ci sono per pavimentare il corridoio.
Ad esempio:
Per n = 3 la riposta `e 1 in quanto l’unica pavimentazione possibile consiste
nel sistemare tre mattonelle in verticale.
per n = 5 la risposta `e 3. Possiamo infatti inserire una prima mattonella
in verticale e le altre 4 in orizzontale oppure inserire l’ultima mattonella
in verticale e le altre 4 in orizzontale o inserire semplicemente tutte le 5
mattonelle in verticale.
Progettare un algoritmo basato sulla programmazione dinamica che dato n ri-
solve il problema in tempo theta(n).
"""

def soluzione(n):
    T = [0]*(n+1)
    T[1] = 1
    T[2] = 1
    T[3] = 1
    T[4] = 2
    for i in range(5,n+1):
        T[i] = T[i-1] + T[i-4]
    return T[n]

print(soluzione(20))

"""
infatti:
se i<=3 posso solo inserire le mattonelle in verticale,
se i=4 posso inserire le 4 mattonelle o tutte in verticale o
    tutt in orizzonatale
se i>4 se l'ultima mattonella è orizzonatale allora ho T[i-1] modi
    di inserire le altre mentre se l'ultima mattonella è orizzonale allora ho T[i-4] modi di
    inserire le altre
"""