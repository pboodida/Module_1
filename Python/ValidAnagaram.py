#ValidAnagaram
def isAnagram(self, s: str, t: str) -> bool: #Predefined function
    if len(s)!=len(t): #Checking for both their lengths
        return False
    check={} #Creating a dictionary for storage
    for ch in s:
        check[ch]=check.get(ch,0)+1 #Checking with the dictionary for any occurances
    for ch in t:
        if ch not in check:
            return False
        check[ch]-=1 #Decreasing the count of each character after use of the first occurance if many are there
        if check[ch]<0:
            return False
    return True