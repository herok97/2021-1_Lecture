"""
(1) 6쪽: [실습프로그램] 그래프의 깊이우선검색 알고리즘을 다음 사항을 반영하여
python으로 완성하라. 출력은 (방문순서, 방문노드번호) 되도록 수정한다. 예를 들어, 주
어진 그래프에 대해 다음과 같이 출력되어야 한다. 첫 번째 방문순서는 1로 한다.
1 0
2 1
3 2
4 3
5 4
6 6
7 7
8 5
"""
import utility

e = {0: [1, 2, 3], 1: [2, 5], 2: [3, 4, 5, 6], 3: [4, 6], 4: [6, 7]}
n = 8
a = [[0 for j in range(0, n)] for i in range(0, n)]
for i in range(0, n - 1):
    for j in range(i + 1, n):
        if i in e:
            if j in e[i]:
                a[i][j] = 1
                a[j][i] = 1
utility.printMatrix(a)

visited = n * [0]


def DFS(a, v):
    print(v)
    visited[v] = 1
    for i in range(len(a[v])):
        if a[v][i] == 1 and visited[i] == 0:
            DFS(a, i)


DFS(a, 0)

"""
(2) 18쪽: [실습프로그램] n-Queens 문제 해결 알고리즘을 python으로 완성하여 n=7
문제의 해의 총개수 및 세 번째 해를 출력하라.
"""


def promising(i, col):
    switch = True
    k = 0
    while k < i and switch:
        if col[i] == col[k] or abs(col[i] - col[k]) == i - k:
            switch = False
            # print(f'{col}은 유망하지 않다')
        k += 1
    return switch


def queens(n, i, col):
    if promising(i, col):
        # print(f'{col}은 유망하다.')
        if i == n-1:
            print(col)
        else:
            for j in range(n):
                col[i + 1] = j
                queens(n, i + 1, col)


n = 5
col = n * [0]
queens(n, -1, col)
