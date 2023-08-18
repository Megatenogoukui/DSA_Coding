# Defining the function

def linearSearch(Array , x):

    length = len(Array)
    for i in range(0,length+1):
        if Array[i] == x:
            return i
    return -1



#Driver Code

A =  [20,45,27,47,55,67,75,88,92]
print(linearSearch(A,67))

    