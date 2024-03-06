# BJC, Original Author
# 8/28/23
# Shaker Sort, Counting Sort, Create Random List, Card Shuffling
# Exponents Test Question



A = [3,4,2,1]
def BubbleSort(A):
    changing = True
    while changing:
        changing = False
        for i in range(0,len(A)-1):
            if A[i]>A[i+1]:
                A[i],A[i+1]=A[i+1],A[i]
                changing = True
        for i in range(len(A)-2, -1, -1):
            if A[i]>A[i+1]:
                A[i],A[i+1]=A[i+1],A[i]
                changing = True

# Counting Sort
B = [5,0,4,5,6,7,6,5]
F = [0,0,0,0,0,0,0]
# Frequency list tells us how many there are, which results in an extremely
# fast sort
# This counting sort is actually N, not Nsquared



#Be able to recreate lines 33-37 for exam
def CountingSort(A):
    F = [0] * len(A) #if there was a value of 25, this would crash. Theres not
    # room in the F list to hold it. Need to store as many as there are.
    for v in A:
        F[v]+=1
    k=0
    for i in range(len(F)):
        reps = F[i]
        value = i
        for j in range(reps):
            A[k] = value
            k+=1

import random
def CreateRandomList(size):
    A=[]
    for i in range(size):
        r = random.randrange(0,size)
        A.append(r)
    return A

# For a card shuffle, this would be N cubed
def CreateUniqueRandomList(size):
    A=[]
    while len(A)<size:
        r = random.randrange(0,size)
        if r not in A:
            A.append(r)

    return A



