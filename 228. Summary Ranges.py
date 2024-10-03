# -----------------------------------------------------
# Faster solution

class Solution:
    def summaryRanges(self, nums):
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [f'{nums[0]}']

        curr = front = 0
        start = nums[0]
        ans = []

        for i in range(len(nums) - 1):
            curr = nums[i]
            front = nums[i+1]

            if front != nums[-1]:
                if front - curr != 1:
                    if start != curr:
                        ans.append(f"{str(start) + '->' + str(curr)}")
                    else:
                        ans.append(f"{str(start)}")
                    start = front
            
            else:
                if front - curr != 1:
                    if start != curr:
                        ans.append(f"{str(start) + '->' + str(curr)}")
                    else:
                        ans.append(f"{str(start)}")
                    ans.append(f'{front}')

                else:
                    if start != front:
                        ans.append(f"{str(start) + '->' + str(front)}")
                    else:
                        ans.append(f"{str(start)}")
        
        return ans
        
S = Solution()
nums = [0,2,3,4,6,8,9]
print(S.summaryRanges(nums))


# -----------------------------------------------------
# Slower but easier solution

# class Solution:
#     def summaryRanges(self, nums):
#         if len(nums) == 0:
#             return []

#         if len(nums) == 1:
#             return [f'{nums[0]}']
        
#         lst = []
#         curr = front = 0
#         start = nums[0]
#         ans = []

#         for i in range(len(nums) - 1):
#             curr = nums[i]
#             front = nums[i+1]

#             if front != nums[-1]:
#                 if front - curr != 1:
#                     lst.append([start, curr])
#                     start = front
            
#             else:
#                 if front - curr != 1:
#                     lst.append([start, curr])
#                     lst.append([front])

#                 else:
#                     lst.append([start, front])

#         for i in lst:
#             if len(i) == 1 :
#                 ans.append(f'{i[0]}')
            
#             else:
#                 if i[0] == i[1]:
#                     ans.append(f'{i[0]}')
#                 else:
#                     ans.append(f"{str(i[0]) + '->' + str(i[1])}")
        
#         return ans

# S = Solution()
# nums = [0,2,3,4,6,8,9]
# print(S.summaryRanges(nums))