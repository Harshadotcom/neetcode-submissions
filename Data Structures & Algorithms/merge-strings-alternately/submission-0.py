class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        merged_str = ""
        while j < len(word2) and i < len(word1):
            merged_str = merged_str + word1[i] + word2[j]
            j += 1
            i += 1

        if i >= len(word1):
            merged_str = merged_str + word2[j:]
        else:
            merged_str = merged_str + word1[i:]

        return merged_str


