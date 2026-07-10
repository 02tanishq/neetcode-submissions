class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        left_max = 0
        right_max = 0

        while right > left  :
            if height[left] < height[right] :
                left_max = max(left_max , height[left])
                max_water += left_max- height[left]
                left +=  1 
                
            else :
                right_max = max(right_max , height[right])
                max_water += right_max - height[right]
                right -= 1

        return max_water
