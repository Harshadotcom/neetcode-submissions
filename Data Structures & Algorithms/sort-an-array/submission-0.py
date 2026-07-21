class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        i = 1
        while i < len(nums):
            j = i - 1
            while j >= 0:
                if nums[j + 1] < nums[j]:
                    nums[j + 1], nums[j] = nums[j], nums[j + 1]
                    j -= 1
                else:
                    j -= 1
            i += 1
        
        return nums