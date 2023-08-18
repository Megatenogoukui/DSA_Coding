
def MaxMin(arr,i,j):
    
    # smallest condition
    if i == j:
        mini = arr[i]
        maxi = arr[i] 
    elif i == j - 1:
        if arr[i] < arr[j]:
            mini = arr[i]
            maxi = arr[j]
        else:
            mini = arr[j]
            maxi = arr[i]

    # Big conditions
    else:
        # Dividing 
        mid = i + (j - i)//2
        mini1 , maxi1 = MaxMin(arr,i,mid)
        mini2 , maxi2 = MaxMin(arr,mid + 1,j)
        if mini1 < mini2:
            mini = mini1
        else:
            mini = mini2
        
        if maxi1 > maxi2:
            maxi = maxi1
        else:
            maxi = maxi2
    return mini,maxi

    

arr = [2,4,3,22,55,32]
i = 0
j = len(arr) - 1
mini, maxi = MaxMin(arr,i,j)
print(mini , maxi)
