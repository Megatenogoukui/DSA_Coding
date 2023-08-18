def decimalToBinary(a):
    temp = a
    ans = ""
    while temp > 1:
        ans += str(temp%2)
        temp //= 2
    fans =   ans + "1"
    fans = fans[::-1]
    return int(fans)


a = int(input("Enter the number : "))
print(decimalToBinary(a))