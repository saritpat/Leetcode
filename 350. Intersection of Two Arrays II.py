class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        lst = []

        if len(nums1) >= len(nums2):
            long = nums1
            short = nums2
        else:
            long = nums2
            short = nums1

        for i in long:
            if i in short:
                lst.append(i)
                short.remove(i)
        
        return lst

S = Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(S.intersect(nums1, nums2))