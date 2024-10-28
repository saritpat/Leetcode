class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return False

        if s == t or s == '':
            return True
        
        i = j = 0
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1
                j+=1
            else:
                j+=1
            
            if i ==len(s):
                return True

        return False

S = Solution()
s = "abc"
t = "ahb"
print(S.isSubsequence(s, t))