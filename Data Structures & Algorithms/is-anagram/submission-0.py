class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        hashmap = {}
        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else :
                hashmap[char] = 1

        for char in t:
            if char in hashmap:
                if hashmap[char] > 1:
                    hashmap[char] -= 1
                else :
                    del hashmap[char]
            else:
                return False

        return not bool(hashmap)