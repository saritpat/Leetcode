class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = strs[0]
        length = len(result)

        for i in range(1, len(strs)):
            while strs[i].find(result) != 0:
                result = result[:length - 1]
                length -= 1

            if not result:
                return ""

        return result


        
S = Solution()
s = ["flower","flow","flight"]
print(S.longestCommonPrefix(s))


# -----------------------------------------------------
# Faster solution

# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """

# S = Solution()
# s = ["flower","flow","flight"]
# print(S.longestCommonPrefix(s))