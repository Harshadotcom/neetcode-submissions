class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        
        new_li = []
        for k,v in freq.items():
            if v > (len(nums)/3):
                new_li.append(k)
        return new_li