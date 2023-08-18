
def searchIn2DArray(A,m,n,target):
    
    left  = 0
    right  = m*n - 1
    mid  = left +(right - left)//2   
    
    while left < right:
        i = mid//n  #Row number
        j = mid%n   # Column number
        if A[i][j] == target:
            return True
        elif A[i][j] > target:
            right = mid - 1
        else:
            left  = mid + 1
        mid = left +(right - left)//2   
    return False

#Driver code 
A = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(searchIn2DArray(A,3,4,23))