def valid_paranthesis(string) :
    bracket_mapping = {"(" : ")" , "[" : "]" , "{" : "}"}
    open_params = ["{" , "(" , "["]

    stack = []

    for s in string:
        if s in open_params:
            stack.append(s)
        elif stack and s == bracket_mapping[stack[-1]]:
            stack.pop()
        else :
            return False
    return stack == []


# Driver Code


result = valid_paranthesis("([]))")
if result :
    print("Valid Paranthesis")
else : 
    print("Invalid Paranthesis")