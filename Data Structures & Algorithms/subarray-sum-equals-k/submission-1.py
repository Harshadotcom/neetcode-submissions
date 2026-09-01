class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        count = 0
        prefixSum = 0

        for j in range(len(nums)):
            prefixSum += nums[j]
            if prefixSum - k in hashmap:
                count += hashmap[prefixSum - k]
            hashmap[prefixSum] = hashmap.get(prefixSum, 0) + 1
        
        
        return count