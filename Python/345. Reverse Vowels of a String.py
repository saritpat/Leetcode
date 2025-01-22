# -----------------------------------------------------
# Faster solution

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        lst = list(s)
        ans = ''
        vowel = 'aeiouAEIOU'
        
        i = 0
        j = len(s)-1

        while i < j:
            if lst[i] not in vowel:
                i+=1
            
            if lst[j] not in vowel:
                j-=1

            if lst[i] in vowel and lst[j] in vowel:
                lst[i], lst[j] = lst[j], lst[i]
                i+=1
                j-=1

        return ''.join(lst)

S = Solution()
s = "IceCreAm"
print(S.reverseVowels(s))



class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowel = 'aeiouAEIOU'
        s = list(s)
        vw = []
        ans = ''

        for i in s:
            if i in vowel:
                vw.append(i)

        j = len(vw)-1
        for i in range(len(s)):
            if s[i] in vowel:
                print(j)
                s[i] = vw[j]
                j-=1

        return ''.join(s)

S = Solution()
s = "IceCreAm"
print(S.reverseVowels(s))