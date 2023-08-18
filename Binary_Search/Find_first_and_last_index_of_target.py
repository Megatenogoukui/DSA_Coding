def binarySearchWithoutRecursion(A , x):
    left  = 0
    right = len(A) - 1
    mid = left + (right - left)//2

    while(left<=right):
        if A[mid] == x:
            start = end = mid # Initiating the values of start and end
            while start > 0 and A[start - 1] == x:
                start-=1
            while end < len(A) - 1 and A[end + 1] == x:
                end+=1
            return [start,end]

    
        
        elif A[mid] < x:
            # right side of the mid
            # Search space will be from mid+1 to right
            left = mid + 1
        
        else :
            # left side of the mid
            # Search space will be from  left  to mid-1 
            right  = mid - 1

        mid = left + (right - left)//2
        
    return [-1,-1] #Searching element not present in the array

# Driver Code

A = [2,5,5,7,7,8,8,8,10]
print(binarySearchWithoutRecursion(A,7))