def soluzione(A):
    n = len(A)
    T = [0]*n
    for i in range(n):
        if i == 0:
            T[0] = A[0]
        elif i == 1:
            T[1] = max(A[0],A[1])
        else:
            T[i] = max(T[i-1],T[i-2] + A[i])
    print(T)
    return T[n-1]

A = [3,2,7,10]

print(soluzione(A))