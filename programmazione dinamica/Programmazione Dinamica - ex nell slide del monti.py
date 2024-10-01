"""
slide: PD2 Ex1
"""
def soluzione_pd2_ex1(n):
    T = [0 for _ in range(n+1)]
    T[0] = 1
    T[1] = 2
    for i in range(2,n+1):
        T[i] = T[i-1] + T[i-2]
    return T[n]
#print(soluzione_pd2_ex1(3))


"""
slide : PD2 EX4

"""
def soluzione_pd2_ex4(n):
    T = [0 for _ in range(n+1)]
    T[0] = 1
    T[1] = 2
    T[2] = 4
    for i in range(3,n+1):
        T[i] = T[i-1] + T[i-3] + T[i-2]
    return T[n]


def soluzione_pd2_ex6(A):
    n = len(A)
    T = [0 for _ in range(n+1)]
    T[1] = A[0]
    T[2] = max(A[0],A[1])
    T[3] = max(A[2],T[2])
    for i in range(4,n+1):
        T[i] = max(A[i-1] + T[i-3], T[i-1], T[i-2])
    return T[n]

print(soluzione_pd2_ex6([11,3,8,10,1,32,7]))