
def lowerBound(A ,x) : 
    left = 0
    right = len(A) - 1
    mid = left + (right - left)//2
    ans = -1

    while  left <= right:
        if A[mid] >= x:
            ans = mid
            right = mid - 1
        else: 
            left = mid + 1
        mid = left + (right - left)//2
    return ans





# Driver codde

A = [1,2,3,3,3,4,4,5,5,5,6]
print(lowerBound(A , 3))