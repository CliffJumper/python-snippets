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


if __name__ == '__main__':
    # Test the fun
    import random
    A = [4,5,7,54,234,73,5,8,35,8,35,8,3457,3835,8,358,]
    B = random.sample(range(100),25)
    print(A)
    print("Searching A for:", 5)
    print("\t",recursive_binsearch(A,5))
    
    print("Searching A for:", 3567)
    print("\t",recursive_binsearch(A,5))
    
    print("Searching A for:", 54)
    print("\t",recursive_binsearch(A,5))
        
    print(B)
    print("Searching B for:", 5)
    print("\t",recursive_binsearch(B,5))
       
    print("Searching B for:", 57)
    print("\t",recursive_binsearch(B,57))
    
    print("Searching B for:", 81)
    print("\t",recursive_binsearch(B,81))
    
    

