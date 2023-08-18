

def findCandidate(arr):
    candidate = None
    count =  0

    for num in arr:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate

def ismajority(arr,cand):
    count = 0
    for num in arr:
        if num == cand:
            count += 1
    if count > len(arr)//2:
        return True , str(cand)
    else:
        return False
    
def printMajority(arr):
    cand = findCandidate(arr)
    if ismajority(arr, cand):
        print("The majority element is: " , cand )
    else:
       print("There is no majority Candidate")


# Driver Code

arr = [3,2,3]
printMajority(arr)