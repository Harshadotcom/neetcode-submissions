class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        current_write = m+n-1
        i = m-1
        j = n-1
        while j >= 0 and i >= 0:
            if nums2[j] > nums1[i]:
                nums1[current_write] = nums2[j]
                current_write -= 1
                j -= 1
            else:
                nums1[current_write] = nums1[i]
                current_write -= 1
                i -= 1
        
        if i == -1:
            for i in range(n-1, -1, -1):
                nums1[i] = nums2[j]
                j -= 1



        