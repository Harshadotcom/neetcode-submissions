class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) - 1
        boatCount = 0

        while i < j:
            if people[i] + people[j] > limit:
                boatCount += 1
                j -= 1
            elif people[i] + people[j] < limit:
                boatCount += 1
                i += 1
                j -= 1
            else:
                boatCount += 1
                i += 1
                j -= 1

        if i == j:
            boatCount += 1
        
        return boatCount