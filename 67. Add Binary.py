class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a[::-1] 
        b = b[::-1]
        i = 0
        carry = 0
        ans = '' # 1010 1011
        while(i < len(a) or i < len(b)):
            sum = carry
            if i < len(a): 
                sum += int(a[i])
            if i < len(b): 
                sum += int(b[i])

            ans += str(sum % 2)
            carry = sum // 2 
            
            i+=1
            
        if carry > 0:
            ans+='1'
        ans = ans[::-1]
        return ans
        
        

S = Solution()
x = '1010'
y = '1011'
print(S.addBinary(x, y))        


# class Solution(object):
#     def addBinary(self, a, b):
#         """
#         :type a: str
#         :type b: str
#         :rtype: str
#         """

# S = Solution()
# x = '1010'
# y = '1011'
# print(S.addBinary(x, y))        

        