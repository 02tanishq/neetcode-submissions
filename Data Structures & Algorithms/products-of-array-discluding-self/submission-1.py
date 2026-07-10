class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Build the output array
        output = [1] * len(nums)
        output[0] = 1
        
        # first store the left side products in output
        for i in range(1, len(nums)):
            output[i] = output[i - 1] * nums[i - 1]
            
        right_product = 1
        
        # At each step multiply the current output by the running right_product
        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i] * right_product
            right_product *= nums[i]
            
        return output
