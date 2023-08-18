


def mergeProcedure(arr, p,q ,mid):
    n1 = mid - p + 1
    n2 = q - mid

    lSA = [0] * n1
    rSA = [0] * n2

    for m in range(n1):
        lSA[m] = arr[p + m]
    for n in range(n2):
        rSA[n] = arr[mid + 1 + n]


    i = 0
    j = 0
    k = p

    while i < n1 and  j < n2:
        if lSA[i] <= rSA[j]:
            arr[k] = lSA[i]
            i+=1
        else:
            arr[k] = rSA[j]
            j+=1

        k+=1 
    while i < n1:
        arr[k] = lSA[i]
        i+=1
        k+=1
    while j < n2:
        arr[k] = rSA[j]
        j+=1
        k+=1

def mergeSort(arr , i , j):
    if i < j:
        mid = (i + j)//2
        mergeSort(arr,i,mid)
        mergeSort(arr,mid + 1,j)
        mergeProcedure(arr,i,j,mid)

    return arr







#driver code

arr = [2,253,43,12,32,11]

p = 0
q = len(arr) - 1

result = mergeSort(arr, p, q)
print(result)