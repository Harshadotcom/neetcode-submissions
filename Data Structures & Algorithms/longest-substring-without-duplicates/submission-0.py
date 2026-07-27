class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        longest_substring_count = 0
        substring_set = set()
        while r < len(s):
            if s[r] not in substring_set:
                substring_set.add(s[r])
                longest_substring_count = len(substring_set) if longest_substring_count < len(substring_set) else longest_substring_count
                r += 1
            else:
                substring_set.remove(s[l])
                l += 1
        return longest_substring_count