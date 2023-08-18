
def  findSingleELement(arr):
    left = 0
    right = len(arr) - 1
    mid = left + (right - left)//2

    while left <= right:
        if arr[mid] != arr[mid-1] and arr[mid] != arr[mid + 1]:
            return mid
        
        elif mid%2 == 0 and arr[mid] == arr[mid + 1]:
            left = mid + 2

        else: 
            right = mid - 1  
        mid = left + (right - left)//2


    return -1




#Driver Code
A = [1,1,2,2,3,3,4,4,5,6,6,7,7]
print(findSingleELement(A))