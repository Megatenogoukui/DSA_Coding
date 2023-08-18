
# Defining a function

def binarySearchWithRecursion(A ,x,left ,right):
    
    mid = left + (right - left)//2

    while(left<=right):
        if A[mid] == x:
            return mid
        
        elif A[mid] < x:
            # right side of the mid
            # Search space will be from mid+1 to right
            return binarySearchWithRecursion(A, x , mid + 1 , right)  # Recursion - Calling same function insifde the method defination
        
        else :
            # left side of the mid
            # Search space will be from  left  to mid-1 
            return binarySearchWithRecursion(A,x,left,mid-1)   # Recursion - Calling same function insifde the method defination
        
    return -1 #Searching element not present in the array


def binarySearchWithoutRecursion(A , x):
    left  = 0
    right = len(A) - 1
    mid = left + (right - left)//2

    while(left<=right):
        if A[mid] == x:
            return mid
        
        elif A[mid] < x:
            # right side of the mid
            # Search space will be from mid+1 to right
            left = mid + 1
        
        else :
            # left side of the mid
            # Search space will be from  left  to mid-1 
            right  = mid - 1

        mid = left + (right - left)//2
        
    return -1 #Searching element not present in the array

# Driver Code

A = [20,27,40,47,55,67,75,88,92]
left  = 0
right = len(A) - 1
print(binarySearchWithRecursion(A,67,left,right))
print(binarySearchWithoutRecursion(A,20))