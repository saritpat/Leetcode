class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 3 and n != 1:
            return False

        while n % 3 == 0:
            n = n / 3
        
        if n == 1:
            return True
        
        return False

S = Solution()
n = 1
print(S.isPowerOfThree(n))


# -----------------------------------------------------
# Faster solution

# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         if n < 1:
#             return False

#         return 3**19 % n == 0

# S = Solution()
# n = 27
# print(S.isPowerOfThree(n))