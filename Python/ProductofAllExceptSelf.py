#ProductofAllExceptSelf
def productExceptSelf(self, nums: List[int]) -> List[int]: #Predefined function
    n=len(nums)
    answer=[1]*n
    left=1
    for i in range(n):#For finding the left sided product
        answer[i]*=left
        left*=nums[i]
    right=1
    for i in range(n-1,-1,-1):#For finding the right sided product
        answer[i]*=right
        right*=nums[i]
    return answer