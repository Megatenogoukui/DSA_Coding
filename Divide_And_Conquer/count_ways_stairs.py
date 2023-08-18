# Count the number of ways to reach the nth  stair The person can climb atmost 2 steps at a time


def ways(n):
    #small problem
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        # Recurrsion
        result = ways(n-1) + ways(n-2)
    return result

a = int(input("Enter the number of steps : "))
ans = ways(a)
print("The number of ways to climb the stairs are : ", ans)
    

    
