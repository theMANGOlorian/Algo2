def tasselamento(n):
    T = [0]*(n+1)
    T[1],T[2] = 1,2
    for i in range(3,n+1):
        T[i] = T[i-1] + T[i-2]
    return T[n]

print(tasselamento(7))