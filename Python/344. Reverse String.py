class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        back = -1

        for i in range(len(s) // 2):
            s[i], s[back] = s[back], s[i]
            back -= 1
        
        return s

S = Solution()
s = ["h","e","l","l","o"]
print(S.reverseString(s))