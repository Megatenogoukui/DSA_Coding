from collections import deque

def isValid(str1):
    bracketMapping = {"(":")","[":"]","{":"}"}
    openParams = set(["(" , "[" , "{"])
    stack = []
    for s in str1:
        if s in openParams:
            stack.append(s)
        elif stack and s == bracketMapping[stack[-1]]:
            stack.pop()
        else:
            return False
    return stack == []
    
    


# Driver COde 

str1 = "{[]}"
if(isValid(str1)):
    print("Valid String")
else:
    print("Invalid String")