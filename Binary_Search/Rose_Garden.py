# You are given an array and n roses where arr[i] denotes that ith rose will bloom on arr[ith] day, You can only pick bloomed roses whiche are adjecent to each other and make a bouquet
# You are also told that you require k adjecent bloomed roses to make a single bouquet. Fu=ind the minimum no. of days required to make exactly m bouquets
# containing k roses

def checking(arr,days,r,b):
    count = 0
    no_of_bouquets = 0 
    for i in range(len(arr)):
        if arr[i] <= days:
            count += 1
        else:
            no_of_bouquets += count//r
            count = 0
    no_of_bouquets += count//r
    if no_of_bouquets >= b:
        return True
    else :
        return False


def roseGarden(arr, r, b):
    # write yur code here
    if len(arr) < r*b:
        return -1
    left = min(arr)
    right = max(arr)
    ans = -1
    mid = (left + right)//2

    while left <= right:

        if checking(arr,mid,r,b) == True:
            ans = mid
            right = mid - 1
            
        else :
            left = mid + 1
        mid = (left + right)//2
    return ans


# Driver code
arr = [1, 2, 1, 2, 7, 2, 2 ,3, 1]
print("The minimum no. of days required are : ",roseGarden(arr,3,2))