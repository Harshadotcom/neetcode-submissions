class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(char for char in s if char.isalnum())
        lower_cleaned = cleaned.lower()
        i = 0
        j = len(cleaned) - 1
        while i < j:
            if lower_cleaned[i] != lower_cleaned[j]:
                return False
            i += 1
            j -= 1
        return True
        