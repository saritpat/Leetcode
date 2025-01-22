# -----------------------------------------------------
# Faster solution

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            L = nums[:len(nums) // 2]
            R = nums[len(nums) // 2:]

            S.sortColors(L)
            S.sortColors(R)

            i = 0
            j = 0
            k = 0
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    nums[k] = L[i]
                    i+=1
                else:
                    nums[k] = R[j]
                    j+=1

                k+=1

            while i < len(L):
                nums[k] = L[i]
                i+=1
                k+=1

            while j < len(R):
                nums[k] = R[j]
                j+=1
                k+=1

            return nums



S = Solution()
x = [2,0,2,1,1,0]
print(S.sortColors(x))


# class Solution(object):
#     def sortColors(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         # use func. solution
#         nums = nums.sort()
        
#         # nums = sorted nums


#         # no func. needed
#         red, white, blue = 0, 0, len(nums)-1
    
#         while white <= blue:
#             if nums[white] == 0:
#                 nums[red], nums[white] = nums[white], nums[red]
#                 white += 1
#                 red += 1
#             elif nums[white] == 1:
#                 white += 1
#             else:
#                 nums[white], nums[blue] = nums[blue], nums[white]
#                 blue -= 1
# S = Solution()
# x = [2,0,2,1,1,0]
# print(S.sortColors(x))




