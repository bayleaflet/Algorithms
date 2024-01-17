# Merge Sort, Quicksort, and Modified Quick Sort
# 8/30/23, BJC Original Author

import random

def main():
    A = CreateRandomList(8)
    B = A[:]
    B.sort()
    QuickSort(A,0,len(A)-1)
    if B!=A:
        print ("Error with Quicksort")
    C = CreateRandomList(8)
    D = C[:]
    D.sort()
    ModifiedQuickSort(C,0,len(C)-1)
    if D!=C:
        print ("Error with Modified QuickSort")
    E = CreateRandomList(8)
    F = E[:]
    F.sort()
    MergeSort(E) #error right here
    if F!=E:
        print ("Error with Merge Sort" + str(F) + "   " + str(E))


# Create random list
def CreateRandomList(size):
    A = []
    for i in range(size):
        r = random.randrange(0,size)
        A.append(r)
    return A

# Modified QuickSort, where a midpoint is calculated in case the list given is
# mostly sorted.
def ModifiedQuickSort(A, low, high):
    if high - low <= 0:
        return
    mid = (low + high)//2
    A[low], A[mid] = A[mid], A[low]
    lmgt = low + 1
    for i in range(low+1, high+1):
        if A[i] < A[low]:
            A[i], A[lmgt] = A[lmgt], A[i]
            lmgt += 1
    pivIndex = lmgt-1
    A[low], A[pivIndex] = A[pivIndex], A[low]
    # Recurse
    QuickSort(A, low, pivIndex-1)
    QuickSort(A, pivIndex+1, high)

# Quick Sort
def QuickSort(A, low, high):
    if high - low <= 0:
        return
    # lmgt = left most greater than
    lmgt = low + 1
    for i in range(low+1, high+1):
        if A[i] < A[low]:
            A[i], A[lmgt] = A[lmgt], A[i]
            lmgt += 1
    pivotIndex = lmgt-1
    A[low], A[pivotIndex] = A[pivotIndex], A[low]
    # Recurse
    QuickSort(A, low, pivotIndex-1)
    QuickSort(A,pivotIndex+1,high)

def MergeSort(A):
    if len(A)<=1:
        return
    L = A[0:len(A)//2]
    R = A[len(A)//2:len(A)]
    MergeSort(L)
    MergeSort(R)
    k = 0
    i = 0
    j = 0
    while i<len(L) and j<len(R):
        if L[i]<=R[j]:
            A[k]=L[i]
            k+=1
            i+=1
        else:
            A[k] = R[j]
            k+=1
            j+=1
    while i<len(L):
        A[k]=L[i]
        k+=1
        i+=1
    while j<len(R):
        A[k]=R[j]
        k+=1
        j+=1

if __name__ == "__main__":
    main()
