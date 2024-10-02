# -----------------------------------------------------
# Faster solution

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sett = set()
        for i in range(len(nums)):
            if nums[i] in sett:
                sett.remove(nums[i])
            else:
                sett.add(nums[i])

        for i in sett:
            return i

S = Solution()
nums = [4,1,2,1,2]
print(S.singleNumber(nums))


# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """

#         dict = {}

#         for i in range(len(nums)):
#             dict[nums[i]] = dict.get(nums[i], 0) + 1

#         for i in dict:
#             if dict[i] == 1:
#                 return i


# S = Solution()
# nums = [4,1,2,1,2]
# print(S.singleNumber(nums))