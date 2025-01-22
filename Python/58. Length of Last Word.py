# -----------------------------------------------------
# Faster solution

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        space = False

        for i in s:
            if space == True and i != " ":
                count = 0

            if i == " ":
                space = True
            else:
                space = False
                count += 1
        return count

S = Solution()
x = "   fly me   to   the moon  "
print(S.lengthOfLastWord(x))   


# class Solution(object):
#     def lengthOfLastWord(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         count = 0
        
#         for i in s[::-1]:
#             if count == 0:
#                 if i != ' ':
#                     count += 1
#             else:
#                 if i == ' ':
#                     return count
#                 count += 1

#         return count
            
        
# S = Solution()
# x = "   fly me   to   the moon  " 
# print(S.lengthOfLastWord(x))   