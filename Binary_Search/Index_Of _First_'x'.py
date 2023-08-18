# FaceBook Question

def indexOfFirstx(A):
    left  = 0
    right = len(A) - 1
    ans = -2
    mid = left + (right - left)//2

    while left <= right:

        if  A[mid] == 'x':
            ans = mid
            right = mid - 1

        else :
            left = mid + 1
        mid = left + (right - left)//2
    return ans


A = [-23,40,55,2,27,-89,54,'x','x','x']
print(indexOfFirstx(A))