class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] > target:
                return i
            elif nums[i] == target:
                return i
        
        return len(nums)


S = Solution()
x = [1,3,5,6]
t = 7
print(S.searchInsert(x, t))


# class Solution(object):
#     def searchInsert(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         for i in range(len(nums)):
#             if nums[i] == target:
#                 return i
            
#             if nums[i] >= target:
#                 return i
            
        
#         return i+1

# S = Solution()
# x = [1,3,5,6]
# t = 5
# print(S.searchInsert(x, t))