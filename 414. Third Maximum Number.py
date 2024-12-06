class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        c = 0
        ans = nums[-1]

        for i in range(len(nums)-1, -1, -1):
            if nums[i] < ans:
                ans = nums[i]
                c+=1
                if c == 2:
                    return ans
            
        if c < 2:
            return nums[-1]

S = Solution()
nums = [3,2,1]
print(S.thirdMax(nums))