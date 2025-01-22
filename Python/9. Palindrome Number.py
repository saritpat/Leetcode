class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # base
        if x < 0:
            return False
        x = str(x)

        # base
        if len(x) <= 1:
            return True

        lst = []
        for i in x:
            lst.append(i)
        
        for i in x:
            if i == lst[-1]:
                lst.pop()
    
        if len(lst) == 0:
            return True

        return False


S = Solution()
x = 121
print(S.isPalindrome(x))






# -----------------------------------------------------
# Faster solution

# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """

# S = Solution()
# x = 121
# print(S.isPalindrome(x))