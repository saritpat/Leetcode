class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = '_'
                length += 1
        
        for i in range(length):
            nums.remove('_')
            
        k = len(nums)
        return k

s = Solution()
nums = [3,2,2,3]
v = 3
print(s.removeElement(nums, v))


# -----------------------------------------------------
# Faster solution

# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
#         length = 0
#         for i in range(len(nums)):
#             if nums[i] == val:
#                 nums[i] = '_'
#                 x += 1
        
#         for i in range(length):
#             nums.remove('_')
            
#         k = len(nums)
#         return k

# s = Solution()
# nums = [3,2,2,3]
# v = 3
# print(s.removeElement(nums, v))