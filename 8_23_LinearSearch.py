A = [10,3,7,1,12]

#Linear Search Algorithm

def FindItem(A,x):
    for i in range(len(A)):
        if A[i] == x:
            return i
        return -1
    #return A.index(x) # Apparently this could work

# Binary Search, could throw out half the search .
B = [2,3,6,7,9,14,18,19,23]