class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right = len(heights) -1
        left = 0
        Area = 0
        while left < right:
            Area = max(Area ,min(heights[left],heights[right])*(right-left))
           
            if heights[left] < heights[right]:
                left = left+1
            else:
                right = right - 1

        return Area