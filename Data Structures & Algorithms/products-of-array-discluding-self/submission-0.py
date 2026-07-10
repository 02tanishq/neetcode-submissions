class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # hashmap = {}
        # result = []
        # for i in nums:
        #     if i in hashmap :
        #         hashmap[i] += hashmap[i]
        #     else:
        #         hashmap[i] = 1

        # for i in hashmap:
        #     result[i] = sum

        ans = [0] * len(nums)
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j != i :
                    product = product * nums[j]
                else:
                    product = product * 1
            ans[i]= product 

        return ans

