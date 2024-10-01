"""
[Stampa]
Progettare un algoritmo che dato un intero n >= 3 stampa tutte le
stringhe ternarie lunghe n in cui non compaiono 3 elementi 
adiacenti la cui somma sia un numero pari. ad esempio:
per n = 4 vanno stampate le seguenti 21 stringhe:

0010,0012,0100,0102,0120,0122,0210,0212,1001,1021,1111,
1201,1221,2010,2012,2100,2102,2120,2122,2210,2212

L'algoritmo deve avere complessità O(n*S(n))  dove S(n) è il 
numero di stringhe da stampare.
"""
def solution(n):
    def backtrack(list,length,n):
        if length == n:
            print(''.join(list)) #O(n)
            return

        for i in d: #costante
            list.append(i)   
            if isValid(list,length+1):
                backtrack(list,length+1,n)
            list.pop()
    d = ['0','1','2']
    backtrack([],0,n)
#le stringhe da stampare sono al più 3^n
n = 4
def isValid(list,len):
    #O(1)
    if len < 3:
        return True
    if (int(list[-1]) + int(list[-2]) + int(list[-3])) % 2 == 0:
        return False
    return True

#N.B. n DEVE essere >= 0

solution(7)
