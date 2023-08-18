

# min heap
def minHeapify(arr,n,i):
    l = 2 * i + 1
    r = 2 * i + 2
    smallest = i

    if l < n and arr[l] < arr[smallest]:
        smallest = l

    if r < n and arr[r] < arr[smallest]:
        smallest = r 
    
    if smallest != i:
        arr[i] , arr[smallest] = arr[smallest] , arr[i]
        minHeapify(arr,n,smallest)

    

def buldMinHeap(arr,n):

    startIndex = (n//2) - 1

    for i in range(startIndex,-1,-1):
        minHeapify(arr,n,i)

    return arr



# Max Heap 

def maxHeapify(arr,n,i):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r 
    
    if largest != i:
        arr[i] , arr[largest] = arr[largest] , arr[i]
        maxHeapify(arr,n,largest)

    

def buldMaxHeap(arr,n):

    startIndex = (n//2) - 1

    for i in range(startIndex,-1,-1):
        maxHeapify(arr,n,i)

    return arr


# driver code
arr = [1,3,4,5,6,2]
print(buldMinHeap(arr,6))
print(buldMaxHeap(arr,6))