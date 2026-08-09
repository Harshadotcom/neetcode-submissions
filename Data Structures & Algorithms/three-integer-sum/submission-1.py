class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        my_li = []
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                elif nums[l] + nums[r] + nums[i] < 0:
                    l += 1
                else:
                    if [nums[l], nums[r], nums[i]] not in my_li:
                        my_li.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
        return my_li
