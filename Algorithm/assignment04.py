def allShortestPath(q, n):
    import copy
    d = copy.deepcopy(q)
    p = [[0 for i in range(0, n)] for j in range(0, n)]

    # D_k
    for k in range(0, n):
        # 행
        for i in range(0, n):
            # 열
            for j in range(0, n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    p[i][j] = k + 1
    return d, p


def printMatrix(d):
    n = len(d[0])
    for i in range(0, n):
        for j in range(0, n):
            print(d[i][j], end=" ")
        print()


def path(p, q, r):
    if p[q-1][r-1] != 0:
        path(p, q, p[q-1][r-1])
        print(f'v{p[q-1][r-1]}', end=' ')
        path(p, p[q-1][r-1], r)


inf = 1000
g = [[0, 1, inf, 1, 5],
     [9, 0, 3, 2, inf],
     [inf, inf, 0, 4, inf],
     [inf, inf, 2, 0, 3],
     [3, inf, inf, inf, 0]]

d, p = allShortestPath(g, 5)

printMatrix(g)
print()
printMatrix(d)
print()
printMatrix(p)

path(p, 5, 3)

