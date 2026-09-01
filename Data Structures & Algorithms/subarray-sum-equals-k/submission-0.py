class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0 : 1}
        count = 0

        prefixSumArray = []
        prefixSum = 0
        for j in range(len(nums)):
            prefixSum += nums[j]
            prefixSumArray.append(prefixSum)

        for i in range(len(nums)):
            if prefixSumArray[i] - k in hashmap:
                count += hashmap[prefixSumArray[i] - k]

            hashmap[prefixSumArray[i]] = hashmap.get(prefixSumArray[i], 0) + 1
        
        return count



                