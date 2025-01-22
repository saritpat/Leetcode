# -----------------------------------------------------
# Faster solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}

        if len(s) != len(t):
            return False
        
        for i in s:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

        for i in t:
            if i not in dict:
                return False
            else:
                if dict[i] <= 0:
                    return False
                
                dict[i] -= 1
        
        return True

S = Solution()
s = "anagram"
t = "nagaram"
print(S.isAnagram(s, t))