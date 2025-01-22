class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = []
        length = 0

        for i in range(len(s)):
            if s[i] not in seen:
                seen.append(s[i])
            else:
                seen = seen[seen.index(s[i])+1:]
                seen.append(s[i])
            
            if len(seen) > length:
                length = len(seen)

        return length


# s = "aabaab!bb"

S = Solution()
s = 'aababasdsasd'
print(S.lengthOfLongestSubstring(s))