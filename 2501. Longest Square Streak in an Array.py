class Solution(object):
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        max = 0
        c = 1

        for i in nums:
            while i**2 in nums:
                c += 1
                i = i**2
                if c > max:
                    max = c
            else:
                c = 1
        
        if max == 0:
            return -1

        return max, nums
    
# [2, 3, 4, 6, 8, 16]
s = Solution()
nums = [4,3,6,16,8,2]
print(s.longestSquareStreak(nums))