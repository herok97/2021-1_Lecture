def mergeSort(n, S):
    h = n // 2
    m = n - h
    if n > 1:
        U = S[:h]
        V = S[h:]
        # print('h', h)
        # print('m', m)
        # print('U', U)
        # print('V', V)
        # print('S', S)
        mergeSort(h, U)
        print('U', U)
        mergeSort(m, V)
        print('V', V)
        merge(h, m, U, V, S)



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

s = [3, 5, 2, 9, 10, 14, 4, 8]
mergeSort(8, s)
print(s)
