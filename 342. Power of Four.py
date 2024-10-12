class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 1:
            if n % 4 == 0:
                n = n / 4
            else:
                return False
        
        if n == 1:
            return True
        
        return False

S = Solution()
n = -4
print(S.isPowerOfFour(n))