

def closestSum(arr , target):
    n = len(arr)
    min  = float("inf")
    for i in range(n - 2):
        for j in range(i+1,n - 1):
            for k in range(j+1,n):
                sum = (arr[i] + arr[j] + arr[k]) 
                min_diff = sum - target
                if abs(min_diff) < abs(min) :
                    min = min_diff

    return min + target

arr = [1,2,3,4,-5]
print(closestSum(arr,10))