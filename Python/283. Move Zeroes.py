class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)

        return nums


S = Solution()
nums = [0,1,0,3,12]
print(S.moveZeroes(nums))


# -----------------------------------------------------
# Faster solution

# class Solution:
#     def moveZeroes(self, nums):
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         snowball_size = 0
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 snowball_size += 1
#             else:
#                 if snowball_size > 0:
#                     nums[i - snowball_size] = nums[i]
#                     nums[i] = 0
        
#         return nums

# S = Solution()
# nums = [0,1,0,3,12]
# print(S.moveZeroes(nums))
       