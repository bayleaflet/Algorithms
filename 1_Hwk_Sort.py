# Homework Assignment 1 - Sorting Methods

import random

def main():

    # Create random list
    def CreateRandomList(size):
        A = []
        for i in range(size):
            r = random.randrange(0,size)
            A.append(r)
        return A

   #Bubble Sort
    def BubbleSort(A):
        changing = True
        while changing:
            changing = False
            for i in range(0,len(A)-1):
                if A[i]>A[i+1]:
                    A[i],A[i+1]=A[i+1],A[i]
                    changing = True
        return A

    # Shaker Sort
    def ShakerSort(A):
        changing = True
        while changing:
            changing = False
            for i in range(0,len(A)-1):
                if A[i]>A[i+1]:
                    A[i],A[i+1]=A[i+1],A[i]
                    changing = True
            for i in range(len(A)-2,-1,-1):
                if A[i]>A[i+1]:
                    A[i],A[i+1]=A[i+1],A[i]
                    changing = True
        return A

    # Counting Sort
    def CountingSort(A):
        F = [0] * len(A)
        for v in A:
            F[v]+=1
        k=0
        for i in range(len(F)):
            reps = F[i]
            value = i
            for j in range(reps):
                A[k] = value
                k+=1
        return A

    testlist = CreateRandomList(12)
    print("Original List: ", testlist)
    py_sorted = sorted(testlist)
    print("Python sort:   ", py_sorted)
    print("Bubble sort:   ", BubbleSort(testlist))
    print("Shaker sort:   ", ShakerSort(testlist))
    print("Counting sort: ", CountingSort(testlist))


if __name__ == "__main__":
    main()
