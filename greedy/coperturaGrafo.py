def copertura1(G):
    n = len(G)
    E = [(x,y) for x in range(n) for y in G[x] if x < y]
    print("E:", E)
    presi = [0] * n
    sol = []
    for a,b in E:
        if presi[a] == presi[b] == 0:
            sol.append(a)
            sol.append(b)
            presi[a] = presi[b] = 1
    return sol

if __name__ == "__main__":
    G = [
        [4],
        [3,6],
        [4,5,7,9,11],
        [1,7,8],
        [0,2,10],
        [2],
        [1,7,10],
        [3,6],
        [3],
        [2],
        [4,6],
        [2]
    ]

    print(copertura1(G))