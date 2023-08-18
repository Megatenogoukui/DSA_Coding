# U have an array of numbers Find the pair which gives the sum as 210

 # TWO POINTER APPROACH
def SumOfPairs(A,target):
    left  = 0 
    right = len(A) - 1

    

    while left < right :
        if A[left] + A[right] == target:
            return [A[left],A[right]]
        elif A[left] + A[right] > target:
            right-=1
        else :
            left+=1

    return -1
A = [20,40,60,90,110,120,180,240]
print(SumOfPairs(A,210))