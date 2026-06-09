class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       prevComb = {}

       for i, num in enumerate(nums):
            diff = target - num

            if num in prevComb.keys():
                return [prevComb[num],i]

            prevComb[diff] = i

            
            