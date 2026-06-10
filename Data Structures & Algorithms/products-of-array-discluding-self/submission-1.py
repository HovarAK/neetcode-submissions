class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Variables
        length = len(nums)
        prevNum = 1
        nextNum = 1

        # Allocating the arrays
        prefix = [nums[0]] + [1]*(length-1)
        suffix = [1]*(length-1) + [nums[length-1]]
        res = [0] * length
        
        # Calculating the Prefix Array
        for i in range(1,length):
            prefix[i] = prefix[i-1] * nums[i]
        
        # Calculating the Suffix Array
        for i in range(length-2,-1,-1):
            suffix[i] = suffix[i+1] * nums[i]

        # Calculating the Product of Array Except Self
        for i in range(length):
            prevNum = 1 if i == 0 else prefix[i-1]
            nextNum = 1 if i == length-1 else suffix[i+1]
            res[i] = prevNum * nextNum

        return res
        
