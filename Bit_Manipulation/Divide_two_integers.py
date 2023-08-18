def division(dividend , divisor):
    sign = -1 if (dividend >= 0 and divisor < 0) or (dividend < 0 and divisor >= 0) else 1
    dividend = abs(dividend)
    divisor = abs(divisor)
    result = 0
        
    
    while dividend >= divisor:
        shift = 0
        while dividend >= (divisor << shift):
            shift += 1
        result += (1 << (shift - 1))
        dividend -= (divisor << (shift - 1)) 
        
    return min(2147483647 ,max(-2147483648,result*sign))

#Driver Code
dividend = int(input("Enter the value of dividend : "))
divisor = int(input("Enter the value of divisor : "))
print(division(dividend, divisor))