class Solution:
    def containsDuplicate(self, nums) -> bool:
        sett = set()

        for i in nums:
            if i in sett:
                return True
            else:
                sett.add(i)
        
        return False

S = Solution()
nums = [1,2,3,1]
print(S.containsDuplicate(nums))