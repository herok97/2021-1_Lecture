# (1) 실습동영상 p6_dp_OBStree_alignment.pptx 10쪽
# [실습프로그램] 최적이진검색트리 구축 알고리즘을 python으로 완성하라.
#
# import utility
#
#
# class Node:
#     def __init__(self, data):
#         self.l_child = None
#         self.r_child = None
#         self.data = data
#
#
# def tree(key, r, i, j):
#     k = r[i][j]
#     if k == 0:
#         return
#     else:
#         p = Node(key[k])
#         p.l_child = tree(key, r, i, k - 1)
#         p.r_child = tree(key, r, k + 1, j)
#         return p
#
#
# # 데이터 입력
# key = [" ", "A", "B", "C", "D", "E"]
# p = [0, 4 / 15, 5 / 15, 1 / 15, 3 / 15, 2 / 15]
# n = len(p) - 1
#
# # a와 r의 초기값 설정
# a = [[0 for j in range(0, n + 2)] for i in range(0, n + 2)]
# r = [[0 for j in range(0, n + 2)] for i in range(0, n + 2)]
#
# for i in range(1, n + 1):
#     a[i][i - 1] = 0
#     a[i][i] = p[i]
#     r[i][i] = i
#     r[i][i - 1] = 0
#
# a[n + 1][n] = 0
# r[n + 1][n] = 0
#
# # 구현
# for diagonal in range(1, n):
#     for i in range(1, n - diagonal + 1):
#         j = i + diagonal
#         k_ = None
#         tmp = 0
#         for k in range(i, j + 1):
#             if tmp == 0 or tmp > a[i][k - 1] + a[k + 1][j]:
#                 tmp = a[i][k - 1] + a[k + 1][j]
#                 k_ = k
#         a[i][j] = tmp + sum(p[i:j + 1])
#         r[i][j] = k_
#
# # 결과 출력
# utility.printMatrixF(a)
# print()
# utility.printMatrix(r)
#
# root = tree(key, r, 1, n)
# utility.print_inOrder(root)
# print()
# utility.print_preOrder(root)

# (2) 실습동영상 p6_dp_OBStree_alignment.pptx 29쪽
# [실습프로그램] DNA 서열 맞춤 알고리즘 python으로 완성하라.
# 아래의 데이터를 이용한다.
import utility

a = ['A', 'A', 'C', 'A', 'G', 'T', 'A', 'C', 'C']

b = ['T', 'A', 'C', 'G', 'T', 'T', 'C', 'A']

m = len(a)
n = len(b)
table = [[0 for j in range(0, n + 1)] for i in range(0, m + 1)]
minindex = [[(0, 0) for j in range(0, n + 1)] for i in range(0, m + 1)]

for j in range(n - 1, -1, -1):
    table[m][j] = table[m][j + 1] + 2

for i in range(m - 1, -1, -1):
    table[i][n] = table[i + 1][n] + 2

# 테이블 생성 구현
for row in range(m-1, -1, -1):
    for col in range(n-1, -1, -1):
        if a[row] == b[col]:
            penalty = 0
        else:
            penalty = 1

        if table[row+1][col+1] + penalty < table[row+1][col]+2:

            # 대각선으로 움직인 경우
            if table[row+1][col+1] + penalty < table[row][col+1]+2:
                table[row][col] = table[row+1][col+1] + penalty
                minindex[row][col] = row+1, col+1

            # 왼쪽으로 움직인 경우
            else:
                table[row][col] = table[row][col+1]+2
                minindex[row][col] = row, col + 1
        else:
            
            # 위쪽으로 움직인 경우
            if table[row+1][col]+2 < table[row][col+1] + 2:
                table[row][col] = table[row+1][col] +2
                minindex[row][col] = row + 1, col
            # 왼쪽으로 움직인 경우
            else:
                table[row][col] = table[row][col+1]+2
                minindex[row][col] = row, col + 1

utility.printMatrix(table)


x = 0
y = 0

while (x < m and y < n):
    tx, ty = x, y
    print(minindex[x][y])
    (x, y) = minindex[x][y]
    if x == tx + 1 and y == ty + 1:
        print(a[tx], " ", b[ty])
    elif x == tx and y == ty + 1:
        print(" - ", " ", b[ty])
    else:
        print(a[tx], " ", " -")
