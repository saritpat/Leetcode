class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        
        for i in s:
            if i == '[' or i == '{' or i == '(':
                st.append(i)

            elif len(st) != 0:
                if i == ']' and st[-1] == '[':
                    st.pop()
                elif i == '}' and st[-1] == '{':
                    st.pop()
                elif i == ')' and st[-1] == '(':
                    st.pop()
                else:
                    return False

            else:
                return False
        
        if len(st) == 0:
            return True
        else:
            return False
    
# (()[]) (]) ([)]
S = Solution()
x = "(()[])"
print(S.isValid(x))


# -----------------------------------------------------
# Faster solution

# class Solution(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """

# # (()[]) (]) ([)]
# S = Solution()
# s = "(()[])"
# print(S.isValid(s))