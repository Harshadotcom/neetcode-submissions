class MyStack:

    def __init__(self):
        self.li = deque()
        self.topValue = None

    def push(self, x: int) -> None:
        self.topValue = x
        self.li.append(x)

    def pop(self) -> int:
        for i in range(len(self.li) - 1):
            popVal = self.li.popleft()
            self.li.append(popVal)
            self.topValue = popVal

        removed = self.li.popleft()

        if not self.li:
            self.topValue = None
        
        return removed

    def top(self) -> int:
        return self.topValue

    def empty(self) -> bool:
        return not self.li


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()