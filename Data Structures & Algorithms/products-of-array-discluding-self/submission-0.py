class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array_expect_self = [1 for i in range(len(nums))]

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i !=j:
                    array_expect_self[j] *= nums[i]

        return array_expect_self

