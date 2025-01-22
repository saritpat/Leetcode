# -----------------------------------------------------
# Faster solution

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = ''
        st = str(x)
        neg = False

        if x < 0:
            neg = True
            for i in range(len(st)-1, 0, -1):
                ans += st[i]
            
        else:
            for i in range(len(st)-1, -1, -1):
                ans += st[i]
        
        if neg == True:
            ans = int(ans) * -1
        else:
            ans = int(ans)
        
        if ans < -2**31 or ans > 2**31-1:
            return 0
        
        return ans


S = Solution()
x = -123
print(S.reverse(x))


# class Solution(object):
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         x = str(x)
#         lst = []
#         ans = ""
#         neg = False

#         for i in range(len(x)):
#             lst.append(x[i])

#         if lst[0] == '-':
#             lst.pop(0)
#             neg = True
        
#         for i in range(len(lst)):
#             A = lst[-1]
#             ans += A
#             lst.pop()

#         ans = int(ans)

#         if neg == True:
#             ans = ans * -1

#         if ans >= 2147483647 or ans <= -2147483648:
#             return 0
        
#         return ans

# S = Solution()
# x = -123
# print(S.reverse(x))



