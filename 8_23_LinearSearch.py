# BJC, 8/23/23
# Original Author

A = [10,3,7,1,12]

#Linear Search Algorithm

def FindItem(A,x):
    for i in range(len(A)):
        if A[i] == x:
            return i
        return -1
    return A.index(x)



