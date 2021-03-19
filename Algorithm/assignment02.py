class MemoryCalculator:
    def __init__(self):
        self.total_memory = 0

    def add_memory(self, *args):
        for arg in args:
            self.total_memory += len(arg)
            print(f'<추가> {len(arg)}의 저장공간 추가 || 사용중인 저장공간: {self.total_memory}')
        return args

    def del_memory(self, *args):
        for arg in args:
            self.total_memory -= len(arg)
            print(f'[삭제] {len(arg)}의 저장공간 삭제 || 사용중인 저장공간: {self.total_memory}')
            del arg


memCal01 = MemoryCalculator()
memCal02 = MemoryCalculator()


def mergeSort(n, S):
    h = n // 2
    m = n - h
    if n > 1:
        U, V = memCal01.add_memory(S[:h], S[h:])
        mergeSort(h, U)
        mergeSort(m, V)
        merge(h, m, U, V, S)
        memCal01.del_memory(U, V)


def merge(h, m, U, V, S):
    i, j, k = 0, 0, 0
    while i < h and j < m:
        # print(S)
        if (U[i] < V[j]):
            S[k] = U[i]
            i += 1
        else:
            S[k] = V[j]
            j += 1
        k += 1

    if (i >= h):
        while j < m:
            S[k] = V[j]
            k += 1
            j += 1
    else:
        while i < h:
            S[k] = U[i]
            k += 1
            i += 1


def mergeSort2(S, low, high):
    if low < high:
        mid = (low + high) // 2
        mergeSort2(S, low, mid)
        mergeSort2(S, mid + 1, high)
        merge2(S, low, mid, high)


def merge2(S, low, mid, high):
    i, j, k = low, mid + 1, 0
    U = [0 for i in range(high - low + 1)]
    memCal02.add_memory(U)
    while i <= mid and j <= high:
        if S[i] < S[j]:
            U[k] = S[i]
            i += 1
        else:
            U[k] = S[j]
            j += 1
        k += 1
    if i > mid:
        while j <= high:
            U[k] = S[j]
            j += 1
            k += 1
    else:
        while i <= mid:
            U[k] = S[i]
            i += 1
            k += 1

    for i, j in enumerate(range(low, high + 1)):
        S[j] = U[i]
    memCal02.del_memory(U)


# merge1
print("[합병정렬(Merge sort)1]")
data = [3, 16, 13, 1, 9, 2, 7, 5, 8, 4, 11, 6, 15, 14, 10, 12]
print(f'input={data}')
mergeSort(len(data), data)
print(f'output={data}')

print('\n \n')

# merge2
print("[합병정렬(Merge sort)2]")
[3, 16, 13, 1, 9, 2, 7, 5, 8, 4, 11, 6, 15, 14, 10, 12]
print(f'input={data}')
mergeSort2(data, 0, 15)
print(f'output={data}')
