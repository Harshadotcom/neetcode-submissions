class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for chars in strs:
            count = [0] * 26
            for char in chars:
                count[ord(char) - ord('a')] += 1
            key_val = tuple(count)
            if key_val not in hashmap:
                hashmap[key_val] = [chars]
            else:
                hashmap.get(key_val).append(chars)

        my_li = []
        for values in hashmap.values():
            my_li.append(values)
        return my_li