class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length = len(needle)
        for i in range(len(haystack)+1 - length):
            if haystack[i:i+length] == needle:
                return i
            
        return -1


# "mississippi"
# "issip"

# "mississippi" 
# "sipp"

S = Solution()
s = "mississippi"
n = "sipp"
print(S.strStr(s, n))


# -----------------------------------------------------
# Faster solution

# class Solution(object):
#     def strStr(self, haystack, needle):
#         """
#         :type haystack: str
#         :type needle: str
#         :rtype: int
#         """
#         if haystack == needle:
#             return 0
        
#         if len(haystack) < len(needle):
#             return -1
        
#         first = ''
#         last = ''

#         for i in haystack:
#             if needle in haystack:
#                 first = needle[0]
#                 last = needle[-1]
#                 for i in range(len(haystack)):
#                     if i <= len(haystack) - len(needle):
#                         if haystack[i] == first and haystack[i + len(needle)-1] == last and haystack[i:i + len(needle)] == needle:
#                             return i
#             else:
#                 return -1

# # "mississippi"
# # "issip"

# # "mississippi" 
# # "sipp"

# S = Solution()
# s = "mississippi"
# n = "sipp"
# print(S.strStr(s, n))