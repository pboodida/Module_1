#ValidParentheses
def isValid(self, s: str) -> bool:#Predefined function
    stack=[] #Creating a list
    mapping={ #mapping the valid parentheses 
        ')':'(',
        '}':'{',
        ']':'['
    }
    for ch in s:
        if ch in mapping: #Searching for the right mapping
            if not stack or stack[-1]!=mapping[ch]:
                return False
            stack.pop()
        else: #Adding non-key symbols
            stack.append(ch)
    return not stack