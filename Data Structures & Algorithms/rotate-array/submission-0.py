class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_arr = [0] * len(nums)
        for i in range(len(nums)):
            insert = (i + k) % len(nums)
            new_arr[insert] = nums[i]
        
        nums[:] = new_arr
