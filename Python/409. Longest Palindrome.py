class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        s.sort()
        i = count = 0

        if len(s) == 1:
            return 1
        
        while i < len(s):
            temp = s.count(s[i])
            if temp % 2 == 0:
                count += temp
                i += temp
            
            elif temp > 1:
                count += temp-1
                mid = True
                i += temp
            
            else:
                mid = True
                i+=1
        
        if count < len(s) and mid:
            count+=1

        return count


S = Solution()
s = "bbbbbbba"
print(S.longestPalindrome(s))