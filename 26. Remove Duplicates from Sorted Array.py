class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        curr = -9999999
        x = 0
        for i in range(len(nums)):
            if nums[i] > curr:
                curr = nums[i]
            else:
                nums[i] = '_'
                x += 1

        for i in range(x):
            nums.remove('_')



        k = len(nums)
        return k

# [0,0,1,1,1,2,2,3,3,4] [1,1,2]
s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(s.removeDuplicates(nums))

# -----------------------------------------------------
# Faster solution

# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """

# # [0,0,1,1,1,2,2,3,3,4] [1,1,2]
# s = Solution()
# nums = [1,1,2]
# print(s.removeDuplicates(nums))