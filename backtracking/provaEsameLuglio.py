def elementiDistinti(L):
    M = []
    for i in L:
        if i not in M:
            M.append(i)
    return M

def soluzione3(A):
    def backtrack(lista,index,M):

        print(lista)

        if index == n:
            return

        for i in M:
            if lista == [] or i > lista[-1]:
                lista.append(i)
                backtrack(lista,index+1,M)
                lista.pop()
    M = elementiDistinti(A)
    n = len(M)
    backtrack([],0,M)

A = [5,1,2]
soluzione3(A)
print("-----")
A = [1,3,3,2,2,3,2,1,1,1,1]
soluzione3(A)
print("-----")
