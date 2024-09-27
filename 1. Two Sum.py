class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for index, num in enumerate(nums):
            if target - num not in dict:
                dict[num] = index

            else:
                return [dict[target - num], index]

nums = [2,7,11,15]
target = 9

S = Solution()
print(S.twoSum(nums, target))




# -----------------------------------------------------
# Best solution

# class Solution(object):
#     def twoSum(self, nums, target):
#         dict = {}
#         for i, value in enumerate(nums):
#             if target - value in dict:
#                 # print([dict[target - value], i])
#                 return len([dict[target - value], i])
#             else:
#                 # print(value)
#                 dict[value] = i

# S = Solution()
# nums = [10,13,25,30,12,18,5,7]
# target = 4
# print(S.twoSum(nums, target))

#-----------------------------------
# enumerate example

# for i in enumerate(nums):
#     print('i',i)