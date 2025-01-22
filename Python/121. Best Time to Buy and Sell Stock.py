# -----------------------------------------------------
# Faster solution

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        max = 0

        for i in range(1, len(prices)):
            if buy > prices[i]:
                buy = prices[i]
            elif prices[i] - buy > max:
                max = prices[i] - buy

        return max

# 9 8 7 6 5 4 3 2 1 0

S = Solution()
nums1 = [7,1,5,3,6,4]
print(S.maxProfit(nums1))     



# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """

# # 9 8 7 6 5 4 3 2 1 0

# S = Solution()
# nums1 = [7,1,5,3,6,4]
# print(S.maxProfit(nums1))     