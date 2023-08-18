

def insertionSort(arr):

    n = len(arr)
    for i in range(n):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1

        else:
            arr[j + 1] = key
    return arr

arr = [2,4,5,2,3,5,6,3,3,6,3]
print(insertionSort(arr))