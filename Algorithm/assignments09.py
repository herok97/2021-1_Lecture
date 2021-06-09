import math


class Heap(object):
    n = 0

    def __init__(self, data):
        self.data = data
        # heap size를 하나 줄여야 한다. 인덱스는 1부터. 인덱스의 2* 연산 가능하도록.
        self.n = len(self.data) - 1
        # 힙의 최대 깊이 저장
        self.depth = int(round(math.log2(self.n)))

    def addElt(self, elt):
        # 맨 마지막 인덱스에 추가함
        self.data.append(elt)

        # 길이 1 늘림
        self.n += 1

        # sift Up 진행
        self.siftUp(self.n)

    def print(self):
        for depth in range(0, self.depth + 1):
            try:
                for index in range(2 ** depth, 2 ** (depth + 1)):
                    print(self.data[index], end='\t')
                print()
            except:
                print(end='\n')

    def siftUp(self, i):
        while (i >= 2):
            # 부모 노드와의 값 비교
            if self.data[i // 2] < self.data[i]:
                self.data[i // 2], self.data[i] = self.data[i], self.data[i // 2]
                i = i // 2

            else:
                break

    def siftDown(self, i):
        while i <= 2 ** self.depth - 1:
            try:
                if self.data[2 * i] > self.data[i]:
                    direction = 0
            except IndexError:
                break

            try:
                if self.data[2 * i + 1] > self.data[2 * i]:
                    direction = 1
            except IndexError:
                pass

            try:
                if direction == 0:
                    self.data[2 * i], self.data[i] = self.data[i], self.data[2 * i]
                    i = 2 * i
                else:
                    self.data[2 * i + 1], self.data[i] = self.data[i], self.data[2 * i + 1]
                    i = 2 * i + 1
                del direction
            except Exception:
                break

    def makeHeap2(self):
        # 맨 아래 깊이 - 1 부터 한 칸씩 올라오면서, 깊이 0까지
        for depth in range(self.depth, -1, -1):
            # 각 깊이별로 모든 노드에 대해
            for index in range(2 ** depth, 2 ** (depth + 1)):
                try:
                    data = self.data[index]
                    self.siftDown(index)
                except:
                    break

    def makeHeap1(self):
        for i in range(1, self.n + 1):
            self.siftUp(i)

    def root(self):
        if self.n > 0:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            keyout = self.data[-1]
            del self.data[-1]
            self.siftDown(1)
            return keyout

    def removeKeys(self):
        S = []
        for i in range(self.n):
            S.append(self.root())
        return S


def heapSort(a):
    return Heap(a).removeKeys()


# 인덱스를 간단히 하기 위해 처음 엘리먼트 0 추가
a = [0, 11, 14, 2, 7, 6, 3, 9, 5]
b = Heap(a)
b.makeHeap2()
print(b.data)
b.addElt(50)
print(b.data)
s = heapSort(a)
print(s)

print()

a = [0, 11, 14, 2, 7, 6, 3, 9, 5]
b = Heap(a)
b.makeHeap1()
print(b.data)
s = heapSort(a)
print(s)
