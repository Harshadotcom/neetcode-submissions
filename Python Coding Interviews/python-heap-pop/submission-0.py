import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    new_li = []
    for i in range(len(heap)):
        pop_ele = heapq.heappop(heap)
        new_li.append(pop_ele)
    return new_li


# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
