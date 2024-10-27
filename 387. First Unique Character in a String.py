class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = []
        seen = set()

        for i in s:
            if i not in seen:
                if i not in lst:
                    lst.append(i)
                else:
                    lst.pop(lst.index(i))
                    seen.add(i)
            
            else:
                if i in lst:
                    lst.pop(lst.index(i))
        
        if len(lst) < 1:
            return -1

        return s.index(lst[0])

S = Solution()
s = "leetcode"
print(S.firstUniqChar(s))