"""
[CONTA]
"""

def binomial_coefficient(n, k):
    # Calcola il coefficiente binomiale utilizzando la formula del fattoriale
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)

def count_equal_sum_binary_strings(n):
    # Calcola il numero di stringhe binarie con somme uguali
    result = 0
    for i in range(n+1):
        result += binomial_coefficient(n, i) ** 2
    return result

# Test dell'algoritmo
n = 5
print(count_equal_sum_binary_strings(n))