class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        target_map = {}
        for ele in s1:
            target_map[ele] = target_map.get(ele, 0) + 1


        current_map = {}
        l, r = 0, 0

        while r < len(s2):
            current_map[s2[r]] = current_map.get(s2[r], 0) + 1
            
            if r - l + 1 == len(s1):
                if target_map == current_map:
                    return True
                current_map[s2[l]] -= 1
                if current_map[s2[l]] == 0:
                    current_map.pop(s2[l])
                l += 1
            r += 1
        return False
                
            
            