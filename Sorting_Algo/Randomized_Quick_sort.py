import random


def randomizedPartition(arr, i , j):
    randomPivotElement = random.randrange(i,j)
    arr[i],arr[randomPivotElement] = arr[randomPivotElement] ,arr[i]
    return partition(arr,i,j)


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
        m = randomizedPartition(arr, i , j)
        quickSort(arr, i, m - 1)
        quickSort(arr, m + 1, j)

    return arr

#Driver Code

arr = [50,40,70,10,30,90,45,67,79]
p = 0
q = len(arr) - 1
result = quickSort(arr, p, q)
print(result)