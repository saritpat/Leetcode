# -----------------------------------------------------
# Faster solution

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 1 and n % 2 == 0:
            n = n / 2
        
        if n == 1:
            return True

        return False
    
S = Solution()
n = 3
print(S.isPowerOfTwo(n))