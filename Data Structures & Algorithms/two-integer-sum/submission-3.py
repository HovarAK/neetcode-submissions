class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums):
            # If the current number provides a solution then return
            if n in hashmap:
                return hashmap[n] + [i]

            # Calculate the remainder
            remainder = target - n
            hashmap[remainder] = hashmap.get(remainder, []) + [i]