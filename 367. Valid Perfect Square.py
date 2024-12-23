class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1: 
            return True

        i = 1
        while i*i <= num:
            if i*i == num:
                return True
            i+=1
        
        return False

S = Solution()
num = 16
print(S.isPerfectSquare(num))