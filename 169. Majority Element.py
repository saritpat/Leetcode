class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        max = [0, 0]

        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        
        for i in dict:
            if dict[i] > max[1]:
                max[0] = i
                max[1] = dict[i]
        
        return max[0]


S = Solution()
nums = [3,2,3]
print(S.majorityElement(nums))