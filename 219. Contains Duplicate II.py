class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = i
            else:
                if abs(i - dict[nums[i]]) <= k:
                    return True
                else:
                    dict[nums[i]] = i
        
        return False
    
    # {1:0 0:1 1:2 1:3}
s = Solution()
nums = [1,2,3,1,2,3]
k = 2
print(s.containsNearbyDuplicate(nums, k))


# -----------------------------------------------------
# Faster solution

# class Solution(object):
#     def containsNearbyDuplicate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
#         dic = {}
#         for i in range(len(nums)):
#             if nums[i] in dic and i - dic[nums[i]] <= k:
#                 return True
#             dic[nums[i]] = i
#         return False

# s = Solution()
# nums = [1,2,3,1,2,3]
# k = 2
# print(s.containsNearbyDuplicate(nums, k))