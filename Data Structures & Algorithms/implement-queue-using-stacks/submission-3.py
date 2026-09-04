class MyQueue:

    def __init__(self):
        self.queue = []
        self.newQueue = []
        
    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if not self.newQueue:
            for i in range(len(self.queue)):
                popVal = self.queue.pop()
                self.newQueue.append(popVal)

        removed = self.newQueue.pop()
        return removed

    def peek(self) -> int:
        if not self.newQueue:
            for i in range(len(self.queue)):
                popVal = self.queue.pop()
                self.newQueue.append(popVal)
        return self.newQueue[-1]

    def empty(self) -> bool:
        return not self.newQueue and not self.queue


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()