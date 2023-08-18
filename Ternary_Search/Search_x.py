def ternarySearch(arr , k):
    l = 0
    r = len(arr) - 1
    # Computing the values of mid1 and mid2
    mid1 = l + (r - l)//3
    mid2 = r - (r - l)//3

    while l <= r :
        
        if arr[mid1] == k:
            return mid1
        elif arr[mid2] == k:
            return mid2
        # Searching the first part 
        elif arr[mid1] > k:
            r = mid1 - 1
        # Searching the third part 
        elif arr[mid2] < k:
            l = mid2 + 1
        # Searching the second  part 
        else:
            r = mid2 - 1
            l = mid1 + 1
        mid1 = l + (r - l)//3
        mid2 = r - (r - l)//3
    return -1

arr = [1,3,4,6,8,9]
print(ternarySearch(arr,10))