# We assume A is sorted
def recursive_binsearch(A,k) :
    A = sorted(A)
    size = len(A)
    if size == 0 :
        return 0
    if size==1 :
        if A[0] == k :
            return k
        else :
            return 0
    
    if k < A[size//2]:
        return recursive_binsearch(A[:size//2],k)
    else:
        return recursive_binsearch(A[size//2:],k)


if __name__ == '__main__':
    # Test the fun
    import random
    A = [4,5,7,54,234,73,5,8,35,8,35,8,3457,3835,8,358,]
    B = random.sample(range(100),25)
    C = random.sample(range(100),12)
    print("A =", A)
    print("Searching A for:", 5)
    print("\t",recursive_binsearch(A,5))
    
    print("Searching A for:", 3567)
    print("\t",recursive_binsearch(A,3567))
    
    print("Searching A for:", 54)
    print("\t",recursive_binsearch(A,54))
        
    print("B =", B)
    print("C =", C)

    for i in C:
        print("Searching B for:", i)
        print("\t",recursive_binsearch(B,i))
    
