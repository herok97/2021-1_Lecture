def kp(i, profit, weight):
    global bestset
    global maxp

    # 현재 가방의 상태 점검
    # 무게를 초과하지 않았고, 이익이 이전의 최대이익보다 컸다면
    if (weight <= W and profit > maxp):
        maxp = profit  # 최대 이익을 업데이트
        bestset = include[:]  # 현재 수납 상태를 저장

    # 현재 넣을지 말지 고민하는 물건이 유망하다면 (넣는 것을 시도해볼거라면)
    if promising(i, weight, profit):
        # 다음 물건을 넣어본다.
        include[i + 1] = 1
        kp(i + 1, profit + p[i + 1], weight + w[i + 1])

        # 다음 물건을 안 넣어본다.
        include[i + 1] = 0
        kp(i + 1, profit, weight)


def promising(i, weight, profit):
    global maxp

    # 가방이 꽉 찼다면, 유망하지 않다고 판단
    if weight >= W:
        return False

    # 가방에 공간이 남았다면, 다음을 점검한다.
    else:
        # 현재 아이템 이후의 아이템들을 하나씩 더해본다.
        j = i + 1

        # bound에 현재 이익 저장
        bound = profit

        # totweight에 현재 무게 저장
        totweight = weight

        # 끝까지 넣어보거나 그 전에 무게가 초과할때까지 넣어본다.
        while j < n and totweight + w[j] <= W:
            totweight = totweight + w[j]
            bound = bound + p[j]
            j += 1

        # 그때까지의 이익과 무게가 저장되었다.
        k = j

        # 끝까지 가기 전에 끝났다면
        if k < n:
            bound = bound + (W - totweight) * p[k] / w[k]
        return bound > maxp


n = 4
W = 16
p = [40, 30, 50, 10]
w = [2, 5, 10, 5]
maxp = 0
include = [0, 0, 0, 0]
bestset = [0, 0, 0, 0]
kp(-1, 0, 0)
print(maxp)
print(bestset)

"""
90
[1, 0, 1, 0]
>>> 
"""

import queue

import queue


class Node:
    def __init__(self, level, weight, profit, bound, include):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.bound = bound
        self.include = include

    def __lt__(self, other):
        return self.bound > other.bound

    def __str__(self):
        return f'level: {self.level} weight: {self.weight} profit: {self.profit} bound: {self.bound} include: {self.include}'


def kp_Best_FS():
    # 최대 이익, best set 정의
    global maxProfit
    global bestset
    temp = n * [0]

    # root node 생성
    v = Node(-1, 0, 0, 0.0, temp)
    # bound 를 기준으로 우선순위를 갖는 큐 생성
    q = queue.PriorityQueue()
    q.put(v)
    while not q.empty():
        # 가장 bound 가 높은 노드를 꺼냄
        v = q.get()
        # 그 노드의 bound 가 maxProfit 보다 높으면 노드분할 진행
        if v.bound >= maxProfit and v.level < n-1:
            u1 = Node(v.level + 1, 0, 0, 0, [])
            u1.weight = v.weight + w[u1.level]
            u1.profit = v.profit + p[u1.level]
            u1.include = v.include[:]
            # 중간에 maxProfit 한 번 갱신
            if u1.weight <= W and u1.profit > maxProfit:
                maxProfit = u1.profit


            # 새로 만든 노드(추가) bound 계산
            u1.bound = compBound(u1)
            # 그 노드의 bound 가 maxProfit 보다 높으면 Enqueue
            if u1.bound >= maxProfit:
                u1.include[u1.level] = 1
                q.put(u1)
                bestset = v.include[:]
            # 새로 만든 노드(제외) bound 계산
            u2 = Node(v.level + 1, 0, 0, 0, [])
            u2.include = v.include[:]
            u2.weight = v.weight
            u2.profit = v.profit
            u2.bound = compBound(u2)
            if u2.bound >= maxProfit:
                q.put(u2)
                bestset = v.include[:]

# 구현


def compBound(u):
    if u.weight >= W:
        return 0
    else:
        # 현재 아이템 이후의 아이템들을 하나씩 더해본다.
        j = u.level + 1

        # bound에 현재 이익 저장
        bound = u.profit

        # totweight에 현재 무게 저장
        totweight = u.weight

        # 끝까지 넣어보거나 그 전에 무게가 초과할때까지 넣어본다.
        while j < n and totweight + w[j] <= W:
            totweight = totweight + w[j]
            bound = bound + p[j]
            j += 1

        # 그때까지의 이익과 무게가 저장되었다.
        k = j

        # 끝까지 가기 전에 끝났다면
        if k < n:
            bound = bound + (W - totweight) * p[k] / w[k]
        return bound


# heap이 minheap이라 bound를 계산하여 -를 하여 리턴한다. 비교를 < maxProfit으로 수행한다.
n = 4
W = 16
p = [40, 30, 50, 10]
w = [2, 5, 10, 5]
include = [0] * n
maxProfit = 0
bestset = n * [0]
kp_Best_FS()
print(bestset)
print(maxProfit)
