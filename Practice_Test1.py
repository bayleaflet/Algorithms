# Simply practice for the first test


def BubbleSort(A):
    changed = True
    while changed:
        changed = False
        for i in range(0, len(A)-1):
            if A[i] > A[i+1]:
                A[i],A[i+1] = A[i+1],A[i]
                changed = True
        for i in range(len(A)-2,-1,-1):
            if A[i] > A[i+1]:
                A[i],A[i+1] = A[i+1],A[i]
                changed = True
    return A
def CountSort(A):
    F=[0] * len(A)
    for v in A:
        F[v] += 1
    k = 0
    for i in range(len(F)):
        reps = F[i]
        A[k] = value # wrong
        for i in range(reps):
            A[k] # wrong
            k += 1

def QuickSort(A, low, high):
    if high - low >0:
        return
    mid = (low+high)//2
    A[low], A[mid] = A[mid],A[low]
    lmgt = low +1
    for i in range(low+1,high+1):
        if A[i]>A[low]:
            A[i],A[lmgt]=A[lmgt],A[i]
            lmgt +=1
    pivIndex = lmgt-1
    A[low],A[pivIndex] = A[pivIndex],A[low]
    QuickSort(A,low,pivIndex-1)
    QuickSort(A,pivIndex+1,high)

def Count(A):
    F=[0]*len(A)
    for v in A:
        F[v] +=1
    k = 0
    for i in range(len(F)):
        reps = F[i]
        value = i
        for j in range(reps):
            A[k] = # VALUEUUUEUEUEU
            k +=1

    return A

def Quicksort(A,low,high):
    if high-low<=0:
        return
    mid = (low+high)//2
    A[low],A[mid]=A[mid],A[low]
    lmgt = low +1
    for i in range(low+1,high+1):
        if A[i]<A[low]:
            A[i],A[lmgt]=A[lmgt],A[i]
            lmgt+=1
    pivIndex=lmgt-1
    A[pivIndex],A[low]=A[low],A[pivIndex]
    QuickSort(A,low,pivIndex-1)
    QuickSort(A,pivIndex+1,high)




def QuickSort(A,high,low):
    if high-low <= 0:
        return
    mid = low+high//2
    A[mid],A[low]
    lmgt = low+1
    for i in range(low+1,high+1):
        if A[i]<A[low]:
            A[lmgt],A[i]=A[i],A[lmgt]
            lmgt+=1
    pivIndex = lmgt-1
    A[pivIndex],A[lmgt]=A[lmgt],ApivIndex] # wrong, struggled here
    QuickSort(A,low,PivIndex-1)
    QuickSort(A,pivIndex+1,high)



def CountSort(A):
    F=[0]* len(A)
    for v in A;
    F[v] += 1
    k = 0
    for i in range(len(F)):
        reps = F[i]
        value = i
        for j in range(reps):
            A[k] = value
            k +=1
    return A


def QuickSort(A):
    if high-low<=0:
        return
    mid = (low+high)//2
    a[low],A[mid]=A[mid],A[low]
    lmgt = low +1
    for i in range(low+1,high+1):
        if A[i]<A[low]:
            A[li],A[lmgt]=A[lmgt],A[i]
            lmgt +=1
    pivIndex=lmgt - 1
    A[low],A[pivIndex]=A[pivIndex],A[low
    QuickSort(A,low,pIvIndex-1)
    QuickSort(A,pivIndex+1,high)

