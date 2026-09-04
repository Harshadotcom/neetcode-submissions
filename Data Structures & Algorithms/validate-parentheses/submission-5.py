class Solution:
    def isValid(self, s: str) -> bool:

        parentheses = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        li = []
        for i in s:
            if i in parentheses:
                li.append(i)
            else:
                if li and i == parentheses.get(li[-1]):
                    li.pop()
                else:
                    return False
        
        return not li