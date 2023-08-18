def perfectSquare(M):

    left = 0
    right = M 

    mid = (left +  right)//2

    while left <= right :
        if mid*mid == M:
            return True
        elif mid*mid > M:
            right = mid - 1
        else :
            left = mid + 1
        mid = (left +  right)//2
    return False



A = int(input("Enter the number: "))
print(perfectSquare(A))
