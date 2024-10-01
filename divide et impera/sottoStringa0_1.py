"""
conta le sottostrighe si S che cominciano con 0 e finiscono con 1
"""
def sottoStringa0_1(S,i,j):
    if i == j:
        if S[i] == '0': return (1,0,0)
        else: return (0,1,0)
    m = (i+j)//2
    zs, us, ts = sottoStringa0_1(S,i,m)
    zd, ud ,td = sottoStringa0_1(S,m+1,j)
    return zs + zd, us + ud, ts + td + zs * ud


if __name__ == "__main__":
    stringa = "001"
    print(sottoStringa0_1(stringa,0,len(stringa)-1))

"""
Complessità temporale theta(n)
"""