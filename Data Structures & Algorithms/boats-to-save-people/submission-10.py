class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) - 1
        boatCount = 0

        while i <= j:
            total = people[i] + people[j]

            if total > limit:
                j -= 1
            else:
                i += 1
                j -= 1
            boatCount += 1
        
        return boatCount