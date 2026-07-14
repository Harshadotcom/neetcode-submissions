from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    highest_score = scores[0][1]
    name = scores[0][0]

    for i in range(1, len(scores)):
        if scores[i][1] > highest_score:
            highest_score = scores[i][1]
            name = scores[i][0]
    return name
    
# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
