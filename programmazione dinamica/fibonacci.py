def fibonacci_Iterativo(n):
    if n <= 1:
        return n
    a = b = 1
    for i in range(2,n+1):
        a, b = b, a+b
    return b

#Ricorsivo + Programmazione Dinamica
def fibonacci_Ricorsivo(n):
    F = [-1]*(n+1)
    def fib(n,F):
        if n<=1 : return 1
        if F[n] == -1:
            a = fib(n-1,F)
            b = fib(n-2,F)
            F[n] = a+b
        return F[n]
    return fib(n,F)

if __name__ == "__main__":
    print(fibonacci_Iterativo(6))
    print(fibonacci_Ricorsivo(6))