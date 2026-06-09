class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # combinations
        combinations = {}

        # Account for every combinations
        for i in range(len(nums)):
            diff = target - nums[i]

            # If the current number is a solution then return solution
            if nums[i] in combinations.keys():
                return combinations[nums[i]] + [i]
            
            # Add the difference to the Map
            combinations[diff] = [i]

            
            