#2Sum 
def twoSum(self, nums: List[int], target: int) -> List[int]:#Predefined function
        a={} #Creating a dictionary for storage
        for i,val in enumerate(nums): #enumerating through the indices
            compliment=target-val
            if compliment in a: #Checking whether the number is already present in the dictionary 
                return [a[compliment],i]
            a[val]=i #Maintaining the records for the dictionary
            