class Solution:
    def countBits(self, n: int):
        lst = [0]

        for i in range(1, n+1):
            sum = 0
            str = ''
            str = bin(i)[2:]

            for i in str:
                sum += int(i)

            lst.append(sum)

        return lst

S = Solution()
n = 10
print(S.countBits(n))


# -----------------------------------------------------
# Faster solution

# class Solution:
#     def countBits(self, n: int):
#         ans = [0]
#         for i in range(1, n + 1):
#             ans.append((i & 1) + ans[i >> 1])
#         return ans


# S = Solution()
# n = 5
# print(S.countBits(n))