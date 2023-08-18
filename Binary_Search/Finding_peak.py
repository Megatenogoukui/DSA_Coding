def peakElement(arr):

    n = len(arr)
    left = 0
    right = n - 1
    mid = left + (right-left)//2
    if arr[0] > arr[1]:
        return 0
    elif arr[n-1] > arr[n-2]:
        return n-1


    while left <= right:
        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid + 1]:
            return mid
        elif arr[mid] > arr[mid-1]:
            left = mid + 1
        else:
            right = mid - 1
        mid = left + (right-left)//2


arr = [1,4,5,2,0,3,4,5]
print(peakElement(arr))