class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        my_set = list()
        l = 0
        r = 0
        count = 0
        window_sum = 0
        while r < len(arr):
            window_sum += arr[r] 
            if r - l + 1 == k:
                avg_val = window_sum//k
                if avg_val >= threshold:
                    count += 1
                window_sum -= arr[l]
                l += 1

            r += 1
        
        return count