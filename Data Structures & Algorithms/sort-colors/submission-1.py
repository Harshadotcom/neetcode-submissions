class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]

        for i in nums:
            counts[i] += 1
        
        l = 0
        for j in range(len(counts)):
            for k in range(counts[j]):
                nums[l] = j
                l += 1
        