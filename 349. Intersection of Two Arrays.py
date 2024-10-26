class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        seen = set()
        nums1 = set(nums1)
        nums2 = set(nums2)

        if len(nums1) >= len(nums2):
            long = nums1
            short = nums2
        else:
            long = nums2
            short = nums1

        for i in long:
            if i not in seen and i in short:
                seen.add(i)
        
        return list(seen)

S = Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(S.intersection(nums1, nums2))