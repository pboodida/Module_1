#ContainsDuplicate
def containsDuplicate(self, nums: List[int]) -> bool: #Predefined Function
    a={} #Creating a dictionary for storage
    for i in nums:
        a[i]=a.get(i,0)+1 #Checking for the values present in the list
    for i in a:
        if a[i]!=1: #Checking for the values present in the dictionary
           return True
    return False