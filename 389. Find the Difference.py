class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = list(s)

        for i in t:
            if i not in s:
                return i
            else:
                s.pop(s.index(i))

S = Solution()
s = "ba"
t = "bab"
print(S.findTheDifference(s, t))


# -----------------------------------------------------
# Faster solution
# 
# class Solution(object):
#     def findTheDifference(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         s = list(s)

#         for i in t:
#             if i not in s:
#                 return i
#             else:
#                 if s.count(i) != t.count(i):
#                     return i

# S = Solution()
# s = "ba"
# t = "bab"
# print(S.findTheDifference(s, t))