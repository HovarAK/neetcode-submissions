class Solution:
    def maxArea(self, heights: List[int]) -> int:     
        l, r = 0, len(heights) - 1
        maximum = self.computeArea(heights, l, r)

        while l < r:
            # compute the total area 
            area = self.computeArea(heights, l, r)
            
            if area > maximum:
                maximum = area

            # increment ptrs
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return maximum

    def computeArea(self, heights: List[int], l: int, r: int) -> int:
            min_height = heights[l] if heights[l] < heights[r] else heights[r]
            return min_height * (r-l)