class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0  :
            return 0
        hello = sorted(nums)
        i = 0
        ans = 0
        maximum = 0
        while i < len(nums) - 1:
            if hello[i] == hello[i+1]:
                pass
            elif hello[i] +1 == hello[i+1]:
                ans += 1
                # maximum = ans
            else :
                maximum = max(maximum,ans)
                ans = 0
            
            i += 1 
        maximum = max(maximum,ans)
        return maximum + 1 