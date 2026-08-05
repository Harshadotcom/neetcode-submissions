class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k
        new_li = []
        while r <= len(nums):
            max_window = max(nums[l:r])
            new_li.append(max_window)
            l += 1
            r += 1
        return new_li

