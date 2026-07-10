class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        ans = 0
        l = 0
        r = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1
            while r-l-max(count.values()) + 1 > k :
                count[s[l]] -=1
                l = l+1
                
            ans = max(ans,r-l+1)
                
        return ans

