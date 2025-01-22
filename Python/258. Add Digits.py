class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            new = 0
            st = str(num)
            for i in st:
                new += int(i)
            
            num = new
        
        return num
            

S = Solution()
num = 38
print(S.addDigits(num))


# -----------------------------------------------------
# Faster solution

# class Solution:
#     def addDigits(self, num: int) -> int:
#         if num == 0 : return 0
#         if num % 9 == 0 : return 9
#         else : return (num % 9)    

# S = Solution()
# num = 38
# print(S.addDigits(num))