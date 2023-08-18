def selectionSort(arr):

    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i,n-1):
            if arr[j] < arr[min]:
                min = j
        arr[i] , arr[min] = arr[min] , arr[i]
    return arr

arr = [30,12,34,22,11,45]
print(selectionSort(arr))