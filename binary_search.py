# We assume A is sorted
def recursive_binsearch(A,k) :
    size = len(A)
    if size == 0 :
        return 0
    if size==1 :
        if A[0] == k :
            return k
        else :
            return 0
    
    if k < A[size//2]:
        return binsearch(A[:size//2],k)
    else:
        return binsearch(A[size//2:],k)

