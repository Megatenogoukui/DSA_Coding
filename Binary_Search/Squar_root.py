def squareRoot(M):

    left = 0
    right = M
    mid = (left +right)//2

    while left <= right:
        if mid*mid == M :
            return mid
        elif mid*mid < M:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
        mid = (left +right)//2
    return ans

A = int(input("Enter the number : "))
print(squareRoot(A))