class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        lst = []
        sum = 0
        zero = 1
        for i in range(len(digits)-1, -1, -1):
            sum += digits[i]*(zero)
            zero *= 10
        
        sum = str(sum+1)

        for i in sum:
            lst.append(int(i))
        
        return lst

S = Solution()
x = [1,2,3]
print(S.plusOne(x))


# class Solution(object):
#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         """
        
#         st = ''
        
#         lst = []
        
#         for i in digits:
#             st += str(i)
        
#         st = int(st)
#         st += 1
#         st = str(st)
        
#         for i in st:
#             lst.append(int(i))
        
#         return lst

# S = Solution()
# x = [1,2,3]
# print(S.plusOne(x))