class Solution:
    def isHappy(self, n: int) -> bool:
        ans = 0
        sett = set()
        prev = len(sett)
        count = 0
        while n != 1:
            for i in str(n):
                ans += int(i)**2
            
            n = ans
            if ans not in sett:
                sett.add(ans)
                prev = len(sett)
            else:
                sett.remove(ans)
                prev = len(sett)
            ans = 0
            if len(sett) == prev:
                count += 1
                if count == 10:
                    return False
        
        if n == 1:
            return True

# 2 3 4 19
S = Solution()
n = 19
print(S.isHappy(n))