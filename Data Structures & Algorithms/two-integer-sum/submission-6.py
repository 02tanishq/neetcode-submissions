class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted((nums,i) for i , nums in enumerate(nums))
        l = 0 
        r = len(nums) - 1
        while r > l :
            sum = nums[l][0]  + nums[r][0]
            if target == sum:
                return [min(nums[l][1],nums[r][1]) , max(nums[l][1],nums[r][1])]
            if target < sum :
                r -= 1
            else :
                l += 1
        return []
