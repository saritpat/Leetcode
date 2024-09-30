# -----------------------------------------------------
# Faster solution

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        current = 1
        nums.sort()
        for i in nums:
            if i > 0 and i not in seen:
                seen.add(i)

        for i in seen:
            if current == i:
                current += 1

        return current, seen

S = Solution()
x = [1,2,2,1,3,1,0,4,0]
print(S.firstMissingPositive(x))   



# from collections import OrderedDict 

# class Solution(object):
#     def firstMissingPositive(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
        
#         nums.sort()
#         # lst = []
#         # for i in nums: 
#         #     if i not in lst:
#         #         lst.append(i)
        
#         lst = list(OrderedDict.fromkeys(nums)) 
        
#         nums = lst
#         ans = 1
        
#         for i in nums:
#             if i > ans:
#                 return ans
            
#             if i > 0:
#                 ans += 1
                
#         return ans
    
# # [0, 1, 2]
                

# S = Solution()
# x = [1,1]
# print(S.firstMissingPositive(x))     