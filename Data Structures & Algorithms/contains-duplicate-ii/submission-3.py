class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq = {}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = i
            else:
                if abs(freq.get(nums[i]) - i) <= k:
                    return True
                else:
                    freq[nums[i]] = i
        return False
