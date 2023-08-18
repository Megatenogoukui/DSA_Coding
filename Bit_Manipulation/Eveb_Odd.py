def evenOdd(a):
    
    if a & 1 == 0:
        return "The number is even"
    else:
        return "The number is odd"

# Driver code
a = int(input("Enter the number : "))
print(evenOdd(a))