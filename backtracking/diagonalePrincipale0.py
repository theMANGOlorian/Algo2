def ex3_esame(n):

    def BT(M,i,j):    
        if i == n :
            for row in M:
                print(row)
            print("\n")
            return
        
        for k in [0,1,2,3]:
            M[i][j] = k
            if (i == j and k == 0) or ((i-j == 1) and (k+M[i-1][j+1] == 3)) or (i!=j and i-j != 1):                
                if j < (n-1):
                    BT(M,i,j+1)
                else:
                    BT(M,i+1,0)

    M = [[0 for i in range(n)] for j in range(n)]
    BT(M,0,0)

ex3_esame(2)



