class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        total = 0
        length = float('Inf')

        while r < len(nums):
            total += nums[r]

            while total >= target:
                length = min(r - l + 1, length)
                total -= nums[l]
                l += 1
            r += 1
        
        return 0 if length == float('Inf') else length