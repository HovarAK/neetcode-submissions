class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def computeArea(heights: List[int], l: int, r: int) -> int:
            min_height = heights[l] if heights[l] < heights[r] else heights[r]
            return min_height * (r-l)
        
        l, r = 0, len(heights) - 1
        maximum = computeArea(heights, l, r)

        while l < r:
            # compute the total area 
            area = computeArea(heights, l, r)
            
            if area > maximum:
                maximum = area

            # increment ptrs
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return maximum