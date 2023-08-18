
def partition(arr , a , b):
    p = arr[a]
    i = a
    for j in range( i+1 ,b+1):
        if arr[j] <= p:
            i = i + 1
            arr[i], arr[j] = arr[j] , arr[i]
    
    arr[i], arr[a] = arr[a] , arr[i]
    return i



def quickSort(arr, i, j):
    if i < j:
        m = partition(arr, i , j)
        quickSort(arr, i, m - 1)
        quickSort(arr, m + 1, j)

    return arr

#Driver Code

arr = [2,0,2,1,1,0]
p = 0
q = len(arr) - 1
result = quickSort(arr, p, q)
print(result)