def algo(A, i, C):
    if i == 0 or C == 0:
        return 0, []

    lascio, files_lasciati = algo(A, i-1, C)
    if A[i-1] > C:
        return lascio, files_lasciati

    prendo, files_presi = algo(A, i-1, C - A[i-1])
    prendo += A[i-1]
    files_presi.append(i-1)

    if prendo > lascio:
        return prendo, files_presi
    else:
        return lascio, files_lasciati

def algo2(A,C):
    n = len(A)
    T = [ [0]*(C+1) for i in range(n+1)]
    for i in range(1,n+1):
        for c in range(C+1):
            if c < A[i-1]:
                T[i][c] = T[i-1][c]
            else:
                T[i][c] = max( T[i-1][c], A[i-1] + T[i-1][c-A[i-1]])
    return T[n][C]
if __name__ == "__main__":
    C = 8
    A = [2,3,5]
    capacita_massima, files_selezionati = algo(A, len(A), C)
    print("Massima capacità:", capacita_massima)
    print("Files selezionati:", [A[i] for i in files_selezionati])


    print(algo2(A,C))