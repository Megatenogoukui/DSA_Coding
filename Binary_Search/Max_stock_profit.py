# U have been provided an array named parices in which each element represents the prices of the of the stocks on that day, calculate the max profit that one can earn

def MaxStockProfit(A):

    
    min = float('inf')
    maxProfit = 0
    for i in range(len(A)):
        if A[i] < min :
            min = A[i]
        elif A[i] - min > maxProfit :
            maxProfit = A[i] - min
    return maxProfit

A = [7,1,5,3,6,4]
print(MaxStockProfit(A))