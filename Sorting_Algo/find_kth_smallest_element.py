def partition(arr,a,b):
    p = arr[a]
    i = a
    for j in range(i + 1 , b + 1):
        if arr[j] <= p:
            i+=1
            arr[i] ,arr[j] = arr[j] , arr[i]
    arr[i] ,arr[a] = arr[a] ,arr[i]
    return i



def selectionProcedure(arr, k ,p ,q):
    m = partition(arr,p,q)
    t = k - 1
    if m == t:
        return arr[m]
    elif m > t:
        r = selectionProcedure(arr,k ,p ,m - 1)
    else:
        r = selectionProcedure(arr , k , m + 1  ,q)
    return r
#driver Code

arr = [21 , 25, 68, 79, 52,66,89,97]
k = 4
p = 0
q = len(arr) - 1
result = selectionProcedure(arr, k , p ,q)
print(result)