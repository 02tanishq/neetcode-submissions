class Solution:
    def minWindow(self, s: str, t: str) -> str:
        slow =0
        fast = 0
        t_hash = {}
        ans_hash = {}
        res = [ -1,-1]
        res_len = float("inf")
        
        for char in t:
            t_hash[char] = t_hash.get(char, 0) + 1
        have = 0
        req = len(t_hash)
        for fast in range(len(s)):
            k = s[fast]
            ans_hash[k] = ans_hash.get(k,0) + 1
            if s[fast] in t_hash and ans_hash[k] == t_hash[k]:
                have += 1

            while have == req :

                if (fast - slow + 1) < res_len:
                    res = [slow , fast]
                    res_len = fast- slow + 1
                
                ans_hash[s[slow]] -= 1
                if s[slow] in t_hash and ans_hash[s[slow]] < t_hash[s[slow]]:
                    have -= 1

                
                slow += 1 

        l, r = res
        return s[l:r+1] if res_len != float("inf") else "" 


                
