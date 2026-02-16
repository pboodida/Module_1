#MaximumSubarray
def maxSubArray(self, nums: List[int]) -> int:#Predefined Function
    sum=0
    max_sum=float('-inf') #Initializing the maxsum to minus infinity
    for i in range(len(nums)):
        sum=sum+nums[i]
        if max_sum<sum: #Checking whether the sum is greater than the max sum
            max_sum=sum
        if sum<0: #Update the value of sum,when ever it is less than zero
            sum=0
    return max_sum