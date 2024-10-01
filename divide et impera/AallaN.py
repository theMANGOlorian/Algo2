"""
Dati due interi a ed n, progettare un algoritmo che calcoli
a^n in tempo theta(log n) (le uniche operazioni aritmetiche permesse
sono +,*,e //)
"""

def power(a,n):
    if n == 0:
        return 1
    x = power(a,n//2)
    if n % 2:
        return x*x*a
    return x*x

if __name__ == "__main__":
    a, n = 3,12
    print(power(a,n))
