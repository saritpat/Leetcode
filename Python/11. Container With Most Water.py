class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        target = 0
        i = 0
        j = len(height)-1
        L = height[i]
        R = height[j]

        while i <= j:
            L = height[i]
            if min(L,R)*(j-i) > target:
                target = min(L,R)*(j-i)
                print(target, L,R, i,j, 'a')

            R = height[j]
            if min(L,R)*(j-i) > target:
                target = min(L,R)*(j-i)
                print(target, L,R, i,j, 'a')

            if L < R:
                i += 1
                
            else:
                j -= 1

        return target
        
S = Solution()
height = [1,2,3,4,5,6,7,8,9]
print(S.maxArea(height))


# -----------------------------------------------------
# Faster solution

# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         max_area = 0
#         left_pointer = 0
#         right_pointer = len(height)-1
#         while left_pointer < right_pointer:
#             width = right_pointer - left_pointer
#             if height[left_pointer] < height[right_pointer]:
#                 lower = height[left_pointer]
#                 left_pointer += 1
#             else:
#                 lower = height[right_pointer]
#                 right_pointer -= 1
#             area = width * lower
#             if area > max_area:
#                 max_area = area
#         return max_area

# S = Solution()
# height = [1,2,3,4,5,6,7,8,9]
# print(S.maxArea(height))