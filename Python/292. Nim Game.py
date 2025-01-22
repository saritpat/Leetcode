class Solution:
    def canWinNim(self, n: int) -> bool:
        return n%4 != 0

S = Solution()
n = 9
print(S.canWinNim(n))