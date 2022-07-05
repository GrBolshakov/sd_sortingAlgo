import math
import random

def introSort(a: list, d: int) -> list:
    n = len(a)
    if n <= 1:
        return
    elif d == 0:
        heapSort(a)
    else:
        p = partition(a)
        a1 = a[:p]
        a2 = a[p+1:n]
        introSort(a1, d-1)
        introSort(a2, d-1)
        for i in range(0, len(a1)):
            a.insert(i, a1[i])
            a.pop(i+1)
        for i in range(0, len(a2)-1):
            a.insert(i+p+1, a2[i])
            a.pop(i+p+2)

def heapSort (a: list) -> None:
    END = len(a)
    for k in range ( int(math.floor(END/2)) - 1, -1, -1):
        heapify(a, END, k)

    for k in range(END, 1, -1):
        swap(a, 0, k-1)
        heapify(a, k-1, 0)

def partition(a: list) -> int:
    hi = len(a)-1
    x = a[hi]
    i = 0
    for j in range(0, hi-1):
        if a[j] <= x:
            swap(a, i, j)
            i = i + 1
    swap(a, i, hi)
    return i

def swap(a: list, i: int, j: int) -> None:
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

def heapify(a: list, iEnd: int, iRoot: int) -> None:
    iL = 2*iRoot + 1
    iR = 2*iRoot + 2
    if iR < iEnd:
        if (a[iRoot] >= a[iL] and a[iRoot] >= a[iR]):
            return

        else:
            if(a[iL] > a[iR]):
                j = iL
            else: 
                j = iR
            swap(a, iRoot, j)
            heapify(a, iEnd, j)
    elif iL < iEnd:
        if (a[iRoot] >= a[iL]):
            return
        else:
            swap(a, iRoot, iL)
            heapify(a,iEnd,iL)

    else: 
        return


a = []
for i in range(0,10):
    n = random.randint(1,99)
    a.append(n)

print(a)
introSort(a,2)
print(a)