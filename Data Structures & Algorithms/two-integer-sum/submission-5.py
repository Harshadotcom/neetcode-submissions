class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            x_val = target - nums[i]
            if x_val in freq:
                return [freq[x_val], i]
            else:
                freq[nums[i]] = freq.get(nums[i], i)