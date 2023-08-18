def myPow(x, n) :
    # Write your code here.
    m = n
    if n < 0:
        m = 0 - n
    if m == 0:
        return 1
    elif m == 1:
        if n < 0:
            return 1/x
        else:
            return x
    
    else:
        mid = m//2
        b = myPow(x , mid)
        result = b * b
        if m % 2 == 0:
            if n < 0:
                return 1/result
            else:
                return result
        else:
            if n < 0:
                return 1/(result * x)
            else:
                return result * x
            
number  = int(input("Enter the number : "))
n = int(input("Enter the power : "))          
ans = myPow(number , n)
print(ans)