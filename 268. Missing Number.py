class Solution:
    def missingNumber(self, nums) -> int:
        seen = set()

        for i in range(len(nums)+1):
            seen.add(i)

        for i in nums:
            if i in seen:
                seen.remove(i)
        
        return seen.pop()

# 0 1 3

S = Solution()
nums = [9,6,4,2,3,5,7,0,1]
print(S.missingNumber(nums))


# -----------------------------------------------------
# Faster solution

# class Solution:
#     def missingNumber(self, nums) -> int:
#         nums = set(nums)

#         for i in range(len(nums)):
#             if i not in nums:
#                 return i
        
#         return len(nums)

# # 0 1 3

# S = Solution()
# nums = [9,6,4,2,3,5,7,0,1]
# print(S.missingNumber(nums))



