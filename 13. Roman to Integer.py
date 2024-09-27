class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        num = 0
        prev = 0


        for i in range(len(s)-1, -1, -1):
            current = roman_to_int[s[i]]
            if current >= prev:
                num += current
            else:
                num -= current
            
            prev = current
        
        return(num)
                
# 50 5 1 1 1
S = Solution()
s = "LVIII"
print(S.romanToInt(s))



# -----------------------------------------------------
# Best solution

# class Solution(object):
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """

# S = Solution()
# s = "LVIII"
# print(S.romanToInt(s))