class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for i in strs:
            encodedString += str(len(i)) + "#" + i 
        
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedString = []
        i = 0
        j = 0
        while j < len(s):
            if s[j] == "#":
                length = int(s[i:j])
                start = j + 1
                end = start + length
                decodedString.append(s[j + 1 : end])
                j = end
                i = end
            j += 1
        
        return decodedString
            
