class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """i = 0
        j = 1
        while j < len(nums):
            if nums[j] <= nums[i]:
                j += 1
            elif nums[j] > nums[i]:
                nums[i + 1], nums[j] = nums[j], nums[i + 1]
                i += 1
            else:
                i += 1
                j += 1

        return i+1"""

        i = 0
        j = 1
        while j < len(nums):
            if nums[j] != nums[i] and nums[j] > nums[i]:
                nums[i + 1], nums[j] = nums[j], nums[i + 1]
                i += 1
            j += 1
        
        return i + 1