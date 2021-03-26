def quickSort(s, low, high):
    if low < high:
        pivot = partition(s, low, high)
        quickSort(s, low, pivot -1)
        quickSort(s, pivot + 1, high)


def partition(s, low, high):
    pivot = s[low]
    j = low
    for i in range(low+1, high+1):
        if s[i] < pivot:
            j += 1
            s[i], s[j] = s[j], s[i]

    s[low], s[j] = s[j], s[low]
    return j

s = [3, 5, 2, 9, 10, 14, 4, 8]
quickSort(s, 0, 7)
print(s)


def prod2(a,b):
    u, v = len(str(a)), len(str(b))

    if a == 0 or b == 0:
        return 0
    elif max(u, v) <= 4:
        return a * b
    else:
        m = max(u, v) // 2
        x, y = a // (10 ** m), a % (10 ** m)
        w, z = b // (10 ** m), b % (10 ** m)
        r = prod2(x+y, w+z)
        p = prod2(x, w)
        q = prod2(y, z)
        return p * (10 ** (2*m)) + (r - p - q) * (10 ** m) + q

a = 1234567812345678
b = 2345678923456789

print(prod2(a,b))
print(a*b)
