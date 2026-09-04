class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lastEle = None
        new_li = []
        for i in operations:
            if i == "+":
                lastEle = new_li[-1] + new_li[-2]
                new_li.append(lastEle)
            
            elif i == "C":
                new_li.pop()

            elif i == "D":
                append_val = 2 * new_li[-1]
                new_li.append(append_val)
            
            else:
                new_li.append(int(i))
            
        return sum(new_li)