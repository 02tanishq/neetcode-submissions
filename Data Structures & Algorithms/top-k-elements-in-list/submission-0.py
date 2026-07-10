class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        ans = []
        for i in nums :
            if i in hashmap:
                hashmap[i] +=1
            else :
                hashmap[i]  = 1
        
        while k > 0 :
            max_key = max(hashmap , key =hashmap.get)
            ans.append(max_key)
            hashmap.pop(max_key)
            k -=1

        return ans 

        