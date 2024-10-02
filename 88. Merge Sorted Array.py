class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        lst = nums1 + nums2
        i, j, k = 0, 0, 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                lst[k] = nums1[i]
                i += 1
            else:
                lst[k] = nums2[j]
                j += 1
            
            k += 1
        
        while i < m:
            lst[k] = nums1[i]
            i += 1
            k += 1

        while j < n:
            lst[k] = nums2[j]
            j += 1
            k += 1

        for i in range(len(lst)):
            if i < m+n:
                nums1[i] = lst[i]
        
        return nums1
        
S = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(S.merge(nums1, m, nums2, n))



# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#         """
        


# S = Solution()
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
# print(S.merge(nums1, m, nums2, n))