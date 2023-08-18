# NO of inversions is 1) i < j 2) arr[i] > arr[j]


#Code for MergeProcedure
def mergeProcedure(arr, lb, ub ,mid):
    i = lb
    j = mid + 1
    countInversion = 0
    #making a temperory array
    temparr = []


    """ So here I'll explain u this logic , SO we know that all the elements in left and the right side 
        are sorted . If the value of the left side is less than the value on the rright side we can say that
        it would be less than all the elements after the left side element(Since they are sorted) ,THerefore
        we just count the number of elments after the left side element and add it to the countInversion 
        value"""
    while i <= mid and j <= ub:
        if arr[j] < arr[i]:
            countInversion += (mid - i ) + 1
            temparr.append(arr[j])
            j+=1
        else:
            temparr.append(arr[i])
            i+=1
    while i <= mid:
        temparr.append(arr[i])
        i+=1
    while j <= ub:
        temparr.append(arr[j])
        j+=1
    
    i = lb
    #Pushing all the values from the temperory array to main array
    for num in temparr:
        arr[i] = num
        i+=1

    #finally returning the value of inversion count
    return countInversion



# Code for Dividing
def dividing(arr, lb , ub ):
    
    if lb < ub:
        #Dividing
        mid = lb + (ub - lb)//2

        #Reccursive calling
        cntl = dividing(arr, lb, mid)
        cntr = dividing(arr, mid + 1, ub)
        cnt = mergeProcedure(arr , lb ,ub ,mid)
        return cntl + cntr + cnt
    
    #If we hit the small problem
    return 0
# Code for countNoOfInversion
def countNoOfInversion(arr):
    return dividing(arr , 0 , len(arr) - 1)

# Driver Code 
arr = [70,50,60, 10,20,30,80,15]
print(countNoOfInversion(arr))