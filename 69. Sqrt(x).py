class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        a = x
        while a*a > x:
            a = (a + x/a)//2
        
        return a

S = Solution()
x = 2147395599
print(S.mySqrt(x))


# import math

# class Solution(object):
#     def mySqrt(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
        
#         return int(math.sqrt(x))

# S = Solution()
# x = 4
# print(S.mySqrt(x))