# BJC, Original Author 8/21/24
# This is called an n cubed algorithm.... it would take forever
# A more complex algorithm would pass over the list one time.
# We are looking at algorithms and categorizing them as best to worst
A=[2,-3,4,1,-4,6,-5,3,3,-7,4]

def MaxSubsequence(A):
    bests = 0
    beste = 0
    bestsum = A[0]
    if not A:
        return -1
    for s in range(0, len(A)):
        for e in range( s, len(A)):
            xsum = 0
            for i in range(s, e+1):
                xsum += A[i]
                if xsum > bestsum:
                    bestsum = xsum
                    bests = s
                    beste = e
    return bests, beste
