def conta_alberi_binari(n):
    T = [0] * (n + 1)
    
    T[0] = 1 
    
    # Costruire l'array C fino a C(n)
    for nodo in range(1, n + 1):
        for left in range(nodo):
            right = nodo - 1 - left
            T[nodo] += T[left] * T[right]
    
    return T[n]


print(conta_alberi_binari(1))
print(conta_alberi_binari(2)) 
print(conta_alberi_binari(3))  
print(conta_alberi_binari(4))  
print(conta_alberi_binari(5))  
