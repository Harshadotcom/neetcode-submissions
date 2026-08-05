class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        my_set = list()
        l = 0
        r = 0
        count = 0
        while r < len(arr):
            my_set.append(arr[r])
            if len(my_set) == k:
                avg_val = sum(my_set)//len(my_set)
                if avg_val >= threshold:
                    count += 1
                my_set.remove(arr[l])
                l += 1

            r += 1
        
        return count