# -----------------------------------------------------
# Faster solution

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = ''.join(char for char in s if char.isalnum())
        
        if len(s) == 1:
            return True
        
        lst = []
        mid = len(s) // 2
        front = s[:mid]
        back = s[mid:]


        for i in front:
            if i.isalnum():
                lst.append(i)
        
        for i in back:
            if i.isalnum():
                if i == lst[-1]:
                    lst.pop()
        
        if len(lst) == 0:
            return True

        return False

S = Solution()
s = "A man, a plan, a canal: Panama"
print(S.isPalindrome(s))


# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
        
#         lst = []
#         lst2= []

#         s = s.lower()

#         for i in s:
#             if i.isalpha() or ord(i) >= 48 and ord(i) <= 57:
#                 lst.append(i)

#         for i in range(len(lst) // 2):
#             if lst[i] == lst[-1]:
#                 lst2.append(lst[-1])
#                 lst.pop()

#         print(lst)
#         print(lst2)
        
#         if len(lst) > len(lst2):
#             lst.pop()

#         if lst == lst2:
#             return True
#         else:
#             return False

# S = Solution()
# nums1 = "A man, a plan, a canal: Panama"
# print(S.isPalindrome(nums1))